# 3DV 2026

> **最后更新**： 2026-07-05 07:34:00

本页面包含 2026 年 3DV 会议的论文列表。

## 1. PointSplat: Compact Gaussian Splatting via Human-Centric Prediction

- **作者**: Yujie Guo, Yudong Jin, Lingteng Qiu et al.
- **发布时间**: 2026-06-30
- **arXiv链接**: [arXiv:2606.32036v1](https://arxiv.org/abs/2606.32036v1)
- **说明**: Project Page: https://zju3dv.github.io/pointsplat
- **英文摘要**: Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

---

## 2. Frequency-Aware Gaussian Splatting Decomposition

- **作者**: Yishai Lavi, Leo Segre, Shai Avidan
- **发布时间**: 2025-03-27
- **arXiv链接**: [arXiv:2503.21226v2](https://arxiv.org/abs/2503.21226v2)
- **说明**: Accepted to the International Conference on 3D Vision (3DV) 2026
- **英文摘要**: 3D Gaussian Splatting (3D-GS) enables efficient novel view synthesis, but treats all frequencies uniformly, making it difficult to separate coarse structure from fine detail. Recent works have started to exploit frequency signals, but lack explicit frequency decomposition of the 3D representation itself. We propose a frequency-aware decomposition that organizes 3D Gaussians into groups corresponding to Laplacian-pyramid subbands of the input images. Each group is trained with spatial frequency regularization to confine it to its target frequency, while higher-frequency bands use signed residual colors to capture fine details that may be missed by lower-frequency reconstructions. A progressive coarse-to-fine training schedule stabilizes the decomposition. Our method achieves state-of-the-art reconstruction quality and rendering speed among all LOD-capable methods. In addition to improved interpretability, our method enables dynamic level-of-detail rendering, progressive streaming, foveated rendering, promptable 3D focus, and artistic filtering. Our code will be made publicly available.

---

