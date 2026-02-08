# WACV 2026

> **最后更新**： 2026-02-08 02:11:48

本页面包含 2026 年 WACV 会议的论文列表。

## 1. CSGaussian: Progressive Rate-Distortion Compression and Segmentation for 3D Gaussian Splatting

- **作者**: Yu-Jen Tseng, Chia-Hao Kao, Jing-Zhong Chen et al.
- **发布时间**: 2026-01-19
- **arXiv链接**: [arXiv:2601.12814v1](https://arxiv.org/abs/2601.12814v1)
- **说明**: Accepted at WACV 2026
- **英文摘要**: We present the first unified framework for rate-distortion-optimized compression and segmentation of 3D Gaussian Splatting (3DGS). While 3DGS has proven effective for both real-time rendering and semantic scene understanding, prior works have largely treated these tasks independently, leaving their joint consideration unexplored. Inspired by recent advances in rate-distortion-optimized 3DGS compression, this work integrates semantic learning into the compression pipeline to support decoder-side applications--such as scene editing and manipulation--that extend beyond traditional scene reconstruction and view synthesis. Our scheme features a lightweight implicit neural representation-based hyperprior, enabling efficient entropy coding of both color and semantic attributes while avoiding costly grid-based hyperprior as seen in many prior works. To facilitate compression and segmentation, we further develop compression-guided segmentation learning, consisting of quantization-aware training to enhance feature separability and a quality-aware weighting mechanism to suppress unreliable Gaussian primitives. Extensive experiments on the LERF and 3D-OVS datasets demonstrate that our approach significantly reduces transmission cost while preserving high rendering quality and strong segmentation performance.

---

