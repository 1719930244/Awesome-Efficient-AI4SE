# Survey Methodology

This document provides supplementary materials for our survey paper "Efficient AI for Software Engineering: A Comprehensive Survey on Models, Tasks, and Evaluation".

## Reproducibility Snapshot (as of 2026-02-05)

- **Time window**: 2018-01-01 to 2026-02-05 (inclusive)
- **Programmatic snapshot**: OpenAlex Works API snapshot executed on 2026-02-03 (PRISMA-style counts are reported in the manuscript)
- **Core synthesis size**: 100 primary studies (manuscript, February 2026)

## Related Surveys

| Year | Title |
|------|-------|
| 2025 | [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/abs/2506.23749) |
| 2025 | [LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights](https://doi.org/10.1145/3769082) |
| 2025 | [Agents in Software Engineering: Survey, Landscape, and Vision](https://doi.org/10.1007/s10515-025-00544-2) |
| 2025 | [LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead](https://doi.org/10.1145/3712003) |
| 2025 | [From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future](https://arxiv.org/abs/2408.02479) |
| 2025 | [Towards an Understanding of Large Language Models in Software Engineering Tasks](https://doi.org/10.1007/s10664-024-10602-0) |
| 2024 | [Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977) |
| 2024 | [Efficient and Green Large Language Models for Software Engineering: Literature Review, Vision, and the Road Ahead](https://doi.org/10.1145/3708525) |
| 2024 | [Robustness, Security, Privacy, Explainability, Efficiency, and Usability of Large Language Models for Code](https://arxiv.org/abs/2403.07506) |
| 2024 | [Large Language Models for Software Engineering: A Systematic Literature Review](https://doi.org/10.1145/3695988) |
| 2024 | [Software Testing with Large Language Models: Survey, Landscape, and Vision](https://doi.org/10.1109/tse.2024.3368208) |
| 2024 | [A Systematic Literature Review on Using NLP in Requirements Engineering](https://www.mdpi.com/2079-9292/13/11/2055) |
| 2024 | [A Survey on Evaluating Large Language Models in Code Generation Tasks](https://arxiv.org/abs/2408.16498) |
| 2023 | [Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code](https://arxiv.org/abs/2311.07989) |
| 2023 | [A Survey of Large Language Models for Code: Evolution, Benchmarking, and Future Trends](https://arxiv.org/abs/2311.10372) |
| 2023 | [Large Language Models for Software Engineering: Survey and Open Problems](https://doi.org/10.1109/icse-fose59343.2023.00008) |
| 2023 | [A Survey of Source Code Search: A 3-Dimensional Perspective](https://doi.org/10.1145/3656341) |
| 2023 | [A Survey on Automated Software Vulnerability Detection Using ML/DL](https://arxiv.org/abs/2306.11673) |

## Search Query Strings

Our literature search combined terms from three dimensions using Boolean AND/OR operators.

### Dimension 1: Efficiency-Related Terms

| Category | Keywords |
|----------|----------|
| **General** | efficient, lightweight, fast, accelerate, speedup, optimization, compact, tiny |
| **Compression** | quantization, pruning, sparsity, low-rank, distillation, factorization |
| **Resource** | parameter-efficient, compute-efficient, memory-efficient, energy-efficient |

### Dimension 2: Technique-Specific Terms

| Category | Keywords |
|----------|----------|
| **PEFT** | LoRA, adapter, prefix/prompt tuning, QLoRA, BitFit, PEFT |
| **Learning** | few-shot, zero-shot, in-context learning, transfer learning |
| **Inference** | speculative decoding, early exit, KV cache, token pruning |
| **Deployment** | edge, on-device, mobile, TinyML, model serving |

### Dimension 3: SE-Domain Terms

| Category | Keywords |
|----------|----------|
| **General SE** | software engineering, code, program, programming |
| **Code AI** | code model, code LLM, code generation, program synthesis |
| **SE tasks** | bug detection, code review, program repair, test generation |
| **Identifiers** | AI4SE, ML4SE, DL4SE, LLM for code |

### Query Combinations

Queries were constructed as: `(term₁ OR term₂ OR ...) AND (SE-term₁ OR SE-term₂ OR ...)`

| ID | Efficiency Terms (D1/D2) | SE Terms (D3) |
|----|--------------------------|---------------|
| Q1 | efficient, lightweight, fast, compact | code, program, software engineering |
| Q2 | quantization, pruning, sparsity, compression | code model, code generation |
| Q3 | parameter-efficient, memory-efficient | code LLM, code completion |
| Q4 | knowledge distillation, teacher-student | AI4SE, ML4SE, code intelligence |
| Q5 | LoRA, adapter, prompt tuning, PEFT | code, code generation, code model |
| Q6 | NAS, AutoML, layer dropping | code model, AI4SE |
| Q7 | few-shot, zero-shot, in-context learning | code, bug detection, program repair |
| Q8 | speculative decoding, KV cache, early exit | code LLM, code generation |
| Q9 | edge deployment, on-device, TinyML | code model, code intelligence |
| Q10 | green AI, carbon footprint, energy | AI4SE, LLM for code |
