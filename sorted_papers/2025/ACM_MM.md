# ACM MM 2025

> **最后更新**： 2026-01-04 01:31:16

本页面包含 2025 年 ACM MM 会议的论文列表。

## 1. FlexGaussian: Flexible and Cost-Effective Training-Free Compression for 3D Gaussian Splatting

- **作者**: Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang
- **发布时间**: 2025-07-09
- **arXiv链接**: [arXiv:2507.06671v1](https://arxiv.org/abs/2507.06671v1)
- **说明**: To appear at ACM MM 2025
- **英文摘要**: 3D Gaussian splatting has become a prominent technique for representing and rendering complex 3D scenes, due to its high fidelity and speed advantages. However, the growing demand for large-scale models calls for effective compression to reduce memory and computation costs, especially on mobile and edge devices with limited resources. Existing compression methods effectively reduce 3D Gaussian parameters but often require extensive retraining or fine-tuning, lacking flexibility under varying compression constraints.   In this paper, we introduce FlexGaussian, a flexible and cost-effective method that combines mixed-precision quantization with attribute-discriminative pruning for training-free 3D Gaussian compression. FlexGaussian eliminates the need for retraining and adapts easily to diverse compression targets. Evaluation results show that FlexGaussian achieves up to 96.4% compression while maintaining high rendering quality (<1 dB drop in PSNR), and is deployable on mobile devices. FlexGaussian delivers high compression ratios within seconds, being 1.7-2.1x faster than state-of-the-art training-free methods and 10-100x faster than training-involved approaches. The code is being prepared and will be released soon at: https://github.com/Supercomputing-System-AI-Lab/FlexGaussian

---

