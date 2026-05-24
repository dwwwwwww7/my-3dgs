# AAAI 2026

> **最后更新**： 2026-05-24 02:54:02

本页面包含 2026 年 AAAI 会议的论文列表。

## 1. GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting

- **作者**: Tiantian Li, Xinjie Zhang, Xingtong Ge et al.
- **发布时间**: 2025-12-22
- **arXiv链接**: [arXiv:2512.19108v2](https://arxiv.org/abs/2512.19108v2)
- **说明**: Accepted to AAAI 2026. Code URL:https://github.com/Sweethyh/GaussianImage_plus.git
- **英文摘要**: Implicit neural representations (INRs) have achieved remarkable success in image representation and compression, but they require substantial training time and memory. Meanwhile, recent 2D Gaussian Splatting (GS) methods (\textit{e.g.}, GaussianImage) offer promising alternatives through efficient primitive-based rendering. However, these methods require excessive Gaussian primitives to maintain high visual fidelity. To exploit the potential of GS-based approaches, we present GaussianImage++, which utilizes limited Gaussian primitives to achieve impressive representation and compression performance. Firstly, we introduce a distortion-driven densification mechanism. It progressively allocates Gaussian primitives according to signal intensity. Secondly, we employ context-aware Gaussian filters for each primitive, which assist in the densification to optimize Gaussian primitives based on varying image content. Thirdly, we integrate attribute-separated learnable scalar quantizers and quantization-aware training, enabling efficient compression of primitive attributes. Experimental results demonstrate the effectiveness of our method. In particular, GaussianImage++ outperforms GaussianImage and INRs-based COIN in representation and compression performance while maintaining real-time decoding and low memory usage.

---

