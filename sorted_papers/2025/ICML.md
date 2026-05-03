# ICML 2025

> **最后更新**： 2026-05-03 02:35:11

本页面包含 2025 年 ICML 会议的论文列表。

## 1. HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder

- **作者**: Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li
- **发布时间**: 2025-05-03
- **arXiv链接**: [arXiv:2505.01938v1](https://arxiv.org/abs/2505.01938v1)
- **说明**: Accepted by ICML2025
- **英文摘要**: Most existing 3D Gaussian Splatting (3DGS) compression schemes focus on producing compact 3DGS representation via implicit data embedding. They have long coding times and highly customized data format, making it difficult for widespread deployment. This paper presents a new 3DGS compression framework called HybridGS, which takes advantage of both compact generation and standardized point cloud data encoding. HybridGS first generates compact and explicit 3DGS data. A dual-channel sparse representation is introduced to supervise the primitive position and feature bit depth. It then utilizes a canonical point cloud encoder to perform further data compression and form standard output bitstreams. A simple and effective rate control scheme is proposed to pivot the interpretable data compression scheme. At the current stage, HybridGS does not include any modules aimed at improving 3DGS quality during generation. But experiment results show that it still provides comparable reconstruction performance against state-of-the-art methods, with evidently higher encoding and decoding speed. The code is publicly available at https://github.com/Qi-Yangsjtu/HybridGS.

---

