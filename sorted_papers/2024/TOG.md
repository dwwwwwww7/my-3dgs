# TOG 2024

> **最后更新**： 2025-12-28 01:29:40

本页面包含 2024 年 TOG 会议的论文列表。

## 1. GaussianObject: High-Quality 3D Object Reconstruction from Four Views with Gaussian Splatting

- **作者**: Chen Yang, Sikuang Li, Jiemin Fang et al.
- **发布时间**: 2024-02-15
- **arXiv链接**: [arXiv:2402.10259v4](https://arxiv.org/abs/2402.10259v4)
- **说明**: ACM Transactions on Graphics (SIGGRAPH Asia 2024). Project page: https://gaussianobject.github.io/ Code: https://github.com/chensjtu/GaussianObject
- **英文摘要**: Reconstructing and rendering 3D objects from highly sparse views is of critical importance for promoting applications of 3D vision techniques and improving user experience. However, images from sparse views only contain very limited 3D information, leading to two significant challenges: 1) Difficulty in building multi-view consistency as images for matching are too few; 2) Partially omitted or highly compressed object information as view coverage is insufficient. To tackle these challenges, we propose GaussianObject, a framework to represent and render the 3D object with Gaussian splatting that achieves high rendering quality with only 4 input images. We first introduce techniques of visual hull and floater elimination, which explicitly inject structure priors into the initial optimization process to help build multi-view consistency, yielding a coarse 3D Gaussian representation. Then we construct a Gaussian repair model based on diffusion models to supplement the omitted object information, where Gaussians are further refined. We design a self-generating strategy to obtain image pairs for training the repair model. We further design a COLMAP-free variant, where pre-given accurate camera poses are not required, which achieves competitive quality and facilitates wider applications. GaussianObject is evaluated on several challenging datasets, including MipNeRF360, OmniObject3D, OpenIllumination, and our-collected unposed images, achieving superior performance from only four vie...

---

