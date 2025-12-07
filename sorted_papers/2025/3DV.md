# 3DV 2025

> **最后更新**： 2025-12-07 01:27:31

本页面包含 2025 年 3DV 会议的论文列表。

## 1. Deep Polycuboid Fitting for Compact 3D Representation of Indoor Scenes

- **作者**: Gahye Lee, Hyejeong Yoon, Jungeon Kim, Seungyong Lee
- **发布时间**: 2025-03-19
- **arXiv链接**: [arXiv:2503.14912v2](https://arxiv.org/abs/2503.14912v2)
- **说明**: Accepted to 3DV 2025. For project page, see this https://waldstein94.github.io/deep-polycuboid-fitting/
- **英文摘要**: This paper presents a novel framework for compactly representing a 3D indoor scene using a set of polycuboids through a deep learning-based fitting method. Indoor scenes mainly consist of man-made objects, such as furniture, which often exhibit rectilinear geometry. This property allows indoor scenes to be represented using combinations of polycuboids, providing a compact representation that benefits downstream applications like furniture rearrangement. Our framework takes a noisy point cloud as input and first detects six types of cuboid faces using a transformer network. Then, a graph neural network is used to validate the spatial relationships of the detected faces to form potential polycuboids. Finally, each polycuboid instance is reconstructed by forming a set of boxes based on the aggregated face labels. To train our networks, we introduce a synthetic dataset encompassing a diverse range of cuboid and polycuboid shapes that reflect the characteristics of indoor scenes. Our framework generalizes well to real-world indoor scene datasets, including Replica, ScanNet, and scenes captured with an iPhone. The versatility of our method is demonstrated through practical applications, such as virtual room tours and scene editing.

---

## 2. LapisGS: Layered Progressive 3D Gaussian Splatting for Adaptive Streaming

- **作者**: Yuang Shi, Géraldine Morin, Simone Gasparini, Wei Tsang Ooi
- **发布时间**: 2024-08-27
- **arXiv链接**: [arXiv:2408.14823v2](https://arxiv.org/abs/2408.14823v2)
- **说明**: 3DV 2025; Project Page: https://yuang-ian.github.io/lapisgs/ ; Code: https://github.com/nus-vv-streams/lapis-gs
- **英文摘要**: The rise of Extended Reality (XR) requires efficient streaming of 3D online worlds, challenging current 3DGS representations to adapt to bandwidth-constrained environments. This paper proposes LapisGS, a layered 3DGS that supports adaptive streaming and progressive rendering. Our method constructs a layered structure for cumulative representation, incorporates dynamic opacity optimization to maintain visual fidelity, and utilizes occupancy maps to efficiently manage Gaussian splats. This proposed model offers a progressive representation supporting a continuous rendering quality adapted for bandwidth-aware streaming. Extensive experiments validate the effectiveness of our approach in balancing visual fidelity with the compactness of the model, with up to 50.71% improvement in SSIM, 286.53% improvement in LPIPS with 23% of the original model size, and shows its potential for bandwidth-adapted 3D streaming and rendering applications.

---

## 3. SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting

- **作者**: Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi
- **发布时间**: 2023-11-30
- **arXiv链接**: [arXiv:2312.00206v3](https://arxiv.org/abs/2312.00206v3)
- **说明**: Version accepted to 3DV 2025. Project page: https://github.com/ForMyCat/SparseGS
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently enabled real-time rendering of unbounded 3D scenes for novel view synthesis. However, this technique requires dense training views to accurately reconstruct 3D geometry. A limited number of input views will significantly degrade reconstruction quality, resulting in artifacts such as "floaters" and "background collapse" at unseen viewpoints. In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views. SparseGS incorporates depth priors, novel depth rendering techniques, and a pruning heuristic to mitigate floater artifacts, alongside an Unseen Viewpoint Regularization module to alleviate background collapses. Our extensive evaluations on the Mip-NeRF360, LLFF, and DTU datasets demonstrate that SparseGS achieves high-quality reconstruction in both unbounded and forward-facing scenarios, with as few as 12 and 3 input images, respectively, while maintaining fast training and real-time rendering capabilities.

---

