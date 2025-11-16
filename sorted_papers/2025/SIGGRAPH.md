# SIGGRAPH 2025

> **最后更新**： 2025-11-16 09:25:49

本页面包含 2025 年 SIGGRAPH 会议的论文列表。

## 1. AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting

- **作者**: Gurutva Patle, Nilay Girgaonkar, Nagabhushan Somraj, Rajiv Soundararajan
- **发布时间**: 2025-09-13
- **arXiv链接**: [arXiv:2509.11003v2](https://arxiv.org/abs/2509.11003v2)
- **说明**: SIGGRAPH Asia 2025
- **英文摘要**: 3D Gaussian Splatting (3DGS) has shown impressive results in real-time novel view synthesis. However, it often struggles under sparse-view settings, producing undesirable artifacts such as floaters, inaccurate geometry, and overfitting due to limited observations. We find that a key contributing factor is uncontrolled densification, where adding Gaussian primitives rapidly without guidance can harm geometry and cause artifacts. We propose AD-GS, a novel alternating densification framework that interleaves high and low densification phases. During high densification, the model densifies aggressively, followed by photometric loss based training to capture fine-grained scene details. Low densification then primarily involves aggressive opacity pruning of Gaussians followed by regularizing their geometry through pseudo-view consistency and edge-aware depth smoothness. This alternating approach helps reduce overfitting by carefully controlling model capacity growth while progressively refining the scene representation. Extensive experiments on challenging datasets demonstrate that AD-GS significantly improves rendering quality and geometric consistency compared to existing methods. The source code for our model can be found on our project page: https://gurutvapatle.github.io/publications/2025/ADGS.html .

---

