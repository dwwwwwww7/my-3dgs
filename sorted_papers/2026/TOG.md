# TOG 2026

> **最后更新**： 2026-04-05 02:06:34

本页面包含 2026 年 TOG 会议的论文列表。

## 1. EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting

- **作者**: Miriam Jäger, Boris Jutzi
- **发布时间**: 2026-03-06
- **arXiv链接**: [arXiv:2603.06216v1](https://arxiv.org/abs/2603.06216v1)
- **说明**: Submitted to ISPRS Journal of Photogrammetry and Remote Sensing on 20 February 2026
- **英文摘要**: We present a novel Eigenentropy-optimized neighboorhood densification strategy EntON in 3D Gaussian Splatting (3DGS) for geometrically accurate and high-quality rendered 3D reconstruction. While standard 3DGS produces Gaussians whose centers and surfaces are poorly aligned with the underlying object geometry, surface-focused reconstruction methods frequently sacrifice photometric accuracy. In contrast to the conventional densification strategy, which relies on the magnitude of the view-space position gradient, our approach introduces a geometry-aware strategy to guide adaptive splitting and pruning. Specifically, we compute the 3D shape feature Eigenentropy from the eigenvalues of the covariance matrix in the k-nearest neighborhood of each Gaussian center, which quantifies the local structural order. These Eigenentropy values are integrated into an alternating optimization framework: During the optimization process, the algorithm alternates between (i) standard gradient-based densification, which refines regions via view-space gradients, and (ii) Eigenentropy-aware densification, which preferentially densifies Gaussians in low-Eigenentropy (ordered, flat) neighborhoods to better capture fine geometric details on the object surface, and prunes those in high-Eigenentropy (disordered, spherical) regions. We provide quantitative and qualitative evaluations on two benchmark datasets: small-scale DTU dataset and large-scale TUM2TWIN dataset, covering man-made objects and urban scen...

---

