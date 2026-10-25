# ICME 2026

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2026 年 ICME 会议的论文列表。

## 1. TETRIS-4DGS: Efficient Post-Training Compression of 4D Gaussian Splatting

- **作者**: Chengzhen Wu, Kelei Liu, Sicheng Li, Lu Yu, Yiyi Liao
- **发布时间**: 2026-10-10
- **arXiv链接**: [arXiv:2610.14663v1](https://arxiv.org/abs/2610.14663v1)
- **说明**: ICME 2026
- **英文摘要**: 4D Gaussian Splatting (4DGS) has emerged as a powerful dynamic scene representation, supporting real-time high quality rendering but suffers from prohibitive storage overhead. Existing methods typically attempt to solve this by treating compression as a per-scene optimization problem, limiting generalizability and applicability where low-latency compression is required. In this work, we leverage existing image and video codecs and propose a generalized post-training compression framework for 4DGS to address these issues. Specifically, we apply importance-based adaptive quantization to Gaussians according to their importance levels, effectively refining bitrate allocation while remaining fully compatible with existing codecs. To further improve compression efficiency, we utilize the statistical properties of 4DGS and propose motion- and importance-aware packing to reorganize attributes into codec-friendly 2D maps. Our approach can achieve over 40x compression rate in seconds while maintaining high quality, facilitating the practical deployment of 4DGS.

---

