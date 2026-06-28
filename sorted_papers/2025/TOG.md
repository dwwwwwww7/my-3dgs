# TOG 2025

> **最后更新**： 2026-06-28 03:03:07

本页面包含 2025 年 TOG 会议的论文列表。

## 1. GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building Reconstruction

- **作者**: Qilin Zhang, Olaf Wysocki, Boris Jutzi
- **发布时间**: 2025-08-10
- **arXiv链接**: [arXiv:2508.07355v1](https://arxiv.org/abs/2508.07355v1)
- **说明**: Accepted for presentation at ISPRS 3D GeoInfo & Smart Data, Smart Cities 2025, Kashiwa, Japan. To appear in the ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences
- **英文摘要**: Recent advances in Gaussian Splatting (GS) have demonstrated its effectiveness in photo-realistic rendering and 3D reconstruction. Among these, 2D Gaussian Splatting (2DGS) is particularly suitable for surface reconstruction due to its flattened Gaussian representation and integrated normal regularization. However, its performance often degrades in large-scale and complex urban scenes with frequent occlusions, leading to incomplete building reconstructions. We propose GS4Buildings, a novel prior-guided Gaussian Splatting method leveraging the ubiquity of semantic 3D building models for robust and scalable building surface reconstruction. Instead of relying on traditional Structure-from-Motion (SfM) pipelines, GS4Buildings initializes Gaussians directly from low-level Level of Detail (LoD)2 semantic 3D building models. Moreover, we generate prior depth and normal maps from the planar building geometry and incorporate them into the optimization process, providing strong geometric guidance for surface consistency and structural accuracy. We also introduce an optional building-focused mode that limits reconstruction to building regions, achieving a 71.8% reduction in Gaussian primitives and enabling a more efficient and compact representation. Experiments on urban datasets demonstrate that GS4Buildings improves reconstruction completeness by 20.5% and geometric accuracy by 32.8%. These results highlight the potential of semantic building model integration to advance GS-based reco...

---

