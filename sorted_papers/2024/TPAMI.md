# TPAMI 2024

> **最后更新**： 2025-11-09 18:32:32

本页面包含 2024 年 TPAMI 会议的论文列表。

## 1. MCGS: Multiview Consistency Enhancement for Sparse-View 3D Gaussian  Radiance Fields

- **作者**: Yuru Xiao, Deming Zhai, Wenbo Zhao et al.
- **发布时间**: 2024-10-15
- **arXiv链接**: [arXiv:2410.11394v2](http://arxiv.org/abs/2410.11394v2)
- **说明**: Accepted by IEEE Transactions on Pattern Analysis and Machine
  Intelligence
- **英文摘要**: Radiance fields represented by 3D Gaussians excel at synthesizing novel views, offering both high training efficiency and fast rendering. However, with sparse input views, the lack of multi-view consistency constraints results in poorly initialized Gaussians and unreliable heuristics for optimization, leading to suboptimal performance. Existing methods often incorporate depth priors from dense estimation networks but overlook the inherent multi-view consistency in input images. Additionally, they rely on dense initialization, which limits the efficiency of scene representation. To overcome these challenges, we propose a view synthesis framework based on 3D Gaussian Splatting, named MCGS, enabling photorealistic scene reconstruction from sparse views. The key innovations of MCGS in enhancing multi-view consistency are as follows: i) We leverage matching priors from a sparse matcher to initialize Gaussians primarily on textured regions, while low-texture areas are populated with randomly distributed Gaussians. This yields a compact yet sufficient set of initial Gaussians. ii) We propose a multi-view consistency-guided progressive pruning strategy to dynamically eliminate inconsistent Gaussians. This approach confines their optimization to a consistency-constrained space, which ensures robust and coherent scene reconstruction. These strategies enhance robustness to sparse views, accelerate rendering, and reduce memory consumption, making MCGS a practical framework for 3D Gaussia...

---

