# 未知会议 2026

> **最后更新**： 2025-12-14 01:27:11

本页面包含 2026 年 未知会议 会议的论文列表。

## 1. SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting

- **作者**: Zihan Li, Tengfei Wang, Wentian Gan et al.
- **发布时间**: 2025-11-17
- **arXiv链接**: [arXiv:2511.13278v2](https://arxiv.org/abs/2511.13278v2)
- **说明**: This paper has been submitted to the 2026 ISPRS Congress
- **英文摘要**: Lightweight building surface models are crucial for digital city, navigation, and fast geospatial analytics, yet conventional multi-view geometry pipelines remain cumbersome and quality-sensitive due to their reliance on dense reconstruction, meshing, and subsequent simplification. This work presents SF-Recon, a method that directly reconstructs lightweight building surfaces from multi-view images without post-hoc mesh simplification. We first train an initial 3D Gaussian Splatting (3DGS) field to obtain a view-consistent representation. Building structure is then distilled by a normal-gradient-guided Gaussian optimization that selects primitives aligned with roof and wall boundaries, followed by multi-view edge-consistency pruning to enhance structural sharpness and suppress non-structural artifacts without external supervision. Finally, a multi-view depth-constrained Delaunay triangulation converts the structured Gaussian field into a lightweight, structurally faithful building mesh. Based on a proposed SF dataset, the experimental results demonstrate that our SF-Recon can directly reconstruct lightweight building models from multi-view imagery, achieving substantially fewer faces and vertices while maintaining computational efficiency. Website:https://lzh282140127-cell.github.io/SF-Recon-project/

---

