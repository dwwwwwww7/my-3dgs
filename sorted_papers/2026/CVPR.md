# CVPR 2026

> **最后更新**： 2026-03-08 01:50:50

本页面包含 2026 年 CVPR 会议的论文列表。

## 1. Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives

- **作者**: Haoran Wang, Guoxi Huang, Fan Zhang, David Bull, Nantheera Anantrasirichai
- **发布时间**: 2026-02-27
- **arXiv链接**: [arXiv:2602.24136v1](https://arxiv.org/abs/2602.24136v1)
- **说明**: CVPR2026
- **英文摘要**: Recent significant advances in 3D scene representation have been driven by 3D Gaussian Splatting (3DGS), which has enabled real-time rendering with photorealistic quality. 3DGS often requires a large number of primitives to achieve high fidelity, leading to redundant representations and high resource consumption, thereby limiting its scalability for complex or large-scale scenes. Consequently, effective pruning strategies and more expressive primitives that can reduce redundancy while preserving visual quality are crucial for practical deployment. We propose an efficient, integrated reconstruction-aware pruning strategy that adaptively determines pruning timing and refining intervals based on reconstruction quality, thus reducing model size while enhancing rendering quality. Moreover, we introduce a 3D Difference-of-Gaussians primitive that jointly models both positive and negative densities in a single primitive, improving the expressiveness of Gaussians under compact configurations. Our method significantly improves model compactness, achieving up to 90\% reduction in Gaussian-count while delivering visual quality that is similar to, or in some cases better than, that produced by state-of-the-art methods. Code will be made publicly available.

---

## 2. Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting

- **作者**: Shuangkang Fang, I-Chao Shen, Xuanyang Zhang et al.
- **发布时间**: 2026-02-24
- **arXiv链接**: [arXiv:2602.20933v1](https://arxiv.org/abs/2602.20933v1)
- **说明**: Accepted by CVPR 2026
- **英文摘要**: Recent 3D Gaussian Splatting (3DGS) Dropout methods address overfitting under sparse-view conditions by randomly nullifying Gaussian opacities. However, we identify a neighbor compensation effect in these approaches: dropped Gaussians are often compensated by their neighbors, weakening the intended regularization. Moreover, these methods overlook the contribution of high-degree spherical harmonic coefficients (SH) to overfitting. To address these issues, we propose DropAnSH-GS, a novel anchor-based Dropout strategy. Rather than dropping Gaussians independently, our method randomly selects certain Gaussians as anchors and simultaneously removes their spatial neighbors. This effectively disrupts local redundancies near anchors and encourages the model to learn more robust, globally informed representations. Furthermore, we extend the Dropout to color attributes by randomly dropping higher-degree SH to concentrate appearance information in lower-degree SH. This strategy further mitigates overfitting and enables flexible post-training model compression via SH truncation. Experimental results demonstrate that DropAnSH-GS substantially outperforms existing Dropout methods with negligible computational overhead, and can be readily integrated into various 3DGS variants to enhance their performances. Project Website: https://sk-fun.fun/DropAnSH-GS

---

## 3. RAP: Fast Feedforward Rendering-Free Attribute-Guided Primitive Importance Score Prediction for Efficient 3D Gaussian Splatting Processing

- **作者**: Kaifa Yang, Qi Yang, Yiling Xu, Zhu Li
- **发布时间**: 2026-02-23
- **arXiv链接**: [arXiv:2602.19753v1](https://arxiv.org/abs/2602.19753v1)
- **说明**: Accepted by CVPR 2026
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a leading technology for high-quality 3D scene reconstruction. However, the iterative refinement and densification process leads to the generation of a large number of primitives, each contributing to the reconstruction to a substantially different extent. Estimating primitive importance is thus crucial, both for removing redundancy during reconstruction and for enabling efficient compression and transmission. Existing methods typically rely on rendering-based analyses, where each primitive is evaluated through its contribution across multiple camera viewpoints. However, such methods are sensitive to the number and selection of views, rely on specialized differentiable rasterizers, and have long calculation times that grow linearly with view count, making them difficult to integrate as plug-and-play modules and limiting scalability and generalization. To address these issues, we propose RAP, a fast feedforward rendering-free attribute-guided method for efficient importance score prediction in 3DGS. RAP infers primitive significance directly from intrinsic Gaussian attributes and local neighborhood statistics, avoiding rendering-based or visibility-dependent computations. A compact MLP predicts per-primitive importance scores using rendering loss, pruning-aware loss, and significance distribution regularization. After training on a small set of scenes, RAP generalizes effectively to unseen data and can be seamlessly integrated into r...

---

