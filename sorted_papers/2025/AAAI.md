# AAAI 2025

> **最后更新**： 2025-11-09 19:36:40

本页面包含 2025 年 AAAI 会议的论文列表。

## 1. BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal  Scene Generation

- **作者**: Xiaolu Hou, Mingcheng Li, Dingkang Yang et al.
- **发布时间**: 2025-01-15
- **arXiv链接**: [arXiv:2501.10462v2](http://arxiv.org/abs/2501.10462v2)
- **说明**: Accepted by AAAI 2025. Code: https://github.com/SparklingH/BloomScene
- **英文摘要**: With the widespread use of virtual reality applications, 3D scene generation has become a new challenging research frontier. 3D scenes have highly complex structures and need to ensure that the output is dense, coherent, and contains all necessary structures. Many current 3D scene generation methods rely on pre-trained text-to-image diffusion models and monocular depth estimators. However, the generated scenes occupy large amounts of storage space and often lack effective regularisation methods, leading to geometric distortions. To this end, we propose BloomScene, a lightweight structured 3D Gaussian splatting for crossmodal scene generation, which creates diverse and high-quality 3D scenes from text or image inputs. Specifically, a crossmodal progressive scene generation framework is proposed to generate coherent scenes utilizing incremental point cloud reconstruction and 3D Gaussian splatting. Additionally, we propose a hierarchical depth prior-based regularization mechanism that utilizes multi-level constraints on depth accuracy and smoothness to enhance the realism and continuity of the generated scenes. Ultimately, we propose a structured context-guided compression mechanism that exploits structured hash grids to model the context of unorganized anchor attributes, which significantly eliminates structural redundancy and reduces storage overhead. Comprehensive experiments across multiple scenes demonstrate the significant potential and advantages of our framework compared...

---

## 2. GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians

- **作者**: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian
- **发布时间**: 2024-12-18
- **arXiv链接**: [arXiv:2412.13983v1](http://arxiv.org/abs/2412.13983v1)
- **说明**: accepted by AAAI2025
- **英文摘要**: Rendering photorealistic head avatars from arbitrary viewpoints is crucial for various applications like virtual reality. Although previous methods based on Neural Radiance Fields (NeRF) can achieve impressive results, they lack fidelity and efficiency. Recent methods using 3D Gaussian Splatting (3DGS) have improved rendering quality and real-time performance but still require significant storage overhead. In this paper, we introduce a method called GraphAvatar that utilizes Graph Neural Networks (GNN) to generate 3D Gaussians for the head avatar. Specifically, GraphAvatar trains a geometric GNN and an appearance GNN to generate the attributes of the 3D Gaussians from the tracked mesh. Therefore, our method can store the GNN models instead of the 3D Gaussians, significantly reducing the storage overhead to just 10MB. To reduce the impact of face-tracking errors, we also present a novel graph-guided optimization module to refine face-tracking parameters during training. Finally, we introduce a 3D-aware enhancer for post-processing to enhance the rendering quality. We conduct comprehensive experiments to demonstrate the advantages of GraphAvatar, surpassing existing methods in visual fidelity and storage consumption. The ablation study sheds light on the trade-offs between rendering quality and model size. The code will be released at: https://github.com/ucwxb/GraphAvatar

---

