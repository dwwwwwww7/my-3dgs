# ICCV 2025

> **最后更新**： 2025-11-09 19:01:26

本页面包含 2025 年 ICCV 会议的论文列表。

## 1. Leveraging Learned Image Prior for 3D Gaussian Compression

- **作者**: Seungjoo Shin, Jaesik Park, Sunghyun Cho
- **发布时间**: 2025-10-16
- **arXiv链接**: [arXiv:2510.14705v1](http://arxiv.org/abs/2510.14705v1)
- **说明**: Accepted to ICCV 2025 Workshop on ECLR
- **英文摘要**: Compression techniques for 3D Gaussian Splatting (3DGS) have recently achieved considerable success in minimizing storage overhead for 3D Gaussians while preserving high rendering quality. Despite the impressive storage reduction, the lack of learned priors restricts further advances in the rate-distortion trade-off for 3DGS compression tasks. To address this, we introduce a novel 3DGS compression framework that leverages the powerful representational capacity of learned image priors to recover compression-induced quality degradation. Built upon initially compressed Gaussians, our restoration network effectively models the compression artifacts in the image space between degraded and original Gaussians. To enhance the rate-distortion performance, we provide coarse rendering residuals into the restoration network as side information. By leveraging the supervision of restored images, the compressed Gaussians are refined, resulting in a highly compact representation with enhanced rendering performance. Our framework is designed to be compatible with existing Gaussian compression methods, making it broadly applicable across different baselines. Extensive experiments validate the effectiveness of our framework, demonstrating superior rate-distortion performance and outperforming the rendering quality of state-of-the-art 3DGS compression methods while requiring substantially less storage.

---

