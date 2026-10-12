# ICRA 2026

> **最后更新**： 2026-10-12 10:46:20

本页面包含 2026 年 ICRA 会议的论文列表。

## 1. GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting

- **作者**: Huiwen Xue, Kaixing Zhao, Zuheng Ming, Tingcheng Li
- **发布时间**: 2026-09-20
- **arXiv链接**: [arXiv:2609.23509v1](https://arxiv.org/abs/2609.23509v1)
- **说明**: 8 pages. Accepted to IEEE ICRA 2026
- **英文摘要**: Novel view synthesis is a key task for dynamic scene reconstruction, where high rendering speed is essential for applications such as virtual reality. Existing deformable Gaussian Splatting methods achieve high-fidelity dynamic scene modeling, but still face limitations in memory usage and rendering efficiency due to the large number of redundant Gaussians. To address these challenges, we propose Geometry-Aware Redundancy Optimization (GARO), a unified redundancy measurement framework in the adaptive density control stage of the traditional dynamic scene reconstruction pipeline. This framework first selects low-gradient candidates using an optimization activity assessment strategy, and then evaluates geometric complexity through low curvature analysis to further filter and prune redundant points, resulting in a compact and expressive Gaussian representation. Extensive experiments on synthetic and real-world datasets demonstrate that GARO achieves robust trade-offs between quality and speed, with PSNR remaining stable and rendering speed improved by 2x, validating the efficiency and effectiveness of GARO.

---

## 2. Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM

- **作者**: Leshu Li, Jie Peng, Yang Zhao
- **发布时间**: 2026-06-23
- **arXiv链接**: [arXiv:2606.24796v1](https://arxiv.org/abs/2606.24796v1)
- **说明**: 2026 IEEE International Conference on Robotics and Automation(ICRA)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at https://github.com/UMN-ZhaoLab/Pocket-SLAM.git.

---

