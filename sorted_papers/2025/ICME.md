# ICME 2025

> **最后更新**： 2025-11-10 01:57:48

本页面包含 2025 年 ICME 会议的论文列表。

## 1. Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based  Prediction

- **作者**: Jingui Ma, Yang Hu, Luyang Tang et al.
- **发布时间**: 2025-03-30
- **arXiv链接**: [arXiv:2503.23337v1](http://arxiv.org/abs/2503.23337v1)
- **说明**: The paper has been accepted by ICME2025 in March,2025
- **英文摘要**: Recently, 3D Gaussian Spatting (3DGS) has gained widespread attention in Novel View Synthesis (NVS) due to the remarkable real-time rendering performance. However, the substantial cost of storage and transmission of vanilla 3DGS hinders its further application (hundreds of megabytes or even gigabytes for a single scene). Motivated by the achievements of prediction in video compression, we introduce the prediction technique into the anchor-based Gaussian representation to effectively reduce the bit rate. Specifically, we propose a spatial condition-based prediction module to utilize the grid-captured scene information for prediction, with a residual compensation strategy designed to learn the missing fine-grained information. Besides, to further compress the residual, we propose an instance-aware hyper prior, developing a structure-aware and instance-aware entropy model. Extensive experiments demonstrate the effectiveness of our prediction-based compression framework and each technical component. Even compared with SOTA compression method, our framework still achieves a bit rate savings of 24.42 percent. Code is to be released!

---

## 2. TC-GS: Tri-plane based compression for 3D Gaussian Splatting

- **作者**: Taorui Wang, Zitong Yu, Yong Xu
- **发布时间**: 2025-03-26
- **arXiv链接**: [arXiv:2503.20221v1](http://arxiv.org/abs/2503.20221v1)
- **说明**: Accepted by ICME 2025
- **英文摘要**: Recently, 3D Gaussian Splatting (3DGS) has emerged as a prominent framework for novel view synthesis, providing high fidelity and rapid rendering speed. However, the substantial data volume of 3DGS and its attributes impede its practical utility, requiring compression techniques for reducing memory cost. Nevertheless, the unorganized shape of 3DGS leads to difficulties in compression. To formulate unstructured attributes into normative distribution, we propose a well-structured tri-plane to encode Gaussian attributes, leveraging the distribution of attributes for compression. To exploit the correlations among adjacent Gaussians, K-Nearest Neighbors (KNN) is used when decoding Gaussian distribution from the Tri-plane. We also introduce Gaussian position information as a prior of the position-sensitive decoder. Additionally, we incorporate an adaptive wavelet loss, aiming to focus on the high-frequency details as iterations increase. Our approach has achieved results that are comparable to or surpass that of SOTA 3D Gaussians Splatting compression work in extensive experiments across multiple datasets. The codes are released at https://github.com/timwang2001/TC-GS.

---

