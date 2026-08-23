# ICCV 2025

> **最后更新**： 2026-08-23 01:22:53

本页面包含 2025 年 ICCV 会议的论文列表。

## 1. Leveraging Learned Image Prior for 3D Gaussian Compression

- **作者**: Seungjoo Shin, Jaesik Park, Sunghyun Cho
- **发布时间**: 2025-10-16
- **arXiv链接**: [arXiv:2510.14705v1](https://arxiv.org/abs/2510.14705v1)
- **说明**: Accepted to ICCV 2025 Workshop on ECLR
- **英文摘要**: Compression techniques for 3D Gaussian Splatting (3DGS) have recently achieved considerable success in minimizing storage overhead for 3D Gaussians while preserving high rendering quality. Despite the impressive storage reduction, the lack of learned priors restricts further advances in the rate-distortion trade-off for 3DGS compression tasks. To address this, we introduce a novel 3DGS compression framework that leverages the powerful representational capacity of learned image priors to recover compression-induced quality degradation. Built upon initially compressed Gaussians, our restoration network effectively models the compression artifacts in the image space between degraded and original Gaussians. To enhance the rate-distortion performance, we provide coarse rendering residuals into the restoration network as side information. By leveraging the supervision of restored images, the compressed Gaussians are refined, resulting in a highly compact representation with enhanced rendering performance. Our framework is designed to be compatible with existing Gaussian compression methods, making it broadly applicable across different baselines. Extensive experiments validate the effectiveness of our framework, demonstrating superior rate-distortion performance and outperforming the rendering quality of state-of-the-art 3DGS compression methods while requiring substantially less storage.

---

## 2. ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via Gaussian Splatting

- **作者**: Ruijie Zhu, Mulin Yu, Linning Xu et al.
- **发布时间**: 2025-07-21
- **arXiv链接**: [arXiv:2507.15454v1](https://arxiv.org/abs/2507.15454v1)
- **说明**: Accepted by ICCV 2025
- **英文摘要**: 3D Gaussian Splatting is renowned for its high-fidelity reconstructions and real-time novel view synthesis, yet its lack of semantic understanding limits object-level perception. In this work, we propose ObjectGS, an object-aware framework that unifies 3D scene reconstruction with semantic understanding. Instead of treating the scene as a unified whole, ObjectGS models individual objects as local anchors that generate neural Gaussians and share object IDs, enabling precise object-level reconstruction. During training, we dynamically grow or prune these anchors and optimize their features, while a one-hot ID encoding with a classification loss enforces clear semantic constraints. We show through extensive experiments that ObjectGS not only outperforms state-of-the-art methods on open-vocabulary and panoptic segmentation tasks, but also integrates seamlessly with applications like mesh extraction and scene editing. Project page: https://ruijiezhu94.github.io/ObjectGS_page

---

## 3. Curve-Aware Gaussian Splatting for 3D Parametric Curve Reconstruction

- **作者**: Zhirui Gao, Renjiao Yi, Yaqiao Dai et al.
- **发布时间**: 2025-06-26
- **arXiv链接**: [arXiv:2506.21401v3](https://arxiv.org/abs/2506.21401v3)
- **说明**: Accepted by ICCV 2025, Code: https://github.com/zhirui-gao/Curve-Gaussian
- **英文摘要**: This paper presents an end-to-end framework for reconstructing 3D parametric curves directly from multi-view edge maps. Contrasting with existing two-stage methods that follow a sequential ``edge point cloud reconstruction and parametric curve fitting'' pipeline, our one-stage approach optimizes 3D parametric curves directly from 2D edge maps, eliminating error accumulation caused by the inherent optimization gap between disconnected stages. However, parametric curves inherently lack suitability for rendering-based multi-view optimization, necessitating a complementary representation that preserves their geometric properties while enabling differentiable rendering. We propose a novel bi-directional coupling mechanism between parametric curves and edge-oriented Gaussian components. This tight correspondence formulates a curve-aware Gaussian representation, \textbf{CurveGaussian}, that enables differentiable rendering of 3D curves, allowing direct optimization guided by multi-view evidence. Furthermore, we introduce a dynamically adaptive topology optimization framework during training to refine curve structures through linearization, merging, splitting, and pruning operations. Comprehensive evaluations on the ABC dataset and real-world benchmarks demonstrate our one-stage method's superiority over two-stage alternatives, particularly in producing cleaner and more robust reconstructions. Additionally, by directly optimizing parametric curves, our method significantly reduces th...

---

## 4. CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

- **作者**: Lei Tian, Xiaomin Li, Liqian Ma et al.
- **发布时间**: 2025-05-26
- **arXiv链接**: [arXiv:2505.20469v2](https://arxiv.org/abs/2505.20469v2)
- **说明**: ICCV 2025
- **英文摘要**: Recent advances in 3D reconstruction techniques and vision-language models have fueled significant progress in 3D semantic understanding, a capability critical to robotics, autonomous driving, and virtual/augmented reality. However, methods that rely on 2D priors are prone to a critical challenge: cross-view semantic inconsistencies induced by occlusion, image blur, and view-dependent variations. These inconsistencies, when propagated via projection supervision, deteriorate the quality of 3D Gaussian semantic fields and introduce artifacts in the rendered outputs. To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues. Specifically, our approach first employs a zero-shot tracker to align a set of SAM-generated 2D masks and reliably identify their corresponding categories. Next, we utilize CLIP to extract robust semantic encodings across views. Finally, our Contrastive Codebook Learning (CCL) module distills discriminative semantic features by enforcing intra-class compactness and inter-class distinctiveness. In contrast to previous methods that directly apply CLIP to imperfect masks, our framework explicitly resolves semantic conflicts while preserving category discriminability. Extensive experiments demonstrate that CCL-LGS outperforms previous state-of-the-art methods. Our project page is available at https://epsilontl.github.io/CCL-LGS/.

---

## 5. MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes

- **作者**: Xinjie Zhang, Zhening Liu, Yifan Zhang et al.
- **发布时间**: 2024-10-17
- **arXiv链接**: [arXiv:2410.13613v3](https://arxiv.org/abs/2410.13613v3)
- **说明**: Accepted by ICCV 2025
- **英文摘要**: 4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly rasterizer, enabling rapid rendering speeds. Despite its advantages, 4DGS faces significant challenges, notably the requirement of millions of 4D Gaussians, each with extensive associated attributes, leading to substantial memory and storage cost. This paper introduces a memory-efficient framework for 4DGS. We streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. This approach eliminates the need for spherical harmonics coefficients, which typically involve up to 144 parameters in classic 4DGS, thereby creating a memory-efficient 4D Gaussian representation. Furthermore, we introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit the number of Gaussians, thus forcing our model to use as few Gaussians as possible to fit a dynamic scene well. With simple half-precision storage and zip compression, our framework achieves a storage reduction by approximately 190$\times$ and 125$\times$ on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. Meanwhile, it maintains comparable rendering speeds and sce...

---

