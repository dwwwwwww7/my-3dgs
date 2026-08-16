# CVPR 2026

> **最后更新**： 2026-08-16 01:20:46

本页面包含 2026 年 CVPR 会议的论文列表。

## 1. Z-Order Transformer for Feed-Forward Gaussian Splatting

- **作者**: Can Wang, Lei Liu, Wei Jiang, Dong Xu
- **发布时间**: 2026-05-13
- **arXiv链接**: [arXiv:2605.13465v1](https://arxiv.org/abs/2605.13465v1)
- **说明**: Accept by CVPR 2026, Oral
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in photorealistic novel view synthesis. However, traditional 3DGS relies on a slow, iterative optimization process, which limits its use in scenarios demanding real-time results. To overcome this bottleneck, recent feed-forward methods aim to predict Gaussian attributes directly from images, but they often struggle with the redundancy of Gaussian primitives and rendering quality. In this work, we introduce a transformer-based architecture specifically designed for feed-forward Gaussian Splatting. Our key insight is that spatial and semantic relationships among Gaussians can be effectively captured through a sparse attention mechanism, enabled by a Z-order strategy that organizes the unstructured Gaussian set into a spatially coherent sequence. Furthermore, we incorporate this Z-order strategy to adaptively suppress redundancy while preserving critical structural details. This allows the transformer to efficiently model context, compress Gaussian primitives, and predict Gaussian attributes in a single forward pass. Comprehensive experiments demonstrate that our method achieves fast and high-quality novel view synthesis with fewer Gaussian primitives.

---

## 2. Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction

- **作者**: Haato Watanabe, Nobuyuki Umetani
- **发布时间**: 2026-04-17
- **arXiv链接**: [arXiv:2604.15941v1](https://arxiv.org/abs/2604.15941v1)
- **说明**: Accepted to CVPR 2026
- **英文摘要**: Recent years have witnessed the rapid emergence of 3D Gaussian splatting (3DGS) as a powerful approach for 3D reconstruction and novel view synthesis. Its explicit representation with Gaussian primitives enables fast training, real-time rendering, and convenient post-processing such as editing and surface reconstruction. However, 3DGS suffers from a critical drawback: the number of primitives grows drastically for scenes with high-frequency appearance details, since each primitive can represent only a single color, requiring multiple primitives for every sharp color transition. To overcome this limitation, we propose neural Gabor splatting, which augments each Gaussian primitive with a lightweight multi-layer perceptron that models a wide range of color variations within a single primitive. To further control primitive numbers, we introduce a frequency-aware densification strategy that selects mismatch primitives for pruning and cloning based on frequency energy. Our method achieves accurate reconstruction of challenging high-frequency surfaces. We demonstrate its effectiveness through extensive experiments on both standard benchmarks, such as Mip-NeRF360 and High-Frequency datasets (e.g., checkered patterns), supported by comprehensive ablation studies.

---

## 3. PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting

- **作者**: Anh Thuan Tran, Jana Kosecka
- **发布时间**: 2026-04-10
- **arXiv链接**: [arXiv:2604.09903v1](https://arxiv.org/abs/2604.09903v1)
- **说明**: Accepted to CVPRW 2026 (3DMV)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently unlocked real-time, high-fidelity novel view synthesis by representing scenes using explicit 3D primitives. However, traditional methods often require millions of Gaussians to capture complex scenes, leading to significant memory and storage demands. Recent approaches have addressed this issue through pruning and per-scene fine-tuning of Gaussian parameters, thereby reducing the model size while maintaining visual quality. These strategies typically rely on 2D images to compute important scores followed by scene-specific optimization. In this work, we introduce PointSplat, 3D geometry-driven prune-and-refine framework that bridges previously disjoint directions of gaussian pruning and transformer refinement. Our method includes two key components: (1) an efficient geometry-driven strategy that ranks Gaussians based solely on their 3D attributes, removing reliance on 2D images during pruning stage, and (2) a dual-branch encoder that separates, re-weights geometric and appearance to avoid feature imbalance. Extensive experiments on ScanNet++ and Replica across varying sparsity levels demonstrate that PointSplat consistently achieves competitive rendering quality and superior efficiency without additional per-scene optimization.

---

## 4. Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos

- **作者**: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang
- **发布时间**: 2026-03-26
- **arXiv链接**: [arXiv:2603.25058v1](https://arxiv.org/abs/2603.25058v1)
- **说明**: Accepted to CVPR 2026
- **英文摘要**: We present an approach for high-quality dynamic Gaussian Splatting from monocular videos. To this end, we in this work go one step further beyond previous methods to explicitly model continuous position and orientation deformation of dynamic Gaussians, using an SE(3) B-spline motion bases with a compact set of control points. To improve computational efficiency while enhancing the ability to model complex motions, an adaptive control mechanism is devised to dynamically adjust the number of motion bases and control points. Besides, we develop a soft segment reconstruction strategy to mitigate long-interval motion interference, and employ a multi-view diffusion model to provide multi-view cues for avoiding overfitting to training views. Extensive experiments demonstrate that our method outperforms state-of-the-art methods in novel view synthesis. Our code is available at https://github.com/hhhddddddd/se3bsplinegs.

---

## 5. GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction

- **作者**: Di Kong, Yikai Wang, Wenjie Guo et al.
- **发布时间**: 2026-03-21
- **arXiv链接**: [arXiv:2603.20611v1](https://arxiv.org/abs/2603.20611v1)
- **说明**: Accepted by IEEE/CVF Conference on Computer Vision and Pattern Recognition 2026 (CVPR 2026)
- **英文摘要**: Slice-based volumetric imaging is widely applied and it demands representations that compress aggressively while preserving internal structure for analysis. We introduce GaussianPile, unifying 3D Gaussian splatting with an imaging system-aware focus model to address this challenge. Our proposed method introduces three key innovations: (i) a slice-aware piling strategy that positions anisotropic 3D Gaussians to model through-slice contributions, (ii) a differentiable projection operator that encodes the finite-thickness point spread function of the imaging acquisition system, and (iii) a compact encoding and joint optimization pipeline that simultaneously reconstructs and compresses the Gaussian sets. Our CUDA-based design retains the compression and real-time rendering efficiency of Gaussian primitives while preserving high-frequency internal volumetric detail. Experiments on microscopy and ultrasound datasets demonstrate that our method reduces storage and reconstruction cost, sustains diagnostic fidelity, and enables fast 2D visualization, along with 3D voxelization. In practice, it delivers high-quality results in as few as 3 minutes, up to 11x faster than NeRF-based approaches, and achieves consistent 16x compression over voxel grids, offering a practical path to deployable compression and exploration of slice-based volumetric datasets.

---

## 6. ReLaGS: Relational Language Gaussian Splatting

- **作者**: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi et al.
- **发布时间**: 2026-03-18
- **arXiv链接**: [arXiv:2603.17605v1](https://arxiv.org/abs/2603.17605v1)
- **说明**: Accepted at CVPR 2026
- **英文摘要**: Achieving unified 3D perception and reasoning across tasks such as segmentation, retrieval, and relation understanding remains challenging, as existing methods are either object-centric or rely on costly training for inter-object reasoning. We present a novel framework that constructs a hierarchical language-distilled Gaussian scene and its 3D semantic scene graph without scene-specific training. A Gaussian pruning mechanism refines scene geometry, while a robust multi-view language alignment strategy aggregates noisy 2D features into accurate 3D object embeddings. On top of this hierarchy, we build an open-vocabulary 3D scene graph with Vision Language derived annotations and Graph Neural Network-based relational reasoning. Our approach enables efficient and scalable open-vocabulary 3D reasoning by jointly modeling hierarchical semantics and inter/intra-object relationships, validated across tasks including open-vocabulary segmentation, scene graph generation, and relation-guided retrieval. Project page: https://dfki-av.github.io/ReLaGS/

---

## 7. Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives

- **作者**: Haoran Wang, Guoxi Huang, Fan Zhang, David Bull, Nantheera Anantrasirichai
- **发布时间**: 2026-02-27
- **arXiv链接**: [arXiv:2602.24136v1](https://arxiv.org/abs/2602.24136v1)
- **说明**: CVPR2026
- **英文摘要**: Recent significant advances in 3D scene representation have been driven by 3D Gaussian Splatting (3DGS), which has enabled real-time rendering with photorealistic quality. 3DGS often requires a large number of primitives to achieve high fidelity, leading to redundant representations and high resource consumption, thereby limiting its scalability for complex or large-scale scenes. Consequently, effective pruning strategies and more expressive primitives that can reduce redundancy while preserving visual quality are crucial for practical deployment. We propose an efficient, integrated reconstruction-aware pruning strategy that adaptively determines pruning timing and refining intervals based on reconstruction quality, thus reducing model size while enhancing rendering quality. Moreover, we introduce a 3D Difference-of-Gaussians primitive that jointly models both positive and negative densities in a single primitive, improving the expressiveness of Gaussians under compact configurations. Our method significantly improves model compactness, achieving up to 90\% reduction in Gaussian-count while delivering visual quality that is similar to, or in some cases better than, that produced by state-of-the-art methods. Code will be made publicly available.

---

## 8. Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting

- **作者**: Shuangkang Fang, I-Chao Shen, Xuanyang Zhang et al.
- **发布时间**: 2026-02-24
- **arXiv链接**: [arXiv:2602.20933v1](https://arxiv.org/abs/2602.20933v1)
- **说明**: Accepted by CVPR 2026
- **英文摘要**: Recent 3D Gaussian Splatting (3DGS) Dropout methods address overfitting under sparse-view conditions by randomly nullifying Gaussian opacities. However, we identify a neighbor compensation effect in these approaches: dropped Gaussians are often compensated by their neighbors, weakening the intended regularization. Moreover, these methods overlook the contribution of high-degree spherical harmonic coefficients (SH) to overfitting. To address these issues, we propose DropAnSH-GS, a novel anchor-based Dropout strategy. Rather than dropping Gaussians independently, our method randomly selects certain Gaussians as anchors and simultaneously removes their spatial neighbors. This effectively disrupts local redundancies near anchors and encourages the model to learn more robust, globally informed representations. Furthermore, we extend the Dropout to color attributes by randomly dropping higher-degree SH to concentrate appearance information in lower-degree SH. This strategy further mitigates overfitting and enables flexible post-training model compression via SH truncation. Experimental results demonstrate that DropAnSH-GS substantially outperforms existing Dropout methods with negligible computational overhead, and can be readily integrated into various 3DGS variants to enhance their performances. Project Website: https://sk-fun.fun/DropAnSH-GS

---

## 9. RAP: Fast Feedforward Rendering-Free Attribute-Guided Primitive Importance Score Prediction for Efficient 3D Gaussian Splatting Processing

- **作者**: Kaifa Yang, Qi Yang, Yiling Xu, Zhu Li
- **发布时间**: 2026-02-23
- **arXiv链接**: [arXiv:2602.19753v1](https://arxiv.org/abs/2602.19753v1)
- **说明**: Accepted by CVPR 2026
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a leading technology for high-quality 3D scene reconstruction. However, the iterative refinement and densification process leads to the generation of a large number of primitives, each contributing to the reconstruction to a substantially different extent. Estimating primitive importance is thus crucial, both for removing redundancy during reconstruction and for enabling efficient compression and transmission. Existing methods typically rely on rendering-based analyses, where each primitive is evaluated through its contribution across multiple camera viewpoints. However, such methods are sensitive to the number and selection of views, rely on specialized differentiable rasterizers, and have long calculation times that grow linearly with view count, making them difficult to integrate as plug-and-play modules and limiting scalability and generalization. To address these issues, we propose RAP, a fast feedforward rendering-free attribute-guided method for efficient importance score prediction in 3DGS. RAP infers primitive significance directly from intrinsic Gaussian attributes and local neighborhood statistics, avoiding rendering-based or visibility-dependent computations. A compact MLP predicts per-primitive importance scores using rendering loss, pruning-aware loss, and significance distribution regularization. After training on a small set of scenes, RAP generalizes effectively to unseen data and can be seamlessly integrated into r...

---

## 10. GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation

- **作者**: Tianchen Deng, Xuefeng Chen, Yi Chen et al.
- **发布时间**: 2025-12-29
- **arXiv链接**: [arXiv:2512.23180v3](https://arxiv.org/abs/2512.23180v3)
- **说明**: Accepted by CVPR 2026
- **英文摘要**: Driving World Models (DWMs) have been developing rapidly with the advances of generative models. However, existing DWMs lack 3D scene understanding capabilities and can only generate content conditioned on input data, without the ability to interpret or reason about the driving environment. Moreover, current approaches represent 3D spatial information with point cloud or BEV features do not accurately align textual information with the underlying 3D scene. To address these limitations, we propose a novel unified DWM framework based on 3D Gaussian scene representation, which enables both 3D scene understanding and multi-modal scene generation, while also enabling contextual enrichment for understanding and generation tasks. Our approach directly aligns textual information with the 3D scene by embedding rich linguistic features into each Gaussian primitive, thereby achieving early modality alignment. In addition, we design a novel task-aware language-guided sampling strategy that removes redundant 3D Gaussians and injects accurate and compact 3D tokens into LLM. Furthermore, we design a dual-condition multi-modal generation model, where the information captured by our vision-language model is leveraged as a high-level language condition in combination with a low-level image condition, jointly guiding the multi-modal generation process. We conduct comprehensive studies on the nuScenes, and NuInteract datasets to validate the effectiveness of our framework. Our method achieves st...

---

