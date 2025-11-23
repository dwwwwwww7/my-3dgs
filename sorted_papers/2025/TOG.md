# TOG 2025

> **最后更新**： 2025-11-23 01:26:52

本页面包含 2025 年 TOG 会议的论文列表。

## 1. GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building Reconstruction

- **作者**: Qilin Zhang, Olaf Wysocki, Boris Jutzi
- **发布时间**: 2025-08-10
- **arXiv链接**: [arXiv:2508.07355v1](https://arxiv.org/abs/2508.07355v1)
- **说明**: Accepted for presentation at ISPRS 3D GeoInfo & Smart Data, Smart Cities 2025, Kashiwa, Japan. To appear in the ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences
- **英文摘要**: Recent advances in Gaussian Splatting (GS) have demonstrated its effectiveness in photo-realistic rendering and 3D reconstruction. Among these, 2D Gaussian Splatting (2DGS) is particularly suitable for surface reconstruction due to its flattened Gaussian representation and integrated normal regularization. However, its performance often degrades in large-scale and complex urban scenes with frequent occlusions, leading to incomplete building reconstructions. We propose GS4Buildings, a novel prior-guided Gaussian Splatting method leveraging the ubiquity of semantic 3D building models for robust and scalable building surface reconstruction. Instead of relying on traditional Structure-from-Motion (SfM) pipelines, GS4Buildings initializes Gaussians directly from low-level Level of Detail (LoD)2 semantic 3D building models. Moreover, we generate prior depth and normal maps from the planar building geometry and incorporate them into the optimization process, providing strong geometric guidance for surface consistency and structural accuracy. We also introduce an optional building-focused mode that limits reconstruction to building regions, achieving a 71.8% reduction in Gaussian primitives and enabling a more efficient and compact representation. Experiments on urban datasets demonstrate that GS4Buildings improves reconstruction completeness by 20.5% and geometric accuracy by 32.8%. These results highlight the potential of semantic building model integration to advance GS-based reco...

---

## 2. Building LOD Representation for 3D Urban Scenes

- **作者**: Shanshan Pan, Runze Zhang, Yilin Liu, Minglun Gong, Hui Huang
- **发布时间**: 2025-05-21
- **arXiv链接**: [arXiv:2505.15190v1](https://arxiv.org/abs/2505.15190v1)
- **说明**: ISPRS Journal of Photogrammetry and Remote Sensing 2025 (Patent Protected); Project page: https://vcc.tech/research/2025/LODRecon
- **英文摘要**: The advances in 3D reconstruction technology, such as photogrammetry and LiDAR scanning, have made it easier to reconstruct accurate and detailed 3D models for urban scenes. Nevertheless, these reconstructed models often contain a large number of geometry primitives, making interactive manipulation and rendering challenging, especially on resource-constrained devices like virtual reality platforms. Therefore, the generation of appropriate levels-of-detail (LOD) representations for these models is crucial. Additionally, automatically reconstructed 3D models tend to suffer from noise and lack semantic information. Dealing with these issues and creating LOD representations that are robust against noise while capturing the semantic meaning present significant challenges. In this paper, we propose a novel algorithm to address these challenges. We begin by analysing the properties of planar primitives detected from the input and group these primitives into multiple level sets by forming meaningful 3D structures. These level sets form the nodes of our innovative LOD-Tree. By selecting nodes at appropriate depths within the LOD-Tree, different LOD representations can be generated. Experimental results on real and complex urban scenes demonstrate the merits of our approach in generating clean, accurate, and semantically meaningful LOD representations.

---

