# 未知会议 2025

> **最后更新**： 2026-05-17 02:44:34

本页面包含 2025 年 未知会议 会议的论文列表。

## 1. MSGS: Multispectral 3D Gaussian Splatting

- **作者**: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang
- **发布时间**: 2026-04-14
- **arXiv链接**: [arXiv:2604.13340v1](http://arxiv.org/abs/2604.13340v1)
- **说明**: Published in IEEE ISMAR 2025 Adjunct
- **英文摘要**: We present a multispectral extension to 3D Gaussian Splatting (3DGS) for wavelength-aware view synthesis. Each Gaussian is augmented with spectral radiance, represented via per-band spherical harmonics, and optimized under a dual-loss supervision scheme combining RGB and multispectral signals. To improve rendering fidelity, we perform spectral-to-RGB conversion at the pixel level, allowing richer spectral cues to be retained during optimization. Our method is evaluated on both public and self-captured real-world datasets, demonstrating consistent improvements over the RGB-only 3DGS baseline in terms of image quality and spectral consistency. Notably, it excels in challenging scenes involving translucent materials and anisotropic reflections. The proposed approach maintains the compactness and real-time efficiency of 3DGS while laying the foundation for future integration with physically based shading models.

---

## 2. Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression

- **作者**: Xiang Liu, Yimin Zhou, Jinxiang Wang et al.
- **发布时间**: 2025-12-31
- **arXiv链接**: [arXiv:2512.24742v1](http://arxiv.org/abs/2512.24742v1)
- **代码链接**: [GitHub](https://github.com/splatwizard/splatwizard)
- **英文摘要**: The recent advent of 3D Gaussian Splatting (3DGS) has marked a significant breakthrough in real-time novel view synthesis. However, the rapid proliferation of 3DGS-based algorithms has created a pressing need for standardized and comprehensive evaluation tools, especially for compression task. Existing benchmarks often lack the specific metrics necessary to holistically assess the unique characteristics of different methods, such as rendering speed, rate distortion trade-offs memory efficiency, and geometric accuracy. To address this gap, we introduce Splatwizard, a unified benchmark toolkit designed specifically for benchmarking 3DGS compression models. Splatwizard provides an easy-to-use framework to implement new 3DGS compression model and utilize state-of-the-art techniques proposed by previous work. Besides, an integrated pipeline that automates the calculation of key performance indicators, including image-based quality metrics, chamfer distance of reconstruct mesh, rendering frame rates, and computational resource consumption is included in the framework as well. Code is available at https://github.com/splatwizard/splatwizard

---

## 3. Contour Information Aware 2D Gaussian Splatting for Image Representation

- **作者**: Masaya Takabe, Hiroshi Watanabe, Sujun Hong et al.
- **发布时间**: 2025-12-29
- **arXiv链接**: [arXiv:2512.23255v1](http://arxiv.org/abs/2512.23255v1)
- **英文摘要**: Image representation is a fundamental task in computer vision. Recently, Gaussian Splatting has emerged as an efficient representation framework, and its extension to 2D image representation enables lightweight, yet expressive modeling of visual content. While recent 2D Gaussian Splatting (2DGS) approaches provide compact storage and real-time decoding, they often produce blurry or indistinct boundaries when the number of Gaussians is small due to the lack of contour awareness. In this work, we propose a Contour Information-Aware 2D Gaussian Splatting framework that incorporates object segmentation priors into Gaussian-based image representation. By constraining each Gaussian to a specific segmentation region during rasterization, our method prevents cross-boundary blending and preserves edge structures under high compression. We also introduce a warm-up scheme to stabilize training and improve convergence. Experiments on synthetic color charts and the DAVIS dataset demonstrate that our approach achieves higher reconstruction quality around object edges compared to existing 2DGS methods. The improvement is particularly evident in scenarios with very few Gaussians, while our method still maintains fast rendering and low memory usage.

---

## 4. GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation

- **作者**: Tianchen Deng, Xuefeng Chen, Yi Chen et al.
- **发布时间**: 2025-12-29
- **arXiv链接**: [arXiv:2512.23180v2](http://arxiv.org/abs/2512.23180v2)
- **代码链接**: [GitHub](https://github.com/dtc111111/GaussianDWM)
- **英文摘要**: Driving World Models (DWMs) have been developing rapidly with the advances of generative models. However, existing DWMs lack 3D scene understanding capabilities and can only generate content conditioned on input data, without the ability to interpret or reason about the driving environment. Moreover, current approaches represent 3D spatial information with point cloud or BEV features do not accurately align textual information with the underlying 3D scene. To address these limitations, we propose a novel unified DWM framework based on 3D Gaussian scene representation, which enables both 3D scene understanding and multi-modal scene generation, while also enabling contextual enrichment for understanding and generation tasks. Our approach directly aligns textual information with the 3D scene by embedding rich linguistic features into each Gaussian primitive, thereby achieving early modality alignment. In addition, we design a novel task-aware language-guided sampling strategy that removes redundant 3D Gaussians and injects accurate and compact 3D tokens into LLM. Furthermore, we design a dual-condition multi-modal generation model, where the information captured by our vision-language model is leveraged as a high-level language condition in combination with a low-level image condition, jointly guiding the multi-modal generation process. We conduct comprehensive studies on the nuScenes, and NuInteract datasets to validate the effectiveness of our framework. Our method achieves st...

---

## 5. Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting

- **作者**: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe
- **发布时间**: 2025-12-24
- **arXiv链接**: [arXiv:2512.20927v1](http://arxiv.org/abs/2512.20927v1)
- **说明**: Will be updated
- **英文摘要**: Recent advancements in computer vision have successfully extended Open-vocabulary segmentation (OVS) to the 3D domain by leveraging 3D Gaussian Splatting (3D-GS). Despite this progress, efficiently rendering the high-dimensional features required for open-vocabulary queries poses a significant challenge. Existing methods employ codebooks or feature compression, causing information loss, thereby degrading segmentation quality. To address this limitation, we introduce Quantile Rendering (Q-Render), a novel rendering strategy for 3D Gaussians that efficiently handles high-dimensional features while maintaining high fidelity. Unlike conventional volume rendering, which densely samples all 3D Gaussians intersecting each ray, Q-Render sparsely samples only those with dominant influence along the ray. By integrating Q-Render into a generalizable 3D neural network, we also propose Gaussian Splatting Network (GS-Net), which predicts Gaussian features in a generalizable manner. Extensive experiments on ScanNet and LeRF demonstrate that our framework outperforms state-of-the-art methods, while enabling real-time rendering with an approximate ~43.7x speedup on 512-D feature maps. Code will be made publicly available.

---

## 6. Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization

- **作者**: He Zhu, Zheng Liu, Xingyang Li et al.
- **发布时间**: 2025-12-23
- **arXiv链接**: [arXiv:2512.20495v1](http://arxiv.org/abs/2512.20495v1)
- **英文摘要**: 3D Gaussian splatting (3DGS) has drawn significant attention in the architectural community recently. However, current architectural designs often overlook the 3DGS scalability, making them fragile for extremely large-scale 3DGS. Meanwhile, the VR bandwidth requirement makes it impossible to deliver high-fidelity and smooth VR content from the cloud.   We present Nebula, a coherent acceleration framework for large-scale 3DGS collaborative rendering. Instead of streaming videos, Nebula streams intermediate results after the LoD search, reducing 1925% data communication between the cloud and the client. To further enhance the motion-to-photon experience, we introduce a temporal-aware LoD search in the cloud that tames the irregular memory access and reduces redundant data access by exploiting temporal coherence across frames. On the client side, we propose a novel stereo rasterization that enables two eyes to share most computations during the stereo rendering with bit-accurate quality. With minimal hardware augmentations, Nebula achieves 2.7$\times$ motion-to-photon speedup and reduces 1925% bandwidth over lossy video streaming.

---

## 7. FLEG: Feed-Forward Language Embedded Gaussian Splatting from Any Views via Compact Semantic Representation

- **作者**: Qijian Tian, Xin Tan, Jiayu Ying et al.
- **发布时间**: 2025-12-19
- **arXiv链接**: [arXiv:2512.17541v2](http://arxiv.org/abs/2512.17541v2)
- **说明**: Project page: https://fangzhou2000.github.io/projects/fleg
- **英文摘要**: We present FLEG, a feed-forward network that reconstructs language-embedded 3D Gaussians from arbitrary views. Previous feed-forward language-embedded Gaussian reconstruction methods are restricted to a fixed number of input views and typically attach a language-aligned semantic embedding to each Gaussian, resulting in impractical input settings and semantic redundancy. In contrast, we introduce a geometry-semantic dual-branch distillation framework that enables flexible input from arbitrary multi-view images without camera parameters. We also propose a novel-view-based distillation strategy during training that mitigates overfitting to input views. In addition, we observe that semantic representations are significantly sparser than geometric ones, and per-Gaussian language embedding is unnecessary. To exploit this sparsity, we design a decoupled language embedding strategy that represents language information with a sparse set of semantic Gaussians, rather than attaching embeddings to every Gaussian. Compared with dense pixel-aligned per-Gaussian embedding schemes, our method uses only 5\% of the language embeddings while maintaining comparable semantic fidelity, effectively reducing storage costs. Extensive experiments demonstrate that FLEG outperforms state-of-the-art feed-forward reconstruction and language-embedded Gaussian methods in both reconstruction quality and language-aligned semantic representation. Project page: https://fangzhou2000.github.io/projects/fleg.

---

## 8. HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

- **作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang et al.
- **发布时间**: 2025-12-16
- **arXiv链接**: [arXiv:2512.14352v1](http://arxiv.org/abs/2512.14352v1)
- **说明**: 11 pages, 9 figures
- **英文摘要**: Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It fur...

---

## 9. Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance

- **作者**: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein
- **发布时间**: 2025-12-12
- **arXiv链接**: [arXiv:2512.11800v1](http://arxiv.org/abs/2512.11800v1)
- **英文摘要**: The recent success of 3D Gaussian Splatting (3DGS) has reshaped novel view synthesis by enabling fast optimization and real-time rendering of high-quality radiance fields. However, it relies on simplified, order-dependent alpha blending and coarse approximations of the density integral within the rasterizer, thereby limiting its ability to render complex, overlapping semi-transparent objects. In this paper, we extend rasterization-based rendering of 3D Gaussian representations with a novel method for high-fidelity transmittance computation, entirely avoiding the need for ray tracing or per-pixel sample sorting. Building on prior work in moment-based order-independent transparency, our key idea is to characterize the density distribution along each camera ray with a compact and continuous representation based on statistical moments. To this end, we analytically derive and compute a set of per-pixel moments from all contributing 3D Gaussians. From these moments, a continuous transmittance function is reconstructed for each ray, which is then independently sampled within each Gaussian. As a result, our method bridges the gap between rasterization and physical accuracy by modeling light attenuation in complex translucent media, significantly improving overall reconstruction and rendering quality.

---

## 10. YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos

- **作者**: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana
- **发布时间**: 2025-12-10
- **arXiv链接**: [arXiv:2512.09903v1](http://arxiv.org/abs/2512.09903v1)
- **英文摘要**: Visual navigation has emerged as a practical alternative to traditional robotic navigation pipelines that rely on detailed mapping and path planning. However, constructing and maintaining 3D maps is often computationally expensive and memory-intensive. We address the problem of visual navigation when exploration videos of a large environment are available. The videos serve as a visual reference, allowing a robot to retrace the explored trajectories without relying on metric maps. Our proposed method, YOPO-Nav (You Only Pass Once), encodes an environment into a compact spatial representation composed of interconnected local 3D Gaussian Splatting (3DGS) models. During navigation, the framework aligns the robot's current visual observation with this representation and predicts actions that guide it back toward the demonstrated trajectory. YOPO-Nav employs a hierarchical design: a visual place recognition (VPR) module provides coarse localization, while the local 3DGS models refine the goal and intermediate poses to generate control actions. To evaluate our approach, we introduce the YOPO-Campus dataset, comprising 4 hours of egocentric video and robot controller inputs from over 6 km of human-teleoperated robot trajectories. We benchmark recent visual navigation methods on trajectories from YOPO-Campus using a Clearpath Jackal robot. Experimental results show YOPO-Nav provides excellent performance in image-goal navigation for real-world scenes on a physical robot. The dataset a...

---

## 11. SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting

- **作者**: Seokhyun Youn, Soohyun Lee, Geonho Kim et al.
- **发布时间**: 2025-12-08
- **arXiv链接**: [arXiv:2512.07197v1](http://arxiv.org/abs/2512.07197v1)
- **说明**: The first three authors contributed equally to this work. The last two authors are co-corresponding authors. Please visit our project page at https://cmlab-korea.github.io/Awesome-Efficient-GS/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful explicit representation enabling real-time, high-fidelity 3D reconstruction and novel view synthesis. However, its practical use is hindered by the massive memory and computational demands required to store and render millions of Gaussians. These challenges become even more severe in 4D dynamic scenes. To address these issues, the field of Efficient Gaussian Splatting has rapidly evolved, proposing methods that reduce redundancy while preserving reconstruction quality. This survey provides the first unified overview of efficient 3D and 4D Gaussian Splatting techniques. For both 3D and 4D settings, we systematically categorize existing methods into two major directions, Parameter Compression and Restructuring Compression, and comprehensively summarize the core ideas and methodological trends within each category. We further cover widely used datasets, evaluation metrics, and representative benchmark comparisons. Finally, we discuss current limitations and outline promising research directions toward scalable, compact, and real-time Gaussian Splatting for both static and dynamic 3D scene representation.

---

## 12. RAVE: Rate-Adaptive Visual Encoding for 3D Gaussian Splatting

- **作者**: Hoang-Nhat Tran, Francesco Di Sario, Gabriele Spadaro, Giuseppe Valenzise, Enzo Tartaglione
- **发布时间**: 2025-12-07
- **arXiv链接**: [arXiv:2512.07052v2](http://arxiv.org/abs/2512.07052v2)
- **代码链接**: [GitHub](https://github.com/inspiros/RAVE)
- **英文摘要**: Recent advances in neural scene representations have transformed immersive multimedia, with 3D Gaussian Splatting (3DGS) enabling real-time photorealistic rendering. Despite its efficiency, 3DGS suffers from large memory requirements and costly training procedures, motivating efforts toward compression. Existing approaches, however, operate at fixed rates, limiting adaptability to varying bandwidth and device constraints. In this work, we propose a flexible compression scheme for 3DGS that supports interpolation at any rate between predefined bounds. Our method is computationally lightweight, requires no retraining for any rate, and preserves rendering quality across a broad range of operating points. Experiments demonstrate that the approach achieves efficient, high-quality compression while offering dynamic rate control, making it suitable for practical deployment in immersive applications. The code is available at https://github.com/inspiros/RAVE.

---

## 13. SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training

- **作者**: Yang Zheng, Hao Tan, Kai Zhang et al.
- **发布时间**: 2025-12-05
- **arXiv链接**: [arXiv:2512.05354v1](http://arxiv.org/abs/2512.05354v1)
- **说明**: project page https://y-zheng18.github.io/SplatPainter/
- **英文摘要**: The rise of 3D Gaussian Splatting has revolutionized photorealistic 3D asset creation, yet a critical gap remains for their interactive refinement and editing. Existing approaches based on diffusion or optimization are ill-suited for this task, as they are often prohibitively slow, destructive to the original asset's identity, or lack the precision for fine-grained control. To address this, we introduce \ourmethod, a state-aware feedforward model that enables continuous editing of 3D Gaussian assets from user-provided 2D view(s). Our method directly predicts updates to the attributes of a compact, feature-rich Gaussian representation and leverages Test-Time Training to create a state-aware, iterative workflow. The versatility of our approach allows a single architecture to perform diverse tasks, including high-fidelity local detail refinement, local paint-over, and consistent global recoloring, all at interactive speeds, paving the way for fluid and intuitive 3D content authoring.

---

## 14. TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking

- **作者**: Hanzhi Guo, Dongdong Weng, Mo Su et al.
- **发布时间**: 2025-12-01
- **arXiv链接**: [arXiv:2512.01329v1](http://arxiv.org/abs/2512.01329v1)
- **英文摘要**: Topology-consistent dynamic model sequences are essential for applications such as animation and model editing. However, existing 4D reconstruction methods face challenges in generating high-quality topology-consistent meshes. To address this, we propose a topology-aware dynamic reconstruction framework based on Gaussian Splatting. We introduce a Gaussian topological structure that explicitly encodes spatial connectivity. This structure enables topology-aware densification and pruning, preserving the manifold consistency of the Gaussian representation. Temporal regularization terms further ensure topological coherence over time, while differentiable mesh rasterization improves mesh quality. Experimental results demonstrate that our method reconstructs topology-consistent mesh sequences with significantly higher accuracy than existing approaches. Moreover, the resulting meshes enable precise 3D keypoint tracking. Project page: https://haza628.github.io/tagSplat/

---

## 15. Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation

- **作者**: An Yang, Chenyu Liu, Jun Du et al.
- **发布时间**: 2025-11-30
- **arXiv链接**: [arXiv:2512.00944v1](http://arxiv.org/abs/2512.00944v1)
- **英文摘要**: 3D Gaussian Splatting (3D-GS) has emerged as an efficient 3D representation and a promising foundation for semantic tasks like segmentation. However, existing 3D-GS-based segmentation methods typically rely on high-dimensional category features, which introduce substantial memory overhead. Moreover, fine-grained segmentation remains challenging due to label space congestion and the lack of stable multi-granularity control mechanisms. To address these limitations, we propose a coarse-to-fine binary encoding scheme for per-Gaussian category representation, which compresses each feature into a single integer via the binary-to-decimal mapping, drastically reducing memory usage. We further design a progressive training strategy that decomposes panoptic segmentation into a series of independent sub-tasks, reducing inter-class conflicts and thereby enhancing fine-grained segmentation capability. Additionally, we fine-tune opacity during segmentation training to address the incompatibility between photometric rendering and semantic segmentation, which often leads to foreground-background confusion. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art segmentation performance while significantly reducing memory consumption and accelerating inference.

---

