# ICLR 2027

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2027 年 ICLR 会议的论文列表。

## 1. SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection

- **作者**: Hongbin Ye, Haixu Liu, Shenwei Kang et al.
- **发布时间**: 2026-10-09
- **arXiv链接**: [arXiv:2610.13503v1](https://arxiv.org/abs/2610.13503v1)
- **说明**: Under review at ICLR 2027 (main paper 9 pages, 5 figures, 2 tables; appendix included)
- **英文摘要**: Existing 3D Gaussian Splatting (3DGS) pruning methods primarily rely on global Top-K selection based on independent importance scores, lacking regional budget control and ignoring joint deletion effects. Consequently, they cannot ensure balanced reconstruction quality across a scene. We propose SplatQ, a combinatorial pruning algorithm that coordinates regional budget allocation and joint Gaussian selection under a fixed budget. SplatQ partitions Gaussians by spatial proximity and appearance similarity into size-limited blocks, decomposing global selection into subproblems of a specific size. It then smooths importance-based block retention quotas to prevent excessive budget concentration. Finally, it constructs a quadratic approximation of joint deletion effects using the responses of representative pixel colors to changes in Gaussian opacity. Individual responses, pairwise interactions, and quota penalties are incorporated into a quadratic unconstrained binary optimization (QUBO) objective, solved using simulated annealing (SA) or a coherent Ising machine (CIM) to jointly select Gaussians. Experiments on 5 benchmarks demonstrate that SplatQ outperforms state-of-the-art pruning methods in aggregate reconstruction quality, spatial quality balance, and rendering speed. Ablations confirm that budget smoothing improves local detail reconstruction, while interaction modeling improves Gaussian selection quality under a fixed budget.

---

