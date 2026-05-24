# 3DV 2026

> **最后更新**： 2026-05-24 02:54:02

本页面包含 2026 年 3DV 会议的论文列表。

## 1. Frequency-Aware Gaussian Splatting Decomposition

- **作者**: Yishai Lavi, Leo Segre, Shai Avidan
- **发布时间**: 2025-03-27
- **arXiv链接**: [arXiv:2503.21226v2](https://arxiv.org/abs/2503.21226v2)
- **说明**: Accepted to the International Conference on 3D Vision (3DV) 2026
- **英文摘要**: 3D Gaussian Splatting (3D-GS) enables efficient novel view synthesis, but treats all frequencies uniformly, making it difficult to separate coarse structure from fine detail. Recent works have started to exploit frequency signals, but lack explicit frequency decomposition of the 3D representation itself. We propose a frequency-aware decomposition that organizes 3D Gaussians into groups corresponding to Laplacian-pyramid subbands of the input images. Each group is trained with spatial frequency regularization to confine it to its target frequency, while higher-frequency bands use signed residual colors to capture fine details that may be missed by lower-frequency reconstructions. A progressive coarse-to-fine training schedule stabilizes the decomposition. Our method achieves state-of-the-art reconstruction quality and rendering speed among all LOD-capable methods. In addition to improved interpretability, our method enables dynamic level-of-detail rendering, progressive streaming, foveated rendering, promptable 3D focus, and artistic filtering. Our code will be made publicly available.

---

