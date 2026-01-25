# 未知会议 2026

> **最后更新**： 2026-01-25 01:32:49

本页面包含 2026 年 未知会议 会议的论文列表。

## 1. LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting

- **作者**: Yuhan Chen, Wenxuan Yu, Guofa Li et al.
- **发布时间**: 2026-01-22
- **arXiv链接**: [arXiv:2601.15772v1](https://arxiv.org/abs/2601.15772v1)
- **英文摘要**: 2D Gaussian Splatting (2DGS) is an emerging explicit scene representation method with significant potential for image compression due to high fidelity and high compression ratios. However, existing low-light enhancement algorithms operate predominantly within the pixel domain. Processing 2DGS-compressed images necessitates a cumbersome decompression-enhancement-recompression pipeline, which compromises efficiency and introduces secondary degradation. To address these limitations, we propose LL-GaussianImage, the first zero-shot unsupervised framework designed for low-light enhancement directly within the 2DGS compressed representation domain. Three primary advantages are offered by this framework. First, a semantic-guided Mixture-of-Experts enhancement framework is designed. Dynamic adaptive transformations are applied to the sparse attribute space of 2DGS using rendered images as guidance to enable compression-as-enhancement without full decompression to a pixel grid. Second, a multi-objective collaborative loss function system is established to strictly constrain smoothness and fidelity during enhancement, suppressing artifacts while improving visual quality. Third, a two-stage optimization process is utilized to achieve reconstruction-as-enhancement. The accuracy of the base representation is ensured through single-scale reconstruction and network robustness is enhanced. High-quality enhancement of low-light images is achieved while high compression ratios are maintained. ...

---

## 2. POTR: Post-Training 3DGS Compression

- **作者**: Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael
- **发布时间**: 2026-01-21
- **arXiv链接**: [arXiv:2601.14821v1](https://arxiv.org/abs/2601.14821v1)
- **说明**: 15 pages, 12 figures. Submitted to IEEE TCSVT, under review
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a promising contender to Neural Radiance Fields (NeRF) in 3D scene reconstruction and real-time novel view synthesis. 3DGS outperforms NeRF in training and inference speed but has substantially higher storage requirements. To remedy this downside, we propose POTR, a post-training 3DGS codec built on two novel techniques. First, POTR introduces a novel pruning approach that uses a modified 3DGS rasterizer to efficiently calculate every splat's individual removal effect simultaneously. This technique results in 2-4x fewer splats than other post-training pruning techniques and as a result also significantly accelerates inference with experiments demonstrating 1.5-2x faster inference than other compressed models. Second, we propose a novel method to recompute lighting coefficients, significantly reducing their entropy without using any form of training. Our fast and highly parallel approach especially increases AC lighting coefficient sparsity, with experiments demonstrating increases from 70% to 97%, with minimal loss in quality. Finally, we extend POTR with a simple fine-tuning scheme to further enhance pruning, inference, and rate-distortion performance. Experiments demonstrate that POTR, even without fine-tuning, consistently outperforms all other post-training compression techniques in both rate-distortion performance and inference speed.

---

## 3. Structured Image-based Coding for Efficient Gaussian Splatting Compression

- **作者**: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz
- **发布时间**: 2026-01-20
- **arXiv链接**: [arXiv:2601.14510v2](https://arxiv.org/abs/2601.14510v2)
- **英文摘要**: Gaussian Splatting (GS) has recently emerged as a state-of-the-art representation for radiance fields, combining real-time rendering with high visual fidelity. However, GS models require storing millions of parameters, leading to large file sizes that impair their use in practical multimedia systems. To address this limitation, this paper introduces GS Image-based Compression (GSICO), a novel GS codec that efficiently compresses pre-trained GS models while preserving perceptual fidelity. The core contribution lies in a mapping procedure that arranges GS parameters into structured images, guided by a novel algorithm that enhances spatial coherence. These GS parameter images are then encoded using a conventional image codec. Experimental evaluations on Tanks and Temples, Deep Blending, and Mip-NeRF360 datasets show that GSICO achieves average compression factors of 20.2x with minimal loss in visual quality, as measured by PSNR, SSIM, and LPIPS. Compared with state-of-the-art GS compression methods, the proposed codec consistently yields superior rate-distortion (RD) trade-offs.

---

## 4. TIDI-GS: Floater Suppression in 3D Gaussian Splatting for Enhanced Indoor Scene Fidelity

- **作者**: Sooyeun Yang, Cheyul Im, Jee Won Lee, Jongseong Brad Choi
- **发布时间**: 2026-01-14
- **arXiv链接**: [arXiv:2601.09291v2](https://arxiv.org/abs/2601.09291v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a technique to create high-quality, real-time 3D scenes from images. This method often produces visual artifacts known as floaters--nearly transparent, disconnected elements that drift in space away from the actual surface. This geometric inaccuracy undermines the reliability of these models for practical applications, which is critical. To address this issue, we introduce TIDI-GS, a new training framework designed to eliminate these floaters. A key benefit of our approach is that it functions as a lightweight plugin for the standard 3DGS pipeline, requiring no major architectural changes and adding minimal overhead to the training process. The core of our method is a floater pruning algorithm--TIDI--that identifies and removes floaters based on several criteria: their consistency across multiple viewpoints, their spatial relationship to other elements, and an importance score learned during training. The framework includes a mechanism to preserve fine details, ensuring that important high-frequency elements are not mistakenly removed. This targeted cleanup is supported by a monocular depth-based loss function that helps improve the overall geometric structure of the scene. Our experiments demonstrate that TIDI-GS improves both the perceptual quality and geometric integrity of reconstructions, transforming them into robust digital assets, suitable for high-fidelity applications.

---

## 5. Sketch&Patch++: Efficient Structure-Aware 3D Gaussian Representation

- **作者**: Yuang Shi, Géraldine Morin, Simone Gasparini, Wei Tsang Ooi
- **发布时间**: 2026-01-08
- **arXiv链接**: [arXiv:2601.05394v2](https://arxiv.org/abs/2601.05394v2)
- **英文摘要**: We observe that Gaussians exhibit distinct roles and characteristics analogous to traditional artistic techniques -- like how artists first sketch outlines before filling in broader areas with color, some Gaussians capture high-frequency features such as edges and contours, while others represent broader, smoother regions analogous to brush strokes that add volume and depth. Based on this observation, we propose a hybrid representation that categorizes Gaussians into (i) Sketch Gaussians, which represent high-frequency, boundary-defining features, and (ii) Patch Gaussians, which cover low-frequency, smooth regions. This semantic separation naturally enables layered progressive streaming, where the compact Sketch Gaussians establish the structural skeleton before Patch Gaussians incrementally refine volumetric detail.   In this work, we extend our previous method to arbitrary 3D scenes by proposing a novel hierarchical adaptive categorization framework that operates directly on the 3DGS representation. Our approach employs multi-criteria density-based clustering, combined with adaptive quality-driven refinement. This method eliminates dependency on external 3D line primitives while ensuring optimal parametric encoding effectiveness. Our comprehensive evaluation across diverse scenes, including both man-made and natural environments, demonstrates that our method achieves up to 1.74 dB improvement in PSNR, 6.7% in SSIM, and 41.4% in LPIPS at equivalent model sizes compared to un...

---

## 6. SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting

- **作者**: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang
- **发布时间**: 2026-01-07
- **arXiv链接**: [arXiv:2601.04348v1](https://arxiv.org/abs/2601.04348v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting have allowed for real-time, high-fidelity novel view synthesis. Nonetheless, these models have significant storage requirements for large and medium-sized scenes, hindering their deployment over cloud and streaming services. Some of the most recent progressive compression techniques for these models rely on progressive masking and scalar quantization techniques to reduce the bitrate of Gaussian attributes using spatial context models. While effective, scalar quantization may not optimally capture the correlations of high-dimensional feature vectors, which can potentially limit the rate-distortion performance.   In this work, we introduce a novel progressive codec for 3D Gaussian Splatting that replaces traditional methods with a more powerful Residual Vector Quantization approach to compress the primitive features. Our key contribution is an auto-regressive entropy model, guided by a multi-resolution hash grid, that accurately predicts the conditional probability of each successive transmitted index, allowing for coarse and refinement layers to be compressed with high efficiency.

---

## 7. Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting

- **作者**: Subhankar Mishra
- **发布时间**: 2026-01-01
- **arXiv链接**: [arXiv:2601.00913v1](https://arxiv.org/abs/2601.00913v1)
- **英文摘要**: 3D Gaussian Splatting produces high-quality scene reconstructions but generates hundreds of thousands of spurious Gaussians (floaters) scattered throughout the environment. These artifacts obscure objects of interest and inflate model sizes, hindering deployment in bandwidth-constrained applications. We present Clean-GS, a method for removing background clutter and floaters from 3DGS reconstructions using sparse semantic masks. Our approach combines whitelist-based spatial filtering with color-guided validation and outlier removal to achieve 60-80\% model compression while preserving object quality. Unlike existing 3DGS pruning methods that rely on global importance metrics, Clean-GS uses semantic information from as few as 3 segmentation masks (1\% of views) to identify and remove Gaussians not belonging to the target object. Our multi-stage approach consisting of (1) whitelist filtering via projection to masked regions, (2) depth-buffered color validation, and (3) neighbor-based outlier removal isolates monuments and objects from complex outdoor scenes. Experiments on Tanks and Temples show that Clean-GS reduces file sizes from 125MB to 47MB while maintaining rendering quality, making 3DGS models practical for web deployment and AR/VR applications. Our code is available at https://github.com/smlab-niser/clean-gs

---

## 8. Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding

- **作者**: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li
- **发布时间**: 2025-12-19
- **arXiv链接**: [arXiv:2512.17528v1](https://arxiv.org/abs/2512.17528v1)
- **说明**: Accepted by DCC 2026
- **英文摘要**: Substantial Gaussian splatting format point clouds require effective compression. In this paper, we propose Voxel-GS, a simple yet highly effective framework that departs from the complex neural entropy models of prior work, instead achieving competitive performance using only a lightweight rate proxy and run-length coding. Specifically, we employ a differentiable quantization to discretize the Gaussian attributes of Scaffold-GS. Subsequently, a Laplacian-based rate proxy is devised to impose an entropy constraint, guiding the generation of high-fidelity and compact reconstructions. Finally, this integer-type Gaussian point cloud is compressed losslessly using Octree and run-length coding. Experiments validate that the proposed rate proxy accurately estimates the bitrate of run-length coding, enabling Voxel-GS to eliminate redundancy and optimize for a more compact representation. Consequently, our method achieves a remarkable compression ratio with significantly faster coding speeds than prior art. The code is available at https://github.com/zb12138/VoxelGS.

---

## 9. Lightweight 3D Gaussian Splatting Compression via Video Codec

- **作者**: Qi Yang, Geert Van Der Auwera, Zhu Li
- **发布时间**: 2025-12-12
- **arXiv链接**: [arXiv:2512.11186v1](https://arxiv.org/abs/2512.11186v1)
- **说明**: Accepted by DCC2026 Oral
- **英文摘要**: Current video-based GS compression methods rely on using Parallel Linear Assignment Sorting (PLAS) to convert 3D GS into smooth 2D maps, which are computationally expensive and time-consuming, limiting the application of GS on lightweight devices. In this paper, we propose a Lightweight 3D Gaussian Splatting (GS) Compression method based on Video codec (LGSCV). First, a two-stage Morton scan is proposed to generate blockwise 2D maps that are friendly for canonical video codecs in which the coding units (CU) are square blocks. A 3D Morton scan is used to permute GS primitives, followed by a 2D Morton scan to map the ordered GS primitives to 2D maps in a blockwise style. However, although the blockwise 2D maps report close performance to the PLAS map in high-bitrate regions, they show a quality collapse at medium-to-low bitrates. Therefore, a principal component analysis (PCA) is used to reduce the dimensionality of spherical harmonics (SH), and a MiniPLAS, which is flexible and fast, is designed to permute the primitives within certain block sizes. Incorporating SH PCA and MiniPLAS leads to a significant gain in rate-distortion (RD) performance, especially at medium and low bitrates. MiniPLAS can also guide the setting of the codec CU size configuration and significantly reduce encoding time. Experimental results on the MPEG dataset demonstrate that the proposed LGSCV achieves over 20% RD gain compared with state-of-the-art methods, while reducing 2D map generation time to app...

---

## 10. SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting

- **作者**: Zihan Li, Tengfei Wang, Wentian Gan et al.
- **发布时间**: 2025-11-17
- **arXiv链接**: [arXiv:2511.13278v2](https://arxiv.org/abs/2511.13278v2)
- **说明**: This paper has been submitted to the 2026 ISPRS Congress
- **英文摘要**: Lightweight building surface models are crucial for digital city, navigation, and fast geospatial analytics, yet conventional multi-view geometry pipelines remain cumbersome and quality-sensitive due to their reliance on dense reconstruction, meshing, and subsequent simplification. This work presents SF-Recon, a method that directly reconstructs lightweight building surfaces from multi-view images without post-hoc mesh simplification. We first train an initial 3D Gaussian Splatting (3DGS) field to obtain a view-consistent representation. Building structure is then distilled by a normal-gradient-guided Gaussian optimization that selects primitives aligned with roof and wall boundaries, followed by multi-view edge-consistency pruning to enhance structural sharpness and suppress non-structural artifacts without external supervision. Finally, a multi-view depth-constrained Delaunay triangulation converts the structured Gaussian field into a lightweight, structurally faithful building mesh. Based on a proposed SF dataset, the experimental results demonstrate that our SF-Recon can directly reconstruct lightweight building models from multi-view imagery, achieving substantially fewer faces and vertices while maintaining computational efficiency. Website:https://lzh282140127-cell.github.io/SF-Recon-project/

---

