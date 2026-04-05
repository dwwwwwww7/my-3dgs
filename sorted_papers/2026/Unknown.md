# 未知会议 2026

> **最后更新**： 2026-04-05 02:06:34

本页面包含 2026 年 未知会议 会议的论文列表。

## 1. GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting

- **作者**: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling
- **发布时间**: 2026-04-02
- **arXiv链接**: [arXiv:2604.01884v1](https://arxiv.org/abs/2604.01884v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated breakthrough performance in novel view synthesis and real-time rendering. Nevertheless, its practicality is constrained by the high memory cost due to a huge number of Gaussian points. Many pruning-based 3DGS variants have been proposed for memory saving, but often compromise spatial consistency and may lead to rendering artifacts. To address this issue, we propose graph-based spatial distribution optimization for compact 3D Gaussian Splatting (GS\textasciicircum2), which enhances reconstruction quality by optimizing the spatial distribution of Gaussian points. Specifically, we introduce an evidence lower bound (ELBO)-based adaptive densification strategy that automatically controls the densification process. In addition, an opacity-aware progressive pruning strategy is proposed to further reduce memory consumption by dynamically removing low-opacity Gaussian points. Furthermore, we propose a graph-based feature encoding module to adjust the spatial distribution via feature-guided point shifting. Extensive experiments validate that GS\textasciicircum2 achieves a compact Gaussian representation while delivering superior rendering quality. Compared with 3DGS, it achieves higher PSNR with only about 12.5\% Gaussian points. Furthermore, it outperforms all compared baselines in both rendering quality and memory efficiency.

---

## 2. FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting

- **作者**: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi et al.
- **发布时间**: 2026-04-02
- **arXiv链接**: [arXiv:2604.01844v1](https://arxiv.org/abs/2604.01844v1)
- **英文摘要**: Gaussian Splatting (GS) has emerged as a dominating technique for image rendering and has quickly been adapted for the X-ray Computed Tomography (CT) reconstruction task. However, despite being on par or better than many of its predecessors, the benefits of GS are typically not substantial enough to motivate a transition from well-established reconstruction algorithms. This paper addresses the most significant remaining limitations of the GS-based approach by introducing FaCT-GS, a framework for fast and flexible CT reconstruction. Enabled by an in-depth optimization of the voxelization and rasterization pipelines, our new method is significantly faster than its predecessors and scales well with projection and output volume size. Furthermore, the improved voxelization enables rapid fitting of Gaussians to pre-existing volumes, which can serve as a prior for warm-starting the reconstruction, or simply as an alternative, compressed representation. FaCT-GS is over 4X faster than the State of the Art GS CT reconstruction on standard 512x512 projections, and over 13X faster on 2k projections. Implementation available at: https://github.com/PaPieta/fact-gs.

---

## 3. Autoregressive Appearance Prediction for 3D Gaussian Avatars

- **作者**: Michael Steiner, Zhang Chen, Alexander Richard et al.
- **发布时间**: 2026-04-01
- **arXiv链接**: [arXiv:2604.00928v1](https://arxiv.org/abs/2604.00928v1)
- **说明**: Project Page: https://steimich96.github.io/AAP-3DGA/
- **英文摘要**: A photorealistic and immersive human avatar experience demands capturing fine, person-specific details such as cloth and hair dynamics, subtle facial expressions, and characteristic motion patterns. Achieving this requires large, high-quality datasets, which often introduce ambiguities and spurious correlations when very similar poses correspond to different appearances. Models that fit these details during training can overfit and produce unstable, abrupt appearance changes for novel poses. We propose a 3D Gaussian Splatting avatar model with a spatial MLP backbone that is conditioned on both pose and an appearance latent. The latent is learned during training by an encoder, yielding a compact representation that improves reconstruction quality and helps disambiguate pose-driven renderings. At driving time, our predictor autoregressively infers the latent, producing temporally smooth appearance evolution and improved stability. Overall, our method delivers a robust and practical path to high-fidelity, stable avatar driving.

---

## 4. Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM

- **作者**: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame
- **发布时间**: 2026-04-01
- **arXiv链接**: [arXiv:2604.00804v1](https://arxiv.org/abs/2604.00804v1)
- **英文摘要**: Efficient multi-agent 3D mapping is essential for robotic teams operating in unknown environments, but dense representations hinder real-time exchange over constrained communication links. In multi-agent Simultaneous Localization and Mapping (SLAM), systems typically rely on a centralized server to merge and optimize the local maps produced by individual agents. However, sharing these large map representations, particularly those generated by recent methods such as Gaussian Splatting, becomes a bottleneck in real-world scenarios with limited bandwidth. We present an improved multi-agent RGB-D Gaussian Splatting SLAM framework that reduces communication load while preserving map fidelity. First, we incorporate a compaction step into our SLAM system to remove redundant 3D Gaussians, without degrading the rendering quality. Second, our approach performs centralized loop closure computation without initial guess, operating in two modes: a pure rendered-depth mode that requires no data beyond the 3D Gaussians, and a camera-depth mode that includes lightweight depth images for improved registration accuracy and additional Gaussian pruning. Evaluation on both synthetic and real-world datasets shows up to 85-95\% reduction in transmitted data compared to state-of-the-art approaches in both modes, bringing 3D Gaussian multi-agent SLAM closer to practical deployment in real-world scenarios. Code: https://github.com/lemonci/coko-slam

---

## 5. Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping

- **作者**: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze
- **发布时间**: 2026-03-30
- **arXiv链接**: [arXiv:2603.29005v1](https://arxiv.org/abs/2603.29005v1)
- **说明**: Accepted to IEEE Symposium on VLSI Technology & Circuits (VLSI), 2026. To appear
- **英文摘要**: High-fidelity 3D occupancy mapping is essential for many edge-based applications (such as AR/VR and autonomous navigation) but is limited by power constraints. We present Gleanmer, a system on chip (SoC) with an accelerator for GMMap, a 3D occupancy map using Gaussians. Through algorithm-hardware co-optimizations for direct computation and efficient reuse of these compact Gaussians, Gleanmer reduces construction and query energy by up to 63% and 81%, respectively. Approximate computation on Gaussians reduces accelerator area by 38%. Using 16nm CMOS, Gleanmer processes 640x480 images in real time beyond 88 fps during map construction and processes over 540K coordinates per second during map query. To our knowledge, Gleanmer is the first fabricated SoC to achieve real-time 3D occupancy mapping under 6 mW for edge-based applications.

---

## 6. LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting

- **作者**: Xuan Deng, Xiandong Meng, Hengyu Man et al.
- **发布时间**: 2026-03-30
- **arXiv链接**: [arXiv:2603.28431v3](https://arxiv.org/abs/2603.28431v3)
- **说明**: 10
- **英文摘要**: Although 3D Gaussian Splatting (3DGS) enables high-fidelity real-time rendering, its prohibitive storage overhead severely hinders practical deployment. Recent anchor-based 3DGS compression schemes reduce gaussian redundancy through some advanced context models. However, they overlook explicit geometric dependencies, leading to structural degradation and suboptimal ratedistortion performance. In this paper, we propose a Local Geometry-aware Hierarchical Context Compression framework for 3DGS(LG-HCC) that incorporates inter-anchor geometric correlations into anchor pruning and entropy coding for compact representation. Specifically, we introduce an Neighborhood-Aware Anchor Pruning (NAAP) strategy, which evaluates anchor importance via weighted neighborhood feature aggregation and then merges low-contribution anchors into salient neighbors, yielding a compact yet geometry-consistent anchor set. Moreover, we further develop a hierarchical entropy coding scheme, in which coarse-to-fine priors are exploited through a lightweight Geometry-Guided Convolution(GG-Conv) operator to enable spatially adaptive context modeling and rate-distortion optimization. Extensive experiments show that LG-HCC effectively alleviates structural preservation issues,achieving superior geometric integrity and rendering fidelity while reducing storage by up to 30.85x compared to the Scaffold-GS baseline on the Mip-NeRF360 dataset

---

## 7. GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation

- **作者**: Nicolas von Lützow, Barbara Rössle, Katharina Schmid, Matthias Nießner
- **发布时间**: 2026-03-27
- **arXiv链接**: [arXiv:2603.26661v1](https://arxiv.org/abs/2603.26661v1)
- **说明**: Project page: https://nicolasvonluetzow.github.io/GaussianGPT/ - Project video: https://youtu.be/zVnMHkFzHDg
- **英文摘要**: Most recent advances in 3D generative modeling rely on diffusion or flow-matching formulations. We instead explore a fully autoregressive alternative and introduce GaussianGPT, a transformer-based model that directly generates 3D Gaussians via next-token prediction, thus facilitating full 3D scene generation. We first compress Gaussian primitives into a discrete latent grid using a sparse 3D convolutional autoencoder with vector quantization. The resulting tokens are serialized and modeled using a causal transformer with 3D rotary positional embedding, enabling sequential generation of spatial structure and appearance. Unlike diffusion-based methods that refine scenes holistically, our formulation constructs scenes step-by-step, naturally supporting completion, outpainting, controllable sampling via temperature, and flexible generation horizons. This formulation leverages the compositional inductive biases and scalability of autoregressive modeling while operating on explicit representations compatible with modern neural rendering pipelines, positioning autoregressive transformers as a complementary paradigm for controllable and context-aware 3D generation.

---

## 8. FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting

- **作者**: Yixian Wang, Haolin Yu, Jiadong Tang et al.
- **发布时间**: 2026-03-25
- **arXiv链接**: [arXiv:2603.23891v1](https://arxiv.org/abs/2603.23891v1)
- **英文摘要**: 3D Gaussian Splatting has revolutionized neural rendering with real-time performance. However, scaling this approach to large scenes using Level-of-Detail methods faces critical challenges: inefficient serial traversal consuming over 60\% of rendering time, and redundant Gaussian-tile pairs that incur unnecessary processing overhead. To address these limitations, we introduce FilterGS, featuring a parallel filtering mechanism with two complementary filters that select Gaussian elements efficiently without tree traversal. Additionally, we propose a novel GTC metric that quantifies the redundancy of Gaussian-tile key-value pairs. Based on this metric, we introduce a scene-adaptive Gaussian shrinking strategy that effectively reduces redundant pairs. Extensive experiments demonstrate that FilterGS achieves state-of-the-art rendering speeds while maintaining competitive visual quality across multiple large-scale datasets. Project page: https://github.com/xenon-w/FilterGS

---

## 9. Drop-In Perceptual Optimization for 3D Gaussian Splatting

- **作者**: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.23297v1](https://arxiv.org/abs/2603.23297v1)
- **说明**: Project page: https://apple.github.io/ml-perceptual-3dgs
- **英文摘要**: Despite their output being ultimately consumed by human viewers, 3D Gaussian Splatting (3DGS) methods often rely on ad-hoc combinations of pixel-level losses, resulting in blurry renderings. To address this, we systematically explore perceptual optimization strategies for 3DGS by searching over a diverse set of distortion losses. We conduct the first-of-its-kind large-scale human subjective study on 3DGS, involving 39,320 pairwise ratings across several datasets and 3DGS frameworks. A regularized version of Wasserstein Distortion, which we call WD-R, emerges as the clear winner, excelling at recovering fine textures without incurring a higher splat count. WD-R is preferred by raters more than $2.3\times$ over the original 3DGS loss, and $1.5\times$ over current best method Perceptual-GS. WD-R also consistently achieves state-of-the-art LPIPS, DISTS, and FID scores across various datasets, and generalizes across recent frameworks, such as Mip-Splatting and Scaffold-GS, where replacing the original loss with WD-R consistently enhances perceptual quality within a similar resource budget (number of splats for Mip-Splatting, model size for Scaffold-GS), and leads to reconstructions being preferred by human raters $1.8\times$ and $3.6\times$, respectively. We also find that this carries over to the task of 3DGS scene compression, with $\approx 50\%$ bitrate savings for comparable perceptual metric performance.

---

## 10. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

- **作者**: Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, Hamed Rezazadegan Tavakoli
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.21933v1](https://arxiv.org/abs/2603.21933v1)
- **说明**: 14 pages, 3 figures, 2 tables
- **英文摘要**: The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training pruning method for 3D Gaussian splats that relies solely on attribute-derived neighbourhood descriptors. As our primary contribution, we introduce a hybrid descriptor framework that captures structural and appearance consistency directly from the splat representation. Building on these descriptors, we formulate pruning as a statistical evidence estimation problem and introduce a Beta evidence model that quantifies per-splat reliability through a probabilistic confidence score.   Experiments conducted on standardized test sequences defined by the ISO/IEC MPEG Common Test Conditions (CTC) demonstrate that our approach achieves substantial pruning while preserving reconstruction quality, establishing a practical and generalizable alternative to existing camera-dependent pruning strategies.

---

## 11. F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting

- **作者**: Injae Kim, Chaehyeon Kim, Minseong Bae, Minseok Joo, Hyunwoo J. Kim
- **发布时间**: 2026-03-22
- **arXiv链接**: [arXiv:2603.21304v2](https://arxiv.org/abs/2603.21304v2)
- **说明**: Project Page: $\href{https://mlvlab.github.io/F4Splat}{\text{this http URL}}$
- **英文摘要**: Feed-forward 3D Gaussian Splatting methods enable single-pass reconstruction and real-time rendering. However, they typically adopt rigid pixel-to-Gaussian or voxel-to-Gaussian pipelines that uniformly allocate Gaussians, leading to redundant Gaussians across views. Moreover, they lack an effective mechanism to control the total number of Gaussians while maintaining reconstruction fidelity. To address these limitations, we present F4Splat, which performs Feed-Forward predictive densification for Feed-Forward 3D Gaussian Splatting, introducing a densification-score-guided allocation strategy that adaptively distributes Gaussians according to spatial complexity and multi-view overlap. Our model predicts per-region densification scores to estimate the required Gaussian density and allows explicit control over the final Gaussian budget without retraining. This spatially adaptive allocation reduces redundancy in simple regions and minimizes duplicate Gaussians across overlapping views, producing compact yet high-quality 3D representations. Extensive experiments demonstrate that our model achieves superior novel-view synthesis performance compared to prior uncalibrated feed-forward methods, while using significantly fewer Gaussians.

---

## 12. Matryoshka Gaussian Splatting

- **作者**: Zhilin Guo, Boqiao Zhang, Hakan Aktas et al.
- **发布时间**: 2026-03-19
- **arXiv链接**: [arXiv:2603.19234v2](https://arxiv.org/abs/2603.19234v2)
- **说明**: project page: https://zhilinguo.github.io/MGS
- **英文摘要**: The ability to render scenes at adjustable fidelity from a single model, known as level of detail (LoD), is crucial for practical deployment of 3D Gaussian Splatting (3DGS). Existing discrete LoD methods expose only a limited set of operating points, while concurrent continuous LoD approaches enable smoother scaling but often suffer noticeable quality degradation at full capacity, making LoD a costly design decision. We introduce Matryoshka Gaussian Splatting (MGS), a training framework that enables continuous LoD for standard 3DGS pipelines without sacrificing full-capacity rendering quality. MGS learns a single ordered set of Gaussians such that rendering any prefix, the first k splats, produces a coherent reconstruction whose fidelity improves smoothly with increasing budget. Our key idea is stochastic budget training: each iteration samples a random splat budget and optimises both the corresponding prefix and the full set. This strategy requires only two forward passes and introduces no architectural modifications. Experiments across four benchmarks and six baselines show that MGS matches the full-capacity performance of its backbone while enabling a continuous speed-quality trade-off from a single model. Extensive ablations on ordering strategies, training objectives, and model capacity further validate the designs.

---

## 13. NanoGS: Training-Free Gaussian Splat Simplification

- **作者**: Butian Xiong, Rong Liu, Tiantian Zhou et al.
- **发布时间**: 2026-03-17
- **arXiv链接**: [arXiv:2603.16103v1](https://arxiv.org/abs/2603.16103v1)
- **英文摘要**: 3D Gaussian Splat (3DGS) enables high-fidelity, real-time novel view synthesis by representing scenes with large sets of anisotropic primitives, but often requires millions of Splats, incurring significant storage and transmission costs. Most existing compression methods rely on GPU-intensive post-training optimization with calibrated images, limiting practical deployment. We introduce NanoGS, a training-free and lightweight framework for Gaussian Splat simplification. Instead of relying on image-based rendering supervision, NanoGS formulates simplification as local pairwise merging over a sparse spatial graph. The method approximates a pair of Gaussians with a single primitive using mass preserved moment matching and evaluates merge quality through a principled merge cost between the original mixture and its approximation. By restricting merge candidates to local neighborhoods and selecting compatible pairs efficiently, NanoGS produces compact Gaussian representations while preserving scene structure and appearance. NanoGS operates directly on existing Gaussian Splat models, runs efficiently on CPU, and preserves the standard 3DGS parameterization, enabling seamless integration with existing rendering pipelines. Experiments demonstrate that NanoGS substantially reduces primitive count while maintaining high rendering fidelity, providing an efficient and practical solution for Gaussian Splat simplification. Our project website is available at https://saliteta.github.io/NanoGS...

---

## 14. Direct Object-Level Reconstruction via Probabilistic Gaussian Splatting

- **作者**: Shuai Guo, Ao Guo, Junchao Zhao et al.
- **发布时间**: 2026-03-15
- **arXiv链接**: [arXiv:2603.14316v1](https://arxiv.org/abs/2603.14316v1)
- **英文摘要**: Object-level 3D reconstruction play important roles across domains such as cultural heritage digitization, industrial manufacturing, and virtual reality. However, existing Gaussian Splatting-based approaches generally rely on full-scene reconstruction, in which substantial redundant background information is introduced, leading to increased computational and storage overhead. To address this limitation, we propose an efficient single-object 3D reconstruction method based on 2D Gaussian Splatting. By directly integrating foreground-background probability cues into Gaussian primitives and dynamically pruning low-probability Gaussians during training, the proposed method fundamentally focuses on an object of interest and improves the memory and computational efficiency. Our pipeline leverages probability masks generated by YOLO and SAM to supervise probabilistic Gaussian attributes, replacing binary masks with continuous probability values to mitigate boundary ambiguity. Additionally, we propose a dual-stage filtering strategy for training's startup to suppress background Gaussians. And, during training, rendered probability masks are conversely employed to refine supervision and enhance boundary consistency across views. Experiments conducted on the MIP-360, T&T, and NVOS datasets demonstrate that our method exhibits strong self-correction capability in the presence of mask errors and achieves reconstruction quality comparable to standard 3DGS approaches, while requiring only a...

---

## 15. Spectral Defense Against Resource-Targeting Attack in 3D Gaussian Splatting

- **作者**: Yang Chen, Yi Yu, Jiaming He et al.
- **发布时间**: 2026-03-13
- **arXiv链接**: [arXiv:2603.12796v1](https://arxiv.org/abs/2603.12796v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) deliver high-quality rendering, yet the Gaussian representation exposes a new attack surface, the resource-targeting attack. This attack poisons training images, excessively inducing Gaussian growth to cause resource exhaustion. Although efficiency-oriented methods such as smoothing, thresholding, and pruning have been explored, these spatial-domain strategies operate on visible structures but overlook how stealthy perturbations distort the underlying spectral behaviors of training data. As a result, poisoned inputs introduce abnormal high-frequency amplifications that mislead 3DGS into interpreting noisy patterns as detailed structures, ultimately causing unstable Gaussian overgrowth and degraded scene fidelity. To address this, we propose \textbf{Spectral Defense} in Gaussian and image fields. We first design a 3D frequency filter to selectively prune Gaussians exhibiting abnormally high frequencies. Since natural scenes also contain legitimate high-frequency structures, directly suppressing high frequencies is insufficient, and we further develop a 2D spectral regularization on renderings, distinguishing naturally isotropic frequencies while penalizing anisotropic angular energy to constrain noisy patterns. Experiments show that our defense builds robust, accurate, and secure 3DGS, suppressing overgrowth by up to $5.92\times$, reducing memory by up to $3.66\times$, and improving speed by up to $4.34\times$ under attacks.

---

## 16. Mobile-GS: Real-time Gaussian Splatting for Mobile Devices

- **作者**: Xiaobiao Du, Yida Wang, Kun Zhan, Xin Yu
- **发布时间**: 2026-03-12
- **arXiv链接**: [arXiv:2603.11531v1](https://arxiv.org/abs/2603.11531v1)
- **说明**: Project Page: https://xiaobiaodu.github.io/mobile-gs-project/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for high-quality rendering across a wide range of applications.However, its high computational demands and large storage costs pose significant challenges for deployment on mobile devices. In this work, we propose a mobile-tailored real-time Gaussian Splatting method, dubbed Mobile-GS, enabling efficient inference of Gaussian Splatting on edge devices. Specifically, we first identify alpha blending as the primary computational bottleneck, since it relies on the time-consuming Gaussian depth sorting process. To solve this issue, we propose a depth-aware order-independent rendering scheme that eliminates the need for sorting, thereby substantially accelerating rendering. Although this order-independent rendering improves rendering speed, it may introduce transparency artifacts in regions with overlapping geometry due to the scarcity of rendering order. To address this problem, we propose a neural view-dependent enhancement strategy, enabling more accurate modeling of view-dependent effects conditioned on viewing direction, 3D Gaussian geometry, and appearance attributes. In this way, Mobile-GS can achieve both high-quality and real-time rendering. Furthermore, to facilitate deployment on memory-constrained mobile platforms, we also introduce first-order spherical harmonics distillation, a neural vector quantization technique, and a contribution-based pruning strategy to reduce the number of Gaussian primitive...

---

## 17. ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare

- **作者**: Freeman Cheng, Botao Ye, Xueting Li et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09968v1](https://arxiv.org/abs/2603.09968v1)
- **英文摘要**: Online novel view synthesis remains challenging, requiring robust scene reconstruction from sequential, often unposed, observations. We present ReCoSplat, an autoregressive feed-forward Gaussian Splatting model supporting posed or unposed inputs, with or without camera intrinsics. While assembling local Gaussians using camera poses scales better than canonical-space prediction, it creates a dilemma during training: using ground-truth poses ensures stability but causes a distribution mismatch when predicted poses are used at inference. To address this, we introduce a Render-and-Compare (ReCo) module. ReCo renders the current reconstruction from the predicted viewpoint and compares it with the incoming observation, providing a stable conditioning signal that compensates for pose errors. To support long sequences, we propose a hybrid KV cache compression strategy combining early-layer truncation with chunk-level selective retention, reducing the KV cache size by over 90% for 100+ frames. ReCoSplat achieves state-of-the-art performance across different input settings on both in- and out-of-distribution benchmarks. Code and pretrained models will be released. Our project page is at https://freemancheng.com/ReCoSplat .

---

## 18. GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System

- **作者**: Zhiye Tang, Qiudan Zhang, Lei Zhang et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09718v1](https://arxiv.org/abs/2603.09718v1)
- **英文摘要**: Recently, the 3D Gaussian splatting (3DGS) technique for real-time radiance field rendering has revolutionized the field of volumetric scene representation, providing users with an immersive experience. But in return, it also poses a large amount of data volume, which is extremely bandwidth-intensive. Cutting-edge researchers have tried to introduce different approaches and construct multiple variants for 3DGS to obtain a more compact scene representation, but it is still challenging for real-time distribution. In this paper, we propose GSStream, a novel volumetric scene streaming system to support 3DGS data format. Specifically, GSStream integrates a collaborative viewport prediction module to better predict users' future behaviors by learning collaborative priors and historical priors from multiple users and users' viewport sequences and a deep reinforcement learning (DRL)-based bitrate adaptation module to tackle the state and action space variability challenge of the bitrate adaptation problem, achieving efficient volumetric scene delivery. Besides, we first build a user viewport trajectory dataset for volumetric scenes to support the training and streaming simulation. Extensive experiments prove that our proposed GSStream system outperforms existing representative volumetric scene streaming systems in visual quality and network usage. Demo video: https://youtu.be/3WEe8PN8yvA.

---

## 19. ProGS: Towards Progressive Coding for 3D Gaussian Splatting

- **作者**: Zhiye Tang, Lingzhuo Liu, Shengjie Jiao et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09703v1](https://arxiv.org/abs/2603.09703v1)
- **英文摘要**: With the emergence of 3D Gaussian Splatting (3DGS), numerous pioneering efforts have been made to address the effective compression issue of massive 3DGS data. 3DGS offers an efficient and scalable representation of 3D scenes by utilizing learnable 3D Gaussians, but the large size of the generated data has posed significant challenges for storage and transmission. Existing methods, however, have been limited by their inability to support progressive coding, a crucial feature in streaming applications with varying bandwidth. To tackle this limitation, this paper introduce a novel approach that organizes 3DGS data into an octree structure, enabling efficient progressive coding. The proposed ProGS is a streaming-friendly codec that facilitates progressive coding for 3D Gaussian splatting, and significantly improves both compression efficiency and visual fidelity. The proposed method incorporates mutual information enhancement mechanisms to mitigate structural redundancy, leveraging the relevance between nodes in the octree hierarchy. By adapting the octree structure and dynamically adjusting the anchor nodes, ProGS ensures scalable data compression without compromising the rendering quality. ProGS achieves a remarkable 45X reduction in file storage compared to the original 3DGS format, while simultaneously improving visual performance by over 10%. This demonstrates that ProGS can provide a robust solution for real-time applications with varying network conditions.

---

## 20. X-GS: An Extensible Open Framework for Perceiving and Thinking via 3D Gaussian Splatting

- **作者**: Yueen Ma, Zenglin Xu, Irwin King
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09632v2](https://arxiv.org/abs/2603.09632v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications. However, most existing 3DGS methods operate in isolation, focusing on specific domains such as pose-free 3DGS, online SLAM, and semantic enrichment. In this paper, we introduce X-GS, an extensible open framework consisting of two major components: the X-GS-Perceiver, which unifies a broad range of 3DGS techniques to enable real-time online SLAM and distill semantic features; and the X-GS-Thinker, which interfaces with downstream multimodal models. In our implementation of the Perceiver, we integrate various 3DGS methods through three novel mechanisms: an online Vector Quantization (VQ) module, a GPU-accelerated grid-sampling scheme, and a highly parallelized pipeline design. The Thinker accommodates vision-language models and utilizes the resulting 3D semantic Gaussians, enabling downstream applications such as object detection, caption generation, and potentially embodied tasks. Experimental results on real-world datasets demonstrate the efficiency and newly unlocked multimodal capabilities of the X-GS framework.

---

## 21. Improving Continual Learning for Gaussian Splatting based Environments Reconstruction on Commercial Off-the-Shelf Edge Devices

- **作者**: Ivan Zaino, Matteo Risso, Daniele Jahier Pagliari et al.
- **发布时间**: 2026-03-09
- **arXiv链接**: [arXiv:2603.08499v1](https://arxiv.org/abs/2603.08499v1)
- **英文摘要**: Novel view synthesis (NVS) is increasingly relevant for edge robotics, where compact and incrementally updatable 3D scene models are needed for SLAM, navigation, and inspection under tight memory and latency budgets. Variational Bayesian Gaussian Splatting (VBGS) enables replay-free continual updates for the 3DGS algorithm by maintaining a probabilistic scene model, but its high-precision computations and large intermediate tensors make on-device training impractical. We present a precision-adaptive optimization framework that enables VBGS training on resource-constrained hardware without altering its variational formulation. We (i) profile VBGS to identify memory/latency hotspots, (ii) fuse memory-dominant kernels to reduce materialized intermediate tensors, and (iii) automatically assign operation-level precisions via a mixed-precision search with bounded relative error. Across the Blender, Habitat, and Replica datasets, our optimised pipeline reduces peak memory from 9.44 GB to 1.11 GB and training time from ~234 min to ~61 min on an A5000 GPU, while preserving (and in some cases improving) reconstruction quality of the state-of-the-art VBGS baseline. We also enable for the first time NVS training on a commercial embedded platform, the Jetson Orin Nano, reducing per-frame latency by 19x compared to 3DGS.

---

## 22. Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis

- **作者**: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang
- **发布时间**: 2026-03-03
- **arXiv链接**: [arXiv:2603.02866v1](https://arxiv.org/abs/2603.02866v1)
- **英文摘要**: We present multimodal-prior-guided importance sampling as the central mechanism for hierarchical 3D Gaussian Splatting (3DGS) in sparse-view novel view synthesis. Our sampler fuses complementary cues { -- } photometric rendering residuals, semantic priors, and geometric priors { -- } to produce a robust, local recoverability estimate that directly drives where to inject fine Gaussians. Built around this sampling core, our framework comprises (1) a coarse-to-fine Gaussian representation that encodes global shape with a stable coarse layer and selectively adds fine primitives where the multimodal metric indicates recoverable detail; and (2) a geometric-aware sampling and retention policy that concentrates refinement on geometrically critical and complex regions while protecting newly added primitives in underconstrained areas from premature pruning. By prioritizing regions supported by consistent multimodal evidence rather than raw residuals alone, our method alleviates overfitting texture-induced errors and suppresses noise from pose/appearance inconsistencies. Experiments on diverse sparse-view benchmarks demonstrate state-of-the-art reconstructions, with up to +0.3 dB PSNR on DTU.

---

## 23. HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views

- **作者**: Jiashu Li, Xumeng Han, Zhaoyang Wei et al.
- **发布时间**: 2026-03-01
- **arXiv链接**: [arXiv:2603.01099v2](https://arxiv.org/abs/2603.01099v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a promising approach in novel view synthesis, combining photorealistic rendering with real-time efficiency. However, its success heavily relies on dense camera coverage; under sparse-view conditions, insufficient supervision leads to irregular Gaussian distributions, characterized by globally sparse coverage, blurred background, and distorted high-frequency areas. To address this, we propose HeroGS, Hierarchical Guidance for Robust 3D Gaussian Splatting, a unified framework that establishes hierarchical guidance across the image, feature, and parameter levels. At the image level, sparse supervision is converted into pseudo-dense guidance, globally regularizing the Gaussian distributions and forming a consistent foundation for subsequent optimization. Building upon this, Feature-Adaptive Densification and Pruning (FADP) at the feature level leverages low-level features to refine high-frequency details and adaptively densifies Gaussians in background regions. The optimized distributions then support Co-Pruned Geometry Consistency (CPG) at parameter level, which guides geometric consistency through parameter freezing and co-pruning, effectively removing inconsistent splats. The hierarchical guidance strategy effectively constrains and optimizes the overall Gaussian distributions, thereby enhancing both structural fidelity and rendering quality. Extensive experiments demonstrate that HeroGS achieves high-fidelity reconstruction...

---

## 24. Semantic-Guided 3D Gaussian Splatting for Transient Object Removal

- **作者**: Aditi Prabakaran, Priyesh Shukla
- **发布时间**: 2026-02-17
- **arXiv链接**: [arXiv:2602.15516v1](https://arxiv.org/abs/2602.15516v1)
- **英文摘要**: Transient objects in casual multi-view captures cause ghosting artifacts in 3D Gaussian Splatting (3DGS) reconstruction. Existing solutions relied on scene decomposition at significant memory cost or on motion-based heuristics that were vulnerable to parallax ambiguity. A semantic filtering framework was proposed for category-aware transient removal using vision-language models. CLIP similarity scores between rendered views and distractor text prompts were accumulated per-Gaussian across training iterations. Gaussians exceeding a calibrated threshold underwent opacity regularization and periodic pruning. Unlike motion-based approaches, semantic classification resolved parallax ambiguity by identifying object categories independently of motion patterns. Experiments on the RobustNeRF benchmark demonstrated consistent improvement in reconstruction quality over vanilla 3DGS across four sequences, while maintaining minimal memory overhead and real-time rendering performance. Threshold calibration and comparisons with baselines validated semantic guidance as a practical strategy for transient removal in scenarios with predictable distractor categories.

---

## 25. CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video

- **作者**: Hojun Song, Heejung Choi, Aro Kim et al.
- **发布时间**: 2026-02-10
- **arXiv链接**: [arXiv:2602.09816v1](https://arxiv.org/abs/2602.09816v1)
- **说明**: Preprint. Under review
- **英文摘要**: High-quality novel view synthesis (NVS) from real-world videos is crucial for applications such as cultural heritage preservation, digital twins, and immersive media. However, real-world videos typically contain long sequences with irregular camera trajectories and unknown poses, leading to pose drift, feature misalignment, and geometric distortion during reconstruction. Moreover, lossy compression amplifies these issues by introducing inconsistencies that gradually degrade geometry and rendering quality. While recent studies have addressed either long-sequence NVS or unposed reconstruction, compression-aware approaches still focus on specific artifacts or limited scenarios, leaving diverse compression patterns in long videos insufficiently explored. In this paper, we propose CompSplat, a compression-aware training framework that explicitly models frame-wise compression characteristics to mitigate inter-frame inconsistency and accumulated geometric errors. CompSplat incorporates compression-aware frame weighting and an adaptive pruning strategy to enhance robustness and geometric consistency, particularly under heavy compression. Extensive experiments on challenging benchmarks, including Tanks and Temples, Free, and Hike, demonstrate that CompSplat achieves state-of-the-art rendering quality and pose accuracy, significantly surpassing most recent state-of-the-art NVS approaches under severe compression conditions.

---

## 26. Forecasting as Rendering: A 2D Gaussian Splatting Framework for Time Series Forecasting

- **作者**: Yixin Wang, Yifan Hu, Peiyuan Liu et al.
- **发布时间**: 2026-02-10
- **arXiv链接**: [arXiv:2603.02220v1](https://arxiv.org/abs/2603.02220v1)
- **英文摘要**: Time series forecasting (TSF) remains a challenging problem due to the intricate entanglement of intraperiod-fluctuations and interperiod-trends. While recent advances have attempted to reshape 1D sequences into 2D period-phase representations, they suffer from two principal limitations.Firstly, treating reshaped tensors as static images results in a topological mismatch, as standard spatial operators sever chronological continuity at grid boundaries. Secondly, relying on uniform fixed-size representations allocates modeling capacity inefficiently and fails to provide the adaptive resolution required for compressible, non-stationary temporal patterns. To address these limitations, we introduce TimeGS, a novel framework that fundamentally shifts the forecasting paradigm from regression to 2D generative rendering. By reconceptualizing the future sequence as a continuous latent surface, TimeGS utilizes the inherent anisotropy of Gaussian kernels to adaptively model complex variations with flexible geometric alignment. To realize this, we introduce a Multi-Basis Gaussian Kernel Generation (MB-GKG) block that synthesizes kernels from a fixed dictionary to stabilize optimization, and a Multi-Period Chronologically Continuous Rasterization (MP-CCR) block that enforces strict temporal continuity across periodic boundaries. Comprehensive experiments on standard benchmark datasets demonstrate that TimeGS attains state-of-the-art performance.

---

## 27. GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification

- **作者**: Soonbin Lee, Yeong-Gyu Kim, Simon Sasse et al.
- **发布时间**: 2026-02-06
- **arXiv链接**: [arXiv:2602.06830v1](https://arxiv.org/abs/2602.06830v1)
- **英文摘要**: Existing 3D Gaussian Splatting simplification methods commonly use importance scores, such as blending weights or sensitivity, to identify redundant Gaussians. However, these scores are not driven by visual error metrics, often leading to suboptimal trade-offs between compactness and rendering fidelity. We present GaussianPOP, a principled simplification framework based on analytical Gaussian error quantification. Our key contribution is a novel error criterion, derived directly from the 3DGS rendering equation, that precisely measures each Gaussian's contribution to the rendered image. By introducing a highly efficient algorithm, our framework enables practical error calculation in a single forward pass. The framework is both accurate and flexible, supporting on-training pruning as well as post-training simplification via iterative error re-quantification for improved stability. Experimental results show that our method consistently outperforms existing state-of-the-art pruning methods across both application scenarios, achieving a superior trade-off between model compactness and high rendering quality.

---

## 28. Nix and Fix: Targeting 1000x Compression of 3D Gaussian Splatting with Diffusion Models

- **作者**: Cem Eteke, Enzo Tartaglione
- **发布时间**: 2026-02-04
- **arXiv链接**: [arXiv:2602.04549v1](https://arxiv.org/abs/2602.04549v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) revolutionized novel view rendering. Instead of inferring from dense spatial points, as implicit representations do, 3DGS uses sparse Gaussians. This enables real-time performance but increases space requirements, hindering applications such as immersive communication. 3DGS compression emerged as a field aimed at alleviating this issue. While impressive progress has been made, at low rates, compression introduces artifacts that degrade visual quality significantly. We introduce NiFi, a method for extreme 3DGS compression through restoration via artifact-aware, diffusion-based one-step distillation. We show that our method achieves state-of-the-art perceptual quality at extremely low rates, down to 0.1 MB, and towards 1000x rate improvement over 3DGS at comparable perceptual performance. The code will be open-sourced upon acceptance.

---

## 29. Constrained Dynamic Gaussian Splatting

- **作者**: Zihan Zheng, Zhenglong Wu, Xuanxuan Wang et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.03538v1](https://arxiv.org/abs/2602.03538v1)
- **英文摘要**: While Dynamic Gaussian Splatting enables high-fidelity 4D reconstruction, its deployment is severely hindered by a fundamental dilemma: unconstrained densification leads to excessive memory consumption incompatible with edge devices, whereas heuristic pruning fails to achieve optimal rendering quality under preset Gaussian budgets. In this work, we propose Constrained Dynamic Gaussian Splatting (CDGS), a novel framework that formulates dynamic scene reconstruction as a budget-constrained optimization problem to enforce a strict, user-defined Gaussian budget during training. Our key insight is to introduce a differentiable budget controller as the core optimization driver. Guided by a multi-modal unified importance score, this controller fuses geometric, motion, and perceptual cues for precise capacity regulation. To maximize the utility of this fixed budget, we further decouple the optimization of static and dynamic elements, employing an adaptive allocation mechanism that dynamically distributes capacity based on motion complexity. Furthermore, we implement a three-phase training strategy to seamlessly integrate these constraints, ensuring precise adherence to the target count. Coupled with a dual-mode hybrid compression scheme, CDGS not only strictly adheres to hardware constraints (error < 2%}) but also pushes the Pareto frontier of rate-distortion performance. Extensive experiments demonstrate that CDGS delivers optimal rendering quality under varying capacity limits, ach...

---

## 30. WebSplatter: Enabling Cross-Device Efficient Gaussian Splatting in Web Browsers via WebGPU

- **作者**: Yudong Han, Chao Xu, Xiaodan Ye et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.03207v1](https://arxiv.org/abs/2602.03207v1)
- **英文摘要**: We present WebSplatter, an end-to-end GPU rendering pipeline for the heterogeneous web ecosystem. Unlike naive ports, WebSplatter introduces a wait-free hierarchical radix sort that circumvents the lack of global atomics in WebGPU, ensuring deterministic execution across diverse hardware. Furthermore, we propose an opacity-aware geometry culling stage that dynamically prunes splats before rasterization, significantly reducing overdraw and peak memory footprint. Evaluation demonstrates that WebSplatter consistently achieves 1.2$\times$ to 4.5$\times$ speedups over state-of-the-art web viewers.

---

## 31. SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation

- **作者**: Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.02989v2](https://arxiv.org/abs/2602.02989v2)
- **英文摘要**: Novel view synthesis of dynamic scenes is fundamental to achieving photorealistic 4D reconstruction and immersive visual experiences. Recent progress in Gaussian-based representations has significantly improved real-time rendering quality, yet existing methods still struggle to maintain a balance between long-term static and short-term dynamic regions in both representation and optimization. To address this, we present SharpTimeGS, a lifespan-aware 4D Gaussian framework that achieves temporally adaptive modeling of both static and dynamic regions under a unified representation. Specifically, we introduce a learnable lifespan parameter that reformulates temporal visibility from a Gaussian-shaped decay into a flat-top profile, allowing primitives to remain consistently active over their intended duration and avoiding redundant densification. In addition, the learned lifespan modulates each primitives' motion, reducing drift in long-lived static points while retaining unrestricted motion for short-lived dynamic ones. This effectively decouples motion magnitude from temporal duration, improving long-term stability without compromising dynamic fidelity. Moreover, we design a lifespan-velocity-aware densification strategy that mitigates optimization imbalance between static and dynamic regions by allocating more capacity to regions with pronounced motion while keeping static areas compact and stable. Extensive experiments on multiple benchmarks demonstrate that our method achieves ...

---

## 32. HPC: Hierarchical Point-based Latent Representation for Streaming Dynamic Gaussian Splatting Compression

- **作者**: Yangzhi Ma, Bojun Liu, Wenting Liao et al.
- **发布时间**: 2026-01-31
- **arXiv链接**: [arXiv:2602.00671v1](https://arxiv.org/abs/2602.00671v1)
- **英文摘要**: While dynamic Gaussian Splatting has driven significant advances in free-viewpoint video, maintaining its rendering quality with a small memory footprint for efficient streaming transmission still presents an ongoing challenge. Existing streaming dynamic Gaussian Splatting compression methods typically leverage a latent representation to drive the neural network for predicting Gaussian residuals between frames. Their core latent representations can be categorized into structured grid-based and unstructured point-based paradigms. However, the former incurs significant parameter redundancy by inevitably modeling unoccupied space, while the latter suffers from limited compactness as it fails to exploit local correlations. To relieve these limitations, we propose HPC, a novel streaming dynamic Gaussian Splatting compression framework. It employs a hierarchical point-based latent representation that operates on a per-Gaussian basis to avoid parameter redundancy in unoccupied space. Guided by a tailored aggregation scheme, these latent points achieve high compactness with low spatial redundancy. To improve compression efficiency, we further undertake the first investigation to compress neural networks for streaming dynamic Gaussian Splatting through mining and exploiting the inter-frame correlation of parameters. Combined with latent compression, this forms a fully end-to-end compression framework. Comprehensive experimental evaluations demonstrate that HPC substantially outperform...

---

## 33. LangGS-SLAM: Real-Time Language-Feature Gaussian Splatting SLAM

- **作者**: Seongbo Ha, Sibaek Lee, Kyungsu Kang et al.
- **发布时间**: 2026-01-28
- **arXiv链接**: [arXiv:2602.06991v1](https://arxiv.org/abs/2602.06991v1)
- **说明**: 17 pages, 4 figures
- **英文摘要**: In this paper, we propose a RGB-D SLAM system that reconstructs a language-aligned dense feature field while sustaining low-latency tracking and mapping. First, we introduce a Top-K Rendering pipeline, a high-throughput and semantic-distortion-free method for efficiently rendering high-dimensional feature maps. To address the resulting semantic-geometric discrepancy and mitigate the memory consumption, we further design a multi-criteria map management strategy that prunes redundant or inconsistent Gaussians while preserving scene integrity. Finally, a hybrid field optimization framework jointly refines the geometric and semantic fields under real-time constraints by decoupling their optimization frequencies according to field characteristics. The proposed system achieves superior geometric fidelity compared to geometric-only baselines and comparable semantic fidelity to offline approaches while operating at 15 FPS. Our results demonstrate that online SLAM with dense, uncompressed language-aligned feature fields is both feasible and effective, bridging the gap between 3D perception and language-based reasoning.

---

## 34. LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction

- **作者**: Xinhui Liu, Can Wang, Lei Liu et al.
- **发布时间**: 2026-01-26
- **arXiv链接**: [arXiv:2601.18475v1](https://arxiv.org/abs/2601.18475v1)
- **英文摘要**: Free-Viewpoint Video (FVV) reconstruction enables photorealistic and interactive 3D scene visualization; however, real-time streaming is often bottlenecked by sparse-view inputs, prohibitive training costs, and bandwidth constraints. While recent 3D Gaussian Splatting (3DGS) has advanced FVV due to its superior rendering speed, Streaming Free-Viewpoint Video (SFVV) introduces additional demands for rapid optimization, high-fidelity reconstruction under sparse constraints, and minimal storage footprints. To bridge this gap, we propose StreamLoD-GS, an LoD-based Gaussian Splatting framework designed specifically for SFVV. Our approach integrates three core innovations: 1) an Anchor- and Octree-based LoD-structured 3DGS with a hierarchical Gaussian dropout technique to ensure efficient and stable optimization while maintaining high-quality rendering; 2) a GMM-based motion partitioning mechanism that separates dynamic and static content, refining dynamic regions while preserving background stability; and 3) a quantized residual refinement framework that significantly reduces storage requirements without compromising visual fidelity. Extensive experiments demonstrate that StreamLoD-GS achieves competitive or state-of-the-art performance in terms of quality, efficiency, and storage.

---

## 35. PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling

- **作者**: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang
- **发布时间**: 2026-01-24
- **arXiv链接**: [arXiv:2601.17354v4](https://arxiv.org/abs/2601.17354v4)
- **英文摘要**: Efficient and high-fidelity 3D scene modeling is a long-standing pursuit in computer graphics. While recent 3D Gaussian Splatting (3DGS) methods achieve impressive real-time modeling performance, they rely on resource-unconstrained training assumptions that fail on mobile devices, which are limited by minute-scale training budgets and hardware-available peak-memory. We present PocketGS, a mobile scene modeling paradigm that enables on-device 3DGS training under these tightly coupled constraints while preserving high perceptual fidelity. Our method resolves the fundamental contradictions of standard 3DGS through three co-designed operators: G builds geometry-faithful point-cloud priors; I injects local surface statistics to seed anisotropic Gaussians, thereby reducing early conditioning gaps; and T unrolls alpha compositing with cached intermediates and index-mapped gradient scattering for stable mobile backpropagation. Collectively, these operators satisfy the competing requirements of training efficiency, memory compactness, and modeling fidelity. Extensive experiments demonstrate that PocketGS is able to outperform the powerful mainstream workstation 3DGS baseline to deliver high-quality reconstructions, enabling a fully on-device, practical capture-to-rendering workflow.

---

## 36. LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting

- **作者**: Yuhan Chen, Wenxuan Yu, Guofa Li et al.
- **发布时间**: 2026-01-22
- **arXiv链接**: [arXiv:2601.15772v1](https://arxiv.org/abs/2601.15772v1)
- **英文摘要**: 2D Gaussian Splatting (2DGS) is an emerging explicit scene representation method with significant potential for image compression due to high fidelity and high compression ratios. However, existing low-light enhancement algorithms operate predominantly within the pixel domain. Processing 2DGS-compressed images necessitates a cumbersome decompression-enhancement-recompression pipeline, which compromises efficiency and introduces secondary degradation. To address these limitations, we propose LL-GaussianImage, the first zero-shot unsupervised framework designed for low-light enhancement directly within the 2DGS compressed representation domain. Three primary advantages are offered by this framework. First, a semantic-guided Mixture-of-Experts enhancement framework is designed. Dynamic adaptive transformations are applied to the sparse attribute space of 2DGS using rendered images as guidance to enable compression-as-enhancement without full decompression to a pixel grid. Second, a multi-objective collaborative loss function system is established to strictly constrain smoothness and fidelity during enhancement, suppressing artifacts while improving visual quality. Third, a two-stage optimization process is utilized to achieve reconstruction-as-enhancement. The accuracy of the base representation is ensured through single-scale reconstruction and network robustness is enhanced. High-quality enhancement of low-light images is achieved while high compression ratios are maintained. ...

---

## 37. POTR: Post-Training 3DGS Compression

- **作者**: Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael
- **发布时间**: 2026-01-21
- **arXiv链接**: [arXiv:2601.14821v1](https://arxiv.org/abs/2601.14821v1)
- **说明**: 15 pages, 12 figures. Submitted to IEEE TCSVT, under review
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a promising contender to Neural Radiance Fields (NeRF) in 3D scene reconstruction and real-time novel view synthesis. 3DGS outperforms NeRF in training and inference speed but has substantially higher storage requirements. To remedy this downside, we propose POTR, a post-training 3DGS codec built on two novel techniques. First, POTR introduces a novel pruning approach that uses a modified 3DGS rasterizer to efficiently calculate every splat's individual removal effect simultaneously. This technique results in 2-4x fewer splats than other post-training pruning techniques and as a result also significantly accelerates inference with experiments demonstrating 1.5-2x faster inference than other compressed models. Second, we propose a novel method to recompute lighting coefficients, significantly reducing their entropy without using any form of training. Our fast and highly parallel approach especially increases AC lighting coefficient sparsity, with experiments demonstrating increases from 70% to 97%, with minimal loss in quality. Finally, we extend POTR with a simple fine-tuning scheme to further enhance pruning, inference, and rate-distortion performance. Experiments demonstrate that POTR, even without fine-tuning, consistently outperforms all other post-training compression techniques in both rate-distortion performance and inference speed.

---

## 38. Structured Image-based Coding for Efficient Gaussian Splatting Compression

- **作者**: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz
- **发布时间**: 2026-01-20
- **arXiv链接**: [arXiv:2601.14510v3](https://arxiv.org/abs/2601.14510v3)
- **英文摘要**: Gaussian Splatting (GS) has recently emerged as a state-of-the-art representation for radiance fields, combining real-time rendering with high visual fidelity. However, GS models require storing millions of parameters, leading to large file sizes that impair their use in practical multimedia systems. To address this limitation, this paper introduces GS Image-based Compression (GSICO), a novel GS codec that efficiently compresses pre-trained GS models while preserving perceptual fidelity. The core contribution lies in a mapping procedure that arranges GS parameters into structured images, guided by a novel algorithm that enhances spatial coherence. These GS parameter images are then encoded using a conventional image codec. Experimental evaluations on Tanks and Temples, Deep Blending, and Mip-NeRF360 datasets show that GSICO achieves average compression factors of 20.2x with minimal loss in visual quality, as measured by PSNR, SSIM, and LPIPS. Compared with state-of-the-art GS compression methods, the proposed codec consistently yields superior rate-distortion (RD) trade-offs.

---

## 39. TIDI-GS: Floater Suppression in 3D Gaussian Splatting for Enhanced Indoor Scene Fidelity

- **作者**: Sooyeun Yang, Cheyul Im, Jee Won Lee, Jongseong Brad Choi
- **发布时间**: 2026-01-14
- **arXiv链接**: [arXiv:2601.09291v2](https://arxiv.org/abs/2601.09291v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a technique to create high-quality, real-time 3D scenes from images. This method often produces visual artifacts known as floaters--nearly transparent, disconnected elements that drift in space away from the actual surface. This geometric inaccuracy undermines the reliability of these models for practical applications, which is critical. To address this issue, we introduce TIDI-GS, a new training framework designed to eliminate these floaters. A key benefit of our approach is that it functions as a lightweight plugin for the standard 3DGS pipeline, requiring no major architectural changes and adding minimal overhead to the training process. The core of our method is a floater pruning algorithm--TIDI--that identifies and removes floaters based on several criteria: their consistency across multiple viewpoints, their spatial relationship to other elements, and an importance score learned during training. The framework includes a mechanism to preserve fine details, ensuring that important high-frequency elements are not mistakenly removed. This targeted cleanup is supported by a monocular depth-based loss function that helps improve the overall geometric structure of the scene. Our experiments demonstrate that TIDI-GS improves both the perceptual quality and geometric integrity of reconstructions, transforming them into robust digital assets, suitable for high-fidelity applications.

---

## 40. Sketch&Patch++: Efficient Structure-Aware 3D Gaussian Representation

- **作者**: Yuang Shi, Géraldine Morin, Simone Gasparini, Wei Tsang Ooi
- **发布时间**: 2026-01-08
- **arXiv链接**: [arXiv:2601.05394v2](https://arxiv.org/abs/2601.05394v2)
- **英文摘要**: We observe that Gaussians exhibit distinct roles and characteristics analogous to traditional artistic techniques -- like how artists first sketch outlines before filling in broader areas with color, some Gaussians capture high-frequency features such as edges and contours, while others represent broader, smoother regions analogous to brush strokes that add volume and depth. Based on this observation, we propose a hybrid representation that categorizes Gaussians into (i) Sketch Gaussians, which represent high-frequency, boundary-defining features, and (ii) Patch Gaussians, which cover low-frequency, smooth regions. This semantic separation naturally enables layered progressive streaming, where the compact Sketch Gaussians establish the structural skeleton before Patch Gaussians incrementally refine volumetric detail.   In this work, we extend our previous method to arbitrary 3D scenes by proposing a novel hierarchical adaptive categorization framework that operates directly on the 3DGS representation. Our approach employs multi-criteria density-based clustering, combined with adaptive quality-driven refinement. This method eliminates dependency on external 3D line primitives while ensuring optimal parametric encoding effectiveness. Our comprehensive evaluation across diverse scenes, including both man-made and natural environments, demonstrates that our method achieves up to 1.74 dB improvement in PSNR, 6.7% in SSIM, and 41.4% in LPIPS at equivalent model sizes compared to un...

---

## 41. SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting

- **作者**: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang
- **发布时间**: 2026-01-07
- **arXiv链接**: [arXiv:2601.04348v1](https://arxiv.org/abs/2601.04348v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting have allowed for real-time, high-fidelity novel view synthesis. Nonetheless, these models have significant storage requirements for large and medium-sized scenes, hindering their deployment over cloud and streaming services. Some of the most recent progressive compression techniques for these models rely on progressive masking and scalar quantization techniques to reduce the bitrate of Gaussian attributes using spatial context models. While effective, scalar quantization may not optimally capture the correlations of high-dimensional feature vectors, which can potentially limit the rate-distortion performance.   In this work, we introduce a novel progressive codec for 3D Gaussian Splatting that replaces traditional methods with a more powerful Residual Vector Quantization approach to compress the primitive features. Our key contribution is an auto-regressive entropy model, guided by a multi-resolution hash grid, that accurately predicts the conditional probability of each successive transmitted index, allowing for coarse and refinement layers to be compressed with high efficiency.

---

## 42. Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting

- **作者**: Subhankar Mishra
- **发布时间**: 2026-01-01
- **arXiv链接**: [arXiv:2601.00913v1](https://arxiv.org/abs/2601.00913v1)
- **英文摘要**: 3D Gaussian Splatting produces high-quality scene reconstructions but generates hundreds of thousands of spurious Gaussians (floaters) scattered throughout the environment. These artifacts obscure objects of interest and inflate model sizes, hindering deployment in bandwidth-constrained applications. We present Clean-GS, a method for removing background clutter and floaters from 3DGS reconstructions using sparse semantic masks. Our approach combines whitelist-based spatial filtering with color-guided validation and outlier removal to achieve 60-80\% model compression while preserving object quality. Unlike existing 3DGS pruning methods that rely on global importance metrics, Clean-GS uses semantic information from as few as 3 segmentation masks (1\% of views) to identify and remove Gaussians not belonging to the target object. Our multi-stage approach consisting of (1) whitelist filtering via projection to masked regions, (2) depth-buffered color validation, and (3) neighbor-based outlier removal isolates monuments and objects from complex outdoor scenes. Experiments on Tanks and Temples show that Clean-GS reduces file sizes from 125MB to 47MB while maintaining rendering quality, making 3DGS models practical for web deployment and AR/VR applications. Our code is available at https://github.com/smlab-niser/clean-gs

---

## 43. Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding

- **作者**: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li
- **发布时间**: 2025-12-19
- **arXiv链接**: [arXiv:2512.17528v1](https://arxiv.org/abs/2512.17528v1)
- **说明**: Accepted by DCC 2026
- **英文摘要**: Substantial Gaussian splatting format point clouds require effective compression. In this paper, we propose Voxel-GS, a simple yet highly effective framework that departs from the complex neural entropy models of prior work, instead achieving competitive performance using only a lightweight rate proxy and run-length coding. Specifically, we employ a differentiable quantization to discretize the Gaussian attributes of Scaffold-GS. Subsequently, a Laplacian-based rate proxy is devised to impose an entropy constraint, guiding the generation of high-fidelity and compact reconstructions. Finally, this integer-type Gaussian point cloud is compressed losslessly using Octree and run-length coding. Experiments validate that the proposed rate proxy accurately estimates the bitrate of run-length coding, enabling Voxel-GS to eliminate redundancy and optimize for a more compact representation. Consequently, our method achieves a remarkable compression ratio with significantly faster coding speeds than prior art. The code is available at https://github.com/zb12138/VoxelGS.

---

## 44. Lightweight 3D Gaussian Splatting Compression via Video Codec

- **作者**: Qi Yang, Geert Van Der Auwera, Zhu Li
- **发布时间**: 2025-12-12
- **arXiv链接**: [arXiv:2512.11186v1](https://arxiv.org/abs/2512.11186v1)
- **说明**: Accepted by DCC2026 Oral
- **英文摘要**: Current video-based GS compression methods rely on using Parallel Linear Assignment Sorting (PLAS) to convert 3D GS into smooth 2D maps, which are computationally expensive and time-consuming, limiting the application of GS on lightweight devices. In this paper, we propose a Lightweight 3D Gaussian Splatting (GS) Compression method based on Video codec (LGSCV). First, a two-stage Morton scan is proposed to generate blockwise 2D maps that are friendly for canonical video codecs in which the coding units (CU) are square blocks. A 3D Morton scan is used to permute GS primitives, followed by a 2D Morton scan to map the ordered GS primitives to 2D maps in a blockwise style. However, although the blockwise 2D maps report close performance to the PLAS map in high-bitrate regions, they show a quality collapse at medium-to-low bitrates. Therefore, a principal component analysis (PCA) is used to reduce the dimensionality of spherical harmonics (SH), and a MiniPLAS, which is flexible and fast, is designed to permute the primitives within certain block sizes. Incorporating SH PCA and MiniPLAS leads to a significant gain in rate-distortion (RD) performance, especially at medium and low bitrates. MiniPLAS can also guide the setting of the codec CU size configuration and significantly reduce encoding time. Experimental results on the MPEG dataset demonstrate that the proposed LGSCV achieves over 20% RD gain compared with state-of-the-art methods, while reducing 2D map generation time to app...

---

## 45. SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting

- **作者**: Zihan Li, Tengfei Wang, Wentian Gan et al.
- **发布时间**: 2025-11-17
- **arXiv链接**: [arXiv:2511.13278v2](https://arxiv.org/abs/2511.13278v2)
- **说明**: This paper has been submitted to the 2026 ISPRS Congress
- **英文摘要**: Lightweight building surface models are crucial for digital city, navigation, and fast geospatial analytics, yet conventional multi-view geometry pipelines remain cumbersome and quality-sensitive due to their reliance on dense reconstruction, meshing, and subsequent simplification. This work presents SF-Recon, a method that directly reconstructs lightweight building surfaces from multi-view images without post-hoc mesh simplification. We first train an initial 3D Gaussian Splatting (3DGS) field to obtain a view-consistent representation. Building structure is then distilled by a normal-gradient-guided Gaussian optimization that selects primitives aligned with roof and wall boundaries, followed by multi-view edge-consistency pruning to enhance structural sharpness and suppress non-structural artifacts without external supervision. Finally, a multi-view depth-constrained Delaunay triangulation converts the structured Gaussian field into a lightweight, structurally faithful building mesh. Based on a proposed SF dataset, the experimental results demonstrate that our SF-Recon can directly reconstruct lightweight building models from multi-view imagery, achieving substantially fewer faces and vertices while maintaining computational efficiency. Website:https://lzh282140127-cell.github.io/SF-Recon-project/

---

