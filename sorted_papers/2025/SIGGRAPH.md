# SIGGRAPH 2025

> **最后更新**： 2026-06-21 03:41:08

本页面包含 2025 年 SIGGRAPH 会议的论文列表。

## 1. Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction

- **作者**: Ziyu Zhang, Tianle Liu, Diantao Tu, Shuhan Shen
- **发布时间**: 2026-01-27
- **arXiv链接**: [arXiv:2601.19489v2](https://arxiv.org/abs/2601.19489v2)
- **说明**: First Rank of SIGGRAPH Asia 2025 3DGS Challenge. Code available at https://github.com/will-zzy/siggraph_asia
- **英文摘要**: We present a fast 3DGS reconstruction pipeline designed to converge within one minute, developed for the SIGGRAPH Asia 3DGS Fast Reconstruction Challenge. The challenge consists of an initial round using SLAM-generated camera poses (with noisy trajectories) and a final round using COLMAP poses (highly accurate). To robustly handle these heterogeneous settings, we develop a two-stage solution. In the first round, we use reverse per-Gaussian parallel optimization and compact forward splatting based on Taming-GS and Speedy-splat, load-balanced tiling, an anchor-based Neural-Gaussian representation enabling rapid convergence with fewer learnable parameters, initialization from monocular depth and partially from feed-forward 3DGS models, and a global pose refinement module for noisy SLAM trajectories. In the final round, the accurate COLMAP poses change the optimization landscape; we disable pose refinement, revert from Neural-Gaussians back to standard 3DGS to eliminate MLP inference overhead, introduce multi-view consistency-guided Gaussian splitting inspired by Fast-GS, and introduce a depth estimator to supervise the rendered depth. Together, these techniques enable high-fidelity reconstruction under a strict one-minute budget. Our method achieved the top performance with a PSNR of 28.43 and ranked first in the competition.

---

## 2. AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting

- **作者**: Gurutva Patle, Nilay Girgaonkar, Nagabhushan Somraj, Rajiv Soundararajan
- **发布时间**: 2025-09-13
- **arXiv链接**: [arXiv:2509.11003v2](https://arxiv.org/abs/2509.11003v2)
- **说明**: SIGGRAPH Asia 2025
- **英文摘要**: 3D Gaussian Splatting (3DGS) has shown impressive results in real-time novel view synthesis. However, it often struggles under sparse-view settings, producing undesirable artifacts such as floaters, inaccurate geometry, and overfitting due to limited observations. We find that a key contributing factor is uncontrolled densification, where adding Gaussian primitives rapidly without guidance can harm geometry and cause artifacts. We propose AD-GS, a novel alternating densification framework that interleaves high and low densification phases. During high densification, the model densifies aggressively, followed by photometric loss based training to capture fine-grained scene details. Low densification then primarily involves aggressive opacity pruning of Gaussians followed by regularizing their geometry through pseudo-view consistency and edge-aware depth smoothness. This alternating approach helps reduce overfitting by carefully controlling model capacity growth while progressively refining the scene representation. Extensive experiments on challenging datasets demonstrate that AD-GS significantly improves rendering quality and geometric consistency compared to existing methods. The source code for our model can be found on our project page: https://gurutvapatle.github.io/publications/2025/ADGS.html .

---

