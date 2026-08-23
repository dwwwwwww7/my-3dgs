# MICCAI 2024

> **最后更新**： 2026-08-23 01:22:53

本页面包含 2024 年 MICCAI 会议的论文列表。

## 1. LGS: A Light-weight 4D Gaussian Splatting for Efficient Surgical Scene Reconstruction

- **作者**: Hengyu Liu, Yifan Liu, Chenxin Li, Wuyang Li, Yixuan Yuan
- **发布时间**: 2024-06-23
- **arXiv链接**: [arXiv:2406.16073v1](https://arxiv.org/abs/2406.16073v1)
- **说明**: Accepted by MICCAI 2024. Project page: https://lgs-endo.github.io/
- **英文摘要**: The advent of 3D Gaussian Splatting (3D-GS) techniques and their dynamic scene modeling variants, 4D-GS, offers promising prospects for real-time rendering of dynamic surgical scenarios. However, the prerequisite for modeling dynamic scenes by a large number of Gaussian units, the high-dimensional Gaussian attributes and the high-resolution deformation fields, all lead to serve storage issues that hinder real-time rendering in resource-limited surgical equipment. To surmount these limitations, we introduce a Lightweight 4D Gaussian Splatting framework (LGS) that can liberate the efficiency bottlenecks of both rendering and storage for dynamic endoscopic reconstruction. Specifically, to minimize the redundancy of Gaussian quantities, we propose Deformation-Aware Pruning by gauging the impact of each Gaussian on deformation. Concurrently, to reduce the redundancy of Gaussian attributes, we simplify the representation of textures and lighting in non-crucial areas by pruning the dimensions of Gaussian attributes. We further resolve the feature field redundancy caused by the high resolution of 4D neural spatiotemporal encoder for modeling dynamic scenes via a 4D feature field condensation. Experiments on public benchmarks demonstrate efficacy of LGS in terms of a compression rate exceeding 9 times while maintaining the pleasing visual quality and real-time rendering efficiency. LGS confirms a substantial step towards its application in robotic surgical services.

---

