# ECCV 2026

> **最后更新**： 2026-06-28 03:03:07

本页面包含 2026 年 ECCV 会议的论文列表。

## 1. Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation

- **作者**: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt
- **发布时间**: 2026-06-20
- **arXiv链接**: [arXiv:2606.22197v1](https://arxiv.org/abs/2606.22197v1)
- **说明**: Accepted by ECCV 2026, project page:https://batfacewayne.github.io/Multi4D.io/
- **英文摘要**: Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: https://batfacewayne.github.io/Multi4D.io/

---

