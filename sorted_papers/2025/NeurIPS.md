# NeurIPS 2025

> **最后更新**： 2025-11-10 01:23:10

本页面包含 2025 年 NeurIPS 会议的论文列表。

## 1. Instant4D: 4D Gaussian Splatting in Minutes

- **作者**: Zhanpeng Luo, Haoxi Ran, Li Lu
- **发布时间**: 2025-10-01
- **arXiv链接**: [arXiv:2510.01119v1](http://arxiv.org/abs/2510.01119v1)
- **说明**: Accepted by NeurIPS 25
- **英文摘要**: Dynamic view synthesis has seen significant advances, yet reconstructing scenes from uncalibrated, casual video remains challenging due to slow optimization and complex parameter estimation. In this work, we present Instant4D, a monocular reconstruction system that leverages native 4D representation to efficiently process casual video sequences within minutes, without calibrated cameras or depth sensors. Our method begins with geometric recovery through deep visual SLAM, followed by grid pruning to optimize scene representation. Our design significantly reduces redundancy while maintaining geometric integrity, cutting model size to under 10% of its original footprint. To handle temporal dynamics efficiently, we introduce a streamlined 4D Gaussian representation, achieving a 30x speed-up and reducing training time to within two minutes, while maintaining competitive performance across several benchmarks. Our method reconstruct a single video within 10 minutes on the Dycheck dataset or for a typical 200-frame video. We further apply our model to in-the-wild videos, showcasing its generalizability. Our project website is published at https://instant4d.github.io/.

---

## 2. Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian  Splatting

- **作者**: Hyeongmin Lee, Kyungjune Baek
- **发布时间**: 2025-07-23
- **arXiv链接**: [arXiv:2507.17336v2](http://arxiv.org/abs/2507.17336v2)
- **说明**: 24 pages, 10 figures, NeurIPS 2025
- **英文摘要**: Dynamic 4D Gaussian Splatting (4DGS) effectively extends the high-speed rendering capabilities of 3D Gaussian Splatting (3DGS) to represent volumetric videos. However, the large number of Gaussians, substantial temporal redundancies, and especially the absence of an entropy-aware compression framework result in large storage requirements. Consequently, this poses significant challenges for practical deployment, efficient edge-device processing, and data transmission. In this paper, we introduce a novel end-to-end RD-optimized compression framework tailored for 4DGS, aiming to enable flexible, high-fidelity rendering across varied computational platforms. Leveraging Fully Explicit Dynamic Gaussian Splatting (Ex4DGS), one of the state-of-the-art 4DGS methods, as our baseline, we start from the existing 3DGS compression methods for compatibility while effectively addressing additional challenges introduced by the temporal axis. In particular, instead of storing motion trajectories independently per point, we employ a wavelet transform to reflect the real-world smoothness prior, significantly enhancing storage efficiency. This approach yields significantly improved compression ratios and provides a user-controlled balance between compression efficiency and rendering quality. Extensive experiments demonstrate the effectiveness of our method, achieving up to 91$\times$ compression compared to the original Ex4DGS model while maintaining high visual fidelity. These results highlight ...

---

## 3. Metropolis-Hastings Sampling for 3D Gaussian Reconstruction

- **作者**: Hyunjin Kim, Haebeom Jung, Jaesik Park
- **发布时间**: 2025-06-15
- **arXiv链接**: [arXiv:2506.12945v2](http://arxiv.org/abs/2506.12945v2)
- **说明**: NeurIPS 2025. Project Page: https://hjhyunjinkim.github.io/MH-3DGS
- **英文摘要**: We propose an adaptive sampling framework for 3D Gaussian Splatting (3DGS) that leverages comprehensive multi-view photometric error signals within a unified Metropolis-Hastings approach. Vanilla 3DGS heavily relies on heuristic-based density-control mechanisms (e.g., cloning, splitting, and pruning), which can lead to redundant computations or premature removal of beneficial Gaussians. Our framework overcomes these limitations by reformulating densification and pruning as a probabilistic sampling process, dynamically inserting and relocating Gaussians based on aggregated multi-view errors and opacity scores. Guided by Bayesian acceptance tests derived from these error-based importance scores, our method substantially reduces reliance on heuristics, offers greater flexibility, and adaptively infers Gaussian distributions without requiring predefined scene complexity. Experiments on benchmark datasets, including Mip-NeRF360, Tanks and Temples and Deep Blending, show that our approach reduces the number of Gaussians needed, achieving faster convergence while matching or modestly surpassing the view-synthesis quality of state-of-the-art models.

---

## 4. ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS

- **作者**: Weijie Wang, Donny Y. Chen, Zeyu Zhang et al.
- **发布时间**: 2025-05-29
- **arXiv链接**: [arXiv:2505.23734v3](http://arxiv.org/abs/2505.23734v3)
- **说明**: NeurIPS 2025, Project Page: https://lhmd.top/zpressor, Code:
  https://github.com/ziplab/ZPressor
- **英文摘要**: Feed-forward 3D Gaussian Splatting (3DGS) models have recently emerged as a promising solution for novel view synthesis, enabling one-pass inference without the need for per-scene 3DGS optimization. However, their scalability is fundamentally constrained by the limited capacity of their models, leading to degraded performance or excessive memory consumption as the number of input views increases. In this work, we analyze feed-forward 3DGS frameworks through the lens of the Information Bottleneck principle and introduce ZPressor, a lightweight architecture-agnostic module that enables efficient compression of multi-view inputs into a compact latent state $Z$ that retains essential scene information while discarding redundancy. Concretely, ZPressor enables existing feed-forward 3DGS models to scale to over 100 input views at 480P resolution on an 80GB GPU, by partitioning the views into anchor and support sets and using cross attention to compress the information from the support views into anchor views, forming the compressed latent state $Z$. We show that integrating ZPressor into several state-of-the-art feed-forward 3DGS models consistently improves performance under moderate input views and enhances robustness under dense view settings on two large-scale benchmarks DL3DV-10K and RealEstate10K. The video results, code and trained models are available on our project page: https://lhmd.top/zpressor.

---

## 5. LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient  Rendering

- **作者**: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt et al.
- **发布时间**: 2025-05-29
- **arXiv链接**: [arXiv:2505.23158v2](http://arxiv.org/abs/2505.23158v2)
- **说明**: NeurIPS 2025; Web: https://lodge-gs.github.io/
- **英文摘要**: In this work, we present a novel level-of-detail (LOD) method for 3D Gaussian Splatting that enables real-time rendering of large-scale scenes on memory-constrained devices. Our approach introduces a hierarchical LOD representation that iteratively selects optimal subsets of Gaussians based on camera distance, thus largely reducing both rendering time and GPU memory usage. We construct each LOD level by applying a depth-aware 3D smoothing filter, followed by importance-based pruning and fine-tuning to maintain visual fidelity. To further reduce memory overhead, we partition the scene into spatial chunks and dynamically load only relevant Gaussians during rendering, employing an opacity-blending mechanism to avoid visual artifacts at chunk boundaries. Our method achieves state-of-the-art performance on both outdoor (Hierarchical 3DGS) and indoor (Zip-NeRF) datasets, delivering high-quality renderings with reduced latency and memory requirements.

---

