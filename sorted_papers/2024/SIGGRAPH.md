# SIGGRAPH 2024

> **最后更新**： 2026-06-21 03:41:08

本页面包含 2024 年 SIGGRAPH 会议的论文列表。

## 1. L3DG: Latent 3D Gaussian Diffusion

- **作者**: Barbara Roessle, Norman Müller, Lorenzo Porzi et al.
- **发布时间**: 2024-10-17
- **arXiv链接**: [arXiv:2410.13530v1](https://arxiv.org/abs/2410.13530v1)
- **说明**: SIGGRAPH Asia 2024, project page: https://barbararoessle.github.io/l3dg , video: https://youtu.be/UHEEiXCYeLU
- **英文摘要**: We propose L3DG, the first approach for generative 3D modeling of 3D Gaussians through a latent 3D Gaussian diffusion formulation. This enables effective generative 3D modeling, scaling to generation of entire room-scale scenes which can be very efficiently rendered. To enable effective synthesis of 3D Gaussians, we propose a latent diffusion formulation, operating in a compressed latent space of 3D Gaussians. This compressed latent space is learned by a vector-quantized variational autoencoder (VQ-VAE), for which we employ a sparse convolutional architecture to efficiently operate on room-scale scenes. This way, the complexity of the costly generation process via diffusion is substantially reduced, allowing higher detail on object-level generation, as well as scalability to large scenes. By leveraging the 3D Gaussian representation, the generated scenes can be rendered from arbitrary viewpoints in real-time. We demonstrate that our approach significantly improves visual quality over prior work on unconditional object-level radiance field synthesis and showcase its applicability to room-scale scene generation.

---

## 2. AdR-Gaussian: Accelerating Gaussian Splatting with Adaptive Radius

- **作者**: Xinzhe Wang, Ran Yi, Lizhuang Ma
- **发布时间**: 2024-09-13
- **arXiv链接**: [arXiv:2409.08669v1](https://arxiv.org/abs/2409.08669v1)
- **说明**: SIGGRAPH Asia 2024 Conference Papers (SA Conference Papers '24), December 03-06, 2024, Tokyo, Japan
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a recent explicit 3D representation that has achieved high-quality reconstruction and real-time rendering of complex scenes. However, the rasterization pipeline still suffers from unnecessary overhead resulting from avoidable serial Gaussian culling, and uneven load due to the distinct number of Gaussian to be rendered across pixels, which hinders wider promotion and application of 3DGS. In order to accelerate Gaussian splatting, we propose AdR-Gaussian, which moves part of serial culling in Render stage into the earlier Preprocess stage to enable parallel culling, employing adaptive radius to narrow the rendering pixel range for each Gaussian, and introduces a load balancing method to minimize thread waiting time during the pixel-parallel rendering. Our contributions are threefold, achieving a rendering speed of 310% while maintaining equivalent or even better quality than the state-of-the-art. Firstly, we propose to early cull Gaussian-Tile pairs of low splatting opacity based on an adaptive radius in the Gaussian-parallel Preprocess stage, which reduces the number of affected tile through the Gaussian bounding circle, thus reducing unnecessary overhead and achieving faster rendering speed. Secondly, we further propose early culling based on axis-aligned bounding box for Gaussian splatting, which achieves a more significant reduction in ineffective expenses by accurately calculating the Gaussian size in the 2D directions. Thirdly, we propose ...

---

## 3. Robust Dual Gaussian Splatting for Immersive Human-centric Volumetric Videos

- **作者**: Yuheng Jiang, Zhehao Shen, Yu Hong et al.
- **发布时间**: 2024-09-12
- **arXiv链接**: [arXiv:2409.08353v1](https://arxiv.org/abs/2409.08353v1)
- **说明**: Accepted at SIGGRAPH Asia 2024. Project page: https://nowheretrix.github.io/DualGS/
- **英文摘要**: Volumetric video represents a transformative advancement in visual media, enabling users to freely navigate immersive virtual experiences and narrowing the gap between digital and real worlds. However, the need for extensive manual intervention to stabilize mesh sequences and the generation of excessively large assets in existing workflows impedes broader adoption. In this paper, we present a novel Gaussian-based approach, dubbed \textit{DualGS}, for real-time and high-fidelity playback of complex human performance with excellent compression ratios. Our key idea in DualGS is to separately represent motion and appearance using the corresponding skin and joint Gaussians. Such an explicit disentanglement can significantly reduce motion redundancy and enhance temporal coherence. We begin by initializing the DualGS and anchoring skin Gaussians to joint Gaussians at the first frame. Subsequently, we employ a coarse-to-fine training strategy for frame-by-frame human performance modeling. It includes a coarse alignment phase for overall motion prediction as well as a fine-grained optimization for robust tracking and high-fidelity rendering. To integrate volumetric video seamlessly into VR environments, we efficiently compress motion using entropy encoding and appearance using codec compression coupled with a persistent codebook. Our approach achieves a compression ratio of up to 120 times, only requiring approximately 350KB of storage per frame. We demonstrate the efficacy of our rep...

---

## 4. RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting

- **作者**: Zhexi Peng, Tianjia Shao, Yong Liu et al.
- **发布时间**: 2024-04-30
- **arXiv链接**: [arXiv:2404.19706v3](https://arxiv.org/abs/2404.19706v3)
- **说明**: To be published in ACM SIGGRAPH 2024
- **英文摘要**: We present Real-time Gaussian SLAM (RTG-SLAM), a real-time 3D reconstruction system with an RGBD camera for large-scale environments using Gaussian splatting. The system features a compact Gaussian representation and a highly efficient on-the-fly Gaussian optimization scheme. We force each Gaussian to be either opaque or nearly transparent, with the opaque ones fitting the surface and dominant colors, and transparent ones fitting residual colors. By rendering depth in a different way from color rendering, we let a single opaque Gaussian well fit a local surface region without the need of multiple overlapping Gaussians, hence largely reducing the memory and computation cost. For on-the-fly Gaussian optimization, we explicitly add Gaussians for three types of pixels per frame: newly observed, with large color errors, and with large depth errors. We also categorize all Gaussians into stable and unstable ones, where the stable Gaussians are expected to well fit previously observed RGBD images and otherwise unstable. We only optimize the unstable Gaussians and only render the pixels occupied by unstable Gaussians. In this way, both the number of Gaussians to be optimized and pixels to be rendered are largely reduced, and the optimization can be done in real time. We show real-time reconstructions of a variety of large scenes. Compared with the state-of-the-art NeRF-based RGBD SLAM, our system achieves comparable high-quality reconstruction but with around twice the speed and half ...

---

