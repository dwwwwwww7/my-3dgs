# ICRA 2025

> **最后更新**： 2026-05-31 03:02:39

本页面包含 2025 年 ICRA 会议的论文列表。

## 1. Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

- **作者**: Justin Yu, Kush Hari, Karim El-Refai et al.
- **发布时间**: 2025-03-07
- **arXiv链接**: [arXiv:2503.05189v1](https://arxiv.org/abs/2503.05189v1)
- **说明**: Accepted to ICRA 2025
- **英文摘要**: Tracking and manipulating irregularly-shaped, previously unseen objects in dynamic environments is important for robotic applications in manufacturing, assembly, and logistics. Recently introduced Gaussian Splats efficiently model object geometry, but lack persistent state estimation for task-oriented manipulation. We present Persistent Object Gaussian Splat (POGS), a system that embeds semantics, self-supervised visual features, and object grouping features into a compact representation that can be continuously updated to estimate the pose of scanned objects. POGS updates object states without requiring expensive rescanning or prior CAD models of objects. After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose estimation. POGS supports grasping, reorientation, and natural language-driven manipulation by refining object pose estimates, facilitating sequential object reset operations with human-induced object perturbations and tool servoing, where robots recover tool pose despite tool perturbations of up to 30°. POGS achieves up to 12 consecutive successful object resets and recovers from 80% of in-grasp tool perturbations.

---

## 2. GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM

- **作者**: Mingrui Li, Weijian Chen, Na Cheng et al.
- **发布时间**: 2025-02-05
- **arXiv链接**: [arXiv:2502.03228v2](https://arxiv.org/abs/2502.03228v2)
- **说明**: The paper was accepted by ICRA 2025
- **英文摘要**: The 3D Gaussian Splatting (3DGS)-based SLAM system has garnered widespread attention due to its excellent performance in real-time high-fidelity rendering. However, in real-world environments with dynamic objects, existing 3DGS-based SLAM systems often face mapping errors and tracking drift issues. To address these problems, we propose GARAD-SLAM, a real-time 3DGS-based SLAM system tailored for dynamic scenes. In terms of tracking, unlike traditional methods, we directly perform dynamic segmentation on Gaussians and map them back to the front-end to obtain dynamic point labels through a Gaussian pyramid network, achieving precise dynamic removal and robust tracking. For mapping, we impose rendering penalties on dynamically labeled Gaussians, which are updated through the network, to avoid irreversible erroneous removal caused by simple pruning. Our results on real-world datasets demonstrate that our method is competitive in tracking compared to baseline methods, generating fewer artifacts and higher-quality reconstructions in rendering.

---

## 3. Hier-SLAM: Scaling-up Semantics in SLAM with a Hierarchically Categorical Gaussian Splatting

- **作者**: Boying Li, Zhixi Cai, Yuan-Fang Li, Ian Reid, Hamid Rezatofighi
- **发布时间**: 2024-09-19
- **arXiv链接**: [arXiv:2409.12518v4](https://arxiv.org/abs/2409.12518v4)
- **说明**: Accepted for publication at ICRA 2025. Code is available at https://github.com/LeeBY68/Hier-SLAM
- **英文摘要**: We propose Hier-SLAM, a semantic 3D Gaussian Splatting SLAM method featuring a novel hierarchical categorical representation, which enables accurate global 3D semantic mapping, scaling-up capability, and explicit semantic label prediction in the 3D world. The parameter usage in semantic SLAM systems increases significantly with the growing complexity of the environment, making it particularly challenging and costly for scene understanding. To address this problem, we introduce a novel hierarchical representation that encodes semantic information in a compact form into 3D Gaussian Splatting, leveraging the capabilities of large language models (LLMs). We further introduce a novel semantic loss designed to optimize hierarchical semantic information through both inter-level and cross-level optimization. Furthermore, we enhance the whole SLAM system, resulting in improved tracking and mapping performance. Our \MethodName{} outperforms existing dense SLAM methods in both mapping and tracking accuracy, while achieving a 2x operation speed-up. Additionally, it achieves on-par semantic rendering performance compared to existing methods while significantly reducing storage and training time requirements. Rendering FPS impressively reaches 2,000 with semantic information and 3,000 without it. Most notably, it showcases the capability of handling the complex real-world scene with more than 500 semantic classes, highlighting its valuable scaling-up capability. The open-source code is ava...

---

## 4. Gradient-Driven 3D Segmentation and Affordance Transfer in Gaussian Splatting Using 2D Masks

- **作者**: Joji Joseph, Bharadwaj Amrutur, Shalabh Bhatnagar
- **发布时间**: 2024-09-18
- **arXiv链接**: [arXiv:2409.11681v1](https://arxiv.org/abs/2409.11681v1)
- **说明**: Preprint, Under review for ICRA 2025
- **英文摘要**: 3D Gaussian Splatting has emerged as a powerful 3D scene representation technique, capturing fine details with high efficiency. In this paper, we introduce a novel voting-based method that extends 2D segmentation models to 3D Gaussian splats. Our approach leverages masked gradients, where gradients are filtered by input 2D masks, and these gradients are used as votes to achieve accurate segmentation. As a byproduct, we discovered that inference-time gradients can also be used to prune Gaussians, resulting in up to 21% compression. Additionally, we explore few-shot affordance transfer, allowing annotations from 2D images to be effectively transferred onto 3D Gaussian splats. The robust yet straightforward mathematical formulation underlying this approach makes it a highly effective tool for numerous downstream applications, such as augmented reality (AR), object editing, and robotics. The project code and additional resources are available at https://jojijoseph.github.io/3dgs-segmentation.

---

