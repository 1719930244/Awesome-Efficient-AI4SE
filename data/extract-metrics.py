#!/usr/bin/env python3
"""
Extract efficiency metrics from primary studies.
Step 0: Download PDFs, extract text, identify reported metrics.
"""

import re
import os
import csv
import sys
import time
import subprocess
import json
from collections import defaultdict

# Paths
README_PATH = "/home/szw/github/Awesome-Efficient-AI4SE/README.md"
PAPERS_DIR = "/home/szw/overleaf/efficient-ai4se-survey/materials/papers"
TEXT_DIR = "/home/szw/overleaf/efficient-ai4se-survey/materials/papers_text"
OUTPUT_CSV = "/home/szw/overleaf/efficient-ai4se-survey/materials/metric-frequency.csv"
DETAIL_CSV = "/home/szw/overleaf/efficient-ai4se-survey/materials/metric-per-paper.csv"

os.makedirs(PAPERS_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

# --- METRIC PATTERNS ---
# Each entry: (category, metric_name, [regex_patterns])
# Patterns are case-insensitive and match in context
METRIC_PATTERNS = [
    # === Computational / Time ===
    ("Computational", "Latency", [
        r'\blatency\b', r'\bresponse\s+time\b', r'\binference\s+time\b',
        r'\bwall[\s-]?clock\s+time\b', r'\bexecution\s+time\b',
        r'\btime[\s-]?to[\s-]?first[\s-]?token\b', r'\bTTFT\b',
        r'\bend[\s-]?to[\s-]?end\s+time\b', r'\bgeneration\s+time\b',
    ]),
    ("Computational", "Tail latency (P50/P95/P99)", [
        r'\bP50\b', r'\bP95\b', r'\bP99\b', r'\bp50\b', r'\bp95\b', r'\bp99\b',
        r'\btail\s+latency\b', r'\bpercentile\s+latency\b',
    ]),
    ("Computational", "Throughput", [
        r'\bthroughput\b', r'\btokens?\s*/\s*s\b', r'\btokens?\s+per\s+second\b',
        r'\brequests?\s*/\s*s\b', r'\brequests?\s+per\s+second\b',
        r'\bsamples?\s*/\s*s\b', r'\bsamples?\s+per\s+second\b',
    ]),
# PLACEHOLDER_METRICS_CONT
]

METRIC_PATTERNS_CONT = [
    ("Computational", "Speedup ratio", [
        r'\bspeedup\b', r'\b\d+(\.\d+)?[x×]\s*(faster|speedup)\b',
        r'\baccelerat(e|ion)\b',
    ]),
    ("Computational", "Training time", [
        r'\btraining\s+time\b', r'\btrain(ing)?\s+hours?\b',
        r'\bfine[\s-]?tun(e|ing)\s+time\b', r'\bepoch\s+time\b',
        r'\bconvergence\s+time\b', r'\btraining\s+cost\b',
    ]),
    # === Computational / Size ===
    ("Computational", "FLOPs", [
        r'\bFLOPs?\b', r'\bGFLOPs?\b', r'\bTFLOPs?\b',
        r'\bfloating[\s-]?point\s+operations?\b', r'\bMACs?\b',
    ]),
    ("Computational", "Parameters", [
        r'\bparameters?\s+count\b', r'\bmodel\s+size\b',
        r'\b\d+(\.\d+)?\s*[BMK]\s+param(eter)?s?\b',
        r'\bnumber\s+of\s+parameters?\b',
    ]),
    ("Computational", "Peak memory", [
        r'\bpeak\s+memory\b', r'\bVRAM\b', r'\bGPU\s+memory\b',
        r'\bmemory\s+(usage|footprint|consumption|overhead)\b',
        r'\bRAM\s+(usage|footprint|consumption)\b',
        r'\bOOM\b', r'\bout[\s-]?of[\s-]?memory\b',
    ]),
    # === Environmental ===
    ("Environmental", "Energy consumption", [
        r'\benergy\s+(consumption|usage|cost|efficiency)\b',
        r'\bkWh\b', r'\bwatt[\s-]?hours?\b', r'\bpower\s+consumption\b',
        r'\bjoules?\b', r'\benergy[\s-]?aware\b',
    ]),
    ("Environmental", "Carbon emissions", [
        r'\bcarbon\s+(emission|footprint|cost)\b',
        r'\bCO2\b', r'\bCO₂\b', r'\bkgCO2\b',
        r'\bcarbon[\s-]?aware\b', r'\bgreen\s+AI\b',
    ]),
    ("Environmental", "Monetary cost", [
        r'\b(API|token|inference|total)\s+cost\b',
        r'\$\s*\d+', r'\bdollar\b', r'\bcost[\s-]?per[\s-]?(task|query|bug|token)\b',
        r'\bcost[\s-]?efficient\b', r'\bcost[\s-]?effective\b',
        r'\bpricing\b', r'\bbudget\b',
    ]),
    # === Task Quality ===
    ("Task Quality", "pass@k", [
        r'\bpass@\d+\b', r'\bpass\s*@\s*k\b', r'\bpass\s*@\s*\d+\b',
    ]),
    ("Task Quality", "Accuracy", [
        r'\baccuracy\b', r'\btop[\s-]?\d+\s+accuracy\b',
        r'\bexact\s+match\b', r'\bEM\s+score\b',
    ]),
    ("Task Quality", "F1 score", [
        r'\bF1[\s-]?score\b', r'\bF1\b', r'\bmicro[\s-]?F1\b', r'\bmacro[\s-]?F1\b',
    ]),
    ("Task Quality", "Precision / Recall", [
        r'\bprecision\b', r'\brecall\b',
        r'\bfalse\s+positive\s+rate\b', r'\bFPR\b',
        r'\btrue\s+positive\s+rate\b', r'\bTPR\b',
    ]),
    ("Task Quality", "BLEU / CodeBLEU", [
        r'\bBLEU\b', r'\bCodeBLEU\b', r'\bROUGE\b',
        r'\bCrystalBLEU\b', r'\bMETEOR\b',
    ]),
    ("Task Quality", "AUROC / AUC", [
        r'\bAUROC\b', r'\bAUC\b', r'\bROC\b',
    ]),
    ("Task Quality", "MRR / Recall@k", [
        r'\bMRR\b', r'\bmean\s+reciprocal\s+rank\b',
        r'\bRecall@\d+\b', r'\bNDCG\b', r'\bMAP\b',
    ]),
    ("Task Quality", "Resolve rate / Fix rate", [
        r'\bresolve\s+rate\b', r'\bfix\s+rate\b', r'\brepair\s+rate\b',
        r'\bpatch\s+(success|rate)\b', r'\bplausible\s+patches?\b',
    ]),
    ("Task Quality", "Code coverage", [
        r'\b(code|line|branch|statement)\s+coverage\b',
        r'\bcoverage\s+rate\b',
    ]),
    # === Composite ===
    ("Composite", "Quality-cost trade-off", [
        r'\btrade[\s-]?off\b', r'\bPareto\b', r'\bcost[\s-]?quality\b',
        r'\bquality[\s-]?cost\b', r'\baccuracy[\s-]?per[\s-]?FLOP\b',
        r'\bpass@k[\s-]?per\b', r'\bper[\s-]?dollar\b',
        r'\benergy[\s-]?per[\s-]?task\b',
    ]),
    ("Composite", "Compression ratio", [
        r'\bcompression\s+ratio\b', r'\bmodel\s+reduction\b',
        r'\b\d+[x×]\s+compress(ion|ed)\b', r'\bpruning\s+ratio\b',
        r'\bsparsity\s+ratio\b',
    ]),
    ("Composite", "Tokens / Turns (agent cost)", [
        r'\btotal\s+tokens?\b', r'\btoken\s+(count|usage|consumption)\b',
        r'\bnumber\s+of\s+turns?\b', r'\bagent\s+turns?\b',
        r'\bLLM\s+calls?\b', r'\bAPI\s+calls?\b',
    ]),
]

ALL_METRICS = METRIC_PATTERNS + METRIC_PATTERNS_CONT


def parse_readme():
    """Extract ⭐ papers with URLs from README.md."""
    papers = []
    with open(README_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith('| ⭐'):
                continue
            # Parse markdown table row
            cols = [c.strip() for c in line.split('|')[1:-1]]
            if len(cols) < 4:
                continue
            title = cols[0].replace('⭐ ', '').strip()
            venue = cols[1].strip()
            year = cols[2].strip()
            links_col = cols[3].strip()
            # Extract URL from markdown link [text](url)
            url_match = re.search(r'\[.*?\]\((https?://[^\)]+)\)', links_col)
            url = url_match.group(1) if url_match else ''
            papers.append({
                'title': title,
                'venue': venue,
                'year': year,
                'url': url,
                'pdf_url': '',
            })
    return papers


def get_pdf_url(paper):
    """Convert paper URL to direct PDF download URL."""
    url = paper['url']
    if not url:
        return ''
    # arXiv
    if 'arxiv.org/abs/' in url:
        arxiv_id = url.split('arxiv.org/abs/')[-1].split('?')[0]
        return 'https://arxiv.org/pdf/{}.pdf'.format(arxiv_id)
    # OpenReview
    if 'openreview.net/forum' in url:
        oid = re.search(r'id=([^&]+)', url)
        if oid:
            return 'https://openreview.net/pdf?id={}'.format(oid.group(1))
    # PMLR (proceedings.mlr.press)
    if 'proceedings.mlr.press' in url:
        # e.g. https://proceedings.mlr.press/v235/gong24c.html
        return url.replace('.html', '') + '/' + url.split('/')[-1].replace('.html', '') + '.pdf'
    # ACL Anthology
    if 'aclanthology.org' in url:
        # e.g. https://aclanthology.org/2024.acl-long.607/
        clean = url.rstrip('/')
        return clean + '.pdf'
    # ACM DL, IEEE - harder to get PDFs directly, skip for now
    return ''


def download_pdf(paper, idx):
    """Download PDF for a paper. Returns path or empty string."""
    pdf_url = get_pdf_url(paper)
    if not pdf_url:
        return ''
    safe_name = re.sub(r'[^\w\-]', '_', paper['title'][:60])
    pdf_path = os.path.join(PAPERS_DIR, '{}_{}.pdf'.format(idx, safe_name))
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
        return pdf_path
    try:
        import requests
        resp = requests.get(pdf_url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (research survey metric extraction)'
        })
        if resp.status_code == 200 and len(resp.content) > 1000:
            with open(pdf_path, 'wb') as f:
                f.write(resp.content)
            return pdf_path
    except Exception as e:
        print('  Download failed: {}'.format(e))
    return ''


def extract_text(pdf_path, idx):
    """Extract text from PDF using pdftotext."""
    txt_path = os.path.join(TEXT_DIR, '{}.txt'.format(idx))
    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 100:
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    try:
        subprocess.run(['pdftotext', '-layout', pdf_path, txt_path],
                       timeout=30, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print('  Text extraction failed: {}'.format(e))
    return ''


def find_metrics_in_text(text):
    """Search text for all metric patterns. Returns set of (category, metric_name)."""
    found = set()
    for category, metric_name, patterns in ALL_METRICS:
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                found.add((category, metric_name))
                break  # one match per metric is enough
    return found


def main():
    print("=== Step 0: Metric Frequency Extraction ===\n")

    # 1. Parse README
    print("[1/4] Parsing README.md for primary studies...")
    papers = parse_readme()
    print("  Found {} primary studies with ⭐\n".format(len(papers)))

    # 2. Download PDFs
    print("[2/4] Downloading PDFs...")
    downloaded = 0
    failed_downloads = []
    for i, p in enumerate(papers):
        pdf_path = download_pdf(p, i)
        p['pdf_path'] = pdf_path
        if pdf_path:
            downloaded += 1
            print("  [{}/{}] OK: {}".format(i+1, len(papers), p['title'][:50]))
        else:
            failed_downloads.append(p['title'])
            print("  [{}/{}] SKIP (no PDF URL): {}".format(i+1, len(papers), p['title'][:50]))
        time.sleep(0.5)  # be polite
    print("\n  Downloaded: {}/{}, Skipped: {}\n".format(
        downloaded, len(papers), len(failed_downloads)))

    # 3. Extract text + find metrics
    print("[3/4] Extracting text and finding metrics...")
    metric_counts = defaultdict(int)  # (category, metric) -> count
    paper_metrics = []  # per-paper detail

    for i, p in enumerate(papers):
        if not p.get('pdf_path'):
            paper_metrics.append({
                'idx': i, 'title': p['title'], 'venue': p['venue'],
                'status': 'no_pdf', 'metrics': []
            })
            continue

        text = extract_text(p['pdf_path'], i)
        if not text:
            paper_metrics.append({
                'idx': i, 'title': p['title'], 'venue': p['venue'],
                'status': 'no_text', 'metrics': []
            })
            continue

        found = find_metrics_in_text(text)
        metric_names = sorted(['{}/{}'.format(c, m) for c, m in found])
        for c, m in found:
            metric_counts[(c, m)] += 1

        paper_metrics.append({
            'idx': i, 'title': p['title'], 'venue': p['venue'],
            'status': 'ok', 'metrics': metric_names
        })
        print("  [{}/{}] {} metrics: {}".format(
            i+1, len(papers), len(found), p['title'][:40]))

    # 4. Write output CSVs
    print("\n[4/4] Writing output CSVs...")

    # Frequency summary
    total_analyzed = sum(1 for pm in paper_metrics if pm['status'] == 'ok')
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['category', 'metric_name', 'count', 'percentage', 'total_analyzed'])
        for (cat, met), cnt in sorted(metric_counts.items(),
                                       key=lambda x: -x[1]):
            pct = round(100.0 * cnt / total_analyzed, 1) if total_analyzed else 0
            w.writerow([cat, met, cnt, pct, total_analyzed])
    print("  Wrote: {}".format(OUTPUT_CSV))

    # Per-paper detail
    with open(DETAIL_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['idx', 'title', 'venue', 'status', 'num_metrics', 'metrics'])
        for pm in paper_metrics:
            w.writerow([pm['idx'], pm['title'], pm['venue'],
                        pm['status'], len(pm['metrics']),
                        '; '.join(pm['metrics'])])
    print("  Wrote: {}".format(DETAIL_CSV))

    # Summary
    print("\n=== Summary ===")
    print("Total primary studies: {}".format(len(papers)))
    print("PDFs downloaded: {}".format(downloaded))
    print("Successfully analyzed: {}".format(total_analyzed))
    print("\nMetric frequency (top 20):")
    for (cat, met), cnt in sorted(metric_counts.items(), key=lambda x: -x[1])[:20]:
        pct = round(100.0 * cnt / total_analyzed, 1) if total_analyzed else 0
        print("  {:>5.1f}%  ({:>2}/{})  [{}] {}".format(pct, cnt, total_analyzed, cat, met))

    if failed_downloads:
        print("\n--- Papers without PDF (need manual download) ---")
        for t in failed_downloads:
            print("  - {}".format(t))


if __name__ == '__main__':
    main()

