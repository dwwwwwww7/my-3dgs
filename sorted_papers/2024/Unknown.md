# 未知会议 2024

> **最后更新**： 2025-12-14 01:27:11

本页面包含 2024 年 未知会议 会议的论文列表。

## 1. CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction

- **作者**: Yuanyuan Gao, Yalun Dai, Hao Li et al.
- **发布时间**: 2024-12-23
- **arXiv链接**: [arXiv:2412.17612v1](https://arxiv.org/abs/2412.17612v1)
- **说明**: Our project page is available at \url{https://gyy456.github.io/CoSurfGS}
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated impressive performance in scene reconstruction. However, most existing GS-based surface reconstruction methods focus on 3D objects or limited scenes. Directly applying these methods to large-scale scene reconstruction will pose challenges such as high memory costs, excessive time consumption, and lack of geometric detail, which makes it difficult to implement in practical applications. To address these issues, we propose a multi-agent collaborative fast 3DGS surface reconstruction framework based on distributed learning for large-scale surface reconstruction. Specifically, we develop local model compression (LMC) and model aggregation schemes (MAS) to achieve high-quality surface representation of large scenes while reducing GPU memory consumption. Extensive experiments on Urban3d, MegaNeRF, and BlendedMVS demonstrate that our proposed method can achieve fast and scalable high-fidelity surface reconstruction and photorealistic rendering. Our project page is available at \url{https://gyy456.github.io/CoSurfGS}.

---

## 2. HyperGS: Hyperspectral 3D Gaussian Splatting

- **作者**: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield
- **发布时间**: 2024-12-17
- **arXiv链接**: [arXiv:2412.12849v1](https://arxiv.org/abs/2412.12849v1)
- **英文摘要**: We introduce HyperGS, a novel framework for Hyperspectral Novel View Synthesis (HNVS), based on a new latent 3D Gaussian Splatting (3DGS) technique. Our approach enables simultaneous spatial and spectral renderings by encoding material properties from multi-view 3D hyperspectral datasets. HyperGS reconstructs high-fidelity views from arbitrary perspectives with improved accuracy and speed, outperforming currently existing methods. To address the challenges of high-dimensional data, we perform view synthesis in a learned latent space, incorporating a pixel-wise adaptive density function and a pruning technique for increased training stability and efficiency. Additionally, we introduce the first HNVS benchmark, implementing a number of new baselines based on recent SOTA RGB-NVS techniques, alongside the small number of prior works on HNVS. We demonstrate HyperGS's robustness through extensive evaluation of real and simulated hyperspectral scenes with a 14db accuracy improvement upon previously published models.

---

## 3. EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting

- **作者**: Dong In Lee, Hyeongcheol Park, Jiyoung Seo et al.
- **发布时间**: 2024-12-16
- **arXiv链接**: [arXiv:2412.11520v2](https://arxiv.org/abs/2412.11520v2)
- **英文摘要**: Recent advancements in 3D editing have highlighted the potential of text-driven methods in real-time, user-friendly AR/VR applications. However, current methods rely on 2D diffusion models without adequately considering multi-view information, resulting in multi-view inconsistency. While 3D Gaussian Splatting (3DGS) significantly improves rendering quality and speed, its 3D editing process encounters difficulties with inefficient optimization, as pre-trained Gaussians retain excessive source information, hindering optimization. To address these limitations, we propose EditSplat, a novel text-driven 3D scene editing framework that integrates Multi-view Fusion Guidance (MFG) and Attention-Guided Trimming (AGT). Our MFG ensures multi-view consistency by incorporating essential multi-view information into the diffusion process, leveraging classifier-free guidance from the text-to-image diffusion model and the geometric structure inherent to 3DGS. Additionally, our AGT utilizes the explicit representation of 3DGS to selectively prune and optimize 3D Gaussians, enhancing optimization efficiency and enabling precise, semantically rich local editing. Through extensive qualitative and quantitative evaluations, EditSplat achieves state-of-the-art performance, establishing a new benchmark for text-driven 3D scene editing.

---

## 4. TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views

- **作者**: Liang Zhao, Zehan Bao, Yi Xie et al.
- **发布时间**: 2024-12-13
- **arXiv链接**: [arXiv:2412.10051v1](https://arxiv.org/abs/2412.10051v1)
- **英文摘要**: Recent advances in Gaussian Splatting have significantly advanced the field, achieving both panoptic and interactive segmentation of 3D scenes. However, existing methodologies often overlook the critical need for reconstructing specified targets with complex structures from sparse views. To address this issue, we introduce TSGaussian, a novel framework that combines semantic constraints with depth priors to avoid geometry degradation in challenging novel view synthesis tasks. Our approach prioritizes computational resources on designated targets while minimizing background allocation. Bounding boxes from YOLOv9 serve as prompts for Segment Anything Model to generate 2D mask predictions, ensuring semantic accuracy and cost efficiency. TSGaussian effectively clusters 3D gaussians by introducing a compact identity encoding for each Gaussian ellipsoid and incorporating 3D spatial consistency regularization. Leveraging these modules, we propose a pruning strategy to effectively reduce redundancy in 3D gaussians. Extensive experiments demonstrate that TSGaussian outperforms state-of-the-art methods on three standard datasets and a new challenging dataset we collected, achieving superior results in novel view synthesis of specific objects. Code is available at: https://github.com/leon2000-ai/TSGaussian.

---

## 5. SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video

- **作者**: Jongmin Park, Minh-Quan Viet Bui, Juan Luis Gonzalez Bello et al.
- **发布时间**: 2024-12-13
- **arXiv链接**: [arXiv:2412.09982v2](https://arxiv.org/abs/2412.09982v2)
- **说明**: The first two authors contributed equally to this work (equal contribution). The last two authors advised equally to this work. Please visit our project page at this https://kaist-viclab.github.io/splinegs-site/
- **英文摘要**: Synthesizing novel views from in-the-wild monocular videos is challenging due to scene dynamics and the lack of multi-view cues. To address this, we propose SplineGS, a COLMAP-free dynamic 3D Gaussian Splatting (3DGS) framework for high-quality reconstruction and fast rendering from monocular videos. At its core is a novel Motion-Adaptive Spline (MAS) method, which represents continuous dynamic 3D Gaussian trajectories using cubic Hermite splines with a small number of control points. For MAS, we introduce a Motion-Adaptive Control points Pruning (MACP) method to model the deformation of each dynamic 3D Gaussian across varying motions, progressively pruning control points while maintaining dynamic modeling integrity. Additionally, we present a joint optimization strategy for camera parameter estimation and 3D Gaussian attributes, leveraging photometric and geometric consistency. This eliminates the need for Structure-from-Motion preprocessing and enhances SplineGS's robustness in real-world conditions. Experiments show that SplineGS significantly outperforms state-of-the-art methods in novel view synthesis quality for dynamic scenes from monocular videos, achieving thousands times faster rendering speed.

---

## 6. RP-SLAM: Real-time Photorealistic SLAM with Efficient 3D Gaussian Splatting

- **作者**: Lizhi Bai, Chunqi Tian, Jun Yang et al.
- **发布时间**: 2024-12-13
- **arXiv链接**: [arXiv:2412.09868v1](https://arxiv.org/abs/2412.09868v1)
- **英文摘要**: 3D Gaussian Splatting has emerged as a promising technique for high-quality 3D rendering, leading to increasing interest in integrating 3DGS into realism SLAM systems. However, existing methods face challenges such as Gaussian primitives redundancy, forgetting problem during continuous optimization, and difficulty in initializing primitives in monocular case due to lack of depth information. In order to achieve efficient and photorealistic mapping, we propose RP-SLAM, a 3D Gaussian splatting-based vision SLAM method for monocular and RGB-D cameras. RP-SLAM decouples camera poses estimation from Gaussian primitives optimization and consists of three key components. Firstly, we propose an efficient incremental mapping approach to achieve a compact and accurate representation of the scene through adaptive sampling and Gaussian primitives filtering. Secondly, a dynamic window optimization method is proposed to mitigate the forgetting problem and improve map consistency. Finally, for the monocular case, a monocular keyframe initialization method based on sparse point cloud is proposed to improve the initialization accuracy of Gaussian primitives, which provides a geometric basis for subsequent optimization. The results of numerous experiments demonstrate that RP-SLAM achieves state-of-the-art map rendering accuracy while ensuring real-time performance and model compactness.

---

## 7. SizeGS: Size-aware Compression of 3D Gaussian Splatting via Mixed Integer Programming

- **作者**: Shuzhao Xie, Jiahang Liu, Weixiang Zhang et al.
- **发布时间**: 2024-12-08
- **arXiv链接**: [arXiv:2412.05808v2](https://arxiv.org/abs/2412.05808v2)
- **说明**: Automatically compressing 3DGS into the desired file size while maximizing the visual quality
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) have greatly improved 3D reconstruction. However, its substantial data size poses a significant challenge for transmission and storage. While many compression techniques have been proposed, they fail to efficiently adapt to fluctuating network bandwidth, leading to resource wastage. We address this issue from the perspective of size-aware compression, where we aim to compress 3DGS to a desired size by quickly searching for suitable hyperparameters. Through a measurement study, we identify key hyperparameters that affect the size -- namely, the reserve ratio of Gaussians and bit-width settings for Gaussian attributes. Then, we formulate this hyperparameter optimization problem as a mixed-integer nonlinear programming (MINLP) problem, with the goal of maximizing visual quality while respecting the size budget constraint. To solve the MINLP, we decouple this problem into two parts: discretely sampling the reserve ratio and determining the bit-width settings using integer linear programming (ILP). To solve the ILP more quickly and accurately, we design a quality loss estimator and a calibrated size estimator, as well as implement a CUDA kernel. Extensive experiments on multiple 3DGS variants demonstrate that our method achieves state-of-the-art performance in post-training compression. Furthermore, our method can achieve comparable quality to leading training-required methods after fine-tuning.

---

## 8. WATER-GS: Toward Copyright Protection for 3D Gaussian Splatting via Universal Watermarking

- **作者**: Yuqi Tan, Xiang Liu, Shuzhao Xie et al.
- **发布时间**: 2024-12-07
- **arXiv链接**: [arXiv:2412.05695v1](https://arxiv.org/abs/2412.05695v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a pivotal technique for 3D scene representation, providing rapid rendering speeds and high fidelity. As 3DGS gains prominence, safeguarding its intellectual property becomes increasingly crucial since 3DGS could be used to imitate unauthorized scene creations and raise copyright issues. Existing watermarking methods for implicit NeRFs cannot be directly applied to 3DGS due to its explicit representation and real-time rendering process, leaving watermarking for 3DGS largely unexplored. In response, we propose WATER-GS, a novel method designed to protect 3DGS copyrights through a universal watermarking strategy. First, we introduce a pre-trained watermark decoder, treating raw 3DGS generative modules as potential watermark encoders to ensure imperceptibility. Additionally, we implement novel 3D distortion layers to enhance the robustness of the embedded watermark against common real-world distortions of point cloud data. Comprehensive experiments and ablation studies demonstrate that WATER-GS effectively embeds imperceptible and robust watermarks into 3DGS without compromising rendering efficiency and quality. Our experiments indicate that the 3D distortion layers can yield up to a 20% improvement in accuracy rate. Notably, our method is adaptable to different 3DGS variants, including 3DGS compression frameworks and 2D Gaussian splatting.

---

## 9. 2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction

- **作者**: Wanting Zhang, Haodong Xiang, Zhichao Liao et al.
- **发布时间**: 2024-12-04
- **arXiv链接**: [arXiv:2412.03428v1](https://arxiv.org/abs/2412.03428v1)
- **英文摘要**: The reconstruction of indoor scenes remains challenging due to the inherent complexity of spatial structures and the prevalence of textureless regions. Recent advancements in 3D Gaussian Splatting have improved novel view synthesis with accelerated processing but have yet to deliver comparable performance in surface reconstruction. In this paper, we introduce 2DGS-Room, a novel method leveraging 2D Gaussian Splatting for high-fidelity indoor scene reconstruction. Specifically, we employ a seed-guided mechanism to control the distribution of 2D Gaussians, with the density of seed points dynamically optimized through adaptive growth and pruning mechanisms. To further improve geometric accuracy, we incorporate monocular depth and normal priors to provide constraints for details and textureless regions respectively. Additionally, multi-view consistency constraints are employed to mitigate artifacts and further enhance reconstruction quality. Extensive experiments on ScanNet and ScanNet++ datasets demonstrate that our method achieves state-of-the-art performance in indoor scene reconstruction.

---

## 10. SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images

- **作者**: Junqiu Yu, Xinlin Ren, Yongchong Gu et al.
- **发布时间**: 2024-12-03
- **arXiv链接**: [arXiv:2412.02140v1](https://arxiv.org/abs/2412.02140v1)
- **英文摘要**: Language-guided robotic grasping is a rapidly advancing field where robots are instructed using human language to grasp specific objects. However, existing methods often depend on dense camera views and struggle to quickly update scenes, limiting their effectiveness in changeable environments.   In contrast, we propose SparseGrasp, a novel open-vocabulary robotic grasping system that operates efficiently with sparse-view RGB images and handles scene updates fastly. Our system builds upon and significantly enhances existing computer vision modules in robotic learning. Specifically, SparseGrasp utilizes DUSt3R to generate a dense point cloud as the initialization for 3D Gaussian Splatting (3DGS), maintaining high fidelity even under sparse supervision. Importantly, SparseGrasp incorporates semantic awareness from recent vision foundation models. To further improve processing efficiency, we repurpose Principal Component Analysis (PCA) to compress features from 2D models. Additionally, we introduce a novel render-and-compare strategy that ensures rapid scene updates, enabling multi-turn grasping in changeable environments.   Experimental results show that SparseGrasp significantly outperforms state-of-the-art methods in terms of both speed and adaptability, providing a robust solution for multi-turn grasping in changeable environment.

---

## 11. HDGS: Textured 2D Gaussian Splatting for Enhanced Scene Rendering

- **作者**: Yunzhou Song, Heguang Lin, Jiahui Lei, Lingjie Liu, Kostas Daniilidis
- **发布时间**: 2024-12-02
- **arXiv链接**: [arXiv:2412.01823v1](https://arxiv.org/abs/2412.01823v1)
- **说明**: Project Page: https://timsong412.github.io/HDGS-ProjPage/
- **英文摘要**: Recent advancements in neural rendering, particularly 2D Gaussian Splatting (2DGS), have shown promising results for jointly reconstructing fine appearance and geometry by leveraging 2D Gaussian surfels. However, current methods face significant challenges when rendering at arbitrary viewpoints, such as anti-aliasing for down-sampled rendering, and texture detail preservation for high-resolution rendering. We proposed a novel method to align the 2D surfels with texture maps and augment it with per-ray depth sorting and fisher-based pruning for rendering consistency and efficiency. With correct order, per-surfel texture maps significantly improve the capabilities to capture fine details. Additionally, to render high-fidelity details in varying viewpoints, we designed a frustum-based sampling method to mitigate the aliasing artifacts. Experimental results on benchmarks and our custom texture-rich dataset demonstrate that our method surpasses existing techniques, particularly in detail preservation and anti-aliasing.

---

## 12. Occam's LGS: An Efficient Approach for Language Gaussian Splatting

- **作者**: Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, Danda Pani Paudel
- **发布时间**: 2024-12-02
- **arXiv链接**: [arXiv:2412.01807v2](https://arxiv.org/abs/2412.01807v2)
- **说明**: Project Page: https://insait-institute.github.io/OccamLGS/
- **英文摘要**: TL;DR: Gaussian Splatting is a widely adopted approach for 3D scene representation, offering efficient, high-quality reconstruction and rendering. A key reason for its success is the simplicity of representing scenes with sets of Gaussians, making it interpretable and adaptable. To enhance understanding beyond visual representation, recent approaches extend Gaussian Splatting with semantic vision-language features, enabling open-set tasks. Typically, these language features are aggregated from multiple 2D views, however, existing methods rely on cumbersome techniques, resulting in high computational costs and longer training times.   In this work, we show that the complicated pipelines for language 3D Gaussian Splatting are simply unnecessary. Instead, we follow a probabilistic formulation of Language Gaussian Splatting and apply Occam's razor to the task at hand, leading to a highly efficient weighted multi-view feature aggregation technique. Doing so offers us state-of-the-art results with a speed-up of two orders of magnitude without any compression, allowing for easy scene manipulation. Project Page: https://insait-institute.github.io/OccamLGS/

---

## 13. 6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting

- **作者**: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, Mathias Franzius, Georgia Chalvatzaki
- **发布时间**: 2024-12-02
- **arXiv链接**: [arXiv:2412.01543v2](https://arxiv.org/abs/2412.01543v2)
- **英文摘要**: Efficient and accurate object pose estimation is an essential component for modern vision systems in many applications such as Augmented Reality, autonomous driving, and robotics. While research in model-based 6D object pose estimation has delivered promising results, model-free methods are hindered by the high computational load in rendering and inferring consistent poses of arbitrary objects in a live RGB-D video stream. To address this issue, we present 6DOPE-GS, a novel method for online 6D object pose estimation \& tracking with a single RGB-D camera by effectively leveraging advances in Gaussian Splatting. Thanks to the fast differentiable rendering capabilities of Gaussian Splatting, 6DOPE-GS can simultaneously optimize for 6D object poses and 3D object reconstruction. To achieve the necessary efficiency and accuracy for live tracking, our method uses incremental 2D Gaussian Splatting with an intelligent dynamic keyframe selection procedure to achieve high spatial object coverage and prevent erroneous pose updates. We also propose an opacity statistic-based pruning mechanism for adaptive Gaussian density control, to ensure training stability and efficiency. We evaluate our method on the HO3D and YCBInEOAT datasets and show that 6DOPE-GS matches the performance of state-of-the-art baselines for model-free simultaneous 6D pose tracking and reconstruction while providing a 5$\times$ speedup. We also demonstrate the method's suitability for live, dynamic object tracking an...

---

## 14. LineGS : 3D Line Segment Representation on 3D Gaussian Splatting

- **作者**: Chenggang Yang, Yuang Shi
- **发布时间**: 2024-11-30
- **arXiv链接**: [arXiv:2412.00477v3](https://arxiv.org/abs/2412.00477v3)
- **英文摘要**: Abstract representations of 3D scenes play a crucial role in computer vision, enabling a wide range of applications such as mapping, localization, surface reconstruction, and even advanced tasks like SLAM and rendering. Among these representations, line segments are widely used because of their ability to succinctly capture the structural features of a scene. However, existing 3D reconstruction methods often face significant challenges. Methods relying on 2D projections suffer from instability caused by errors in multi-view matching and occlusions, while direct 3D approaches are hampered by noise and sparsity in 3D point cloud data. This paper introduces LineGS, a novel method that combines geometry-guided 3D line reconstruction with a 3D Gaussian splatting model to address these challenges and improve representation ability. The method leverages the high-density Gaussian point distributions along the edge of the scene to refine and optimize initial line segments generated from traditional geometric approaches. By aligning these segments with the underlying geometric features of the scene, LineGS achieves a more precise and reliable representation of 3D structures. The results show significant improvements in both geometric accuracy and model compactness compared to baseline methods.

---

## 15. SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors

- **作者**: Rui Xu, Wenyue Chen, Jiepeng Wang et al.
- **发布时间**: 2024-11-28
- **arXiv链接**: [arXiv:2411.18966v1](https://arxiv.org/abs/2411.18966v1)
- **英文摘要**: Gaussian Splattings demonstrate impressive results in multi-view reconstruction based on Gaussian explicit representations. However, the current Gaussian primitives only have a single view-dependent color and an opacity to represent the appearance and geometry of the scene, resulting in a non-compact representation. In this paper, we introduce a new method called SuperGaussians that utilizes spatially varying colors and opacity in a single Gaussian primitive to improve its representation ability. We have implemented bilinear interpolation, movable kernels, and even tiny neural networks as spatially varying functions. Quantitative and qualitative experimental results demonstrate that all three functions outperform the baseline, with the best movable kernels achieving superior novel view synthesis performance on multiple datasets, highlighting the strong potential of spatially varying functions.

---

## 16. HEMGS: A Hybrid Entropy Model for 3D Gaussian Splatting Data Compression

- **作者**: Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu
- **发布时间**: 2024-11-27
- **arXiv链接**: [arXiv:2411.18473v2](https://arxiv.org/abs/2411.18473v2)
- **英文摘要**: In this work, we propose a novel compression framework for 3D Gaussian Splatting (3DGS) data. Building on anchor-based 3DGS methodologies, our approach compresses all attributes within each anchor by introducing a novel Hybrid Entropy Model for 3D Gaussian Splatting (HEMGS) to achieve hybrid lossy-lossless compression. It consists of three main components: a variable-rate predictor, a hyperprior network, and an autoregressive network. First, unlike previous methods that adopt multiple models to achieve multi-rate lossy compression, thereby increasing training overhead, our variable-rate predictor enables variable-rate compression with a single model and a hyperparameter $λ$ by producing a learned Quantization Step feature for versatile lossy compression. Second, to improve lossless compression, the hyperprior network captures both scene-agnostic and scene-specific features to generate a prior feature, while the autoregressive network employs an adaptive context selection algorithm with flexible receptive fields to produce a contextual feature. By integrating these two features, HEMGS can accurately estimate the distribution of the current coding element within each attribute, enabling improved entropy coding and reduced storage. We integrate HEMGS into a compression framework, and experimental results on four benchmarks indicate that HEMGS achieves about a 40% average reduction in size while maintaining rendering quality over baseline methods and achieving state-of-the-art co...

---

## 17. Distractor-free Generalizable 3D Gaussian Splatting

- **作者**: Yanqi Bao, Jing Liao, Jing Huo, Yang Gao
- **发布时间**: 2024-11-26
- **arXiv链接**: [arXiv:2411.17605v2](https://arxiv.org/abs/2411.17605v2)
- **英文摘要**: We present DGGS, a novel framework that addresses the previously unexplored challenge: $\textbf{Distractor-free Generalizable 3D Gaussian Splatting}$ (3DGS). It mitigates 3D inconsistency and training instability caused by distractor data in the cross-scenes generalizable train setting while enabling feedforward inference for 3DGS and distractor masks from references in the unseen scenes. To achieve these objectives, DGGS proposes a scene-agnostic reference-based mask prediction and refinement module during the training phase, effectively eliminating the impact of distractor on training stability. Moreover, we combat distractor-induced artifacts and holes at inference time through a novel two-stage inference framework for references scoring and re-selection, complemented by a distractor pruning mechanism that further removes residual distractor 3DGS-primitive influences. Extensive feedforward experiments on the real and our synthetic data show DGGS's reconstruction capability when dealing with novel distractor scenes. Moreover, our generalizable mask prediction even achieves an accuracy superior to existing scene-specific training methods. Homepage is https://github.com/bbbbby-99/DGGS.

---

## 18. 4D Scaffold Gaussian Splatting with Dynamic-Aware Anchor Growing for Efficient and High-Fidelity Dynamic Scene Reconstruction

- **作者**: Woong Oh Cho, In Cho, Seoha Kim et al.
- **发布时间**: 2024-11-26
- **arXiv链接**: [arXiv:2411.17044v2](https://arxiv.org/abs/2411.17044v2)
- **英文摘要**: Modeling dynamic scenes through 4D Gaussians offers high visual fidelity and fast rendering speeds, but comes with significant storage overhead. Recent approaches mitigate this cost by aggressively reducing the number of Gaussians. However, this inevitably removes Gaussians essential for high-quality rendering, leading to severe degradation in dynamic regions. In this paper, we introduce a novel 4D anchor-based framework that tackles the storage cost in different perspective. Rather than reducing the number of Gaussians, our method retains a sufficient quantity to accurately model dynamic contents, while compressing them into compact, grid-aligned 4D anchor features. Each anchor is processed by an MLP to spawn a set of neural 4D Gaussians, which represent a local spatiotemporal region. We design these neural 4D Gaussians to capture temporal changes with minimal parameters, making them well-suited for the MLP-based spawning. Moreover, we introduce a dynamic-aware anchor growing strategy to effectively assign additional anchors to under-reconstructed dynamic regions. Our method adjusts the accumulated gradients with Gaussians' temporal coverage, significantly improving reconstruction quality in dynamic regions. Experimental results highlight that our method achieves state-of-the-art visual quality in dynamic regions, outperforming all baselines by a large margin with practical storage costs.

---

## 19. SCIGS: 3D Gaussians Splatting from a Snapshot Compressive Image

- **作者**: Zixu Wang, Hao Yang, Yu Guo, Fei Wang
- **发布时间**: 2024-11-19
- **arXiv链接**: [arXiv:2411.12471v2](https://arxiv.org/abs/2411.12471v2)
- **英文摘要**: Snapshot Compressive Imaging (SCI) offers a possibility for capturing information in high-speed dynamic scenes, requiring efficient reconstruction method to recover scene information. Despite promising results, current deep learning-based and NeRF-based reconstruction methods face challenges: 1) deep learning-based reconstruction methods struggle to maintain 3D structural consistency within scenes, and 2) NeRF-based reconstruction methods still face limitations in handling dynamic scenes. To address these challenges, we propose SCIGS, a variant of 3DGS, and develop a primitive-level transformation network that utilizes camera pose stamps and Gaussian primitive coordinates as embedding vectors. This approach resolves the necessity of camera pose in vanilla 3DGS and enhances multi-view 3D structural consistency in dynamic scenes by utilizing transformed primitives. Additionally, a high-frequency filter is introduced to eliminate the artifacts generated during the transformation. The proposed SCIGS is the first to reconstruct a 3D explicit scene from a single compressed image, extending its application to dynamic 3D scenes. Experiments on both static and dynamic scenes demonstrate that SCIGS not only enhances SCI decoding but also outperforms current state-of-the-art methods in reconstructing dynamic 3D scenes from a single compressed image. The code will be made available upon publication.

---

## 20. VeGaS: Video Gaussian Splatting

- **作者**: Weronika Smolak-Dyżewska, Dawid Malarz, Kornel Howil et al.
- **发布时间**: 2024-11-17
- **arXiv链接**: [arXiv:2411.11024v1](https://arxiv.org/abs/2411.11024v1)
- **英文摘要**: Implicit Neural Representations (INRs) employ neural networks to approximate discrete data as continuous functions. In the context of video data, such models can be utilized to transform the coordinates of pixel locations along with frame occurrence times (or indices) into RGB color values. Although INRs facilitate effective compression, they are unsuitable for editing purposes. One potential solution is to use a 3D Gaussian Splatting (3DGS) based model, such as the Video Gaussian Representation (VGR), which is capable of encoding video as a multitude of 3D Gaussians and is applicable for numerous video processing operations, including editing. Nevertheless, in this case, the capacity for modification is constrained to a limited set of basic transformations. To address this issue, we introduce the Video Gaussian Splatting (VeGaS) model, which enables realistic modifications of video data. To construct VeGaS, we propose a novel family of Folded-Gaussian distributions designed to capture nonlinear dynamics in a video stream and model consecutive frames by 2D Gaussians obtained as respective conditional distributions. Our experiments demonstrate that VeGaS outperforms state-of-the-art solutions in frame reconstruction tasks and allows realistic modifications of video data. The code is available at: https://github.com/gmum/VeGaS.

---

## 21. Efficient Density Control for 3D Gaussian Splatting

- **作者**: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu
- **发布时间**: 2024-11-15
- **arXiv链接**: [arXiv:2411.10133v4](https://arxiv.org/abs/2411.10133v4)
- **说明**: Resubmission version in arxiv at arXiv:2508.12313
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated outstanding performance in novel view synthesis, achieving a balance between rendering quality and real-time performance. 3DGS employs Adaptive Density Control (ADC) to increase the number of Gaussians. However, the clone and split operations within ADC are not sufficiently efficient, impacting optimization speed and detail recovery. Additionally, overfitted Gaussians that affect rendering quality may exist, and the original ADC is unable to remove them. To address these issues, we propose two key innovations: (1) Long-Axis Split, which precisely controls the position, shape, and opacity of child Gaussians to minimize the difference before and after splitting. (2) Recovery-Aware Pruning, which leverages differences in recovery speed after resetting opacity to prune overfitted Gaussians, thereby improving generalization performance. Experimental results show that our method significantly enhances rendering quality. Due to resubmission reasons, this version has been abandoned. The improved version is available at https://xiaobin2001.github.io/improved-gs-web .

---

## 22. A Hierarchical Compression Technique for 3D Gaussian Splatting Compression

- **作者**: He Huang, Wenjie Huang, Qi Yang, Yiling Xu, Zhu li
- **发布时间**: 2024-11-11
- **arXiv链接**: [arXiv:2411.06976v2](https://arxiv.org/abs/2411.06976v2)
- **英文摘要**: 3D Gaussian Splatting (GS) demonstrates excellent rendering quality and generation speed in novel view synthesis. However, substantial data size poses challenges for storage and transmission, making 3D GS compression an essential technology. Current 3D GS compression research primarily focuses on developing more compact scene representations, such as converting explicit 3D GS data into implicit forms. In contrast, compression of the GS data itself has hardly been explored. To address this gap, we propose a Hierarchical GS Compression (HGSC) technique. Initially, we prune unimportant Gaussians based on importance scores derived from both global and local significance, effectively reducing redundancy while maintaining visual quality. An Octree structure is used to compress 3D positions. Based on the 3D GS Octree, we implement a hierarchical attribute compression strategy by employing a KD-tree to partition the 3D GS into multiple blocks. We apply farthest point sampling to select anchor primitives within each block and others as non-anchor primitives with varying Levels of Details (LoDs). Anchor primitives serve as reference points for predicting non-anchor primitives across different LoDs to reduce spatial redundancy. For anchor primitives, we use the region adaptive hierarchical transform to achieve near-lossless compression of various attributes. For non-anchor primitives, each is predicted based on the k-nearest anchor primitives. To further minimize prediction errors, the ...

---

## 23. ELMGS: Enhancing memory and computation scaLability through coMpression for 3D Gaussian Splatting

- **作者**: Muhammad Salman Ali, Sung-Ho Bae, Enzo Tartaglione
- **发布时间**: 2024-10-30
- **arXiv链接**: [arXiv:2410.23213v1](https://arxiv.org/abs/2410.23213v1)
- **英文摘要**: 3D models have recently been popularized by the potentiality of end-to-end training offered first by Neural Radiance Fields and most recently by 3D Gaussian Splatting models. The latter has the big advantage of naturally providing fast training convergence and high editability. However, as the research around these is still in its infancy, there is still a gap in the literature regarding the model's scalability. In this work, we propose an approach enabling both memory and computation scalability of such models. More specifically, we propose an iterative pruning strategy that removes redundant information encoded in the model. We also enhance compressibility for the model by including in the optimization strategy a differentiable quantization and entropy coding estimator. Our results on popular benchmarks showcase the effectiveness of the proposed approach and open the road to the broad deployability of such a solution even on resource-constrained devices.

---

## 24. PixelGaussian: Generalizable 3D Gaussian Reconstruction from Arbitrary Views

- **作者**: Xin Fei, Wenzhao Zheng, Yueqi Duan et al.
- **发布时间**: 2024-10-24
- **arXiv链接**: [arXiv:2410.18979v1](https://arxiv.org/abs/2410.18979v1)
- **说明**: Code is available at: https://github.com/Barrybarry-Smith/PixelGaussian
- **英文摘要**: We propose PixelGaussian, an efficient feed-forward framework for learning generalizable 3D Gaussian reconstruction from arbitrary views. Most existing methods rely on uniform pixel-wise Gaussian representations, which learn a fixed number of 3D Gaussians for each view and cannot generalize well to more input views. Differently, our PixelGaussian dynamically adapts both the Gaussian distribution and quantity based on geometric complexity, leading to more efficient representations and significant improvements in reconstruction quality. Specifically, we introduce a Cascade Gaussian Adapter to adjust Gaussian distribution according to local geometry complexity identified by a keypoint scorer. CGA leverages deformable attention in context-aware hypernetworks to guide Gaussian pruning and splitting, ensuring accurate representation in complex regions while reducing redundancy. Furthermore, we design a transformer-based Iterative Gaussian Refiner module that refines Gaussian representations through direct image-Gaussian interactions. Our PixelGaussian can effectively reduce Gaussian redundancy as input views increase. We conduct extensive experiments on the large-scale ACID and RealEstate10K datasets, where our method achieves state-of-the-art performance with good generalization to various numbers of views. Code: https://github.com/Barrybarry-Smith/PixelGaussian.

---

## 25. Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization

- **作者**: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth
- **发布时间**: 2024-10-22
- **arXiv链接**: [arXiv:2410.16978v1](https://arxiv.org/abs/2410.16978v1)
- **英文摘要**: In medical image visualization, path tracing of volumetric medical data like CT scans produces lifelike three-dimensional visualizations. Immersive VR displays can further enhance the understanding of complex anatomies. Going beyond the diagnostic quality of traditional 2D slices, they enable interactive 3D evaluation of anatomies, supporting medical education and planning. Rendering high-quality visualizations in real-time, however, is computationally intensive and impractical for compute-constrained devices like mobile headsets.   We propose a novel approach utilizing GS to create an efficient but static intermediate representation of CT scans. We introduce a layered GS representation, incrementally including different anatomical structures while minimizing overlap and extending the GS training to remove inactive Gaussians. We further compress the created model with clustering across layers.   Our approach achieves interactive frame rates while preserving anatomical structures, with quality adjustable to the target hardware. Compared to standard GS, our representation retains some of the explorative qualities initially enabled by immersive path tracing. Selective activation and clipping of layers are possible at rendering time, adding a degree of interactivity to otherwise static GS models. This could enable scenarios where high computational demands would otherwise prohibit using path-traced medical volumes.

---

## 26. Long-LRM: Long-sequence Large Reconstruction Model for Wide-coverage Gaussian Splats

- **作者**: Chen Ziwen, Hao Tan, Kai Zhang et al.
- **发布时间**: 2024-10-16
- **arXiv链接**: [arXiv:2410.12781v2](https://arxiv.org/abs/2410.12781v2)
- **英文摘要**: We propose Long-LRM, a feed-forward 3D Gaussian reconstruction model for instant, high-resolution, 360° wide-coverage, scene-level reconstruction. Specifically, it takes in 32 input images at a resolution of 960x540 and produces the Gaussian reconstruction in just 1 second on a single A100 GPU. To handle the long sequence of 250K tokens brought by the large input size, Long-LRM features a mixture of the recent Mamba2 blocks and the classical transformer blocks, enhanced by a light-weight token merging module and Gaussian pruning steps that balance between quality and efficiency. We evaluate Long-LRM on the large-scale DL3DV benchmark and Tanks&Temples, demonstrating reconstruction quality comparable to the optimization-based methods while achieving an 800x speedup w.r.t. the optimization-based approaches and an input size at least 60x larger than the previous feed-forward approaches. We conduct extensive ablation studies on our model design choices for both rendering quality and computation efficiency. We also explore Long-LRM's compatibility with other Gaussian variants such as 2D GS, which enhances Long-LRM's ability in geometry reconstruction. Project page: https://arthurhero.github.io/projects/llrm

---

## 27. GSORB-SLAM: Gaussian Splatting SLAM benefits from ORB features and Transmittance information

- **作者**: Wancai Zheng, Xinyi Yu, Jintao Rong et al.
- **发布时间**: 2024-10-15
- **arXiv链接**: [arXiv:2410.11356v3](https://arxiv.org/abs/2410.11356v3)
- **英文摘要**: The emergence of 3D Gaussian Splatting (3DGS) has recently ignited a renewed wave of research in dense visual SLAM. However, existing approaches encounter challenges, including sensitivity to artifacts and noise, suboptimal selection of training viewpoints, and the absence of global optimization. In this paper, we propose GSORB-SLAM, a dense SLAM framework that integrates 3DGS with ORB features through a tightly coupled optimization pipeline. To mitigate the effects of noise and artifacts, we propose a novel geometric representation and optimization method for tracking, which significantly enhances localization accuracy and robustness. For high-fidelity mapping, we develop an adaptive Gaussian expansion and regularization method that facilitates compact yet expressive scene modeling while suppressing redundant primitives. Furthermore, we design a hybrid graph-based viewpoint selection mechanism that effectively reduces overfitting and accelerates convergence. Extensive evaluations across various datasets demonstrate that our system achieves state-of-the-art performance in both tracking precision-improving RMSE by 16.2% compared to ORB-SLAM2 baselines-and reconstruction quality-improving PSNR by 3.93 dB compared to 3DGS-SLAM baselines. The project: https://aczheng-cai.github.io/gsorb-slam.github.io/

---

## 28. SurgicalGS: Dynamic 3D Gaussian Splatting for Accurate Robotic-Assisted Surgical Scene Reconstruction

- **作者**: Jialei Chen, Xin Zhang, Mobarakol Islam et al.
- **发布时间**: 2024-10-11
- **arXiv链接**: [arXiv:2410.09292v1](https://arxiv.org/abs/2410.09292v1)
- **说明**: 7 pages
- **英文摘要**: Accurate 3D reconstruction of dynamic surgical scenes from endoscopic video is essential for robotic-assisted surgery. While recent 3D Gaussian Splatting methods have shown promise in achieving high-quality reconstructions with fast rendering speeds, their use of inverse depth loss functions compresses depth variations. This can lead to a loss of fine geometric details, limiting their ability to capture precise 3D geometry and effectiveness in intraoperative application. To address these challenges, we present SurgicalGS, a dynamic 3D Gaussian Splatting framework specifically designed for surgical scene reconstruction with improved geometric accuracy. Our approach first initialises a Gaussian point cloud using depth priors, employing binary motion masks to identify pixels with significant depth variations and fusing point clouds from depth maps across frames for initialisation. We use the Flexible Deformation Model to represent dynamic scene and introduce a normalised depth regularisation loss along with an unsupervised depth smoothness constraint to ensure more accurate geometric reconstruction. Extensive experiments on two real surgical datasets demonstrate that SurgicalGS achieves state-of-the-art reconstruction quality, especially in terms of accurate geometry, advancing the usability of 3D Gaussian Splatting in robotic-assisted surgery.

---

## 29. Fast Feedforward 3D Gaussian Splatting Compression

- **作者**: Yihang Chen, Qianyi Wu, Mengyao Li et al.
- **发布时间**: 2024-10-10
- **arXiv链接**: [arXiv:2410.08017v3](https://arxiv.org/abs/2410.08017v3)
- **说明**: Project Page: https://yihangchen-ee.github.io/project_fcgs/ Code: https://github.com/yihangchen-ee/fcgs/
- **英文摘要**: With 3D Gaussian Splatting (3DGS) advancing real-time and high-fidelity rendering for novel view synthesis, storage requirements pose challenges for their widespread adoption. Although various compression techniques have been proposed, previous art suffers from a common limitation: for any existing 3DGS, per-scene optimization is needed to achieve compression, making the compression sluggish and slow. To address this issue, we introduce Fast Compression of 3D Gaussian Splatting (FCGS), an optimization-free model that can compress 3DGS representations rapidly in a single feed-forward pass, which significantly reduces compression time from minutes to seconds. To enhance compression efficiency, we propose a multi-path entropy module that assigns Gaussian attributes to different entropy constraint paths for balance between size and fidelity. We also carefully design both inter- and intra-Gaussian context models to remove redundancies among the unstructured Gaussian blobs. Overall, FCGS achieves a compression ratio of over 20X while maintaining fidelity, surpassing most per-scene SOTA optimization-based methods. Our code is available at: https://github.com/YihangChen-ee/FCGS.

---

## 30. MiraGe: Editable 2D Images using Gaussian Splatting

- **作者**: Joanna Waczyńska, Tomasz Szczepanik, Piotr Borycki et al.
- **发布时间**: 2024-10-02
- **arXiv链接**: [arXiv:2410.01521v2](https://arxiv.org/abs/2410.01521v2)
- **英文摘要**: Implicit Neural Representations (INRs) approximate discrete data through continuous functions and are commonly used for encoding 2D images. Traditional image-based INRs employ neural networks to map pixel coordinates to RGB values, capturing shapes, colors, and textures within the network's weights. Recently, GaussianImage has been proposed as an alternative, using Gaussian functions instead of neural networks to achieve comparable quality and compression. Such a solution obtains a quality and compression ratio similar to classical INR models but does not allow image modification. In contrast, our work introduces a novel method, MiraGe, which uses mirror reflections to perceive 2D images in 3D space and employs flat-controlled Gaussians for precise 2D image editing. Our approach improves the rendering quality and allows realistic image modifications, including human-inspired perception of photos in the 3D world. Thanks to modeling images in 3D space, we obtain the illusion of 3D-based modification in 2D images. We also show that our Gaussian representation can be easily combined with a physics engine to produce physics-based modification of 2D images. Consequently, MiraGe allows for better quality than the standard approach and natural modification of 2D images

---

## 31. GSplatLoc: Grounding Keypoint Descriptors into 3D Gaussian Splatting for Improved Visual Localization

- **作者**: Gennady Sidorov, Malik Mohrat, Denis Gridusov, Ruslan Rakhimov, Sergey Kolyubin
- **发布时间**: 2024-09-24
- **arXiv链接**: [arXiv:2409.16502v3](https://arxiv.org/abs/2409.16502v3)
- **说明**: Project website at https://gsplatloc.github.io/
- **英文摘要**: Although various visual localization approaches exist, such as scene coordinate regression and camera pose regression, these methods often struggle with optimization complexity or limited accuracy. To address these challenges, we explore the use of novel view synthesis techniques, particularly 3D Gaussian Splatting (3DGS), which enables the compact encoding of both 3D geometry and scene appearance. We propose a two-stage procedure that integrates dense and robust keypoint descriptors from the lightweight XFeat feature extractor into 3DGS, enhancing performance in both indoor and outdoor environments. The coarse pose estimates are directly obtained via 2D-3D correspondences between the 3DGS representation and query image descriptors. In the second stage, the initial pose estimate is refined by minimizing the rendering-based photometric warp loss. Benchmarking on widely used indoor and outdoor datasets demonstrates improvements over recent neural rendering-based localization methods, such as NeRFMatch and PNeRFLoc.

---

## 32. 3D-LMVIC: Learning-based Multi-View Image Coding with 3D Gaussian Geometric Priors

- **作者**: Yujun Huang, Bin Chen, Niu Lian, Baoyi An, Shu-Tao Xia
- **发布时间**: 2024-09-06
- **arXiv链接**: [arXiv:2409.04013v2](https://arxiv.org/abs/2409.04013v2)
- **说明**: 17 pages, 10 figures, conference
- **英文摘要**: Existing multi-view image compression methods often rely on 2D projection-based similarities between views to estimate disparities. While effective for small disparities, such as those in stereo images, these methods struggle with the more complex disparities encountered in wide-baseline multi-camera systems, commonly found in virtual reality and autonomous driving applications. To address this limitation, we propose 3D-LMVIC, a novel learning-based multi-view image compression framework that leverages 3D Gaussian Splatting to derive geometric priors for accurate disparity estimation. Furthermore, we introduce a depth map compression model to minimize geometric redundancy across views, along with a multi-view sequence ordering strategy based on a defined distance measure between views to enhance correlations between adjacent views. Experimental results demonstrate that 3D-LMVIC achieves superior performance compared to both traditional and learning-based methods. Additionally, it significantly improves disparity estimation accuracy over existing two-view approaches.

---

## 33. PRoGS: Progressive Rendering of Gaussian Splats

- **作者**: Brent Zoomers, Maarten Wijnants, Ivan Molenaers et al.
- **发布时间**: 2024-09-03
- **arXiv链接**: [arXiv:2409.01761v1](https://arxiv.org/abs/2409.01761v1)
- **英文摘要**: Over the past year, 3D Gaussian Splatting (3DGS) has received significant attention for its ability to represent 3D scenes in a perceptually accurate manner. However, it can require a substantial amount of storage since each splat's individual data must be stored. While compression techniques offer a potential solution by reducing the memory footprint, they still necessitate retrieving the entire scene before any part of it can be rendered. In this work, we introduce a novel approach for progressively rendering such scenes, aiming to display visible content that closely approximates the final scene as early as possible without loading the entire scene into memory. This approach benefits both on-device rendering applications limited by memory constraints and streaming applications where minimal bandwidth usage is preferred. To achieve this, we approximate the contribution of each Gaussian to the final scene and construct an order of prioritization on their inclusion in the rendering process. Additionally, we demonstrate that our approach can be combined with existing compression methods to progressively render (and stream) 3DGS scenes, optimizing bandwidth usage by focusing on the most important splats within a scene. Overall, our work establishes a foundation for making remotely hosted 3DGS content more quickly accessible to end-users in over-the-top consumption scenarios, with our results showing significant improvements in quality across all metrics compared to existing met...

---

## 34. OG-Mapping: Octree-based Structured 3D Gaussians for Online Dense Mapping

- **作者**: Meng Wang, Junyi Wang, Changqun Xia, Chen Wang, Yue Qi
- **发布时间**: 2024-08-30
- **arXiv链接**: [arXiv:2408.17223v1](https://arxiv.org/abs/2408.17223v1)
- **英文摘要**: 3D Gaussian splatting (3DGS) has recently demonstrated promising advancements in RGB-D online dense mapping. Nevertheless, existing methods excessively rely on per-pixel depth cues to perform map densification, which leads to significant redundancy and increased sensitivity to depth noise. Additionally, explicitly storing 3D Gaussian parameters of room-scale scene poses a significant storage challenge. In this paper, we introduce OG-Mapping, which leverages the robust scene structural representation capability of sparse octrees, combined with structured 3D Gaussian representations, to achieve efficient and robust online dense mapping. Moreover, OG-Mapping employs an anchor-based progressive map refinement strategy to recover the scene structures at multiple levels of detail. Instead of maintaining a small number of active keyframes with a fixed keyframe window as previous approaches do, a dynamic keyframe window is employed to allow OG-Mapping to better tackle false local minima and forgetting issues. Experimental results demonstrate that OG-Mapping delivers more robust and superior realism mapping results than existing Gaussian-based RGB-D online mapping methods with a compact model, and no additional post-processing is required.

---

## 35. H3D-DGS: Exploring Heterogeneous 3D Motion Representation for Deformable 3D Gaussian Splatting

- **作者**: Bing He, Yunuo Chen, Guo Lu et al.
- **发布时间**: 2024-08-23
- **arXiv链接**: [arXiv:2408.13036v3](https://arxiv.org/abs/2408.13036v3)
- **英文摘要**: Dynamic scene reconstruction poses a persistent challenge in 3D vision. Deformable 3D Gaussian Splatting has emerged as an effective method for this task, offering real-time rendering and high visual fidelity. This approach decomposes a dynamic scene into a static representation in a canonical space and time-varying scene motion. Scene motion is defined as the collective movement of all Gaussian points, and for compactness, existing approaches commonly adopt implicit neural fields or sparse control points. However, these methods predominantly rely on gradient-based optimization for all motion information. Due to the high degree of freedom, they struggle to converge on real-world datasets exhibiting complex motion. To preserve the compactness of motion representation and address convergence challenges, this paper proposes heterogeneous 3D control points, termed \textbf{H3D control points}, whose attributes are obtained using a hybrid strategy combining optical flow back-projection and gradient-based methods. This design decouples directly observable motion components from those that are geometrically occluded. Specifically, components of 3D motion that project onto the image plane are directly acquired via optical flow back projection, while unobservable portions are refined through gradient-based optimization. Experiments on the Neu3DV and CMU-Panoptic datasets demonstrate that our method achieves superior performance over state-of-the-art deformable 3D Gaussian splatting tec...

---

## 36. FLoD: Integrating Flexible Level of Detail into 3D Gaussian Splatting for Customizable Rendering

- **作者**: Yunji Seo, Young Sun Choi, Hyun Seung Son, Youngjung Uh
- **发布时间**: 2024-08-23
- **arXiv链接**: [arXiv:2408.12894v2](https://arxiv.org/abs/2408.12894v2)
- **说明**: Project page: https://3dgs-flod.github.io/flod/
- **英文摘要**: 3D Gaussian Splatting (3DGS) and its subsequent works are restricted to specific hardware setups, either on only low-cost or on only high-end configurations. Approaches aimed at reducing 3DGS memory usage enable rendering on low-cost GPU but compromise rendering quality, which fails to leverage the hardware capabilities in the case of higher-end GPU. Conversely, methods that enhance rendering quality require high-end GPU with large VRAM, making such methods impractical for lower-end devices with limited memory capacity. Consequently, 3DGS-based works generally assume a single hardware setup and lack the flexibility to adapt to varying hardware constraints.   To overcome this limitation, we propose Flexible Level of Detail (FLoD) for 3DGS. FLoD constructs a multi-level 3DGS representation through level-specific 3D scale constraints, where each level independently reconstructs the entire scene with varying detail and GPU memory usage. A level-by-level training strategy is introduced to ensure structural consistency across levels. Furthermore, the multi-level structure of FLoD allows selective rendering of image regions at different detail levels, providing additional memory-efficient rendering options. To our knowledge, among prior works which incorporate the concept of Level of Detail (LoD) with 3DGS, FLoD is the first to follow the core principle of LoD by offering adjustable options for a broad range of GPU settings.   Experiments demonstrate that FLoD provides various rende...

---

## 37. GSFusion: Online RGB-D Mapping Where Gaussian Splatting Meets TSDF Fusion

- **作者**: Jiaxin Wei, Stefan Leutenegger
- **发布时间**: 2024-08-22
- **arXiv链接**: [arXiv:2408.12677v3](https://arxiv.org/abs/2408.12677v3)
- **英文摘要**: Traditional volumetric fusion algorithms preserve the spatial structure of 3D scenes, which is beneficial for many tasks in computer vision and robotics. However, they often lack realism in terms of visualization. Emerging 3D Gaussian splatting bridges this gap, but existing Gaussian-based reconstruction methods often suffer from artifacts and inconsistencies with the underlying 3D structure, and struggle with real-time optimization, unable to provide users with immediate feedback in high quality. One of the bottlenecks arises from the massive amount of Gaussian parameters that need to be updated during optimization. Instead of using 3D Gaussian as a standalone map representation, we incorporate it into a volumetric mapping system to take advantage of geometric information and propose to use a quadtree data structure on images to drastically reduce the number of splats initialized. In this way, we simultaneously generate a compact 3D Gaussian map with fewer artifacts and a volumetric map on the fly. Our method, GSFusion, significantly enhances computational efficiency without sacrificing rendering quality, as demonstrated on both synthetic and real datasets. Code will be available at https://github.com/goldoak/GSFusion.

---

## 38. Implicit Gaussian Splatting with Efficient Multi-Level Tri-Plane Representation

- **作者**: Minye Wu, Tinne Tuytelaars
- **发布时间**: 2024-08-19
- **arXiv链接**: [arXiv:2408.10041v2](https://arxiv.org/abs/2408.10041v2)
- **说明**: Please note that the authors discovered configuration errors in the comparisons within the experiment section, resulting in unreliable quantitative results. We advise referencing the results in this paper with caution
- **英文摘要**: Recent advancements in photo-realistic novel view synthesis have been significantly driven by Gaussian Splatting (3DGS). Nevertheless, the explicit nature of 3DGS data entails considerable storage requirements, highlighting a pressing need for more efficient data representations. To address this, we present Implicit Gaussian Splatting (IGS), an innovative hybrid model that integrates explicit point clouds with implicit feature embeddings through a multi-level tri-plane architecture. This architecture features 2D feature grids at various resolutions across different levels, facilitating continuous spatial domain representation and enhancing spatial correlations among Gaussian primitives. Building upon this foundation, we introduce a level-based progressive training scheme, which incorporates explicit spatial regularization. This method capitalizes on spatial correlations to enhance both the rendering quality and the compactness of the IGS representation. Furthermore, we propose a novel compression pipeline tailored for both point clouds and 2D feature grids, considering the entropy variations across different levels. Extensive experimental evaluations demonstrate that our algorithm can deliver high-quality rendering using only a few MBs, effectively balancing storage efficiency and rendering fidelity, and yielding results that are competitive with the state-of-the-art.

---

## 39. Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields

- **作者**: Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park
- **发布时间**: 2024-08-07
- **arXiv链接**: [arXiv:2408.03822v1](https://arxiv.org/abs/2408.03822v1)
- **说明**: Project page: https://maincold2.github.io/c3dgs/
- **英文摘要**: 3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussian-based representation and introduces an approximated volumetric rendering, achieving very fast rendering speed and promising image quality. Furthermore, subsequent studies have successfully extended 3DGS to dynamic 3D scenes, demonstrating its wide range of applications. However, a significant drawback arises as 3DGS and its following methods entail a substantial number of Gaussians to maintain the high fidelity of the rendered images, which requires a large amount of memory and storage. To address this critical issue, we place a specific emphasis on two key objectives: reducing the number of Gaussian points without sacrificing performance and compressing the Gaussian attributes, such as view-dependent color and covariance. To this end, we propose a learnable mask strategy that significantly reduces the number of Gaussians while preserving high performance. In addition, we propose a compact but effective representation of view-dependent color by employing a grid-based neural field rather than relying on spherical harmonics. Finally, we learn codebooks to compactly represent the geometric and temporal attributes by residual vector quantization. With model compression techniques such as quantization and entropy coding, we consistently show over 25x reduced storage and enhanced rendering speed compared to 3DGS for static scenes, while maintaining the quality of the scen...

---

## 40. A Benchmark for Gaussian Splatting Compression and Quality Assessment Study

- **作者**: Qi Yang, Kaifa Yang, Yuke Xing, Yiling Xu, Zhu Li
- **发布时间**: 2024-07-19
- **arXiv链接**: [arXiv:2407.14197v1](https://arxiv.org/abs/2407.14197v1)
- **英文摘要**: To fill the gap of traditional GS compression method, in this paper, we first propose a simple and effective GS data compression anchor called Graph-based GS Compression (GGSC). GGSC is inspired by graph signal processing theory and uses two branches to compress the primitive center and attributes. We split the whole GS sample via KDTree and clip the high-frequency components after the graph Fourier transform. Followed by quantization, G-PCC and adaptive arithmetic coding are used to compress the primitive center and attribute residual matrix to generate the bitrate file. GGSS is the first work to explore traditional GS compression, with advantages that can reveal the GS distortion characteristics corresponding to typical compression operation, such as high-frequency clipping and quantization. Second, based on GGSC, we create a GS Quality Assessment dataset (GSQA) with 120 samples. A subjective experiment is conducted in a laboratory environment to collect subjective scores after rendering GS into Processed Video Sequences (PVS). We analyze the characteristics of different GS distortions based on Mean Opinion Scores (MOS), demonstrating the sensitivity of different attributes distortion to visual quality. The GGSC code and the dataset, including GS samples, MOS, and PVS, are made publicly available at https://github.com/Qi-Yangsjtu/GGSC.

---

## 41. MVG-Splatting: Multi-View Guided Gaussian Splatting with Adaptive Quantile-Based Geometric Consistency Densification

- **作者**: Zhuoxiao Li, Shanliang Yao, Yijie Chu et al.
- **发布时间**: 2024-07-16
- **arXiv链接**: [arXiv:2407.11840v1](https://arxiv.org/abs/2407.11840v1)
- **说明**: https://mvgsplatting.github.io
- **英文摘要**: In the rapidly evolving field of 3D reconstruction, 3D Gaussian Splatting (3DGS) and 2D Gaussian Splatting (2DGS) represent significant advancements. Although 2DGS compresses 3D Gaussian primitives into 2D Gaussian surfels to effectively enhance mesh extraction quality, this compression can potentially lead to a decrease in rendering quality. Additionally, unreliable densification processes and the calculation of depth through the accumulation of opacity can compromise the detail of mesh extraction. To address this issue, we introduce MVG-Splatting, a solution guided by Multi-View considerations. Specifically, we integrate an optimized method for calculating normals, which, combined with image gradients, helps rectify inconsistencies in the original depth computations. Additionally, utilizing projection strategies akin to those in Multi-View Stereo (MVS), we propose an adaptive quantile-based method that dynamically determines the level of additional densification guided by depth maps, from coarse to fine detail. Experimental evidence demonstrates that our method not only resolves the issues of rendering quality degradation caused by depth discrepancies but also facilitates direct mesh extraction from dense Gaussian point clouds using the Marching Cubes algorithm. This approach significantly enhances the overall fidelity and accuracy of the 3D reconstruction process, ensuring that both the geometric details and visual quality.

---

## 42. Lightweight Predictive 3D Gaussian Splats

- **作者**: Junli Cao, Vidit Goel, Chaoyang Wang et al.
- **发布时间**: 2024-06-27
- **arXiv链接**: [arXiv:2406.19434v1](https://arxiv.org/abs/2406.19434v1)
- **说明**: Project Page: https://plumpuddings.github.io/LPGS//
- **英文摘要**: Recent approaches representing 3D objects and scenes using Gaussian splats show increased rendering speed across a variety of platforms and devices. While rendering such representations is indeed extremely efficient, storing and transmitting them is often prohibitively expensive. To represent large-scale scenes, one often needs to store millions of 3D Gaussians, occupying gigabytes of disk space. This poses a very practical limitation, prohibiting widespread adoption.Several solutions have been proposed to strike a balance between disk size and rendering quality, noticeably reducing the visual quality. In this work, we propose a new representation that dramatically reduces the hard drive footprint while featuring similar or improved quality when compared to the standard 3D Gaussian splats. When compared to other compact solutions, ours offers higher quality renderings with significantly reduced storage, being able to efficiently run on a mobile device in real-time. Our key observation is that nearby points in the scene can share similar representations. Hence, only a small ratio of 3D points needs to be stored. We introduce an approach to identify such points which are called parent points. The discarded points called children points along with attributes can be efficiently predicted by tiny MLPs.

---

## 43. Reducing the Memory Footprint of 3D Gaussian Splatting

- **作者**: Panagiotis Papantonakis, Georgios Kopanas, Bernhard Kerbl, Alexandre Lanvin, George Drettakis
- **发布时间**: 2024-06-24
- **arXiv链接**: [arXiv:2406.17074v1](https://arxiv.org/abs/2406.17074v1)
- **说明**: Project website: https://repo-sam.inria.fr/fungraph/reduced_3dgs/
- **英文摘要**: 3D Gaussian splatting provides excellent visual quality for novel view synthesis, with fast training and real-time rendering; unfortunately, the memory requirements of this method for storing and transmission are unreasonably high. We first analyze the reasons for this, identifying three main areas where storage can be reduced: the number of 3D Gaussian primitives used to represent a scene, the number of coefficients for the spherical harmonics used to represent directional radiance, and the precision required to store Gaussian primitive attributes. We present a solution to each of these issues. First, we propose an efficient, resolution-aware primitive pruning approach, reducing the primitive count by half. Second, we introduce an adaptive adjustment method to choose the number of coefficients used to represent directional radiance for each Gaussian primitive, and finally a codebook-based quantization method, together with a half-float representation for further memory reduction. Taken together, these three components result in a 27 reduction in overall size on disk on the standard datasets we tested, along with a 1.7 speedup in rendering speed. We demonstrate our method on standard datasets and show how our solution results in significantly reduced download times when using the method on a mobile device.

---

## 44. ClotheDreamer: Text-Guided Garment Generation with 3D Gaussians

- **作者**: Yufei Liu, Junshu Tang, Chu Zheng et al.
- **发布时间**: 2024-06-24
- **arXiv链接**: [arXiv:2406.16815v1](https://arxiv.org/abs/2406.16815v1)
- **说明**: Project Page: https://ggxxii.github.io/clothedreamer
- **英文摘要**: High-fidelity 3D garment synthesis from text is desirable yet challenging for digital avatar creation. Recent diffusion-based approaches via Score Distillation Sampling (SDS) have enabled new possibilities but either intricately couple with human body or struggle to reuse. We introduce ClotheDreamer, a 3D Gaussian-based method for generating wearable, production-ready 3D garment assets from text prompts. We propose a novel representation Disentangled Clothe Gaussian Splatting (DCGS) to enable separate optimization. DCGS represents clothed avatar as one Gaussian model but freezes body Gaussian splats. To enhance quality and completeness, we incorporate bidirectional SDS to supervise clothed avatar and garment RGBD renderings respectively with pose conditions and propose a new pruning strategy for loose clothing. Our approach can also support custom clothing templates as input. Benefiting from our design, the synthetic 3D garment can be easily applied to virtual try-on and support physically accurate animation. Extensive experiments showcase our method's superior and competitive performance. Our project page is at https://ggxxii.github.io/clothedreamer.

---

## 45. Sampling 3D Gaussian Scenes in Seconds with Latent Diffusion Models

- **作者**: Paul Henderson, Melonie de Almeida, Daniela Ivanova, Titas Anciukevičius
- **发布时间**: 2024-06-18
- **arXiv链接**: [arXiv:2406.13099v1](https://arxiv.org/abs/2406.13099v1)
- **英文摘要**: We present a latent diffusion model over 3D scenes, that can be trained using only 2D image data. To achieve this, we first design an autoencoder that maps multi-view images to 3D Gaussian splats, and simultaneously builds a compressed latent representation of these splats. Then, we train a multi-view diffusion model over the latent space to learn an efficient generative model. This pipeline does not require object masks nor depths, and is suitable for complex scenes with arbitrary camera positions. We conduct careful experiments on two large-scale datasets of complex real-world scenes -- MVImgNet and RealEstate10K. We show that our approach enables generating 3D scenes in as little as 0.2 seconds, either from scratch, from a single input view, or from sparse input views. It produces diverse and high-quality results while running an order of magnitude faster than non-latent diffusion models and earlier NeRF-based generative models

---

## 46. A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets

- **作者**: Bernhard Kerbl, Andréas Meuleman, Georgios Kopanas et al.
- **发布时间**: 2024-06-17
- **arXiv链接**: [arXiv:2406.12080v1](https://arxiv.org/abs/2406.12080v1)
- **说明**: Project Page: https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/
- **英文摘要**: Novel view synthesis has seen major advances in recent years, with 3D Gaussian splatting offering an excellent level of visual quality, fast training and real-time rendering. However, the resources needed for training and rendering inevitably limit the size of the captured scenes that can be represented with good visual quality. We introduce a hierarchy of 3D Gaussians that preserves visual quality for very large scenes, while offering an efficient Level-of-Detail (LOD) solution for efficient rendering of distant content with effective level selection and smooth transitions between levels.We introduce a divide-and-conquer approach that allows us to train very large scenes in independent chunks. We consolidate the chunks into a hierarchy that can be optimized to further improve visual quality of Gaussians merged into intermediate nodes. Very large captures typically have sparse coverage of the scene, presenting many challenges to the original 3D Gaussian splatting training method; we adapt and regularize training to account for these issues. We present a complete solution, that enables real-time rendering of very large scenes and can adapt to available resources thanks to our LOD method. We show results for captured scenes with up to tens of thousands of images with a simple and affordable rig, covering trajectories of up to several kilometers and lasting up to one hour. Project Page: https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/

---

## 47. 3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods

- **作者**: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li et al.
- **发布时间**: 2024-06-17
- **arXiv链接**: [arXiv:2407.09510v5](https://arxiv.org/abs/2407.09510v5)
- **说明**: 3D Gaussian Splatting compression survey; 3DGS compression; updated discussion; new approaches added; new illustrations
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a cutting-edge technique for real-time radiance field rendering, offering state-of-the-art performance in terms of both quality and speed. 3DGS models a scene as a collection of three-dimensional Gaussians, with additional attributes optimized to conform to the scene's geometric and visual properties. Despite its advantages in rendering speed and image fidelity, 3DGS is limited by its significant storage and memory demands. These high demands make 3DGS impractical for mobile devices or headsets, reducing its applicability in important areas of computer graphics. To address these challenges and advance the practicality of 3DGS, this survey provides a comprehensive and detailed examination of compression and compaction techniques developed to make 3DGS more efficient. We classify existing methods into two categories: compression, which focuses on reducing file size, and compaction, which aims to minimize the number of Gaussians. Both methods aim to maintain or improve quality, each by minimizing its respective attribute: file size for compression and Gaussian count for compaction. We introduce the basic mathematical concepts underlying the analyzed methods, as well as key implementation details and design choices. Our report thoroughly discusses similarities and differences among the methods, as well as their respective advantages and disadvantages. We establish a consistent framework for comparing the surveyed methods based on key pe...

---

## 48. GaussianForest: Hierarchical-Hybrid 3D Gaussian Splatting for Compressed Scene Modeling

- **作者**: Fengyi Zhang, Yadan Luo, Tianjun Zhang, Lin Zhang, Zi Huang
- **发布时间**: 2024-06-13
- **arXiv链接**: [arXiv:2406.08759v2](https://arxiv.org/abs/2406.08759v2)
- **英文摘要**: The field of novel-view synthesis has recently witnessed the emergence of 3D Gaussian Splatting, which represents scenes in a point-based manner and renders through rasterization. This methodology, in contrast to Radiance Fields that rely on ray tracing, demonstrates superior rendering quality and speed. However, the explicit and unstructured nature of 3D Gaussians poses a significant storage challenge, impeding its broader application. To address this challenge, we introduce the Gaussian-Forest modeling framework, which hierarchically represents a scene as a forest of hybrid 3D Gaussians. Each hybrid Gaussian retains its unique explicit attributes while sharing implicit ones with its sibling Gaussians, thus optimizing parameterization with significantly fewer variables. Moreover, adaptive growth and pruning strategies are designed, ensuring detailed representation in complex regions and a notable reduction in the number of required Gaussians. Extensive experiments demonstrate that Gaussian-Forest not only maintains comparable speed and quality but also achieves a compression rate surpassing 10 times, marking a significant advancement in efficient scene modeling. Codes will be available at https://github.com/Xian-Bei/GaussianForest.

---

## 49. ContextGS: Compact 3D Gaussian Splatting with Anchor Level Context Model

- **作者**: Yufei Wang, Zhihao Li, Lanqing Guo et al.
- **发布时间**: 2024-05-31
- **arXiv链接**: [arXiv:2405.20721v1](https://arxiv.org/abs/2405.20721v1)
- **英文摘要**: Recently, 3D Gaussian Splatting (3DGS) has become a promising framework for novel view synthesis, offering fast rendering speeds and high fidelity. However, the large number of Gaussians and their associated attributes require effective compression techniques. Existing methods primarily compress neural Gaussians individually and independently, i.e., coding all the neural Gaussians at the same time, with little design for their interactions and spatial dependence. Inspired by the effectiveness of the context model in image compression, we propose the first autoregressive model at the anchor level for 3DGS compression in this work. We divide anchors into different levels and the anchors that are not coded yet can be predicted based on the already coded ones in all the coarser levels, leading to more accurate modeling and higher coding efficiency. To further improve the efficiency of entropy coding, e.g., to code the coarsest level with no already coded anchors, we propose to introduce a low-dimensional quantized feature as the hyperprior for each anchor, which can be effectively compressed. Our work pioneers the context model in the anchor level for 3DGS representation, yielding an impressive size reduction of over 100 times compared to vanilla 3DGS and 15 times compared to the most recent state-of-the-art work Scaffold-GS, while achieving comparable or even higher rendering quality.

---

## 50. GaussianRoom: Improving 3D Gaussian Splatting with SDF Guidance and Monocular Cues for Indoor Scene Reconstruction

- **作者**: Haodong Xiang, Xinghui Li, Kai Cheng et al.
- **发布时间**: 2024-05-30
- **arXiv链接**: [arXiv:2405.19671v2](https://arxiv.org/abs/2405.19671v2)
- **英文摘要**: Embodied intelligence requires precise reconstruction and rendering to simulate large-scale real-world data. Although 3D Gaussian Splatting (3DGS) has recently demonstrated high-quality results with real-time performance, it still faces challenges in indoor scenes with large, textureless regions, resulting in incomplete and noisy reconstructions due to poor point cloud initialization and underconstrained optimization. Inspired by the continuity of signed distance field (SDF), which naturally has advantages in modeling surfaces, we propose a unified optimization framework that integrates neural signed distance fields (SDFs) with 3DGS for accurate geometry reconstruction and real-time rendering. This framework incorporates a neural SDF field to guide the densification and pruning of Gaussians, enabling Gaussians to model scenes accurately even with poor initialized point clouds. Simultaneously, the geometry represented by Gaussians improves the efficiency of the SDF field by piloting its point sampling. Additionally, we introduce two regularization terms based on normal and edge priors to resolve geometric ambiguities in textureless areas and enhance detail accuracy. Extensive experiments in ScanNet and ScanNet++ show that our method achieves state-of-the-art performance in both surface reconstruction and novel view synthesis.

---

## 51. LP-3DGS: Learning to Prune 3D Gaussian Splatting

- **作者**: Zhaoliang Zhang, Tianchen Song, Yongjae Lee et al.
- **发布时间**: 2024-05-29
- **arXiv链接**: [arXiv:2405.18784v1](https://arxiv.org/abs/2405.18784v1)
- **英文摘要**: Recently, 3D Gaussian Splatting (3DGS) has become one of the mainstream methodologies for novel view synthesis (NVS) due to its high quality and fast rendering speed. However, as a point-based scene representation, 3DGS potentially generates a large number of Gaussians to fit the scene, leading to high memory usage. Improvements that have been proposed require either an empirical and preset pruning ratio or importance score threshold to prune the point cloud. Such hyperparamter requires multiple rounds of training to optimize and achieve the maximum pruning ratio, while maintaining the rendering quality for each scene. In this work, we propose learning-to-prune 3DGS (LP-3DGS), where a trainable binary mask is applied to the importance score that can find optimal pruning ratio automatically. Instead of using the traditional straight-through estimator (STE) method to approximate the binary mask gradient, we redesign the masking function to leverage the Gumbel-Sigmoid method, making it differentiable and compatible with the existing training process of 3DGS. Extensive experiments have shown that LP-3DGS consistently produces a good balance that is both efficient and high quality.

---

## 52. A Refined 3D Gaussian Representation for High-Quality Dynamic Scene Reconstruction

- **作者**: Bin Zhang, Bi Zeng, Zexin Peng
- **发布时间**: 2024-05-28
- **arXiv链接**: [arXiv:2405.17891v1](https://arxiv.org/abs/2405.17891v1)
- **英文摘要**: In recent years, Neural Radiance Fields (NeRF) has revolutionized three-dimensional (3D) reconstruction with its implicit representation. Building upon NeRF, 3D Gaussian Splatting (3D-GS) has departed from the implicit representation of neural networks and instead directly represents scenes as point clouds with Gaussian-shaped distributions. While this shift has notably elevated the rendering quality and speed of radiance fields but inevitably led to a significant increase in memory usage. Additionally, effectively rendering dynamic scenes in 3D-GS has emerged as a pressing challenge. To address these concerns, this paper purposes a refined 3D Gaussian representation for high-quality dynamic scene reconstruction. Firstly, we use a deformable multi-layer perceptron (MLP) network to capture the dynamic offset of Gaussian points and express the color features of points through hash encoding and a tiny MLP to reduce storage requirements. Subsequently, we introduce a learnable denoising mask coupled with denoising loss to eliminate noise points from the scene, thereby further compressing 3D Gaussian model. Finally, motion noise of points is mitigated through static constraints and motion consistency constraints. Experimental results demonstrate that our method surpasses existing approaches in rendering quality and speed, while significantly reducing the memory usage associated with 3D-GS, making it highly suitable for various tasks such as novel view synthesis, and dynamic mapping...

---

## 53. SafeguardGS: 3D Gaussian Primitive Pruning While Avoiding Catastrophic Scene Destruction

- **作者**: Yongjae Lee, Zhaoliang Zhang, Deliang Fan
- **发布时间**: 2024-05-28
- **arXiv链接**: [arXiv:2405.17793v2](https://arxiv.org/abs/2405.17793v2)
- **说明**: 19 pages, 20 figures, 7 tables
- **英文摘要**: 3D Gaussian Splatting (3DGS) has made significant strides in novel view synthesis. However, its suboptimal densification process results in the excessively large number of Gaussian primitives, which impacts frame-per-second and increases memory usage, making it unsuitable for low-end devices. To address this issue, many follow-up studies have proposed various pruning techniques with score functions designed to identify and remove less important primitives. Nonetheless, a comprehensive discussion of their effectiveness and implications across all techniques is missing. In this paper, we are the first to categorize 3DGS pruning techniques into two types: Scene-level pruning and Pixel-level pruning, distinguished by their scope for ranking primitives. Our subsequent experiments reveal that, while scene-level pruning leads to disastrous quality drops under extreme decimation of Gaussian primitives, pixel-level pruning not only sustains relatively high rendering quality with minuscule performance degradation but also provides an inherent boundary of pruning, i.e., a safeguard of Gaussian pruning. Building on this observation, we further propose multiple variations of score functions based on the factors of rendering equations and discover that assessing based on color similarity with blending weight is the most effective method for discriminating insignificant primitives. In our experiments, our SafeguardGS with the optimal score function shows the highest PSNR-per-primitive perfo...

---

## 54. GOI: Find 3D Gaussians of Interest with an Optimizable Open-vocabulary Semantic-space Hyperplane

- **作者**: Yansong Qu, Shaohui Dai, Xinyang Li et al.
- **发布时间**: 2024-05-27
- **arXiv链接**: [arXiv:2405.17596v2](https://arxiv.org/abs/2405.17596v2)
- **说明**: Our project page is available at https://quyans.github.io/GOI-Hyperplane/
- **英文摘要**: 3D open-vocabulary scene understanding, crucial for advancing augmented reality and robotic applications, involves interpreting and locating specific regions within a 3D space as directed by natural language instructions. To this end, we introduce GOI, a framework that integrates semantic features from 2D vision-language foundation models into 3D Gaussian Splatting (3DGS) and identifies 3D Gaussians of Interest using an Optimizable Semantic-space Hyperplane. Our approach includes an efficient compression method that utilizes scene priors to condense noisy high-dimensional semantic features into compact low-dimensional vectors, which are subsequently embedded in 3DGS. During the open-vocabulary querying process, we adopt a distinct approach compared to existing methods, which depend on a manually set fixed empirical threshold to select regions based on their semantic feature distance to the query text embedding. This traditional approach often lacks universal accuracy, leading to challenges in precisely identifying specific target areas. Instead, our method treats the feature selection process as a hyperplane division within the feature space, retaining only those features that are highly relevant to the query. We leverage off-the-shelf 2D Referring Expression Segmentation (RES) models to fine-tune the semantic-space hyperplane, enabling a more precise distinction between target regions and others. This fine-tuning substantially improves the accuracy of open-vocabulary queries...

---

## 55. F-3DGS: Factorized Coordinates and Representations for 3D Gaussian Splatting

- **作者**: Xiangyu Sun, Joo Chan Lee, Daniel Rho et al.
- **发布时间**: 2024-05-27
- **arXiv链接**: [arXiv:2405.17083v2](https://arxiv.org/abs/2405.17083v2)
- **说明**: Our project page including code is available at https://xiangyu1sun.github.io/Factorize-3DGS/
- **英文摘要**: The neural radiance field (NeRF) has made significant strides in representing 3D scenes and synthesizing novel views. Despite its advancements, the high computational costs of NeRF have posed challenges for its deployment in resource-constrained environments and real-time applications. As an alternative to NeRF-like neural rendering methods, 3D Gaussian Splatting (3DGS) offers rapid rendering speeds while maintaining excellent image quality. However, as it represents objects and scenes using a myriad of Gaussians, it requires substantial storage to achieve high-quality representation. To mitigate the storage overhead, we propose Factorized 3D Gaussian Splatting (F-3DGS), a novel approach that drastically reduces storage requirements while preserving image quality. Inspired by classical matrix and tensor factorization techniques, our method represents and approximates dense clusters of Gaussians with significantly fewer Gaussians through efficient factorization. We aim to efficiently represent dense 3D Gaussians by approximating them with a limited amount of information for each axis and their combinations. This method allows us to encode a substantially large number of Gaussians along with their essential attributes -- such as color, scale, and rotation -- necessary for rendering using a relatively small number of elements. Extensive experimental results demonstrate that F-3DGS achieves a significant reduction in storage costs while maintaining comparable quality in rendered ...

---

## 56. PyGS: Large-scale Scene Representation with Pyramidal 3D Gaussian Splatting

- **作者**: Zipeng Wang, Dan Xu
- **发布时间**: 2024-05-27
- **arXiv链接**: [arXiv:2405.16829v3](https://arxiv.org/abs/2405.16829v3)
- **英文摘要**: Neural Radiance Fields (NeRFs) have demonstrated remarkable proficiency in synthesizing photorealistic images of large-scale scenes. However, they are often plagued by a loss of fine details and long rendering durations. 3D Gaussian Splatting has recently been introduced as a potent alternative, achieving both high-fidelity visual results and accelerated rendering performance. Nonetheless, scaling 3D Gaussian Splatting is fraught with challenges. Specifically, large-scale scenes grapples with the integration of objects across multiple scales and disparate viewpoints, which often leads to compromised efficacy as the Gaussians need to balance between detail levels. Furthermore, the generation of initialization points via COLMAP from large-scale dataset is both computationally demanding and prone to incomplete reconstructions. To address these challenges, we present Pyramidal 3D Gaussian Splatting (PyGS) with NeRF Initialization. Our approach represent the scene with a hierarchical assembly of Gaussians arranged in a pyramidal fashion. The top level of the pyramid is composed of a few large Gaussians, while each subsequent layer accommodates a denser collection of smaller Gaussians. We effectively initialize these pyramidal Gaussians through sampling a rapidly trained grid-based NeRF at various frequencies. We group these pyramidal Gaussians into clusters and use a compact weighting network to dynamically determine the influence of each pyramid level of each cluster considering ...

---

## 57. Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians

- **作者**: Erik Sandström, Keisuke Tateno, Michael Oechsle et al.
- **发布时间**: 2024-05-26
- **arXiv链接**: [arXiv:2405.16544v1](https://arxiv.org/abs/2405.16544v1)
- **说明**: 21 pages
- **英文摘要**: 3D Gaussian Splatting has emerged as a powerful representation of geometry and appearance for RGB-only dense Simultaneous Localization and Mapping (SLAM), as it provides a compact dense map representation while enabling efficient and high-quality map rendering. However, existing methods show significantly worse reconstruction quality than competing methods using other 3D representations, e.g. neural points clouds, since they either do not employ global map and pose optimization or make use of monocular depth. In response, we propose the first RGB-only SLAM system with a dense 3D Gaussian map representation that utilizes all benefits of globally optimized tracking by adapting dynamically to keyframe pose and depth updates by actively deforming the 3D Gaussian map. Moreover, we find that refining the depth updates in inaccurate areas with a monocular depth estimator further improves the accuracy of the 3D reconstruction. Our experiments on the Replica, TUM-RGBD, and ScanNet datasets indicate the effectiveness of globally optimized 3D Gaussians, as the approach achieves superior or on par performance with existing RGB-only SLAM methods methods in tracking, mapping and rendering accuracy while yielding small map sizes and fast runtimes. The source code is available at https://github.com/eriksandstroem/Splat-SLAM.

---

## 58. GS-ROR$^2$: Bidirectional-guided 3DGS and SDF for Reflective Object Relighting and Reconstruction

- **作者**: Zuo-Liang Zhu, Beibei Wang, Jian Yang
- **发布时间**: 2024-05-22
- **arXiv链接**: [arXiv:2406.18544v3](https://arxiv.org/abs/2406.18544v3)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has shown a powerful capability for novel view synthesis due to its detailed expressive ability and highly efficient rendering speed. Unfortunately, creating relightable 3D assets and reconstructing faithful geometry with 3DGS is still problematic, particularly for reflective objects, as its discontinuous representation raises difficulties in constraining geometries. Volumetric signed distance field (SDF) methods provide robust geometry reconstruction, while the expensive ray marching hinders its real-time application and slows the training. Besides, these methods struggle to capture sharp geometric details. To this end, we propose to guide 3DGS and SDF bidirectionally in a complementary manner, including an SDF-aided Gaussian splatting for efficient optimization of the relighting model and a GS-guided SDF enhancement for high-quality geometry reconstruction. At the core of our SDF-aided Gaussian splatting is the mutual supervision of the depth and normal between blended Gaussians and SDF, which avoids the expensive volume rendering of SDF. Thanks to this mutual supervision, the learned blended Gaussians are well-constrained with a minimal time cost. As the Gaussians are rendered in a deferred shading mode, the alpha-blended Gaussians are smooth, while individual Gaussians may still be outliers, yielding floater artifacts. Therefore, we introduce an SDF-aware pruning strategy to remove Gaussian outliers located distant from the surface defined by ...

---

## 59. MotionGS : Compact Gaussian Splatting SLAM by Motion Filter

- **作者**: Xinli Guo, Weidong Zhang, Ruonan Liu, Peng Han, Hongtian Chen
- **发布时间**: 2024-05-18
- **arXiv链接**: [arXiv:2405.11129v2](https://arxiv.org/abs/2405.11129v2)
- **英文摘要**: With their high-fidelity scene representation capability, the attention of SLAM field is deeply attracted by the Neural Radiation Field (NeRF) and 3D Gaussian Splatting (3DGS). Recently, there has been a surge in NeRF-based SLAM, while 3DGS-based SLAM is sparse. A novel 3DGS-based SLAM approach with a fusion of deep visual feature, dual keyframe selection and 3DGS is presented in this paper. Compared with the existing methods, the proposed tracking is achieved by feature extraction and motion filter on each frame. The joint optimization of poses and 3D Gaussians runs through the entire mapping process. Additionally, the coarse-to-fine pose estimation and compact Gaussian scene representation are implemented by dual keyframe selection and novel loss functions. Experimental results demonstrate that the proposed algorithm not only outperforms the existing methods in tracking and mapping, but also has less memory usage.

---

## 60. From NeRFs to Gaussian Splats, and Back

- **作者**: Siming He, Zach Osman, Pratik Chaudhari
- **发布时间**: 2024-05-15
- **arXiv链接**: [arXiv:2405.09717v3](https://arxiv.org/abs/2405.09717v3)
- **英文摘要**: For robotics applications where there is a limited number of (typically ego-centric) views, parametric representations such as neural radiance fields (NeRFs) generalize better than non-parametric ones such as Gaussian splatting (GS) to views that are very different from those in the training data; GS however can render much faster than NeRFs. We develop a procedure to convert back and forth between the two. Our approach achieves the best of both NeRFs (superior PSNR, SSIM, and LPIPS on dissimilar views, and a compact representation) and GS (real-time rendering and ability for easily modifying the representation); the computational cost of these conversions is minor compared to training the two from scratch.

---

## 61. I3DGS: Improve 3D Gaussian Splatting from Multiple Dimensions

- **作者**: Jinwei Lin
- **发布时间**: 2024-05-10
- **arXiv链接**: [arXiv:2405.06408v1](https://arxiv.org/abs/2405.06408v1)
- **说明**: 16 pages
- **英文摘要**: 3D Gaussian Splatting is a novel method for 3D view synthesis, which can gain an implicit neural learning rendering result than the traditional neural rendering technology but keep the more high-definition fast rendering speed. But it is still difficult to achieve a fast enough efficiency on 3D Gaussian Splatting for the practical applications. To Address this issue, we propose the I3DS, a synthetic model performance improvement evaluation solution and experiments test. From multiple and important levels or dimensions of the original 3D Gaussian Splatting, we made more than two thousand various kinds of experiments to test how the selected different items and components can make an impact on the training efficiency of the 3D Gaussian Splatting model. In this paper, we will share abundant and meaningful experiences and methods about how to improve the training, performance and the impacts caused by different items of the model. A special but normal Integer compression in base 95 and a floating-point compression in base 94 with ASCII encoding and decoding mechanism is presented. Many real and effective experiments and test results or phenomena will be recorded. After a series of reasonable fine-tuning, I3DS can gain excellent performance improvements than the previous one. The project code is available as open source.

---

## 62. GDGS: Gradient Domain Gaussian Splatting for Sparse Representation of Radiance Fields

- **作者**: Yuanhao Gong
- **发布时间**: 2024-05-08
- **arXiv链接**: [arXiv:2405.05446v1](https://arxiv.org/abs/2405.05446v1)
- **说明**: arXiv admin note: text overlap with arXiv:2404.09105
- **英文摘要**: The 3D Gaussian splatting methods are getting popular. However, they work directly on the signal, leading to a dense representation of the signal. Even with some techniques such as pruning or distillation, the results are still dense. In this paper, we propose to model the gradient of the original signal. The gradients are much sparser than the original signal. Therefore, the gradients use much less Gaussian splats, leading to the more efficient storage and thus higher computational performance during both training and rendering. Thanks to the sparsity, during the view synthesis, only a small mount of pixels are needed, leading to much higher computational performance ($100\sim 1000\times$ faster). And the 2D image can be recovered from the gradients via solving a Poisson equation with linear computation complexity. Several experiments are performed to confirm the sparseness of the gradients and the computation performance of the proposed method. The method can be applied various applications, such as human body modeling and indoor environment modeling.

---

## 63. SAGS: Structure-Aware 3D Gaussian Splatting

- **作者**: Evangelos Ververas, Rolandos Alexandros Potamias, Jifei Song, Jiankang Deng, Stefanos Zafeiriou
- **发布时间**: 2024-04-29
- **arXiv链接**: [arXiv:2404.19149v1](https://arxiv.org/abs/2404.19149v1)
- **说明**: 15 pages, 8 figures, 3 tables
- **英文摘要**: Following the advent of NeRFs, 3D Gaussian Splatting (3D-GS) has paved the way to real-time neural rendering overcoming the computational burden of volumetric methods. Following the pioneering work of 3D-GS, several methods have attempted to achieve compressible and high-fidelity performance alternatives. However, by employing a geometry-agnostic optimization scheme, these methods neglect the inherent 3D structure of the scene, thereby restricting the expressivity and the quality of the representation, resulting in various floating points and artifacts. In this work, we propose a structure-aware Gaussian Splatting method (SAGS) that implicitly encodes the geometry of the scene, which reflects to state-of-the-art rendering performance and reduced storage requirements on benchmark novel-view synthesis datasets. SAGS is founded on a local-global graph representation that facilitates the learning of complex scenes and enforces meaningful point displacements that preserve the scene's geometry. Additionally, we introduce a lightweight version of SAGS, using a simple yet effective mid-point interpolation scheme, which showcases a compact representation of the scene with up to 24$\times$ size reduction without the reliance on any compression strategies. Extensive experiments across multiple benchmark datasets demonstrate the superiority of SAGS compared to state-of-the-art 3D-GS methods under both rendering quality and model size. Besides, we demonstrate that our structure-aware meth...

---

## 64. GSTalker: Real-time Audio-Driven Talking Face Generation via Deformable Gaussian Splatting

- **作者**: Bo Chen, Shoukang Hu, Qi Chen et al.
- **发布时间**: 2024-04-29
- **arXiv链接**: [arXiv:2404.19040v1](https://arxiv.org/abs/2404.19040v1)
- **英文摘要**: We present GStalker, a 3D audio-driven talking face generation model with Gaussian Splatting for both fast training (40 minutes) and real-time rendering (125 FPS) with a 3$\sim$5 minute video for training material, in comparison with previous 2D and 3D NeRF-based modeling frameworks which require hours of training and seconds of rendering per frame. Specifically, GSTalker learns an audio-driven Gaussian deformation field to translate and transform 3D Gaussians to synchronize with audio information, in which multi-resolution hashing grid-based tri-plane and temporal smooth module are incorporated to learn accurate deformation for fine-grained facial details. In addition, a pose-conditioned deformation field is designed to model the stabilized torso. To enable efficient optimization of the condition Gaussian deformation field, we initialize 3D Gaussians by learning a coarse static Gaussian representation. Extensive experiments in person-specific videos with audio tracks validate that GSTalker can generate high-fidelity and audio-lips synchronized results with fast training and real-time rendering speed.

---

## 65. EfficientGS: Streamlining Gaussian Splatting for Large-Scale High-Resolution Scene Representation

- **作者**: Wenkai Liu, Tao Guan, Bin Zhu et al.
- **发布时间**: 2024-04-19
- **arXiv链接**: [arXiv:2404.12777v1](https://arxiv.org/abs/2404.12777v1)
- **英文摘要**: In the domain of 3D scene representation, 3D Gaussian Splatting (3DGS) has emerged as a pivotal technology. However, its application to large-scale, high-resolution scenes (exceeding 4k$\times$4k pixels) is hindered by the excessive computational requirements for managing a large number of Gaussians. Addressing this, we introduce 'EfficientGS', an advanced approach that optimizes 3DGS for high-resolution, large-scale scenes. We analyze the densification process in 3DGS and identify areas of Gaussian over-proliferation. We propose a selective strategy, limiting Gaussian increase to key primitives, thereby enhancing the representational efficiency. Additionally, we develop a pruning mechanism to remove redundant Gaussians, those that are merely auxiliary to adjacent ones. For further enhancement, we integrate a sparse order increment for Spherical Harmonics (SH), designed to alleviate storage constraints and reduce training overhead. Our empirical evaluations, conducted on a range of datasets including extensive 4K+ aerial images, demonstrate that 'EfficientGS' not only expedites training and rendering times but also achieves this with a model size approximately tenfold smaller than conventional 3DGS while maintaining high rendering fidelity.

---

## 66. Application of 3D Gaussian Splatting for Cinematic Anatomy on Consumer Class Devices

- **作者**: Simon Niedermayr, Christoph Neuhauser, Kaloian Petkov, Klaus Engel, Rüdiger Westermann
- **发布时间**: 2024-04-17
- **arXiv链接**: [arXiv:2404.11285v2](https://arxiv.org/abs/2404.11285v2)
- **英文摘要**: Interactive photorealistic rendering of 3D anatomy is used in medical education to explain the structure of the human body. It is currently restricted to frontal teaching scenarios, where even with a powerful GPU and high-speed access to a large storage device where the data set is hosted, interactive demonstrations can hardly be achieved. We present the use of novel view synthesis via compressed 3D Gaussian Splatting (3DGS) to overcome this restriction, and to even enable students to perform cinematic anatomy on lightweight and mobile devices. Our proposed pipeline first finds a set of camera poses that captures all potentially seen structures in the data. High-quality images are then generated with path tracing and converted into a compact 3DGS representation, consuming < 70 MB even for data sets of multiple GBs. This allows for real-time photorealistic novel view synthesis that recovers structures up to the voxel resolution and is almost indistinguishable from the path-traced images

---

## 67. 3D Gaussian Splatting as Markov Chain Monte Carlo

- **作者**: Shakiba Kheradmand, Daniel Rebain, Gopal Sharma et al.
- **发布时间**: 2024-04-15
- **arXiv链接**: [arXiv:2404.09591v3](https://arxiv.org/abs/2404.09591v3)
- **英文摘要**: While 3D Gaussian Splatting has recently become popular for neural rendering, current methods rely on carefully engineered cloning and splitting strategies for placing Gaussians, which can lead to poor-quality renderings, and reliance on a good initialization. In this work, we rethink the set of 3D Gaussians as a random sample drawn from an underlying probability distribution describing the physical representation of the scene-in other words, Markov Chain Monte Carlo (MCMC) samples. Under this view, we show that the 3D Gaussian updates can be converted as Stochastic Gradient Langevin Dynamics (SGLD) updates by simply introducing noise. We then rewrite the densification and pruning strategies in 3D Gaussian Splatting as simply a deterministic state transition of MCMC samples, removing these heuristics from the framework. To do so, we revise the 'cloning' of Gaussians into a relocalization scheme that approximately preserves sample probability. To encourage efficient use of Gaussians, we introduce a regularizer that promotes the removal of unused Gaussians. On various standard evaluation scenes, we show that our method provides improved rendering quality, easy control over the number of Gaussians, and robustness to initialization.

---

## 68. CompGS: Efficient 3D Scene Representation via Compressed Gaussian Splatting

- **作者**: Xiangrui Liu, Xinju Wu, Pingping Zhang et al.
- **发布时间**: 2024-04-15
- **arXiv链接**: [arXiv:2404.09458v1](https://arxiv.org/abs/2404.09458v1)
- **说明**: Submitted to a conference
- **英文摘要**: Gaussian splatting, renowned for its exceptional rendering quality and efficiency, has emerged as a prominent technique in 3D scene representation. However, the substantial data volume of Gaussian splatting impedes its practical utility in real-world applications. Herein, we propose an efficient 3D scene representation, named Compressed Gaussian Splatting (CompGS), which harnesses compact Gaussian primitives for faithful 3D scene modeling with a remarkably reduced data size. To ensure the compactness of Gaussian primitives, we devise a hybrid primitive structure that captures predictive relationships between each other. Then, we exploit a small set of anchor primitives for prediction, allowing the majority of primitives to be encapsulated into highly compact residual forms. Moreover, we develop a rate-constrained optimization scheme to eliminate redundancies within such hybrid primitives, steering our CompGS towards an optimal trade-off between bitrate consumption and representation efficacy. Experimental results show that the proposed CompGS significantly outperforms existing methods, achieving superior compactness in 3D scene representation without compromising model accuracy and rendering quality. Our code will be released on GitHub for further research.

---

## 69. Revising Densification in Gaussian Splatting

- **作者**: Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder
- **发布时间**: 2024-04-09
- **arXiv链接**: [arXiv:2404.06109v1](https://arxiv.org/abs/2404.06109v1)
- **英文摘要**: In this paper, we address the limitations of Adaptive Density Control (ADC) in 3D Gaussian Splatting (3DGS), a scene representation method achieving high-quality, photorealistic results for novel view synthesis. ADC has been introduced for automatic 3D point primitive management, controlling densification and pruning, however, with certain limitations in the densification logic. Our main contribution is a more principled, pixel-error driven formulation for density control in 3DGS, leveraging an auxiliary, per-pixel error function as the criterion for densification. We further introduce a mechanism to control the total number of primitives generated per scene and correct a bias in the current opacity handling strategy of ADC during cloning operations. Our approach leads to consistent quality improvements across a variety of benchmark scenes, without sacrificing the method's efficiency.

---

## 70. TOGS: Gaussian Splatting with Temporal Opacity Offset for Real-Time 4D DSA Rendering

- **作者**: Shuai Zhang, Huangxuan Zhao, Zhenghong Zhou et al.
- **发布时间**: 2024-03-28
- **arXiv链接**: [arXiv:2403.19586v2](https://arxiv.org/abs/2403.19586v2)
- **英文摘要**: Four-dimensional Digital Subtraction Angiography (4D DSA) is a medical imaging technique that provides a series of 2D images captured at different stages and angles during the process of contrast agent filling blood vessels. It plays a significant role in the diagnosis of cerebrovascular diseases. Improving the rendering quality and speed under sparse sampling is important for observing the status and location of lesions. The current methods exhibit inadequate rendering quality in sparse views and suffer from slow rendering speed. To overcome these limitations, we propose TOGS, a Gaussian splatting method with opacity offset over time, which can effectively improve the rendering quality and speed of 4D DSA. We introduce an opacity offset table for each Gaussian to model the opacity offsets of the Gaussian, using these opacity-varying Gaussians to model the temporal variations in the radiance of the contrast agent. By interpolating the opacity offset table, the opacity variation of the Gaussian at different time points can be determined. This enables us to render the 2D DSA image at that specific moment. Additionally, we introduced a Smooth loss term in the loss function to mitigate overfitting issues that may arise in the model when dealing with sparse view scenarios. During the training phase, we randomly prune Gaussians, thereby reducing the storage overhead of the model. The experimental results demonstrate that compared to previous methods, this model achieves state-of-th...

---

## 71. Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians

- **作者**: Kerui Ren, Lihan Jiang, Tao Lu et al.
- **发布时间**: 2024-03-26
- **arXiv链接**: [arXiv:2403.17898v2](https://arxiv.org/abs/2403.17898v2)
- **说明**: Project page: https://city-super.github.io/octree-gs/
- **英文摘要**: The recent 3D Gaussian splatting (3D-GS) has shown remarkable rendering fidelity and efficiency compared to NeRF-based neural scene representations. While demonstrating the potential for real-time rendering, 3D-GS encounters rendering bottlenecks in large scenes with complex details due to an excessive number of Gaussian primitives located within the viewing frustum. This limitation is particularly noticeable in zoom-out views and can lead to inconsistent rendering speeds in scenes with varying details. Moreover, it often struggles to capture the corresponding level of details at different scales with its heuristic density control operation. Inspired by the Level-of-Detail (LOD) techniques, we introduce Octree-GS, featuring an LOD-structured 3D Gaussian approach supporting level-of-detail decomposition for scene representation that contributes to the final rendering results. Our model dynamically selects the appropriate level from the set of multi-resolution anchor points, ensuring consistent rendering performance with adaptive LOD adjustments while maintaining high-fidelity rendering results.

---

## 72. HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression

- **作者**: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai
- **发布时间**: 2024-03-21
- **arXiv链接**: [arXiv:2403.14530v3](https://arxiv.org/abs/2403.14530v3)
- **说明**: Project Page: https://yihangchen-ee.github.io/project_hac/ Code: https://github.com/YihangChen-ee/HAC
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel view synthesis, boasting rapid rendering speed with high fidelity. However, the substantial Gaussians and their associated attributes necessitate effective compression techniques. Nevertheless, the sparse and unorganized nature of the point cloud of Gaussians (or anchors in our paper) presents challenges for compression. To address this, we make use of the relations between the unorganized anchors and the structured hash grid, leveraging their mutual information for context modeling, and propose a Hash-grid Assisted Context (HAC) framework for highly compact 3DGS representation. Our approach introduces a binary hash grid to establish continuous spatial consistencies, allowing us to unveil the inherent spatial relations of anchors through a carefully designed context model. To facilitate entropy coding, we utilize Gaussian distributions to accurately estimate the probability of each quantized attribute, where an adaptive quantization module is proposed to enable high-precision quantization of these attributes for improved fidelity restoration. Additionally, we incorporate an adaptive masking strategy to eliminate invalid Gaussians and anchors. Importantly, our work is the pioneer to explore context-based compression for 3DGS representation, resulting in a remarkable size reduction of over $75\times$ compared to vanilla 3DGS, while simultaneously improving fidelity, and achieving over $11\times$ size re...

---

## 73. Mini-Splatting: Representing Scenes with a Constrained Number of Gaussians

- **作者**: Guangchi Fang, Bing Wang
- **发布时间**: 2024-03-21
- **arXiv链接**: [arXiv:2403.14166v3](https://arxiv.org/abs/2403.14166v3)
- **英文摘要**: In this study, we explore the challenge of efficiently representing scenes with a constrained number of Gaussians. Our analysis shifts from traditional graphics and 2D computer vision to the perspective of point clouds, highlighting the inefficient spatial distribution of Gaussian representation as a key limitation in model performance. To address this, we introduce strategies for densification including blur split and depth reinitialization, and simplification through intersection preserving and sampling. These techniques reorganize the spatial positions of the Gaussians, resulting in significant improvements across various datasets and benchmarks in terms of rendering quality, resource consumption, and storage compression. Our Mini-Splatting integrates seamlessly with the original rasterization pipeline, providing a strong baseline for future research in Gaussian-Splatting-based works. \href{https://github.com/fatPeter/mini-splatting}{Code is available}.

---

## 74. NEDS-SLAM: A Neural Explicit Dense Semantic SLAM Framework using 3D Gaussian Splatting

- **作者**: Yiming Ji, Yang Liu, Guanghu Xie, Boyu Ma, Zongwu Xie
- **发布时间**: 2024-03-18
- **arXiv链接**: [arXiv:2403.11679v3](https://arxiv.org/abs/2403.11679v3)
- **说明**: accepted by RA-L, IEEE Robotics and Automation Letters
- **英文摘要**: We propose NEDS-SLAM, a dense semantic SLAM system based on 3D Gaussian representation, that enables robust 3D semantic mapping, accurate camera tracking, and high-quality rendering in real-time. In the system, we propose a Spatially Consistent Feature Fusion model to reduce the effect of erroneous estimates from pre-trained segmentation head on semantic reconstruction, achieving robust 3D semantic Gaussian mapping. Additionally, we employ a lightweight encoder-decoder to compress the high-dimensional semantic features into a compact 3D Gaussian representation, mitigating the burden of excessive memory consumption. Furthermore, we leverage the advantage of 3D Gaussian splatting, which enables efficient and differentiable novel view rendering, and propose a Virtual Camera View Pruning method to eliminate outlier gaussians, thereby effectively enhancing the quality of scene representations. Our NEDS-SLAM method demonstrates competitive performance over existing dense semantic SLAM methods in terms of mapping and tracking accuracy on Replica and ScanNet datasets, while also showing excellent capabilities in 3D dense semantic mapping.

---

## 75. Compact 3D Gaussian Splatting For Dense Visual SLAM

- **作者**: Tianchen Deng, Yaohui Chen, Leyan Zhang et al.
- **发布时间**: 2024-03-17
- **arXiv链接**: [arXiv:2403.11247v2](https://arxiv.org/abs/2403.11247v2)
- **英文摘要**: Recent work has shown that 3D Gaussian-based SLAM enables high-quality reconstruction, accurate pose estimation, and real-time rendering of scenes. However, these approaches are built on a tremendous number of redundant 3D Gaussian ellipsoids, leading to high memory and storage costs, and slow training speed. To address the limitation, we propose a compact 3D Gaussian Splatting SLAM system that reduces the number and the parameter size of Gaussian ellipsoids. A sliding window-based masking strategy is first proposed to reduce the redundant ellipsoids. Then we observe that the covariance matrix (geometry) of most 3D Gaussian ellipsoids are extremely similar, which motivates a novel geometry codebook to compress 3D Gaussian geometric attributes, i.e., the parameters. Robust and accurate pose estimation is achieved by a global bundle adjustment method with reprojection loss. Extensive experiments demonstrate that our method achieves faster training and rendering speed while maintaining the state-of-the-art (SOTA) quality of the scene representation.

---

## 76. GeoGS3D: Single-view 3D Reconstruction via Geometric-aware Diffusion Model and Gaussian Splatting

- **作者**: Qijun Feng, Zhen Xing, Zuxuan Wu, Yu-Gang Jiang
- **发布时间**: 2024-03-15
- **arXiv链接**: [arXiv:2403.10242v2](https://arxiv.org/abs/2403.10242v2)
- **英文摘要**: We introduce GeoGS3D, a novel two-stage framework for reconstructing detailed 3D objects from single-view images. Inspired by the success of pre-trained 2D diffusion models, our method incorporates an orthogonal plane decomposition mechanism to extract 3D geometric features from the 2D input, facilitating the generation of multi-view consistent images. During the following Gaussian Splatting, these images are fused with epipolar attention, fully utilizing the geometric correlations across views. Moreover, we propose a novel metric, Gaussian Divergence Significance (GDS), to prune unnecessary operations during optimization, significantly accelerating the reconstruction process. Extensive experiments demonstrate that GeoGS3D generates images with high consistency across views and reconstructs high-quality 3D objects, both qualitatively and quantitatively.

---

## 77. Gaussian Splatting in Style

- **作者**: Abhishek Saroha, Mariia Gladkova, Cecilia Curreli et al.
- **发布时间**: 2024-03-13
- **arXiv链接**: [arXiv:2403.08498v2](https://arxiv.org/abs/2403.08498v2)
- **说明**: GCPR 2024
- **英文摘要**: 3D scene stylization extends the work of neural style transfer to 3D. A vital challenge in this problem is to maintain the uniformity of the stylized appearance across multiple views. A vast majority of the previous works achieve this by training a 3D model for every stylized image and a set of multi-view images. In contrast, we propose a novel architecture trained on a collection of style images that, at test time, produces real time high-quality stylized novel views. We choose the underlying 3D scene representation for our model as 3D Gaussian splatting. We take the 3D Gaussians and process them using a multi-resolution hash grid and a tiny MLP to obtain stylized views. The MLP is conditioned on different style codes for generalization to different styles during test time. The explicit nature of 3D Gaussians gives us inherent advantages over NeRF-based methods, including geometric consistency and a fast training and rendering regime. This enables our method to be useful for various practical use cases, such as augmented or virtual reality. We demonstrate that our method achieves state-of-the-art performance with superior visual quality on various indoor and outdoor real-world data.

---

## 78. Learning Segmented 3D Gaussians via Efficient Feature Unprojection for Zero-shot Neural Scene Segmentation

- **作者**: Bin Dou, Tianyu Zhang, Zhaohui Wang, Yongjia Ma, Zejian Yuan
- **发布时间**: 2024-01-11
- **arXiv链接**: [arXiv:2401.05925v4](https://arxiv.org/abs/2401.05925v4)
- **说明**: 16 pages, 9 figures, correct writing details
- **英文摘要**: Zero-shot neural scene segmentation, which reconstructs 3D neural segmentation field without manual annotations, serves as an effective way for scene understanding. However, existing models, especially the efficient 3D Gaussian-based methods, struggle to produce compact segmentation results. This issue stems primarily from their redundant learnable attributes assigned on individual Gaussians, leading to a lack of robustness against the 3D-inconsistencies in zero-shot generated raw labels. To address this problem, our work, named Compact Segmented 3D Gaussians (CoSegGaussians), proposes the Feature Unprojection and Fusion module as the segmentation field, which utilizes a shallow decoder generalizable for all Gaussians based on high-level features. Specifically, leveraging the learned Gaussian geometric parameters, semantic-aware image-based features are introduced into the scene via our unprojection technique. The lifted features, together with spatial information, are fed into the multi-scale aggregation decoder to generate segmentation identities for all Gaussians. Furthermore, we design CoSeg Loss to boost model robustness against 3D-inconsistent noises. Experimental results show that our model surpasses baselines on zero-shot semantic segmentation task, improving by ~10% mIoU over the best baseline. Code and more results will be available at https://David-Dou.github.io/CoSegGaussians.

---

