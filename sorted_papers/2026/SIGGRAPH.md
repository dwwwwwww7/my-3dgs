# SIGGRAPH 2026

> **最后更新**： 2026-05-17 02:44:34

本页面包含 2026 年 SIGGRAPH 会议的论文列表。

## 1. CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting

- **作者**: Daheng Yin, Yili Jin, Jianxin Shi et al.
- **发布时间**: 2026-05-10
- **arXiv链接**: [arXiv:2605.09279v1](http://arxiv.org/abs/2605.09279v1)
- **说明**: SIGGRAPH 2026 Conference Paper. Code is available at https://github.com/yindaheng98/ColorAdaptiveGaussianSplatting
- **英文摘要**: Volumetric video (VV) streaming enables real-time, immersive access to remote 3D environments, powering telepresence, ecological monitoring, and robotic teleoperation. These applications turn VV streaming into a real-time interface to remote physical environments, imposing new system-level demands for photorealistic scene representation, low-latency interaction, and robust performance under heterogeneous networks. 3D Gaussian Splatting (3DGS) has been widely used for real-time photorealistic rendering, offering superior visual quality and rendering performance, but it faces challenges due to bandwidth consumption. Furthermore, as the foundation of adaptive VV streaming, existing Levels of Detail (LoD) methods based on density are not well-suited to Gaussian representations, leading to visible gaps and severe quality degradation. Recent studies have also explored attribute compression techniques to reduce bandwidth consumption. Our preliminary studies reveal that aggressive attribute compression primarily causes color distortion, which can be effectively corrected in the rendered image using a reference image. Motivated by these findings, we propose a novel Color-Adaptive scheme for adaptive VV streaming that uses vector quantization (VQ) to establish LoDs and correct color distortions with low-resolution reference images. We further present CAGS, an adaptive VV streaming system compatible with diverse Gaussian representations, which integrates the Color-Adaptive scheme by ren...

---

