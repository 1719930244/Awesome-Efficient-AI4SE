#!/usr/bin/env python3
"""Add SE Dimension column to README.md tables."""
import re

# Mapping: partial paper title -> (SE code, SE description)
SE_MAP = {
    "FlashAttention": ("S3", "Adopted by StarCoder, Code Llama, DeepSeek-Coder"),
    "Switch Transformers": ("S3", "MoE architecture adopted by DeepSeek-Coder"),
    "DeepSeekMoE": ("S3", "MoE design used in DeepSeek-Coder family"),
    "Is Quantization a Deal-breaker": ("S1", "Quantization study on code LLMs"),
    "Greening Large Language Models": ("S1", "Pruning study on code LLMs"),
    "On the Compression of Language Models for Code": ("S1", "Compression comparison for code models"),
    "Metamorphic Testing Perspective": ("S1", "Distillation testing for code models"),
    "Compressing Pre-trained Models of Code": ("S1", "Compressing CodeBERT for SE deployment"),
    "Empirical Study of Knowledge Distillation": ("S1", "Distillation for code understanding tasks"),
    "Compact Language Models via Pruning": ("S2", "General compression evaluated on code tasks"),
    "FineSec": ("S1", "Distillation for C/C++ vulnerability detection"),
    "LoRACode": ("S1", "LoRA adapters for code embeddings"),
    "PEFT for Large Models": ("S2", "General PEFT survey covering code tasks"),
    "Astraios": ("S1", "PEFT comparison for code LLMs"),
    "PEFT of Small LMs": ("S1", "PEFT for code generation on small models"),
    "Draft & Verify": ("S2", "General speculative decoding technique"),
    "LayerSkip": ("S2", "General early-exit inference technique"),
    "DynamicKV": ("S2", "General KV cache compression technique"),
    "LaCache": ("S2", "General KV cache for long-context models"),
    "Efficient LLM Inference on CPUs": ("S2", "CPU inference evaluated on code tasks"),
    "Cheaper and Faster Completion": ("S1", "Dynamic inference for code completion"),
    "Accelerating Inference of RAG": ("S2", "General RAG acceleration technique"),
    "Accelerating LLM Inference for Efficient Code": ("S1", "Inference acceleration for code generation"),
    "Speculative Decoding for Verilog": ("S1", "Speculative decoding for hardware code"),
    "FrugalGPT": ("S2", "General LLM cascade framework"),
    "RouteLLM": ("S2", "General LLM routing framework"),
    "Hybrid LLM": ("S2", "General hybrid routing framework"),
    "AutoMix": ("S2", "General self-verification escalation"),
    # PLACEHOLDER_MORE
}

# Task-Level papers
SE_MAP.update({
    "EffiCoder": ("S1", "Efficiency-aware fine-tuning for code generation"),
    "GREEN-CODE": ("S1", "Energy-efficient code generation"),
    "Arctic-SnowCoder": ("S1", "Data-efficient code pretraining"),
    "Code Less, Align More": ("S1", "Data pruning for code alignment"),
    "Learn to Code Sustainably": ("S1", "Green code generation study"),
    "Carbon Footprint Evaluation": ("S1", "Carbon footprint of code generation"),
    "Analyzing the Energy and Accuracy": ("S1", "Energy-accuracy in software development"),
    "Does Few-Shot Learning Help": ("S1", "Few-shot for code synthesis"),
    "Inter-Dataset Code Duplication": ("S1", "Code data deduplication study"),
    "Scaling Laws for Code": ("S1", "Scaling laws for code models"),
    "Scaling Laws Behind Code": ("S1", "Scaling laws for code understanding"),
    "Fast and Memory-Efficient Neural Code": ("S1", "CNN-Transformer for code completion"),
    "Smart Invocation of Automatic Code": ("S1", "Invocation prediction for code completion"),
    "How GitHub Copilot": ("S1", "GitHub Copilot latency management"),
    "CodeSage": ("S1", "Scalable code representation learning"),
    "CodeTransformer": ("S1", "AST-aware attention for code"),
    "Seismic": ("S2", "General retrieval evaluated on code search"),
    "DeepCodeSeek": ("S1", "Real-time API retrieval for code"),
    "Leveraging LLMs for Software Requirements": ("S1", "LLM for requirements traceability"),
})

# Program Repair
SE_MAP.update({
    "FLAMES": ("S1", "Memory-efficient LLM for program repair"),
    "CigaR": ("S1", "Cost-efficient program repair"),
    "RepairLLaMA": ("S1", "LoRA-based program repair"),
    "Accelerating APR": ("S1", "RAG-augmented program repair"),
    "WilliamT": ("S1", "Cheap crash-site program repair"),
    "Automated Program Repair via Conversation": ("S1", "Conversational program repair"),
    "ThinkRepair": ("S1", "Self-directed few-shot program repair"),
    "Code Repair with LLMs gives": ("S1", "Thompson sampling for code repair"),
})

# Vulnerability Detection
SE_MAP.update({
    "White-Basilisk": ("S1", "Hybrid model for vulnerability detection"),
    "DeepDFA": ("S1", "Dataflow-inspired vulnerability detection"),
    "MAGNET: Meta-Path": ("S1", "Meta-path graph for vulnerability detection"),
    "MultiGLICE": ("S1", "GNN+program slicing for vulnerability detection"),
    "Detecting Code Vulnerabilities with Heterogeneous": ("S1", "GNN for code vulnerability detection"),
    "GNN-Powered Vulnerability": ("S1", "GNN for vulnerability path analysis"),
    "Enhancing Software Vulnerability Detection Using CPGs": ("S1", "Multi-view graph for vulnerability detection"),
    "Bridging Semantics and Structure": ("S1", "Hybrid model for vulnerability detection"),
    "LLM Agent for Real-World OSS": ("S1", "LLM agent for OSS vulnerability localization"),
    "Enhancing Pre-Trained LMs for Vulnerability": ("S1", "Augmentation for vulnerability detection"),
})

