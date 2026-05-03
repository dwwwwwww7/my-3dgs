# BMVC 2025

> **最后更新**： 2026-05-03 02:35:11

本页面包含 2025 年 BMVC 会议的论文列表。

## 1. Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes

- **作者**: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann
- **发布时间**: 2024-12-07
- **arXiv链接**: [arXiv:2412.05700v2](https://arxiv.org/abs/2412.05700v2)
- **说明**: Accepted at British Machine Vision Conference (BMVC) 2025
- **英文摘要**: Recent advancements in high-fidelity dynamic scene reconstruction have leveraged dynamic 3D Gaussians and 4D Gaussian Splatting for realistic scene representation. However, to make these methods viable for real-time applications such as AR/VR, gaming, and rendering on low-power devices, substantial reductions in memory usage and improvements in rendering efficiency are required. While many state-of-the-art methods prioritize lightweight implementations, they struggle in handling {scenes with complex motions or long sequences}. In this work, we introduce Temporally Compressed 3D Gaussian Splatting (TC3DGS), a novel technique designed specifically to effectively compress dynamic 3D Gaussian representations. TC3DGS selectively prunes Gaussians based on their temporal relevance and employs gradient-aware mixed-precision quantization to dynamically compress Gaussian parameters. In addition, TC3DGS exploits an adapted version of the Ramer-Douglas-Peucker algorithm to further reduce storage by interpolating Gaussian trajectories across frames. Our experiments on multiple datasets demonstrate that TC3DGS achieves up to 67$\times$ compression with minimal or no degradation in visual quality. More results and videos are provided in the supplementary. Project Page: https://ahmad-jarrar.github.io/tc-3dgs/

---

