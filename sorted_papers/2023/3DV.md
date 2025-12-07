# 3DV 2023

> **最后更新**： 2025-12-07 01:27:31

本页面包含 2023 年 3DV 会议的论文列表。

## 1. Drivable 3D Gaussian Avatars

- **作者**: Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito et al.
- **发布时间**: 2023-11-14
- **arXiv链接**: [arXiv:2311.08581v2](https://arxiv.org/abs/2311.08581v2)
- **说明**: Accepted to 3DV25 Website: https://zielon.github.io/d3ga/
- **英文摘要**: We present Drivable 3D Gaussian Avatars (D3GA), a multi-layered 3D controllable model for human bodies that utilizes 3D Gaussian primitives embedded into tetrahedral cages. The advantage of using cages compared to commonly employed linear blend skinning (LBS) is that primitives like 3D Gaussians are naturally re-oriented and their kernels are stretched via the deformation gradients of the encapsulating tetrahedron. Additional offsets are modeled for the tetrahedron vertices, effectively decoupling the low-dimensional driving poses from the extensive set of primitives to be rendered. This separation is achieved through the localized influence of each tetrahedron on 3D Gaussians, resulting in improved optimization. Using the cage-based deformation model, we introduce a compositional pipeline that decomposes an avatar into layers, such as garments, hands, or faces, improving the modeling of phenomena like garment sliding. These parts can be conditioned on different driving signals, such as keypoints for facial expressions or joint-angle vectors for garments and the body. Our experiments on two multi-view datasets with varied body shapes, clothes, and motions show higher-quality results. They surpass PSNR and SSIM metrics of other SOTA methods using the same data while offering greater flexibility and compactness.

---

