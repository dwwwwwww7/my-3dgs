# ICLR 2026

> **最后更新**： 2026-03-08 01:50:50

本页面包含 2026 年 ICLR 会议的论文列表。

## 1. MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning

- **作者**: Jiarui Chen, Yikeng Chen, Yingshuang Zou et al.
- **发布时间**: 2025-09-07
- **arXiv链接**: [arXiv:2509.07021v3](https://arxiv.org/abs/2509.07021v3)
- **说明**: 20 pages, 8 figures. Accepted by ICLR 2026
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a dominant novel-view synthesis technique, but its high memory consumption severely limits its applicability on edge devices. A growing number of 3DGS compression methods have been proposed to make 3DGS more efficient, yet most only focus on storage compression and fail to address the critical bottleneck of rendering memory. To address this problem, we introduce MEGS$^{2}$, a novel memory-efficient framework that tackles this challenge by jointly optimizing two key factors: the total primitive number and the parameters per primitive, achieving unprecedented memory compression. Specifically, we replace the memory-intensive spherical harmonics with lightweight, arbitrarily oriented spherical Gaussian lobes as our color representations. More importantly, we propose a unified soft pruning framework that models primitive-number and lobe-number pruning as a single constrained optimization problem. Experiments show that MEGS$^{2}$ achieves a 50% static VRAM reduction and a 40% rendering VRAM reduction compared to existing methods, while maintaining comparable rendering quality. Project page: https://megs-2.github.io/

---

