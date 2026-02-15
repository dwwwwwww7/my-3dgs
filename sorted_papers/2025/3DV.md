# 3DV 2025

> **最后更新**： 2026-02-15 01:58:35

本页面包含 2025 年 3DV 会议的论文列表。

## 1. LapisGS: Layered Progressive 3D Gaussian Splatting for Adaptive Streaming

- **作者**: Yuang Shi, Géraldine Morin, Simone Gasparini, Wei Tsang Ooi
- **发布时间**: 2024-08-27
- **arXiv链接**: [arXiv:2408.14823v2](https://arxiv.org/abs/2408.14823v2)
- **说明**: 3DV 2025; Project Page: https://yuang-ian.github.io/lapisgs/ ; Code: https://github.com/nus-vv-streams/lapis-gs
- **英文摘要**: The rise of Extended Reality (XR) requires efficient streaming of 3D online worlds, challenging current 3DGS representations to adapt to bandwidth-constrained environments. This paper proposes LapisGS, a layered 3DGS that supports adaptive streaming and progressive rendering. Our method constructs a layered structure for cumulative representation, incorporates dynamic opacity optimization to maintain visual fidelity, and utilizes occupancy maps to efficiently manage Gaussian splats. This proposed model offers a progressive representation supporting a continuous rendering quality adapted for bandwidth-aware streaming. Extensive experiments validate the effectiveness of our approach in balancing visual fidelity with the compactness of the model, with up to 50.71% improvement in SSIM, 286.53% improvement in LPIPS with 23% of the original model size, and shows its potential for bandwidth-adapted 3D streaming and rendering applications.

---

## 2. SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting

- **作者**: Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi
- **发布时间**: 2023-11-30
- **arXiv链接**: [arXiv:2312.00206v3](https://arxiv.org/abs/2312.00206v3)
- **说明**: Version accepted to 3DV 2025. Project page: https://github.com/ForMyCat/SparseGS
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently enabled real-time rendering of unbounded 3D scenes for novel view synthesis. However, this technique requires dense training views to accurately reconstruct 3D geometry. A limited number of input views will significantly degrade reconstruction quality, resulting in artifacts such as "floaters" and "background collapse" at unseen viewpoints. In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views. SparseGS incorporates depth priors, novel depth rendering techniques, and a pruning heuristic to mitigate floater artifacts, alongside an Unseen Viewpoint Regularization module to alleviate background collapses. Our extensive evaluations on the Mip-NeRF360, LLFF, and DTU datasets demonstrate that SparseGS achieves high-quality reconstruction in both unbounded and forward-facing scenarios, with as few as 12 and 3 input images, respectively, while maintaining fast training and real-time rendering capabilities.

---

