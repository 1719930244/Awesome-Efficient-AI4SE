# Survey Summary

**Paper**: Efficient Technology of LLMs in Software Engineering: A Survey on Models, Patterns, and Evaluation
**Primary Studies**: 98
**Time Span**: 2019--2026

---

## Classification Framework

### Five Lifecycle Stages

| Stage | ID | Count | Key Techniques |
|-------|:--:|:-----:|----------------|
| Data Preprocessing | I0 | 7 | Data curation, deduplication, scaling laws, few-shot example selection |
| Model Design | I1 | 18 | Sparse attention, MoE, structure-aware representations, hybrid architectures |
| Training and Tuning | I2 | 20 | PEFT/LoRA, knowledge distillation, quantization, pruning, energy-aware training |
| Inference and Serving | I3 | 29 | Speculative decoding, KV-cache optimization, model routing, test-time compute |
| Deployment and System Integration | I4 | 24 | Agent frameworks, retrieval infrastructure, task-specific deployment |

### Five Workload Archetypes

| Workload | ID | Count | Description |
|----------|:--:|:-----:|-------------|
| Interactive | W1 | 36 | IDE completion, chat assistance, real-time design |
| Batch / CI | W2 | 31 | Test generation, static analysis, code review |
| Repository-scale | W3 | 25 | Code search, clone detection, vulnerability scanning |
| Agentic | W4 | 20 | Multi-step repair, automated debugging, tool-augmented development |
| Safety-critical | W5 | 13 | Security auditing, compliance checks, high-assurance review |

### Seven Efficiency Patterns

P1 Cascade and Gating, P2 Retrieve then Generate, P3 Speculate then Verify, P4 Cache then Reuse, P5 Adaptive Computation, P6 Incremental Update, P7 Verifier in the Loop.

---

## Key Findings

### RQ1: Lifecycle Distribution
- Inference and Serving attracts the most research attention
- Data Preprocessing and Deployment remain underexplored
- Cross-stage combinations can yield multiplicative gains
- SE-specific constraints shape technique effectiveness

### RQ2: Workload Mapping
- Seven efficiency patterns emerge across workloads
- Matching interventions to the dominant constraint of each workload generally outperforms uniform strategies
- No single pattern dominates all deployment contexts

### RQ3: Evaluation Practices
- Efficiency evaluation concentrates on parameters (61%) and latency (51%)
- Only 17% report energy or carbon metrics
- Only 40% disclose serving configuration
- Reporting checklist proposed to improve cross-study comparability

---

## Efficiency Highlights

- Parameter compression: 30x (White-Basilisk)
- Training speedup: 75x (DeepDFA)
- Memory reduction: 83% (FLAMES)
- Cost reduction: 98% API cost (FrugalGPT), $0.00014/bug (WilliamT)
- Latency reduction: 2.5x (DeepCodeSeek)
- Energy reduction: 23-50% (GREEN-CODE)
