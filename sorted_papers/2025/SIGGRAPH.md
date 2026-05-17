# SIGGRAPH 2025

> **最后更新**： 2026-05-17 02:44:34

本页面包含 2025 年 SIGGRAPH 会议的论文列表。

## 1. Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction

- **作者**: Ziyu Zhang, Tianle Liu, Diantao Tu, Shuhan Shen
- **发布时间**: 2026-01-27
- **arXiv链接**: [arXiv:2601.19489v2](http://arxiv.org/abs/2601.19489v2)
- **说明**: First Rank of SIGGRAPH Asia 2025 3DGS Challenge. Code available at https://github.com/will-zzy/siggraph_asia
- **英文摘要**: We present a fast 3DGS reconstruction pipeline designed to converge within one minute, developed for the SIGGRAPH Asia 3DGS Fast Reconstruction Challenge. The challenge consists of an initial round using SLAM-generated camera poses (with noisy trajectories) and a final round using COLMAP poses (highly accurate). To robustly handle these heterogeneous settings, we develop a two-stage solution. In the first round, we use reverse per-Gaussian parallel optimization and compact forward splatting based on Taming-GS and Speedy-splat, load-balanced tiling, an anchor-based Neural-Gaussian representation enabling rapid convergence with fewer learnable parameters, initialization from monocular depth and partially from feed-forward 3DGS models, and a global pose refinement module for noisy SLAM trajectories. In the final round, the accurate COLMAP poses change the optimization landscape; we disable pose refinement, revert from Neural-Gaussians back to standard 3DGS to eliminate MLP inference overhead, introduce multi-view consistency-guided Gaussian splitting inspired by Fast-GS, and introduce a depth estimator to supervise the rendered depth. Together, these techniques enable high-fidelity reconstruction under a strict one-minute budget. Our method achieved the top performance with a PSNR of 28.43 and ranked first in the competition.

---

