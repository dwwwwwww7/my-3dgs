# CVPR 2024

> **最后更新**： 2026-08-23 01:22:53

本页面包含 2024 年 CVPR 会议的论文列表。

## 1. 3DGStream: On-the-Fly Training of 3D Gaussians for Efficient Streaming of Photo-Realistic Free-Viewpoint Videos

- **作者**: Jiakai Sun, Han Jiao, Guangyuan Li et al.
- **发布时间**: 2024-03-03
- **arXiv链接**: [arXiv:2403.01444v4](https://arxiv.org/abs/2403.01444v4)
- **说明**: CVPR 2024 Accepted (Highlight). Project Page: https://sjojok.github.io/3dgstream
- **英文摘要**: Constructing photo-realistic Free-Viewpoint Videos (FVVs) of dynamic scenes from multi-view videos remains a challenging endeavor. Despite the remarkable advancements achieved by current neural rendering techniques, these methods generally require complete video sequences for offline training and are not capable of real-time rendering. To address these constraints, we introduce 3DGStream, a method designed for efficient FVV streaming of real-world dynamic scenes. Our method achieves fast on-the-fly per-frame reconstruction within 12 seconds and real-time rendering at 200 FPS. Specifically, we utilize 3D Gaussians (3DGs) to represent the scene. Instead of the naïve approach of directly optimizing 3DGs per-frame, we employ a compact Neural Transformation Cache (NTC) to model the translations and rotations of 3DGs, markedly reducing the training time and storage required for each FVV frame. Furthermore, we propose an adaptive 3DG addition strategy to handle emerging objects in dynamic scenes. Experiments demonstrate that 3DGStream achieves competitive performance in terms of rendering speed, image quality, training time, and model storage when compared with state-of-the-art methods.

---

## 2. Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis

- **作者**: Zhan Li, Zhang Chen, Zhong Li, Yi Xu
- **发布时间**: 2023-12-28
- **arXiv链接**: [arXiv:2312.16812v2](https://arxiv.org/abs/2312.16812v2)
- **说明**: Accepted to CVPR 2024. Project page: https://oppo-us-research.github.io/SpacetimeGaussians-website/
- **英文摘要**: Novel view synthesis of dynamic scenes has been an intriguing yet challenging problem. Despite recent advancements, simultaneously achieving high-resolution photorealistic results, real-time rendering, and compact storage remains a formidable task. To address these challenges, we propose Spacetime Gaussian Feature Splatting as a novel dynamic scene representation, composed of three pivotal components. First, we formulate expressive Spacetime Gaussians by enhancing 3D Gaussians with temporal opacity and parametric motion/rotation. This enables Spacetime Gaussians to capture static, dynamic, as well as transient content within a scene. Second, we introduce splatted feature rendering, which replaces spherical harmonics with neural features. These features facilitate the modeling of view- and time-dependent appearance while maintaining small size. Third, we leverage the guidance of training error and coarse depth to sample new Gaussians in areas that are challenging to converge with existing pipelines. Experiments on several established real-world datasets demonstrate that our method achieves state-of-the-art rendering quality and speed, while retaining compact storage. At 8K resolution, our lite-version model can render at 60 FPS on an Nvidia RTX 4090 GPU. Our code is available at https://github.com/oppo-us-research/SpacetimeGaussians.

---

## 3. HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting

- **作者**: Xian Liu, Xiaohang Zhan, Jiaxiang Tang et al.
- **发布时间**: 2023-11-28
- **arXiv链接**: [arXiv:2311.17061v2](https://arxiv.org/abs/2311.17061v2)
- **说明**: Accepted by CVPR 2024, camera-ready version. Project Page: https://alvinliu0.github.io/projects/HumanGaussian
- **英文摘要**: Realistic 3D human generation from text prompts is a desirable yet challenging task. Existing methods optimize 3D representations like mesh or neural fields via score distillation sampling (SDS), which suffers from inadequate fine details or excessive training time. In this paper, we propose an efficient yet effective framework, HumanGaussian, that generates high-quality 3D humans with fine-grained geometry and realistic appearance. Our key insight is that 3D Gaussian Splatting is an efficient renderer with periodic Gaussian shrinkage or growing, where such adaptive density control can be naturally guided by intrinsic human structures. Specifically, 1) we first propose a Structure-Aware SDS that simultaneously optimizes human appearance and geometry. The multi-modal score function from both RGB and depth space is leveraged to distill the Gaussian densification and pruning process. 2) Moreover, we devise an Annealed Negative Prompt Guidance by decomposing SDS into a noisier generative score and a cleaner classifier score, which well addresses the over-saturation issue. The floating artifacts are further eliminated based on Gaussian size in a prune-only phase to enhance generation smoothness. Extensive experiments demonstrate the superior efficiency and competitive quality of our framework, rendering vivid 3D humans under diverse scenarios. Project Page: https://alvinliu0.github.io/projects/HumanGaussian

---

## 4. Text-to-3D using Gaussian Splatting

- **作者**: Zilong Chen, Feng Wang, Yikai Wang, Huaping Liu
- **发布时间**: 2023-09-28
- **arXiv链接**: [arXiv:2309.16585v4](https://arxiv.org/abs/2309.16585v4)
- **说明**: To appear at CVPR 2024. Project page: https://gsgen3d.github.io. Code: https://github.com/gsgen3d/gsgen
- **英文摘要**: Automatic text-to-3D generation that combines Score Distillation Sampling (SDS) with the optimization of volume rendering has achieved remarkable progress in synthesizing realistic 3D objects. Yet most existing text-to-3D methods by SDS and volume rendering suffer from inaccurate geometry, e.g., the Janus issue, since it is hard to explicitly integrate 3D priors into implicit 3D representations. Besides, it is usually time-consuming for them to generate elaborate 3D models with rich colors. In response, this paper proposes GSGEN, a novel method that adopts Gaussian Splatting, a recent state-of-the-art representation, to text-to-3D generation. GSGEN aims at generating high-quality 3D objects and addressing existing shortcomings by exploiting the explicit nature of Gaussian Splatting that enables the incorporation of 3D prior. Specifically, our method adopts a progressive optimization strategy, which includes a geometry optimization stage and an appearance refinement stage. In geometry optimization, a coarse representation is established under 3D point cloud diffusion prior along with the ordinary 2D SDS optimization, ensuring a sensible and 3D-consistent rough shape. Subsequently, the obtained Gaussians undergo an iterative appearance refinement to enrich texture details. In this stage, we increase the number of Gaussians by compactness-based densification to enhance continuity and improve fidelity. With these designs, our approach can generate 3D assets with delicate details ...

---