# Clone Detection
SE_MAP.update({
    "MAGNET: A Multi-Graph": ("S1", "Multi-graph for code clone detection"),
    "Nearest-neighbor, BERT-based": ("S1", "BERT-based scalable clone detection"),
    "Empirical Study of LLM-Based Code Clone": ("S1", "LLM for code clone detection"),
})

# Software Agents
SE_MAP.update({
    "SWE-agent": ("S1", "Agent for automated software engineering"),
    "OpenHands": ("S1", "Platform for AI software developers"),
    "SWE-Pruner": ("S1", "Context pruning for coding agents"),
    "AutoCodeRover": ("S1", "Autonomous program improvement"),
    "CodeAgent": ("S1", "Multi-agent code review"),
    "RepoNavigator": ("S1", "RL agent for repository navigation"),
    "Experience-Driven Early Termination": ("S1", "Early termination for SE agents"),
    "Energy Efficiency in Agentic": ("S1", "Energy-efficient SE agent frameworks"),
    "SWE-Replay": ("S1", "Trajectory recycling for SE agents"),
    "Adaptive Confidence Gating": ("S1", "Confidence-based routing for code generation"),
    "Scaling Test-Time Compute for Software": ("S1", "Test-time compute scaling for SE"),
    "Enhancing SE Agents via": ("S1", "Test-time scaling for SE agents"),
    "Self-Refine": ("S2", "General self-refinement evaluated on code"),
    "Reflexion": ("S2", "General verbal RL evaluated on HumanEval"),
    "Teaching Large Language Models to Self-Debug": ("S1", "Teaching LLMs to debug their own code"),
    "SWE-Effi": ("S1", "SE agent efficiency under resource constraints"),
    "FuseSearch": ("S1", "Adaptive parallel code localization for SE agents"),
})

# Test Generation
SE_MAP.update({
    "CodaMosa": ("S1", "Hybrid search+LLM for test generation"),
    "ASTER": ("S1", "Multi-language unit test generation"),
    "TestGenEval": ("S1", "Real-world test generation benchmark"),
    "Harnessing LLMs for Automated Software Testing": ("S1", "Scalable test generation"),
    "How well LLM-based test generation": ("S1", "LLM test generation scalability"),
    "CodeT": ("S1", "Code generation with generated tests"),
})

# Benchmarks
SE_MAP.update({
    "EffiBench": ("S1", "Benchmark for generated code efficiency"),
    "Learning Performance-Improving Code Edits": ("S1", "Performance-improving code edits"),
})

# Code Pre-trained Models
SE_MAP.update({
    "CodeBERT": ("S1", "Pre-trained model for programming languages"),
    "GraphCodeBERT": ("S1", "Dataflow-aware code representation"),
    "UniXcoder": ("S1", "Cross-modal code pre-training"),
    "Code Llama": ("S1", "Foundation model for code"),
    "StarCoder": ("S1", "Open-source code LLM"),
    "DeepSeek-Coder": ("S1", "MoE code LLM"),
    "code2vec": ("S1", "Distributed representations of code"),
    "Structural Language Models of Code": ("S1", "Structural code representation"),
    "AST-T5": ("S1", "Structure-aware pretraining for code"),
})


def find_se_dim(paper_title):
    """Find SE dimension for a paper by matching title substring."""
    for key, val in SE_MAP.items():
        if key.lower() in paper_title.lower():
            return val
    return None


def process_readme(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    new_lines = []
    unmatched = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect table header row
        if line.startswith('| Paper ') and 'Efficiency Dimension' in line:
            # Add SE Dimension column to header
            new_line = line.rstrip('\n').rstrip() + ' SE Dimension |\n'
            new_lines.append(new_line)
            i += 1

            # Process separator row
            if i < len(lines) and lines[i].startswith('|---'):
                sep = lines[i].rstrip('\n').rstrip()
                new_sep = sep + '----------------------|\n'
                new_lines.append(new_sep)
                i += 1

            # Process data rows until empty line or non-table line
            while i < len(lines) and lines[i].startswith('|'):
                row = lines[i].rstrip('\n').rstrip()
                # Try to find SE dimension
                se_dim = find_se_dim(row)
                if se_dim:
                    code, desc = se_dim
                    new_row = row + f' {code}: {desc} |\n'
                else:
                    new_row = row + ' — |\n'
                    # Extract title for debugging
                    parts = row.split('|')
                    if len(parts) > 1:
                        unmatched.append(parts[1].strip()[:60])
                new_lines.append(new_row)
                i += 1
        else:
            new_lines.append(line)
            i += 1

    with open(filepath, 'w') as f:
        f.writelines(new_lines)

    if unmatched:
        print(f"WARNING: {len(unmatched)} unmatched papers:")
        for t in unmatched:
            print(f"  - {t}")
    else:
        print("All papers matched successfully!")


if __name__ == '__main__':
    process_readme('/home/szw/OVERLEAF/Efficient_AI4SE_Survey/awesome/README.md')
    print("Done!")
