# ECCV 2024

> **最后更新**： 2026-07-12 02:26:50

本页面包含 2024 年 ECCV 会议的论文列表。

## 1. HAC++: Towards 100X Compression of 3D Gaussian Splatting

- **作者**: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai
- **发布时间**: 2025-01-21
- **arXiv链接**: [arXiv:2501.12255v4](http://arxiv.org/abs/2501.12255v4)
- **代码链接**: [GitHub](https://github.com/YihangChen-ee/HAC-plus)
- **说明**: Project Page: https://yihangchen-ee.github.io/project_hac++/ Code: https://github.com/YihangChen-ee/HAC-plus. This paper is a journal extension of HAC at arXiv:2403.14530 (ECCV 2024)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel view synthesis, boasting rapid rendering speed with high fidelity. However, the substantial Gaussians and their associated attributes necessitate effective compression techniques. Nevertheless, the sparse and unorganized nature of the point cloud of Gaussians (or anchors in our paper) presents challenges for compression. To achieve a compact size, we propose HAC++, which leverages the relationships between unorganized anchors and a structured hash grid, utilizing their mutual information for context modeling. Additionally, HAC++ captures intra-anchor contextual relationships to further enhance compression performance. To facilitate entropy coding, we utilize Gaussian distributions to precisely estimate the probability of each quantized attribute, where an adaptive quantization module is proposed to enable high-precision quantization of these attributes for improved fidelity restoration. Moreover, we incorporate an adaptive masking strategy to eliminate invalid Gaussians and anchors. Overall, HAC++ achieves a remarkable size reduction of over 100X compared to vanilla 3DGS when averaged on all datasets, while simultaneously improving fidelity. It also delivers more than 20X size reduction compared to Scaffold-GS. Our code is available at https://github.com/YihangChen-ee/HAC-plus.

---

## 2. MesonGS: Post-training Compression of 3D Gaussians via Efficient Attribute Transformation

- **作者**: Shuzhao Xie, Weixiang Zhang, Chen Tang et al.
- **发布时间**: 2024-09-15
- **arXiv链接**: [arXiv:2409.09756v1](http://arxiv.org/abs/2409.09756v1)
- **说明**: 18 pages, 8 figures, ECCV 2024
- **英文摘要**: 3D Gaussian Splatting demonstrates excellent quality and speed in novel view synthesis. Nevertheless, the huge file size of the 3D Gaussians presents challenges for transmission and storage. Current works design compact models to replace the substantial volume and attributes of 3D Gaussians, along with intensive training to distill information. These endeavors demand considerable training time, presenting formidable hurdles for practical deployment. To this end, we propose MesonGS, a codec for post-training compression of 3D Gaussians. Initially, we introduce a measurement criterion that considers both view-dependent and view-independent factors to assess the impact of each Gaussian point on the rendering output, enabling the removal of insignificant points. Subsequently, we decrease the entropy of attributes through two transformations that complement subsequent entropy coding techniques to enhance the file compression rate. More specifically, we first replace rotation quaternions with Euler angles; then, we apply region adaptive hierarchical transform to key attributes to reduce entropy. Lastly, we adopt finer-grained quantization to avoid excessive information loss. Moreover, a well-crafted finetune scheme is devised to restore quality. Extensive experiments demonstrate that MesonGS significantly reduces the size of 3D Gaussians while preserving competitive quality.

---

## 3. CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization

- **作者**: Jiawei Zhang, Jiahe Li, Xiaohan Yu et al.
- **发布时间**: 2024-05-20
- **arXiv链接**: [arXiv:2405.12110v2](http://arxiv.org/abs/2405.12110v2)
- **说明**: Accepted at ECCV 2024. Project page: https://jiaw-z.github.io/CoR-GS/
- **英文摘要**: 3D Gaussian Splatting (3DGS) creates a radiance field consisting of 3D Gaussians to represent a scene. With sparse training views, 3DGS easily suffers from overfitting, negatively impacting rendering. This paper introduces a new co-regularization perspective for improving sparse-view 3DGS. When training two 3D Gaussian radiance fields, we observe that the two radiance fields exhibit point disagreement and rendering disagreement that can unsupervisedly predict reconstruction quality, stemming from the randomness of densification implementation. We further quantify the two disagreements and demonstrate the negative correlation between them and accurate reconstruction, which allows us to identify inaccurate reconstruction without accessing ground-truth information. Based on the study, we propose CoR-GS, which identifies and suppresses inaccurate reconstruction based on the two disagreements: (1) Co-pruning considers Gaussians that exhibit high point disagreement in inaccurate positions and prunes them. (2) Pseudo-view co-regularization considers pixels that exhibit high rendering disagreement are inaccurate and suppress the disagreement. Results on LLFF, Mip-NeRF360, DTU, and Blender demonstrate that CoR-GS effectively regularizes the scene geometry, reconstructs the compact representations, and achieves state-of-the-art novel view synthesis quality under sparse training views.

---

## 4. End-to-End Rate-Distortion Optimized 3D Gaussian Representation

- **作者**: Henan Wang, Hanxin Zhu, Tianyu He et al.
- **发布时间**: 2024-04-09
- **arXiv链接**: [arXiv:2406.01597v2](http://arxiv.org/abs/2406.01597v2)
- **说明**: ECCV 2024
- **英文摘要**: 3D Gaussian Splatting (3DGS) has become an emerging technique with remarkable potential in 3D representation and image rendering. However, the substantial storage overhead of 3DGS significantly impedes its practical applications. In this work, we formulate the compact 3D Gaussian learning as an end-to-end Rate-Distortion Optimization (RDO) problem and propose RDO-Gaussian that can achieve flexible and continuous rate control. RDO-Gaussian addresses two main issues that exist in current schemes: 1) Different from prior endeavors that minimize the rate under the fixed distortion, we introduce dynamic pruning and entropy-constrained vector quantization (ECVQ) that optimize the rate and distortion at the same time. 2) Previous works treat the colors of each Gaussian equally, while we model the colors of different regions and materials with learnable numbers of parameters. We verify our method on both real and synthetic scenes, showcasing that RDO-Gaussian greatly reduces the size of 3D Gaussian over 40x, and surpasses existing methods in rate-distortion performance.

---

## 5. GaussianImage: 1000 FPS Image Representation and Compression by 2D Gaussian Splatting

- **作者**: Xinjie Zhang, Xingtong Ge, Tongda Xu et al.
- **发布时间**: 2024-03-13
- **arXiv链接**: [arXiv:2403.08551v5](http://arxiv.org/abs/2403.08551v5)
- **代码链接**: [GitHub](https://github.com/Xinjie-Q/GaussianImage)
- **说明**: Accepted by ECCV 2024. Project Page:https://xingtongge.github.io/GaussianImage-page/ Code: https://github.com/Xinjie-Q/GaussianImage
- **英文摘要**: Implicit neural representations (INRs) recently achieved great success in image representation and compression, offering high visual quality and fast rendering speeds with 10-1000 FPS, assuming sufficient GPU resources are available. However, this requirement often hinders their use on low-end devices with limited memory. In response, we propose a groundbreaking paradigm of image representation and compression by 2D Gaussian Splatting, named GaussianImage. We first introduce 2D Gaussian to represent the image, where each Gaussian has 8 parameters including position, covariance and color. Subsequently, we unveil a novel rendering algorithm based on accumulated summation. Remarkably, our method with a minimum of 3$\times$ lower GPU memory usage and 5$\times$ faster fitting time not only rivals INRs (e.g., WIRE, I-NGP) in representation performance, but also delivers a faster rendering speed of 1500-2000 FPS regardless of parameter size. Furthermore, we integrate existing vector quantization technique to build an image codec. Experimental results demonstrate that our codec attains rate-distortion performance comparable to compression-based INRs such as COIN and COIN++, while facilitating decoding speeds of approximately 2000 FPS. Additionally, preliminary proof of concept shows that our codec surpasses COIN and COIN++ in performance when using partial bits-back coding. Code is available at https://github.com/Xinjie-Q/GaussianImage.

---

## 6. A Compact Dynamic 3D Gaussian Representation for Real-Time Dynamic View Synthesis

- **作者**: Kai Katsumata, Duc Minh Vo, Hideki Nakayama
- **发布时间**: 2023-11-21
- **arXiv链接**: [arXiv:2311.12897v2](http://arxiv.org/abs/2311.12897v2)
- **说明**: 17 pages, 11 figures, ECCV 2024
- **英文摘要**: 3D Gaussian Splatting (3DGS) has shown remarkable success in synthesizing novel views given multiple views of a static scene. Yet, 3DGS faces challenges when applied to dynamic scenes because 3D Gaussian parameters need to be updated per timestep, requiring a large amount of memory and at least a dozen observations per timestep. To address these limitations, we present a compact dynamic 3D Gaussian representation that models positions and rotations as functions of time with a few parameter approximations while keeping other properties of 3DGS including scale, color and opacity invariant. Our method can dramatically reduce memory usage and relax a strict multi-view assumption. In our experiments on monocular and multi-view scenarios, we show that our method not only matches state-of-the-art methods, often linked with slower rendering speeds, in terms of high rendering quality but also significantly surpasses them by achieving a rendering speed of $118$ frames per second (FPS) at a resolution of 1,352$\times$1,014 on a single GPU.

---

