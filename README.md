# Awesome Efficient AI4SE

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of papers on **Efficient AI for Software Engineering**, accompanying our survey paper:

> **Efficient Technology of LLMs in Software Engineering: A Survey on Models, Patterns, and Evaluation**
> Zongwen Shen, Jionghan Wu, Yidan Xu, Xuejin Liu, Xiang Chen, Jidong Ge, Chuanyi Li, Liguo Huang, and Bin Luo
> *Manuscript under review, 2026*

## Legend

- ⭐ = **Primary study** (one of the 98 papers analyzed in our survey)
- **Lifecycle Stage**: I0 = Data Preprocessing, I1 = Model Design, I2 = Training/Tuning, I3 = Inference/Serving, I4 = Deployment/System
- **Workload**: W1 = Interactive, W2 = Batch/CI, W3 = Repository-scale, W4 = Agentic, W5 = Safety-critical
- **SE Dimension**: S1 = Code-specific (designed for or evaluated on code/SE tasks), S2 = Code-evaluated (general technique with code/SE evaluation), S3 = SE-adopted (general technique adopted by major code models)

## Contents

- [Model-Level Efficiency](#model-level-efficiency)
  - [Quantization](#quantization)
  - [Knowledge Distillation](#knowledge-distillation)
  - [Parameter-Efficient Fine-Tuning (PEFT)](#parameter-efficient-fine-tuning-peft)
  - [Efficient Inference](#efficient-inference)
  - [Efficient Architectures](#efficient-architectures)
- [Task-Level Efficiency](#task-level-efficiency)
  - [Code Generation](#code-generation)
  - [Code Completion & Search](#code-completion--search)
  - [Program Repair](#program-repair)
  - [Vulnerability Detection](#vulnerability-detection)
  - [Clone Detection](#clone-detection)
  - [Software Agents](#software-agents)
  - [Test Generation](#test-generation)
- [Efficiency-Oriented Benchmarks](#efficiency-oriented-benchmarks)
- [Code Pre-trained Models](#code-pre-trained-models)
- [Supplementary Materials](#supplementary-materials)

---

## Model-Level Efficiency

### Quantization

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ Is Quantization a Deal-breaker? Empirical Insights from Large Code Models | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2507.09665) | I2 | W1, W2 | INT4 quantization, 4× memory reduction | S1: Quantization study on code LLMs |
| ⭐ Greening Large Language Models of Code | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2309.04076) | I2 | W2 | Structured pruning for code LLMs | S1: Pruning study on code LLMs |

### Knowledge Distillation

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ On the Compression of Language Models for Code: Distillation, Quantization, and Pruning | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2412.13737) | I2 | W2 | Compression technique comparison | S1: Compression comparison for code models |
| ⭐ A Metamorphic Testing Perspective on Knowledge Distillation for Code | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2511.05476) | I2 | W2 | Metamorphic distillation testing | S1: Distillation testing for code models |
| ⭐ Compressing Pre-trained Models of Code into 3 MB | ASE | 2022 | [arXiv](https://arxiv.org/abs/2208.07120) | I2 | W2, W3 | 3–6× speedup, 90–95% quality retention | S1: Compressing CodeBERT for SE deployment |
| ⭐ An Empirical Study of Knowledge Distillation for Code Understanding Tasks | ICSE | 2026 | [arXiv](https://arxiv.org/abs/2508.15423) | I2 | W2 | Distillation for code understanding | S1: Distillation for code understanding tasks |
| ⭐ Compact Language Models via Pruning and Knowledge Distillation (Minitron) | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2407.14679) \| [OpenReview](https://openreview.net/forum?id=9U0nLnNMJ7) | I2 | W2 | 2–4× compression via pruning+distillation | S2: General compression evaluated on code tasks |
| ⭐ FineSec: Distilling Lightweight Language Models for C/C++ Vulnerabilities | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.06645) | I2 | W5 | Distillation for C/C++ vuln detection | S1: Distillation for C/C++ vulnerability detection |

### Parameter-Efficient Fine-Tuning (PEFT)

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ LoRACode: LoRA Adapters for Code Embeddings | ICLR | 2024 | [OpenReview](https://openreview.net/forum?id=b0foNPsPaH) | I2 | W2 | <2% trainable params, 50%+ VRAM reduction | S1: LoRA adapters for code embeddings |
| ⭐ PEFT for Large Models: A Comprehensive Survey | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2403.14608) | I2 | W2 | PEFT efficiency for code tasks | S2: General PEFT survey covering code tasks |
| ⭐ Astraios: Parameter-Efficient Instruction Tuning Code LLMs | ICLR | 2025 | [arXiv](https://arxiv.org/abs/2401.00788) | I2 | W2 | PEFT comparison, accuracy-efficiency tradeoff | S1: PEFT comparison for code LLMs |
| ⭐ PEFT of Small LMs for Code Generation (Gemma/Qwen/Llama) | IJECE | 2026 | [Paper](https://doi.org/10.11591/ijece.v16i1.pp278-287) | I2 | W1, W2 | PEFT on 1–3B models, training cost reduction | S1: PEFT for code generation on small models |

### Efficient Inference

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ Draft & Verify: Lossless LLM Acceleration via Self-Speculative Decoding | ACL | 2024 | [arXiv](https://arxiv.org/abs/2309.08168) \| [ACL Anthology](https://aclanthology.org/2024.acl-long.607/) | I3 | W1, W2 | Self-speculative, lossless acceleration | S2: General speculative decoding technique |
| ⭐ LayerSkip: Enabling Early-Exit Inference and Self-Speculative Decoding | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2404.16710) | I3 | W1 | 1.5–2× latency reduction | S2: General early-exit inference technique |
| ⭐ DynamicKV: Task-Aware Adaptive KV Cache Compression | Findings of EMNLP | 2025 | [arXiv](https://arxiv.org/abs/2412.14838) \| [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.426/) | I3 | W1 | Task-aware KV cache compression | S2: General KV cache compression technique |
| ⭐ LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling | ICML | 2025 | [Paper](https://proceedings.mlr.press/v267/shi25b.html) | I3 | W1 | Ladder-shaped cache, OOM prevention | S2: General KV cache for long-context models |
| ⭐ Efficient LLM Inference on CPUs | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2311.00502) | I3 | W1 | CPU-based inference optimization | S2: CPU inference evaluated on code tasks |
| ⭐ Attaining Cheaper and Faster Completion through Dynamic Model Inference | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2401.09964) | I3 | W1 | Adaptive computation, latency reduction | S1: Dynamic inference for code completion |
| ⭐ Accelerating Inference of RAG via Sparse Context Selection | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2405.16178) \| [OpenReview](https://openreview.net/forum?id=HE6pJoNnFp) | I3 | W1, W2 | Early exit for simple cases | S2: General RAG acceleration technique |
| ⭐ Accelerating LLM Inference for Efficient Code Generation | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2502.17139) | I3 | W1 | Code generation acceleration | S1: Inference acceleration for code generation |
| ⭐ Speculative Decoding for Verilog | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2503.14153) | I3 | W2 | Speculative decoding for hardware code | S1: Speculative decoding for hardware code |
| ⭐ FrugalGPT: How to Use LLMs While Reducing Cost | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2305.05176) | I3 | W1, W2, W4 | 98% cost reduction via cascade | S2: General LLM cascade framework |
| ⭐ RouteLLM: Learning to Route LLMs with Preference Data | ICLR | 2025 | [arXiv](https://arxiv.org/abs/2406.18665) \| [OpenReview](https://openreview.net/forum?id=8sSqNntaMr) | I3 | W1, W2, W4 | 2× cost reduction via routing | S2: General LLM routing framework |
| ⭐ Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing | ICLR | 2024 | [arXiv](https://arxiv.org/abs/2404.14618) | I3 | W1, W4 | 40% API call reduction | S2: General hybrid routing framework |
| ⭐ AutoMix: Automatically Mixing Language Models | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2310.12963) \| [OpenReview](https://openreview.net/forum?id=e6WrwIvgzX) | I3 | W1, W2, W4 | Self-verification escalation | S2: General self-verification escalation |

### Efficient Architectures

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | NeurIPS | 2022 | [arXiv](https://arxiv.org/abs/2205.14135) | I1 | W1, W2 | Up to 6.7× throughput via IO-aware attention | S3: Adopted by StarCoder, Code Llama, DeepSeek-Coder |
| ⭐ Switch Transformers: Scaling to Trillion Parameter Models | JMLR | 2022 | [arXiv](https://arxiv.org/abs/2101.03961) | I1 | W1, W2 | MoE sparse activation, reduced active params | S3: MoE architecture adopted by DeepSeek-Coder |
| ⭐ DeepSeekMoE: Towards Ultimate Expert Specialization | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2401.06066) | I1 | W1, W2 | MoE routing efficiency | S3: MoE design used in DeepSeek-Coder family |

---

## Task-Level Efficiency

### Code Generation

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ EffiCoder: Enhancing Code Generation through Efficiency-Aware Fine-tuning | ICML | 2025 | [arXiv](https://arxiv.org/abs/2410.10209) | I2 | W1, W2 | Efficiency-aware training, correctness+runtime | S1: Efficiency-aware fine-tuning for code generation |
| ⭐ GREEN-CODE: Learning to Optimize Energy Efficiency in LLM-based Code Generation | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2501.11006) | I2 | W1 | Energy-aware code generation | S1: Energy-efficient code generation |
| ⭐ Arctic-SnowCoder: Demystifying High-Quality Data in Code Pretraining | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2409.02326) | I0 | W2 | Data quality over scale, 1.3B outperforms larger | S1: Data-efficient code pretraining |
| ⭐ Code Less, Align More: Efficient LLM Fine-tuning with Data Pruning | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2407.05040) | I0 | W2 | Data pruning for alignment | S1: Data pruning for code alignment |
| ⭐ Learn to Code Sustainably: An Empirical Study on LLM-based Green Code Generation | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2403.03344) | I2 | W1, W2 | Sustainable code generation | S1: Green code generation study |
| ⭐ Carbon Footprint Evaluation of Code Generation through LLM as a Service | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2504.01036) | I2 | W2 | Carbon footprint quantification | S1: Carbon footprint of code generation |
| ⭐ Analyzing the Energy and Accuracy of LLMs in Software Development | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2412.00329) | I2 | W1, W2 | Energy-accuracy tradeoff | S1: Energy-accuracy in software development |
| ⭐ Does Few-Shot Learning Help LLM Performance in Code Synthesis? | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2412.02906) | I0 | W1, W2 | Few-shot efficiency, example selection | S1: Few-shot for code synthesis |
| ⭐ On Inter-Dataset Code Duplication and Data Leakage in LLMs | IEEE TSE | 2024 | [arXiv](https://arxiv.org/abs/2401.07930) \| [IEEE](https://doi.org/10.1109/TSE.2024.3504286) | I0 | W2 | Deduplication for valid evaluation | S1: Code data deduplication study |
| ⭐ Scaling Laws for Code: Every Programming Language Matters | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2512.13472) | I0 | W2 | Scaling law analysis for code | S1: Scaling laws for code models |
| ⭐ Scaling Laws Behind Code Understanding Model | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2402.12813) | I0 | W2 | Scaling laws for understanding | S1: Scaling laws for code understanding |

### Code Completion & Search

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ Fast and Memory-Efficient Neural Code Completion | MSR | 2021 | [arXiv](https://arxiv.org/abs/2004.13651) | I1 | W1 | CNN-Transformer hybrid, latency reduction | S1: CNN-Transformer for code completion |
| ⭐ A Transformer-Based Approach for Smart Invocation of Automatic Code Completion | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2405.14753) | I3 | W1 | Invocation prediction, unnecessary call reduction | S1: Invocation prediction for code completion |
| ⭐ How GitHub Copilot Manages Latency | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2401.09964) | I3 | W1 | P95 latency analysis, <200ms target | S1: GitHub Copilot latency management |
| ⭐ CodeSage: Code Representation Learning At Scale | ICLR | 2024 | [arXiv](https://arxiv.org/abs/2402.01935) \| [GitHub](https://github.com/amazon-science/CodeSage) | I1 | W3 | Scalable encoder, inference efficiency | S1: Scalable code representation learning |
| ⭐ CodeTransformer: Modeling ASTs with Self-Attention | ICML Workshop | 2021 | [arXiv](https://arxiv.org/abs/2106.08929) | I1 | W2 | Scope-aware attention reduction | S1: AST-aware attention for code |
| ⭐ Seismic: Efficient Inverted Indexes for Approximate Retrieval | SIGIR | 2024 | [arXiv](https://arxiv.org/abs/2404.18812) | I4 | W3 | Sub-millisecond code search | S2: General retrieval evaluated on code search |
| ⭐ DeepCodeSeek: Real-Time API Retrieval | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2509.25716) | I4 | W3 | 2.5× latency reduction via reranker | S1: Real-time API retrieval for code |
| ⭐ Leveraging LLMs for Software Requirements Traceability | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2401.09764) | I4 | W3 | Two-stage traceability, latency reduction | S1: LLM for requirements traceability |

### Program Repair

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ FLAMES: Memory-Efficient LLMs for Program Repair | ICSE | 2026 | [arXiv](https://arxiv.org/abs/2410.16655) | I4 | W4 | 83% memory reduction | S1: Memory-efficient LLM for program repair |
| ⭐ CigaR: Cost-efficient Program Repair with LLMs | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2402.06598) | I4 | W4 | 80% cost reduction via cascade+verification | S1: Cost-efficient program repair |
| ⭐ RepairLLaMA: Efficient Representations and Fine-Tuned Adapters | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2312.15698) | I2 | W4 | LoRA-based APR, tuning cost reduction | S1: LoRA-based program repair |
| ⭐ Accelerating APR with Dual Retrieval-Augmented Fine-Tuning | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2507.10103) | I4 | W4 | RAG-augmented APR | S1: RAG-augmented program repair |
| ⭐ WilliamT: Cheap Crash-Site Program Repair | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2505.13103) | I4 | W4 | $0.00014/bug, 45.9% token reduction | S1: Cheap crash-site program repair |
| ⭐ Automated Program Repair via Conversation (ChatGPT) | ESEM | 2024 | [ACM DL](https://dl.acm.org/doi/10.1145/3650212.3680323) | I4 | W4 | $0.42/bug via conversational repair | S1: Conversational program repair |
| ⭐ ThinkRepair: Self-Directed Automated Program Repair | ISSTA | 2024 | [arXiv](https://arxiv.org/abs/2407.20898) \| [ACM DL](https://dl.acm.org/doi/10.1145/3650212.3680359) | I2 | W4 | Few-shot APR, no fine-tuning | S1: Self-directed few-shot program repair |
| ⭐ Code Repair with LLMs gives an Exploration-Exploitation Tradeoff | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2405.17503) \| [OpenReview](https://openreview.net/forum?id=o863gX6DxA) | I3 | W4 | Thompson sampling for refinement | S1: Thompson sampling for code repair |

### Vulnerability Detection

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ White-Basilisk: A Hybrid Model for Code Vulnerability Detection | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2507.08540) \| [OpenReview](https://openreview.net/forum?id=Qq3efdQp3f) | I1 | W5 | 30× parameter compression, energy reduction | S1: Hybrid model for vulnerability detection |
| ⭐ DeepDFA: Dataflow Analysis-Inspired Deep Learning | ICSE | 2024 | [arXiv](https://arxiv.org/abs/2212.08108) | I1 | W5 | 75× training speedup, 50-sample efficiency | S1: Dataflow-inspired vulnerability detection |
| ⭐ MAGNET: Meta-Path Based Attentional Graph Learning | IEEE TSE | 2023 | [arXiv](https://arxiv.org/abs/2212.14274) \| [IEEE](https://doi.org/10.1109/TSE.2023.3340267) | I1 | W5 | Meta-path attention efficiency | S1: Meta-path graph for vulnerability detection |
| ⭐ MultiGLICE: Combining GNN and Program Slicing | Computers (MDPI) | 2025 | [MDPI](https://www.mdpi.com/2073-431X/14/3/98) | I1 | W5 | Configurable analysis depth, cost-accuracy tradeoff | S1: GNN+program slicing for vulnerability detection |
| ⭐ Detecting Code Vulnerabilities with Heterogeneous GNN Training | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2502.16835) | I4 | W3, W5 | GNN vuln detection efficiency | S1: GNN for code vulnerability detection |
| ⭐ GNN-Powered Vulnerability Path Discovery in Open Source Code | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2507.17888) | I4 | W3, W5 | GNN vuln path analysis | S1: GNN for vulnerability path analysis |
| ⭐ Enhancing Software Vulnerability Detection Using CPGs and CNNs | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2503.18175) | I1 | W5 | Multi-view graph efficiency | S1: Multi-view graph for vulnerability detection |
| ⭐ Bridging Semantics and Structure for Vulnerability Detection using Hybrid Network Models | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.10321) | I4 | W3, W5 | Hybrid vuln detection | S1: Hybrid model for vulnerability detection |
| ⭐ LLM Agent for Real-World OSS Vulnerability Localization | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.02389) | I4 | W5 | Fine-grained vuln localization | S1: LLM agent for OSS vulnerability localization |
| ⭐ Enhancing Pre-Trained LMs for Vulnerability Detection via Data Augmentation | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2410.00249) | I0 | W5 | Data augmentation, 10% accuracy improvement | S1: Augmentation for vulnerability detection |

### Clone Detection

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ MAGNET: A Multi-Graph Attentional Network for Code Clone Detection | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.24241) | I4 | W3 | Multi-graph clone detection | S1: Multi-graph for code clone detection |
| ⭐ Nearest-neighbor, BERT-based, scalable clone detection | SPE | 2024 | [Paper](https://onlinelibrary.wiley.com/doi/10.1002/spe.3355) | I4 | W3 | Sub-second clone detection at scale | S1: BERT-based scalable clone detection |
| ⭐ An Empirical Study of LLM-Based Code Clone Detection | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2511.01176) | I4 | W3 | LLM-based clone detection | S1: LLM for code clone detection |

### Software Agents

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ SWE-agent: Agent-Computer Interfaces Enable Automated SE | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2405.15793) | I4 | W4 | SWE-agent system | S1: Agent for automated software engineering |
| ⭐ OpenHands: An Open Platform for AI Software Developers | ICLR | 2025 | [arXiv](https://arxiv.org/abs/2407.16741) | I4 | W4 | OpenHands agent system | S1: Platform for AI software developers |
| ⭐ SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2601.16746) | I4 | W4 | 40–60% token reduction via context pruning | S1: Context pruning for coding agents |
| ⭐ AutoCodeRover: Autonomous Program Improvement | ISSTA | 2024 | [ACM DL](https://dl.acm.org/doi/10.1145/3650212.3680384) | I4 | W4 | <$0.7/task, 30–46% solve rate | S1: Autonomous program improvement |
| ⭐ CodeAgent: Autonomous Communicative Agents for Code Review | EMNLP | 2024 | [ACL Anthology](https://aclanthology.org/2024.emnlp-main.632/) | I4 | W4 | Multi-agent collaboration | S1: Multi-agent code review |
| ⭐ RepoNavigator: RL of LLM Agents for Repository-Level Navigation | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2512.20957) | I4 | W4 | RL-based navigation, 7B outperforms 14B | S1: RL agent for repository navigation |
| ⭐ Experience-Driven Early Termination for Cost-Efficient SE Agents | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.05777) | I4 | W4 | Experience-driven early termination | S1: Early termination for SE agents |
| ⭐ Energy Efficiency in Agentic Issue Resolution with SLMs | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2512.09543) | I4 | W4 | Energy-efficient agent frameworks | S1: Energy-efficient SE agent frameworks |
| ⭐ SWE-Replay: Efficient Test-Time Scaling for SE Agents | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.22129) | I4 | W4 | Trajectory recycling, token reduction | S1: Trajectory recycling for SE agents |
| ⭐ Adaptive Confidence Gating in Multi-Agent Code Generation | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.21469) | I4 | W4 | Confidence-based routing, fewer LLM calls | S1: Confidence-based routing for code generation |
| ⭐ Scaling Test-Time Compute for Software Engineering | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2502.13767) | I3 | W4 | Test-time compute scaling for SE | S1: Test-time compute scaling for SE |
| ⭐ Enhancing SE Agents via Scaling Test-Time Compute | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2503.07890) | I3 | W4 | Test-time scaling for agents | S1: Test-time scaling for SE agents |
| ⭐ Self-Refine: Iterative Refinement with Self-Feedback | NeurIPS | 2023 | [arXiv](https://arxiv.org/abs/2303.17651) | I3 | W2, W4 | 5–40% improvement via self-critique | S2: General self-refinement evaluated on code |
| ⭐ Reflexion: Language Agents with Verbal Reinforcement Learning | NeurIPS | 2023 | [arXiv](https://arxiv.org/abs/2303.11366) | I3 | W4 | 91% pass@1 via episodic memory | S2: General verbal RL evaluated on HumanEval |
| ⭐ Teaching Large Language Models to Self-Debug | ICLR | 2024 | [arXiv](https://arxiv.org/abs/2304.05128) \| [OpenReview](https://openreview.net/forum?id=KuPixIqPiq) | I3 | W2, W4 | 12% improvement via self-debugging | S1: Teaching LLMs to debug their own code |
| ⭐ SWE-Effi: Re-Evaluating Under Resource Constraints | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2509.09853) | I3 | W4 | Agent efficiency under resource constraints | S1: SE agent efficiency under resource constraints |
| ⭐ FuseSearch: Learning Adaptive Parallel Execution for Efficient Code Localization | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.19568) | I4 | W4 | 93.6% speedup, 67.7% fewer turns via adaptive parallel search | S1: Adaptive parallel code localization for SE agents |

### Test Generation

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ CodaMosa: Escaping Coverage Plateaus with Pre-trained LLMs | ICSE | 2023 | [ACM DL](https://dl.acm.org/doi/10.1109/ICSE48619.2023.00085) | I4 | W2 | Hybrid search+LLM testing, coverage improvement | S1: Hybrid search+LLM for test generation |
| ⭐ ASTER: Natural and Multi-language Unit Test Generation | ICSE SEIP | 2025 | [arXiv](https://arxiv.org/abs/2409.03093) | I4 | W2 | Multi-language test generation | S1: Multi-language unit test generation |
| ⭐ TestGenEval: Real World Unit Test Generation Benchmark | ICLR | 2025 | [arXiv](https://arxiv.org/abs/2410.00752) | I4 | W2 | Real-world test generation benchmark | S1: Real-world test generation benchmark |
| ⭐ Harnessing LLMs for Automated Software Testing: Scalable Test Case Generation | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2501.05893) | I4 | W2 | Scalable test generation | S1: Scalable test generation |
| ⭐ How well LLM-based test generation techniques perform with newer LLM versions? | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.09695) | I4 | W2 | LLM test generation scalability | S1: LLM test generation scalability |
| ⭐ CodeT: Code Generation with Generated Tests | ICLR | 2023 | [arXiv](https://arxiv.org/abs/2207.10397) | I3 | W2 | Dual execution agreement | S1: Code generation with generated tests |

---

## Efficiency-Oriented Benchmarks

Benchmarks designed with efficiency as a primary evaluation dimension.

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| ⭐ EffiBench: Benchmarking the Efficiency of Automatically Generated Code | NeurIPS | 2024 | [arXiv](https://arxiv.org/abs/2402.02037) | I3 | W2 | Generated code runtime efficiency | S1: Benchmark for generated code efficiency |
| ⭐ Learning Performance-Improving Code Edits (PIE) | ICLR | 2024 | [arXiv](https://arxiv.org/abs/2302.07867) | I3 | W2 | Performance improvement editing | S1: Performance-improving code edits |
| ⭐ SWE-Effi: Re-Evaluating Under Resource Constraints | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2509.09853) | I3 | W4 | Agent efficiency under resource constraints | S1: SE agent efficiency under resource constraints |

---

## Code Pre-trained Models

| Paper | Venue | Year | Links | Stage | Workload | Efficiency Dimension | SE Dimension |
|-------|-------|------|-------|:-----:|:--------:|----------------------|----------------------|
| CodeBERT: A Pre-Trained Model for Programming and Natural Languages | Findings of EMNLP | 2020 | [arXiv](https://arxiv.org/abs/2002.08155) \| [ACL Anthology](https://aclanthology.org/2020.findings-emnlp.139/) | I1 | W2, W3 | Code-text joint pretraining | S1: Pre-trained model for programming languages |
| GraphCodeBERT: Pre-training Code Representations with Data Flow | ICLR | 2021 | [arXiv](https://arxiv.org/abs/2009.08366) | I1 | W2, W3 | Dataflow-aware efficiency | S1: Pre-trained model for programming languages |
| UniXcoder: Unified Cross-Modal Pre-training for Code Representation | ACL | 2022 | [arXiv](https://arxiv.org/abs/2203.03850) | I1 | W2, W3 | Cross-modal efficiency | S1: Cross-modal code pre-training |
| ⭐ Code Llama: Open Foundation Models for Code | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2308.12950) | I1 | W1, W2 | Long-context handling, parameter efficiency | S1: Foundation model for code |
| ⭐ StarCoder: may the source be with you! | TMLR | 2023 | [arXiv](https://arxiv.org/abs/2305.06161) \| [OpenReview](https://openreview.net/forum?id=KoFOg41haE) | I1 | W1, W2 | Architecture efficiency, long-context | S1: Open-source code LLM |
| ⭐ DeepSeek-Coder: When the LLM Meets Programming | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2401.14196) | I1 | W1, W2 | MoE sparse activation, reduced active params | S1: MoE code LLM |
| ⭐ code2vec: Learning Distributed Representations of Code | POPL | 2019 | [Paper](https://doi.org/10.1145/3290353) | I1 | W2, W3 | Path-based representation, parameter reduction | S1: Distributed representations of code |
| ⭐ Structural Language Models of Code | ICML | 2020 | [arXiv](https://arxiv.org/abs/1910.00577) | I1 | W2, W3 | Structural representation efficiency | S1: Structural code representation |
| ⭐ AST-T5: Structure-Aware Pretraining for Code Generation and Understanding | ICML | 2024 | [arXiv](https://arxiv.org/abs/2401.03003) \| [PMLR](https://proceedings.mlr.press/v235/gong24c.html) | I1 | W2, W3 | Structure-aware efficiency | S1: Structure-aware pretraining for code |

---

## Supplementary Materials

- [METHODOLOGY.md](METHODOLOGY.md) - Detailed search methodology, query strings, and related survey list

---

## Primary Study Summary

Our survey analyzes **98 primary studies** across five lifecycle stages and five workload archetypes:

| Lifecycle Stage | Count | Description |
|-----------------|:-----:|-------------|
| I0: Data Preprocessing | 7 | Data curation, deduplication, scaling laws, few-shot example selection |
| I1: Model Design | 18 | Efficient model architectures (MoE, structure-aware, GNN-based) |
| I2: Training / Tuning | 20 | PEFT, distillation, quantization, pruning, energy-aware training |
| I3: Inference / Serving | 29 | Speculative decoding, KV-cache, test-time compute, model routing |
| I4: Deployment / System | 24 | Agent frameworks, retrieval infrastructure, task-specific deployment |

| Workload Archetype | Count | Description |
|--------------------|:-----:|-------------|
| W1: Interactive | 36 | IDE completion, chat assistance, real-time design |
| W2: Batch / CI | 31 | Test generation, static analysis, code review |
| W3: Repository-scale | 25 | Code search, clone detection, vulnerability scanning |
| W4: Agentic | 20 | Multi-step repair, automated debugging, tool-augmented development |
| W5: Safety-critical | 13 | Security auditing, compliance checks, high-assurance review |

---

## Citation

If you find this repository useful, please cite our survey:

```bibtex
@unpublished{shen2026efficient_ai4se_survey,
  title={Efficient Technology of LLMs in Software Engineering: A Survey on Models, Patterns, and Evaluation},
  author={Shen, Zongwen and Wu, Jionghan and Xu, Yidan and Liu, Xuejin and Chen, Xiang and Ge, Jidong and Li, Chuanyi and Huang, Liguo and Luo, Bin},
  note={Manuscript under review},
  year={2026},
}
```

## Contributing

We welcome contributions! Please feel free to submit pull requests to add new papers or improve the organization.

## License

This project is licensed under the MIT License.
