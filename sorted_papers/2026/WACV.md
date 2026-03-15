# WACV 2026

> **最后更新**： 2026-03-15 02:01:55

本页面包含 2026 年 WACV 会议的论文列表。

## 1. CSGaussian: Progressive Rate-Distortion Compression and Segmentation for 3D Gaussian Splatting

- **作者**: Yu-Jen Tseng, Chia-Hao Kao, Jing-Zhong Chen et al.
- **发布时间**: 2026-01-19
- **arXiv链接**: [arXiv:2601.12814v1](https://arxiv.org/abs/2601.12814v1)
- **说明**: Accepted at WACV 2026
- **英文摘要**: We present the first unified framework for rate-distortion-optimized compression and segmentation of 3D Gaussian Splatting (3DGS). While 3DGS has proven effective for both real-time rendering and semantic scene understanding, prior works have largely treated these tasks independently, leaving their joint consideration unexplored. Inspired by recent advances in rate-distortion-optimized 3DGS compression, this work integrates semantic learning into the compression pipeline to support decoder-side applications--such as scene editing and manipulation--that extend beyond traditional scene reconstruction and view synthesis. Our scheme features a lightweight implicit neural representation-based hyperprior, enabling efficient entropy coding of both color and semantic attributes while avoiding costly grid-based hyperprior as seen in many prior works. To facilitate compression and segmentation, we further develop compression-guided segmentation learning, consisting of quantization-aware training to enhance feature separability and a quality-aware weighting mechanism to suppress unreliable Gaussian primitives. Extensive experiments on the LERF and 3D-OVS datasets demonstrate that our approach significantly reduces transmission cost while preserving high rendering quality and strong segmentation performance.

---

## 2. LighthouseGS: Indoor Structure-aware 3D Gaussian Splatting for Panorama-Style Mobile Captures

- **作者**: Seungoh Han, Jaehoon Jang, Hyunsu Kim et al.
- **发布时间**: 2025-07-08
- **arXiv链接**: [arXiv:2507.06109v2](https://arxiv.org/abs/2507.06109v2)
- **说明**: WACV 2026
- **英文摘要**: We introduce LighthouseGS, a practical novel view synthesis framework based on 3D Gaussian Splatting that utilizes simple panorama-style captures from a single mobile device. While convenient, this rotation-dominant motion and narrow baseline make accurate camera pose and 3D point estimation challenging, especially in textureless indoor scenes. To address these challenges, LighthouseGS leverages rough geometric priors, such as mobile device camera poses and monocular depth estimation, and utilizes indoor planar structures. Specifically, we propose a new initialization method called plane scaffold assembly to generate consistent 3D points on these structures, followed by a stable pruning strategy to enhance geometry and optimization stability. Additionally, we present geometric and photometric corrections to resolve inconsistencies from motion drift and auto-exposure in mobile devices. Tested on real and synthetic indoor scenes, LighthouseGS delivers photorealistic rendering, outperforming state-of-the-art methods and enabling applications like panoramic view synthesis and object placement. Project page: https://vision3d-lab.github.io/lighthousegs/

---

