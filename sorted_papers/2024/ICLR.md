# ICLR 2024

> **最后更新**： 2026-01-11 01:31:04

本页面包含 2024 年 ICLR 会议的论文列表。

## 1. 4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives

- **作者**: Zeyu Yang, Zijie Pan, Xiatian Zhu et al.
- **发布时间**: 2024-12-30
- **arXiv链接**: [arXiv:2412.20720v2](https://arxiv.org/abs/2412.20720v2)
- **说明**: Journal extension of ICLR 2024. arXiv admin note: text overlap with arXiv:2310.10642
- **英文摘要**: Dynamic 3D scene representation and novel view synthesis are crucial for enabling immersive experiences required by AR/VR and metaverse applications. It is a challenging task due to the complexity of unconstrained real-world scenes and their temporal dynamics. In this paper, we reformulate the reconstruction of a time-varying 3D scene as approximating its underlying spatiotemporal 4D volume by optimizing a collection of native 4D primitives, i.e., 4D Gaussians, with explicit geometry and appearance modeling. Equipped with a tailored rendering pipeline, our representation can be end-to-end optimized using only photometric supervision while free viewpoint viewing at interactive frame rate, making it suitable for representing real world scene with complex dynamic. This approach has been the first solution to achieve real-time rendering of high-resolution, photorealistic novel views for complex dynamic scenes. To facilitate real-world applications, we derive several compact variants that effectively reduce the memory footprint to address its storage bottleneck. Extensive experiments validate the superiority of 4DGS in terms of visual quality and efficiency across a range of dynamic scene-related tasks (e.g., novel view synthesis, 4D generation, scene understanding) and scenarios (e.g., single object, indoor scenes, driving environments, synthetic and real data).

---

