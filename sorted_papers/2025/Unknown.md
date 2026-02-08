# 未知会议 2025

> **最后更新**： 2026-02-08 02:11:48

本页面包含 2025 年 未知会议 会议的论文列表。

## 1. Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression

- **作者**: Xiang Liu, Yimin Zhou, Jinxiang Wang et al.
- **发布时间**: 2025-12-31
- **arXiv链接**: [arXiv:2512.24742v1](https://arxiv.org/abs/2512.24742v1)
- **英文摘要**: The recent advent of 3D Gaussian Splatting (3DGS) has marked a significant breakthrough in real-time novel view synthesis. However, the rapid proliferation of 3DGS-based algorithms has created a pressing need for standardized and comprehensive evaluation tools, especially for compression task. Existing benchmarks often lack the specific metrics necessary to holistically assess the unique characteristics of different methods, such as rendering speed, rate distortion trade-offs memory efficiency, and geometric accuracy. To address this gap, we introduce Splatwizard, a unified benchmark toolkit designed specifically for benchmarking 3DGS compression models. Splatwizard provides an easy-to-use framework to implement new 3DGS compression model and utilize state-of-the-art techniques proposed by previous work. Besides, an integrated pipeline that automates the calculation of key performance indicators, including image-based quality metrics, chamfer distance of reconstruct mesh, rendering frame rates, and computational resource consumption is included in the framework as well. Code is available at https://github.com/splatwizard/splatwizard

---

## 2. Contour Information Aware 2D Gaussian Splatting for Image Representation

- **作者**: Masaya Takabe, Hiroshi Watanabe, Sujun Hong et al.
- **发布时间**: 2025-12-29
- **arXiv链接**: [arXiv:2512.23255v1](https://arxiv.org/abs/2512.23255v1)
- **英文摘要**: Image representation is a fundamental task in computer vision. Recently, Gaussian Splatting has emerged as an efficient representation framework, and its extension to 2D image representation enables lightweight, yet expressive modeling of visual content. While recent 2D Gaussian Splatting (2DGS) approaches provide compact storage and real-time decoding, they often produce blurry or indistinct boundaries when the number of Gaussians is small due to the lack of contour awareness. In this work, we propose a Contour Information-Aware 2D Gaussian Splatting framework that incorporates object segmentation priors into Gaussian-based image representation. By constraining each Gaussian to a specific segmentation region during rasterization, our method prevents cross-boundary blending and preserves edge structures under high compression. We also introduce a warm-up scheme to stabilize training and improve convergence. Experiments on synthetic color charts and the DAVIS dataset demonstrate that our approach achieves higher reconstruction quality around object edges compared to existing 2DGS methods. The improvement is particularly evident in scenarios with very few Gaussians, while our method still maintains fast rendering and low memory usage.

---

## 3. GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation

- **作者**: Tianchen Deng, Xuefeng Chen, Yi Chen et al.
- **发布时间**: 2025-12-29
- **arXiv链接**: [arXiv:2512.23180v2](https://arxiv.org/abs/2512.23180v2)
- **英文摘要**: Driving World Models (DWMs) have been developing rapidly with the advances of generative models. However, existing DWMs lack 3D scene understanding capabilities and can only generate content conditioned on input data, without the ability to interpret or reason about the driving environment. Moreover, current approaches represent 3D spatial information with point cloud or BEV features do not accurately align textual information with the underlying 3D scene. To address these limitations, we propose a novel unified DWM framework based on 3D Gaussian scene representation, which enables both 3D scene understanding and multi-modal scene generation, while also enabling contextual enrichment for understanding and generation tasks. Our approach directly aligns textual information with the 3D scene by embedding rich linguistic features into each Gaussian primitive, thereby achieving early modality alignment. In addition, we design a novel task-aware language-guided sampling strategy that removes redundant 3D Gaussians and injects accurate and compact 3D tokens into LLM. Furthermore, we design a dual-condition multi-modal generation model, where the information captured by our vision-language model is leveraged as a high-level language condition in combination with a low-level image condition, jointly guiding the multi-modal generation process. We conduct comprehensive studies on the nuScenes, and NuInteract datasets to validate the effectiveness of our framework. Our method achieves st...

---

## 4. Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting

- **作者**: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe
- **发布时间**: 2025-12-24
- **arXiv链接**: [arXiv:2512.20927v1](https://arxiv.org/abs/2512.20927v1)
- **说明**: Will be updated
- **英文摘要**: Recent advancements in computer vision have successfully extended Open-vocabulary segmentation (OVS) to the 3D domain by leveraging 3D Gaussian Splatting (3D-GS). Despite this progress, efficiently rendering the high-dimensional features required for open-vocabulary queries poses a significant challenge. Existing methods employ codebooks or feature compression, causing information loss, thereby degrading segmentation quality. To address this limitation, we introduce Quantile Rendering (Q-Render), a novel rendering strategy for 3D Gaussians that efficiently handles high-dimensional features while maintaining high fidelity. Unlike conventional volume rendering, which densely samples all 3D Gaussians intersecting each ray, Q-Render sparsely samples only those with dominant influence along the ray. By integrating Q-Render into a generalizable 3D neural network, we also propose Gaussian Splatting Network (GS-Net), which predicts Gaussian features in a generalizable manner. Extensive experiments on ScanNet and LeRF demonstrate that our framework outperforms state-of-the-art methods, while enabling real-time rendering with an approximate ~43.7x speedup on 512-D feature maps. Code will be made publicly available.

---

## 5. Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization

- **作者**: He Zhu, Zheng Liu, Xingyang Li et al.
- **发布时间**: 2025-12-23
- **arXiv链接**: [arXiv:2512.20495v1](https://arxiv.org/abs/2512.20495v1)
- **英文摘要**: 3D Gaussian splatting (3DGS) has drawn significant attention in the architectural community recently. However, current architectural designs often overlook the 3DGS scalability, making them fragile for extremely large-scale 3DGS. Meanwhile, the VR bandwidth requirement makes it impossible to deliver high-fidelity and smooth VR content from the cloud.   We present Nebula, a coherent acceleration framework for large-scale 3DGS collaborative rendering. Instead of streaming videos, Nebula streams intermediate results after the LoD search, reducing 1925% data communication between the cloud and the client. To further enhance the motion-to-photon experience, we introduce a temporal-aware LoD search in the cloud that tames the irregular memory access and reduces redundant data access by exploiting temporal coherence across frames. On the client side, we propose a novel stereo rasterization that enables two eyes to share most computations during the stereo rendering with bit-accurate quality. With minimal hardware augmentations, Nebula achieves 2.7$\times$ motion-to-photon speedup and reduces 1925% bandwidth over lossy video streaming.

---

## 6. HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

- **作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang et al.
- **发布时间**: 2025-12-16
- **arXiv链接**: [arXiv:2512.14352v1](https://arxiv.org/abs/2512.14352v1)
- **说明**: 11 pages, 9 figures
- **英文摘要**: Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It fur...

---

## 7. Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance

- **作者**: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein
- **发布时间**: 2025-12-12
- **arXiv链接**: [arXiv:2512.11800v1](https://arxiv.org/abs/2512.11800v1)
- **英文摘要**: The recent success of 3D Gaussian Splatting (3DGS) has reshaped novel view synthesis by enabling fast optimization and real-time rendering of high-quality radiance fields. However, it relies on simplified, order-dependent alpha blending and coarse approximations of the density integral within the rasterizer, thereby limiting its ability to render complex, overlapping semi-transparent objects. In this paper, we extend rasterization-based rendering of 3D Gaussian representations with a novel method for high-fidelity transmittance computation, entirely avoiding the need for ray tracing or per-pixel sample sorting. Building on prior work in moment-based order-independent transparency, our key idea is to characterize the density distribution along each camera ray with a compact and continuous representation based on statistical moments. To this end, we analytically derive and compute a set of per-pixel moments from all contributing 3D Gaussians. From these moments, a continuous transmittance function is reconstructed for each ray, which is then independently sampled within each Gaussian. As a result, our method bridges the gap between rasterization and physical accuracy by modeling light attenuation in complex translucent media, significantly improving overall reconstruction and rendering quality.

---

## 8. YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos

- **作者**: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana
- **发布时间**: 2025-12-10
- **arXiv链接**: [arXiv:2512.09903v1](https://arxiv.org/abs/2512.09903v1)
- **英文摘要**: Visual navigation has emerged as a practical alternative to traditional robotic navigation pipelines that rely on detailed mapping and path planning. However, constructing and maintaining 3D maps is often computationally expensive and memory-intensive. We address the problem of visual navigation when exploration videos of a large environment are available. The videos serve as a visual reference, allowing a robot to retrace the explored trajectories without relying on metric maps. Our proposed method, YOPO-Nav (You Only Pass Once), encodes an environment into a compact spatial representation composed of interconnected local 3D Gaussian Splatting (3DGS) models. During navigation, the framework aligns the robot's current visual observation with this representation and predicts actions that guide it back toward the demonstrated trajectory. YOPO-Nav employs a hierarchical design: a visual place recognition (VPR) module provides coarse localization, while the local 3DGS models refine the goal and intermediate poses to generate control actions. To evaluate our approach, we introduce the YOPO-Campus dataset, comprising 4 hours of egocentric video and robot controller inputs from over 6 km of human-teleoperated robot trajectories. We benchmark recent visual navigation methods on trajectories from YOPO-Campus using a Clearpath Jackal robot. Experimental results show YOPO-Nav provides excellent performance in image-goal navigation for real-world scenes on a physical robot. The dataset a...

---

## 9. SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting

- **作者**: Seokhyun Youn, Soohyun Lee, Geonho Kim et al.
- **发布时间**: 2025-12-08
- **arXiv链接**: [arXiv:2512.07197v1](https://arxiv.org/abs/2512.07197v1)
- **说明**: The first three authors contributed equally to this work. The last two authors are co-corresponding authors. Please visit our project page at https://cmlab-korea.github.io/Awesome-Efficient-GS/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful explicit representation enabling real-time, high-fidelity 3D reconstruction and novel view synthesis. However, its practical use is hindered by the massive memory and computational demands required to store and render millions of Gaussians. These challenges become even more severe in 4D dynamic scenes. To address these issues, the field of Efficient Gaussian Splatting has rapidly evolved, proposing methods that reduce redundancy while preserving reconstruction quality. This survey provides the first unified overview of efficient 3D and 4D Gaussian Splatting techniques. For both 3D and 4D settings, we systematically categorize existing methods into two major directions, Parameter Compression and Restructuring Compression, and comprehensively summarize the core ideas and methodological trends within each category. We further cover widely used datasets, evaluation metrics, and representative benchmark comparisons. Finally, we discuss current limitations and outline promising research directions toward scalable, compact, and real-time Gaussian Splatting for both static and dynamic 3D scene representation.

---

## 10. RAVE: Rate-Adaptive Visual Encoding for 3D Gaussian Splatting

- **作者**: Hoang-Nhat Tran, Francesco Di Sario, Gabriele Spadaro, Giuseppe Valenzise, Enzo Tartaglione
- **发布时间**: 2025-12-07
- **arXiv链接**: [arXiv:2512.07052v2](https://arxiv.org/abs/2512.07052v2)
- **英文摘要**: Recent advances in neural scene representations have transformed immersive multimedia, with 3D Gaussian Splatting (3DGS) enabling real-time photorealistic rendering. Despite its efficiency, 3DGS suffers from large memory requirements and costly training procedures, motivating efforts toward compression. Existing approaches, however, operate at fixed rates, limiting adaptability to varying bandwidth and device constraints. In this work, we propose a flexible compression scheme for 3DGS that supports interpolation at any rate between predefined bounds. Our method is computationally lightweight, requires no retraining for any rate, and preserves rendering quality across a broad range of operating points. Experiments demonstrate that the approach achieves efficient, high-quality compression while offering dynamic rate control, making it suitable for practical deployment in immersive applications. The code is available at https://github.com/inspiros/RAVE.

---

## 11. SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training

- **作者**: Yang Zheng, Hao Tan, Kai Zhang et al.
- **发布时间**: 2025-12-05
- **arXiv链接**: [arXiv:2512.05354v1](https://arxiv.org/abs/2512.05354v1)
- **说明**: project page https://y-zheng18.github.io/SplatPainter/
- **英文摘要**: The rise of 3D Gaussian Splatting has revolutionized photorealistic 3D asset creation, yet a critical gap remains for their interactive refinement and editing. Existing approaches based on diffusion or optimization are ill-suited for this task, as they are often prohibitively slow, destructive to the original asset's identity, or lack the precision for fine-grained control. To address this, we introduce \ourmethod, a state-aware feedforward model that enables continuous editing of 3D Gaussian assets from user-provided 2D view(s). Our method directly predicts updates to the attributes of a compact, feature-rich Gaussian representation and leverages Test-Time Training to create a state-aware, iterative workflow. The versatility of our approach allows a single architecture to perform diverse tasks, including high-fidelity local detail refinement, local paint-over, and consistent global recoloring, all at interactive speeds, paving the way for fluid and intuitive 3D content authoring.

---

## 12. TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking

- **作者**: Hanzhi Guo, Dongdong Weng, Mo Su et al.
- **发布时间**: 2025-12-01
- **arXiv链接**: [arXiv:2512.01329v1](https://arxiv.org/abs/2512.01329v1)
- **英文摘要**: Topology-consistent dynamic model sequences are essential for applications such as animation and model editing. However, existing 4D reconstruction methods face challenges in generating high-quality topology-consistent meshes. To address this, we propose a topology-aware dynamic reconstruction framework based on Gaussian Splatting. We introduce a Gaussian topological structure that explicitly encodes spatial connectivity. This structure enables topology-aware densification and pruning, preserving the manifold consistency of the Gaussian representation. Temporal regularization terms further ensure topological coherence over time, while differentiable mesh rasterization improves mesh quality. Experimental results demonstrate that our method reconstructs topology-consistent mesh sequences with significantly higher accuracy than existing approaches. Moreover, the resulting meshes enable precise 3D keypoint tracking. Project page: https://haza628.github.io/tagSplat/

---

## 13. Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation

- **作者**: An Yang, Chenyu Liu, Jun Du et al.
- **发布时间**: 2025-11-30
- **arXiv链接**: [arXiv:2512.00944v1](https://arxiv.org/abs/2512.00944v1)
- **英文摘要**: 3D Gaussian Splatting (3D-GS) has emerged as an efficient 3D representation and a promising foundation for semantic tasks like segmentation. However, existing 3D-GS-based segmentation methods typically rely on high-dimensional category features, which introduce substantial memory overhead. Moreover, fine-grained segmentation remains challenging due to label space congestion and the lack of stable multi-granularity control mechanisms. To address these limitations, we propose a coarse-to-fine binary encoding scheme for per-Gaussian category representation, which compresses each feature into a single integer via the binary-to-decimal mapping, drastically reducing memory usage. We further design a progressive training strategy that decomposes panoptic segmentation into a series of independent sub-tasks, reducing inter-class conflicts and thereby enhancing fine-grained segmentation capability. Additionally, we fine-tune opacity during segmentation training to address the incompatibility between photometric rendering and semantic segmentation, which often leads to foreground-background confusion. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art segmentation performance while significantly reducing memory consumption and accelerating inference.

---

## 14. Feed-Forward 3D Gaussian Splatting Compression with Long-Context Modeling

- **作者**: Zhening Liu, Rui Song, Yushi Huang et al.
- **发布时间**: 2025-11-30
- **arXiv链接**: [arXiv:2512.00877v1](https://arxiv.org/abs/2512.00877v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a revolutionary 3D representation. However, its substantial data size poses a major barrier to widespread adoption. While feed-forward 3DGS compression offers a practical alternative to costly per-scene per-train compressors, existing methods struggle to model long-range spatial dependencies, due to the limited receptive field of transform coding networks and the inadequate context capacity in entropy models. In this work, we propose a novel feed-forward 3DGS compression framework that effectively models long-range correlations to enable highly compact and generalizable 3D representations. Central to our approach is a large-scale context structure that comprises thousands of Gaussians based on Morton serialization. We then design a fine-grained space-channel auto-regressive entropy model to fully leverage this expansive context. Furthermore, we develop an attention-based transform coding model to extract informative latent priors by aggregating features from a wide range of neighboring Gaussians. Our method yields a $20\times$ compression ratio for 3DGS in a feed-forward inference and achieves state-of-the-art performance among generalizable codecs.

---

## 15. Smol-GS: Compact Representations for Abstract 3D Gaussian Splatting

- **作者**: Haishan Wang, Mohammad Hassan Vali, Arno Solin
- **发布时间**: 2025-11-30
- **arXiv链接**: [arXiv:2512.00850v1](https://arxiv.org/abs/2512.00850v1)
- **英文摘要**: We present Smol-GS, a novel method for learning compact representations for 3D Gaussian Splatting (3DGS). Our approach learns highly efficient encodings in 3D space that integrate both spatial and semantic information. The model captures the coordinates of the splats through a recursive voxel hierarchy, while splat-wise features store abstracted cues, including color, opacity, transformation, and material properties. This design allows the model to compress 3D scenes by orders of magnitude without loss of flexibility. Smol-GS achieves state-of-the-art compression on standard benchmarks while maintaining high rendering quality. Beyond visual fidelity, the discrete representations could potentially serve as a foundation for downstream tasks such as navigation, planning, and broader 3D scene understanding.

---

## 16. TGSFormer: Scalable Temporal Gaussian Splatting for Embodied Semantic Scene Completion

- **作者**: Rui Qian, Haozhi Cao, Tianchen Deng et al.
- **发布时间**: 2025-11-29
- **arXiv链接**: [arXiv:2512.00300v1](https://arxiv.org/abs/2512.00300v1)
- **说明**: 14 pages, 10 figures
- **英文摘要**: Embodied 3D Semantic Scene Completion (SSC) infers dense geometry and semantics from continuous egocentric observations. Most existing Gaussian-based methods rely on random initialization of many primitives within predefined spatial bounds, resulting in redundancy and poor scalability to unbounded scenes. Recent depth-guided approach alleviates this issue but remains local, suffering from latency and memory overhead as scale increases. To overcome these challenges, we propose TGSFormer, a scalable Temporal Gaussian Splatting framework for embodied SSC. It maintains a persistent Gaussian memory for temporal prediction, without relying on image coherence or frame caches. For temporal fusion, a Dual Temporal Encoder jointly processes current and historical Gaussian features through confidence-aware cross-attention. Subsequently, a Confidence-aware Voxel Fusion module merges overlapping primitives into voxel-aligned representations, regulating density and maintaining compactness. Extensive experiments demonstrate that TGSFormer achieves state-of-the-art results on both local and embodied SSC benchmarks, offering superior accuracy and scalability with significantly fewer primitives while maintaining consistent long-term scene integrity. The code will be released upon acceptance.

---

## 17. GSpaRC: Gaussian Splatting for Real-time Reconstruction of RF Channels

- **作者**: Bhavya Sai Nukapotula, Rishabh Tripathi, Seth Pregler et al.
- **发布时间**: 2025-11-27
- **arXiv链接**: [arXiv:2511.22793v1](https://arxiv.org/abs/2511.22793v1)
- **英文摘要**: Channel state information (CSI) is essential for adaptive beamforming and maintaining robust links in wireless communication systems. However, acquiring CSI incurs significant overhead, consuming up to 25\% of spectrum resources in 5G networks due to frequent pilot transmissions at sub-millisecond intervals. Recent approaches aim to reduce this burden by reconstructing CSI from spatiotemporal RF measurements, such as signal strength and direction-of-arrival. While effective in offline settings, these methods often suffer from inference latencies in the 5--100~ms range, making them impractical for real-time systems. We present GSpaRC: Gaussian Splatting for Real-time Reconstruction of RF Channels, the first algorithm to break the 1 ms latency barrier while maintaining high accuracy. GSpaRC represents the RF environment using a compact set of 3D Gaussian primitives, each parameterized by a lightweight neural model augmented with physics-informed features such as distance-based attenuation. Unlike traditional vision-based splatting pipelines, GSpaRC is tailored for RF reception: it employs an equirectangular projection onto a hemispherical surface centered at the receiver to reflect omnidirectional antenna behavior. A custom CUDA pipeline enables fully parallelized directional sorting, splatting, and rendering across frequency and spatial dimensions. Evaluated on multiple RF datasets, GSpaRC achieves similar CSI reconstruction fidelity to recent state-of-the-art methods while re...

---

## 18. NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting

- **作者**: Brent Zoomers, Florian Hahlbohm, Joni Vanherck et al.
- **发布时间**: 2025-11-24
- **arXiv链接**: [arXiv:2511.19202v1](https://arxiv.org/abs/2511.19202v1)
- **说明**: 15 pages, 13 figures
- **英文摘要**: 3D Gaussian Splatting can exploit frustum culling and level-of-detail strategies to accelerate rendering of scenes containing a large number of primitives. However, the semi-transparent nature of Gaussians prevents the application of another highly effective technique: occlusion culling. We address this limitation by proposing a novel method to learn the viewpoint-dependent visibility function of all Gaussians in a trained model using a small, shared MLP across instances of an asset in a scene. By querying it for Gaussians within the viewing frustum prior to rasterization, our method can discard occluded primitives during rendering. Leveraging Tensor Cores for efficient computation, we integrate these neural queries directly into a novel instanced software rasterizer. Our approach outperforms the current state of the art for composed scenes in terms of VRAM usage and image quality, utilizing a combination of our instanced rasterizer and occlusion culling MLP, and exhibits complementary properties to existing LoD techniques.

---

## 19. SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation

- **作者**: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath
- **发布时间**: 2025-11-23
- **arXiv链接**: [arXiv:2511.18386v1](https://arxiv.org/abs/2511.18386v1)
- **英文摘要**: We have introduced SegSplat, a novel framework designed to bridge the gap between rapid, feed-forward 3D reconstruction and rich, open-vocabulary semantic understanding. By constructing a compact semantic memory bank from multi-view 2D foundation model features and predicting discrete semantic indices alongside geometric and appearance attributes for each 3D Gaussian in a single pass, SegSplat efficiently imbues scenes with queryable semantics. Our experiments demonstrate that SegSplat achieves geometric fidelity comparable to state-of-the-art feed-forward 3D Gaussian Splatting methods while simultaneously enabling robust open-set semantic segmentation, crucially \textit{without} requiring any per-scene optimization for semantic feature integration. This work represents a significant step towards practical, on-the-fly generation of semantically aware 3D environments, vital for advancing robotic interaction, augmented reality, and other intelligent systems.

---

## 20. CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation

- **作者**: Yuhang Ming, Chenxin Fang, Xingyuan Yu et al.
- **发布时间**: 2025-11-22
- **arXiv链接**: [arXiv:2511.17904v1](https://arxiv.org/abs/2511.17904v1)
- **说明**: 15 pages, 8 figures, 4 tables
- **英文摘要**: Recent advances in Gaussian Splatting based 3D scene representation have shown two major trends: semantics-oriented approaches that focus on high-level understanding but lack explicit 3D geometry modeling, and structure-oriented approaches that capture spatial structures yet provide limited semantic abstraction. To bridge this gap, we present CUS-GS, a compact unified structured Gaussian Splatting representation, which connects multimodal semantic features with structured 3D geometry. Specifically, we design a voxelized anchor structure that constructs a spatial scaffold, while extracting multimodal semantic features from a set of foundation models (e.g., CLIP, DINOv2, SEEM). Moreover, we introduce a multimodal latent feature allocation mechanism to unify appearance, geometry, and semantics across heterogeneous feature spaces, ensuring a consistent representation across multiple foundation models. Finally, we propose a feature-aware significance evaluation strategy to dynamically guide anchor growing and pruning, effectively removing redundant or invalid anchors while maintaining semantic integrity. Extensive experiments show that CUS-GS achieves competitive performance compared to state-of-the-art methods using as few as 6M parameters - an order of magnitude smaller than the closest rival at 35M - highlighting the excellent trade off between performance and model efficiency of the proposed framework.

---

## 21. SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting

- **作者**: Di Wu, Liu Liu, Xueyu Yuan et al.
- **发布时间**: 2025-11-21
- **arXiv链接**: [arXiv:2511.17092v2](https://arxiv.org/abs/2511.17092v2)
- **说明**: 10 pages, 7 figures
- **英文摘要**: Articulated objects are ubiquitous in daily environments, and their 3D reconstruction holds great significance across various fields. However, existing articulated object reconstruction methods typically require costly inputs such as multi-stage and multi-view observations. To address the limitations, we propose a category-agnostic articulated object reconstruction framework via planar Gaussian Splatting, which only uses sparse-view RGB images from a single state. Specifically, we first introduce a Gaussian information field to perceive the optimal sparse viewpoints from candidate camera poses. Then we compress 3D Gaussians into planar Gaussians to facilitate accurate estimation of normal and depth. The planar Gaussians are optimized in a coarse-to-fine manner through depth smooth regularization and few-shot diffusion. Moreover, we introduce a part segmentation probability for each Gaussian primitive and update them by back-projecting part segmentation masks of renderings. Extensive experimental results demonstrate that our method achieves higher-fidelity part-level surface reconstruction on both synthetic and real-world data than existing methods. Codes will be made publicly available.

---

## 22. Gradient-Driven Natural Selection for Compact 3D Gaussian Splatting

- **作者**: Xiaobin Deng, Qiuli Yu, Changyu Diao, Min Li, Duanqing Xu
- **发布时间**: 2025-11-21
- **arXiv链接**: [arXiv:2511.16980v1](https://arxiv.org/abs/2511.16980v1)
- **英文摘要**: 3DGS employs a large number of Gaussian primitives to fit scenes, resulting in substantial storage and computational overhead. Existing pruning methods rely on manually designed criteria or introduce additional learnable parameters, yielding suboptimal results. To address this, we propose an natural selection inspired pruning framework that models survival pressure as a regularization gradient field applied to opacity, allowing the optimization gradients--driven by the goal of maximizing rendering quality--to autonomously determine which Gaussians to retain or prune. This process is fully learnable and requires no human intervention. We further introduce an opacity decay technique with a finite opacity prior, which accelerates the selection process without compromising pruning effectiveness. Compared to 3DGS, our method achieves over 0.6 dB PSNR gain under 15\% budgets, establishing state-of-the-art performance for compact 3DGS. Project page https://xiaobin2001.github.io/GNS-web.

---

## 23. SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression

- **作者**: Keshav Gupta, Akshat Sanghvi, Shreyas Reddy Palley et al.
- **发布时间**: 2025-11-17
- **arXiv链接**: [arXiv:2511.13264v2](https://arxiv.org/abs/2511.13264v2)
- **说明**: Project Page: https://symgs.github.io/
- **英文摘要**: 3D Gaussian Splatting has emerged as a transformative technique in novel view synthesis, primarily due to its high rendering speed and photorealistic fidelity. However, its memory footprint scales rapidly with scene complexity, often reaching several gigabytes. Existing methods address this issue by introducing compression strategies that exploit primitive-level redundancy through similarity detection and quantization. We aim to surpass the compression limits of such methods by incorporating symmetry-aware techniques, specifically targeting mirror symmetries to eliminate redundant primitives. We propose a novel compression framework, SymGS, introducing learnable mirrors into the scene, thereby eliminating local and global reflective redundancies for compression. Our framework functions as a plug-and-play enhancement to state-of-the-art compression methods, (e.g. HAC) to achieve further compression. Compared to HAC, we achieve $1.66 \times$ compression across benchmark datasets (upto $3\times$ on large-scale scenes). On an average, SymGS enables $\bf{108\times}$ compression of a 3DGS scene, while preserving rendering quality. The project page and supplementary can be found at symgs.github.io

---

## 24. GFix: Perceptually Enhanced Gaussian Splatting Video Compression

- **作者**: Siyue Teng, Ge Gao, Duolikun Danier et al.
- **发布时间**: 2025-11-10
- **arXiv链接**: [arXiv:2511.06953v1](https://arxiv.org/abs/2511.06953v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) enhances 3D scene reconstruction through explicit representation and fast rendering, demonstrating potential benefits for various low-level vision tasks, including video compression. However, existing 3DGS-based video codecs generally exhibit more noticeable visual artifacts and relatively low compression ratios. In this paper, we specifically target the perceptual enhancement of 3DGS-based video compression, based on the assumption that artifacts from 3DGS rendering and quantization resemble noisy latents sampled during diffusion training. Building on this premise, we propose a content-adaptive framework, GFix, comprising a streamlined, single-step diffusion model that serves as an off-the-shelf neural enhancer. Moreover, to increase compression efficiency, We propose a modulated LoRA scheme that freezes the low-rank decompositions and modulates the intermediate hidden states, thereby achieving efficient adaptation of the diffusion backbone with highly compressible updates. Experimental results show that GFix delivers strong perceptual quality enhancement, outperforming GSVC with up to 72.1% BD-rate savings in LPIPS and 21.4% in FID.

---

## 25. FastGS: Training 3D Gaussian Splatting in 100 Seconds

- **作者**: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu
- **发布时间**: 2025-11-06
- **arXiv链接**: [arXiv:2511.04283v3](https://arxiv.org/abs/2511.04283v3)
- **说明**: Project page: https://fastgs.github.io/
- **英文摘要**: The dominant 3D Gaussian splatting (3DGS) acceleration methods fail to properly regulate the number of Gaussians during training, causing redundant computational time overhead. In this paper, we propose FastGS, a novel, simple, and general acceleration framework that fully considers the importance of each Gaussian based on multi-view consistency, efficiently solving the trade-off between training time and rendering quality. We innovatively design a densification and pruning strategy based on multi-view consistency, dispensing with the budgeting mechanism. Extensive experiments on Mip-NeRF 360, Tanks & Temples, and Deep Blending datasets demonstrate that our method significantly outperforms the state-of-the-art methods in training speed, achieving a 3.32$\times$ training acceleration and comparable rendering quality compared with DashGaussian on the Mip-NeRF 360 dataset and a 15.45$\times$ acceleration compared with vanilla 3DGS on the Deep Blending dataset. We demonstrate that FastGS exhibits strong generality, delivering 2-7$\times$ training acceleration across various tasks, including dynamic scene reconstruction, surface reconstruction, sparse-view reconstruction, large-scale reconstruction, and simultaneous localization and mapping. The project page is available at https://fastgs.github.io/

---

## 26. Gen-LangSplat: Generalized Language Gaussian Splatting with Pre-Trained Feature Compression

- **作者**: Pranav Saxena
- **发布时间**: 2025-10-27
- **arXiv链接**: [arXiv:2510.22930v1](https://arxiv.org/abs/2510.22930v1)
- **英文摘要**: Modeling open-vocabulary language fields in 3D is essential for intuitive human-AI interaction and querying within physical environments. State-of-the-art approaches, such as LangSplat, leverage 3D Gaussian Splatting to efficiently construct these language fields, encoding features distilled from high-dimensional models like CLIP. However, this efficiency is currently offset by the requirement to train a scene-specific language autoencoder for feature compression, introducing a costly, per-scene optimization bottleneck that hinders deployment scalability. In this work, we introduce Gen-LangSplat, that eliminates this requirement by replacing the scene-wise autoencoder with a generalized autoencoder, pre-trained extensively on the large-scale ScanNet dataset. This architectural shift enables the use of a fixed, compact latent space for language features across any new scene without any scene-specific training. By removing this dependency, our entire language field construction process achieves a efficiency boost while delivering querying performance comparable to, or exceeding, the original LangSplat method. To validate our design choice, we perform a thorough ablation study empirically determining the optimal latent embedding dimension and quantifying representational fidelity using Mean Squared Error and cosine similarity between the original and reprojected 512-dimensional CLIP embeddings. Our results demonstrate that generalized embeddings can efficiently and accurately su...

---

## 27. Region-Adaptive Learned Hierarchical Encoding for 3D Gaussian Splatting Data

- **作者**: Shashank N. Sridhara, Birendra Kathariya, Fangjun Pu et al.
- **发布时间**: 2025-10-26
- **arXiv链接**: [arXiv:2510.22812v1](https://arxiv.org/abs/2510.22812v1)
- **说明**: 10 Pages, 5 Figures
- **英文摘要**: We introduce Region-Adaptive Learned Hierarchical Encoding (RALHE) for 3D Gaussian Splatting (3DGS) data. While 3DGS has recently become popular for novel view synthesis, the size of trained models limits its deployment in bandwidth-constrained applications such as volumetric media streaming. To address this, we propose a learned hierarchical latent representation that builds upon the principles of "overfitted" learned image compression (e.g., Cool-Chic and C3) to efficiently encode 3DGS attributes. Unlike images, 3DGS data have irregular spatial distributions of Gaussians (geometry) and consist of multiple attributes (signals) defined on the irregular geometry. Our codec is designed to account for these differences between images and 3DGS. Specifically, we leverage the octree structure of the voxelized 3DGS geometry to obtain a hierarchical multi-resolution representation. Our approach overfits latents to each Gaussian attribute under a global rate constraint. These latents are decoded independently through a lightweight decoder network. To estimate the bitrate during training, we employ an autoregressive probability model that leverages octree-derived contexts from the 3D point structure. The multi-resolution latents, decoder, and autoregressive entropy coding networks are jointly optimized for each Gaussian attribute. Experiments demonstrate that the proposed RALHE compression framework achieves a rendering PSNR gain of up to 2dB at low bitrates (less than 1 MB) compared t...

---

## 28. MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting

- **作者**: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong
- **发布时间**: 2025-10-22
- **arXiv链接**: [arXiv:2510.19210v1](https://arxiv.org/abs/2510.19210v1)
- **英文摘要**: Recent advances in dynamic scene reconstruction have significantly benefited from 3D Gaussian Splatting, yet existing methods show inconsistent performance across diverse scenes, indicating no single approach effectively handles all dynamic challenges. To overcome these limitations, we propose Mixture of Experts for Dynamic Gaussian Splatting (MoE-GS), a unified framework integrating multiple specialized experts via a novel Volume-aware Pixel Router. Our router adaptively blends expert outputs by projecting volumetric Gaussian-level weights into pixel space through differentiable weight splatting, ensuring spatially and temporally coherent results. Although MoE-GS improves rendering quality, the increased model capacity and reduced FPS are inherent to the MoE architecture. To mitigate this, we explore two complementary directions: (1) single-pass multi-expert rendering and gate-aware Gaussian pruning, which improve efficiency within the MoE framework, and (2) a distillation strategy that transfers MoE performance to individual experts, enabling lightweight deployment without architectural changes. To the best of our knowledge, MoE-GS is the first approach incorporating Mixture-of-Experts techniques into dynamic Gaussian splatting. Extensive experiments on the N3V and Technicolor datasets demonstrate that MoE-GS consistently outperforms state-of-the-art methods with improved efficiency. Video demonstrations are available at https://anonymous.4open.science/w/MoE-GS-68BA/.

---

## 29. PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes

- **作者**: Ying A, Wenzhang Sun, Chang Zeng et al.
- **发布时间**: 2025-10-14
- **arXiv链接**: [arXiv:2510.12282v1](https://arxiv.org/abs/2510.12282v1)
- **英文摘要**: Reconstructing dynamic 3D urban scenes is crucial for autonomous driving, yet current methods face a stark trade-off between fidelity and computational cost. This inefficiency stems from their semantically agnostic design, which allocates resources uniformly, treating static backgrounds and safety-critical objects with equal importance. To address this, we introduce Priority-Adaptive Gaussian Splatting (PAGS), a framework that injects task-aware semantic priorities directly into the 3D reconstruction and rendering pipeline. PAGS introduces two core contributions: (1) Semantically-Guided Pruning and Regularization strategy, which employs a hybrid importance metric to aggressively simplify non-critical scene elements while preserving fine-grained details on objects vital for navigation. (2) Priority-Driven Rendering pipeline, which employs a priority-based depth pre-pass to aggressively cull occluded primitives and accelerate the final shading computations. Extensive experiments on the Waymo and KITTI datasets demonstrate that PAGS achieves exceptional reconstruction quality, particularly on safety-critical objects, while significantly reducing training time and boosting rendering speeds to over 350 FPS.

---

## 30. UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal Rendering

- **作者**: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma
- **发布时间**: 2025-10-14
- **arXiv链接**: [arXiv:2510.12174v2](https://arxiv.org/abs/2510.12174v2)
- **英文摘要**: In this paper, we propose UniGS, a unified map representation and differentiable framework for high-fidelity multimodal 3D reconstruction based on 3D Gaussian Splatting. Our framework integrates a CUDA-accelerated rasterization pipeline capable of rendering photo-realistic RGB images, geometrically accurate depth maps, consistent surface normals, and semantic logits simultaneously. We redesign the rasterization to render depth via differentiable ray-ellipsoid intersection rather than using Gaussian centers, enabling effective optimization of rotation and scale attribute through analytic depth gradients. Furthermore, we derive the analytic gradient formulation for surface normal rendering, ensuring geometric consistency among reconstructed 3D scenes. To improve computational and storage efficiency, we introduce a learnable attribute that enables differentiable pruning of Gaussians with minimal contribution during training. Quantitative and qualitative experiments demonstrate state-of-the-art reconstruction accuracy across all modalities, validating the efficacy of our geometry-aware paradigm. Source code and multimodal viewer will be available on GitHub.

---

## 31. Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided Framework

- **作者**: Shanzhi Yin, Bolin Chen, Xinju Wu et al.
- **发布时间**: 2025-10-12
- **arXiv链接**: [arXiv:2510.10492v1](https://arxiv.org/abs/2510.10492v1)
- **说明**: 10 pages, 4 figures
- **英文摘要**: This paper proposes an efficient 3D avatar coding framework that leverages compact human priors and canonical-to-target transformation to enable high-quality 3D human avatar video compression at ultra-low bit rates. The framework begins by training a canonical Gaussian avatar using articulated splatting in a network-free manner, which serves as the foundation for avatar appearance modeling. Simultaneously, a human-prior template is employed to capture temporal body movements through compact parametric representations. This decomposition of appearance and temporal evolution minimizes redundancy, enabling efficient compression: the canonical avatar is shared across the sequence, requiring compression only once, while the temporal parameters, consisting of just 94 parameters per frame, are transmitted with minimal bit-rate. For each frame, the target human avatar is generated by deforming canonical avatar via Linear Blend Skinning transformation, facilitating temporal coherent video reconstruction and novel view synthesis. Experimental results demonstrate that the proposed method significantly outperforms conventional 2D/3D codecs and existing learnable dynamic 3D Gaussian splatting compression method in terms of rate-distortion performance on mainstream multi-view human video datasets, paving the way for seamless immersive multimedia experiences in meta-verse applications.

---

## 32. Opacity-Gradient Driven Density Control for Compact and Efficient Few-Shot 3D Gaussian Splatting

- **作者**: Abdelrhman Elrawy, Emad A. Mohammed
- **发布时间**: 2025-10-11
- **arXiv链接**: [arXiv:2510.10257v1](https://arxiv.org/abs/2510.10257v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) struggles in few-shot scenarios, where its standard adaptive density control (ADC) can lead to overfitting and bloated reconstructions. While state-of-the-art methods like FSGS improve quality, they often do so by significantly increasing the primitive count. This paper presents a framework that revises the core 3DGS optimization to prioritize efficiency. We replace the standard positional gradient heuristic with a novel densification trigger that uses the opacity gradient as a lightweight proxy for rendering error. We find this aggressive densification is only effective when paired with a more conservative pruning schedule, which prevents destructive optimization cycles. Combined with a standard depth-correlation loss for geometric guidance, our framework demonstrates a fundamental improvement in efficiency. On the 3-view LLFF dataset, our model is over 40% more compact (32k vs. 57k primitives) than FSGS, and on the Mip-NeRF 360 dataset, it achieves a reduction of approximately 70%. This dramatic gain in compactness is achieved with a modest trade-off in reconstruction metrics, establishing a new state-of-the-art on the quality-vs-efficiency Pareto frontier for few-shot view synthesis.

---

## 33. P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression

- **作者**: Henan Wang, Hanxin Zhu, Xinliang Gong et al.
- **发布时间**: 2025-10-11
- **arXiv链接**: [arXiv:2510.10030v1](https://arxiv.org/abs/2510.10030v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has garnered significant attention due to its superior scene representation fidelity and real-time rendering performance, especially for dynamic 3D scene reconstruction (\textit{i.e.}, 4D reconstruction). However, despite achieving promising results, most existing algorithms overlook the substantial temporal and spatial redundancies inherent in dynamic scenes, leading to prohibitive memory consumption. To address this, we propose P-4DGS, a novel dynamic 3DGS representation for compact 4D scene modeling. Inspired by intra- and inter-frame prediction techniques commonly used in video compression, we first design a 3D anchor point-based spatial-temporal prediction module to fully exploit the spatial-temporal correlations across different 3D Gaussian primitives. Subsequently, we employ an adaptive quantization strategy combined with context-based entropy coding to further reduce the size of the 3D anchor points, thereby achieving enhanced compression efficiency. To evaluate the rate-distortion performance of our proposed P-4DGS in comparison with other dynamic 3DGS representations, we conduct extensive experiments on both synthetic and real-world datasets. Experimental results demonstrate that our approach achieves state-of-the-art reconstruction quality and the fastest rendering speed, with a remarkably low storage footprint (around \textbf{1MB} on average), achieving up to \textbf{40$\times$} and \textbf{90$\times$} compression on synthetic and real...

---

## 34. CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting

- **作者**: Zhigang Cheng, Mingchao Sun, Yu Liu et al.
- **发布时间**: 2025-10-11
- **arXiv链接**: [arXiv:2510.09997v1](https://arxiv.org/abs/2510.09997v1)
- **英文摘要**: Level of Detail (LoD) is a fundamental technique in real-time computer graphics for managing the rendering costs of complex scenes while preserving visual fidelity. Traditionally, LoD is implemented using discrete levels (DLoD), where multiple, distinct versions of a model are swapped out at different distances. This long-standing paradigm, however, suffers from two major drawbacks: it requires significant storage for multiple model copies and causes jarring visual ``popping" artifacts during transitions, degrading the user experience. We argue that the explicit, primitive-based nature of the emerging 3D Gaussian Splatting (3DGS) technique enables a more ideal paradigm: Continuous LoD (CLoD). A CLoD approach facilitates smooth, seamless quality scaling within a single, unified model, thereby circumventing the core problems of DLOD. To this end, we introduce CLoD-GS, a framework that integrates a continuous LoD mechanism directly into a 3DGS representation. Our method introduces a learnable, distance-dependent decay parameter for each Gaussian primitive, which dynamically adjusts its opacity based on viewpoint proximity. This allows for the progressive and smooth filtering of less significant primitives, effectively creating a continuous spectrum of detail within one model. To train this model to be robust across all distances, we introduce a virtual distance scaling mechanism and a novel coarse-to-fine training strategy with rendered point count regularization. Our approach n...

---

## 35. ReSplat: Learning Recurrent Gaussian Splats

- **作者**: Haofei Xu, Daniel Barath, Andreas Geiger, Marc Pollefeys
- **发布时间**: 2025-10-09
- **arXiv链接**: [arXiv:2510.08575v2](https://arxiv.org/abs/2510.08575v2)
- **说明**: Project page: https://haofeixu.github.io/resplat/
- **英文摘要**: While feed-forward Gaussian splatting models offer computational efficiency and can generalize to sparse input settings, their performance is fundamentally constrained by relying on a single forward pass for inference. We propose ReSplat, a feed-forward recurrent Gaussian splatting model that iteratively refines 3D Gaussians without explicitly computing gradients. Our key insight is that the Gaussian splatting rendering error serves as a rich feedback signal, guiding the recurrent network to learn effective Gaussian updates. This feedback signal naturally adapts to unseen data distributions at test time, enabling robust generalization across datasets, view counts and image resolutions. To initialize the recurrent process, we introduce a compact reconstruction model that operates in a $16 \times$ subsampled space, producing $16 \times$ fewer Gaussians than previous per-pixel Gaussian models. This substantially reduces computational overhead and allows for efficient Gaussian updates. Extensive experiments across varying of input views (2, 8, 16, 32), resolutions ($256 \times 256$ to $540 \times 960$), and datasets (DL3DV, RealEstate10K and ACID) demonstrate that our method achieves state-of-the-art performance while significantly reducing the number of Gaussians and improving the rendering speed. Our project page is at https://haofeixu.github.io/resplat/.

---

## 36. PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale 3D Gaussian Splatting

- **作者**: Houqiang Zhong, Zhenglong Wu, Sihua Fu et al.
- **发布时间**: 2025-10-09
- **arXiv链接**: [arXiv:2510.07830v1](https://arxiv.org/abs/2510.07830v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently enabled real-time photorealistic rendering in compact scenes, but scaling to large urban environments introduces severe aliasing artifacts and optimization instability, especially under high-resolution (e.g., 4K) rendering. These artifacts, manifesting as flickering textures and jagged edges, arise from the mismatch between Gaussian primitives and the multi-scale nature of urban geometry. While existing ``divide-and-conquer'' pipelines address scalability, they fail to resolve this fidelity gap. In this paper, we propose PrismGS, a physically-grounded regularization framework that improves the intrinsic rendering behavior of 3D Gaussians. PrismGS integrates two synergistic regularizers. The first is pyramidal multi-scale supervision, which enforces consistency by supervising the rendering against a pre-filtered image pyramid. This compels the model to learn an inherently anti-aliased representation that remains coherent across different viewing scales, directly mitigating flickering textures. This is complemented by an explicit size regularization that imposes a physically-grounded lower bound on the dimensions of the 3D Gaussians. This prevents the formation of degenerate, view-dependent primitives, leading to more stable and plausible geometric surfaces and reducing jagged edges. Our method is plug-and-play and compatible with existing pipelines. Extensive experiments on MatrixCity, Mill-19, and UrbanScene3D demonstrate that PrismGS...

---

## 37. RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy Reduction

- **作者**: Leshu Li, Jiayin Qin, Jie Peng et al.
- **发布时间**: 2025-10-08
- **arXiv链接**: [arXiv:2510.06644v2](https://arxiv.org/abs/2510.06644v2)
- **说明**: Accepted by MICRO2025
- **英文摘要**: 3D Gaussian Splatting (3DGS) based Simultaneous Localization and Mapping (SLAM) systems can largely benefit from 3DGS's state-of-the-art rendering efficiency and accuracy, but have not yet been adopted in resource-constrained edge devices due to insufficient speed. Addressing this, we identify notable redundancies across the SLAM pipeline for acceleration. While conceptually straightforward, practical approaches are required to minimize the overhead associated with identifying and eliminating these redundancies. In response, we propose RTGS, an algorithm-hardware co-design framework that comprehensively reduces the redundancies for real-time 3DGS-SLAM on edge. To minimize the overhead, RTGS fully leverages the characteristics of the 3DGS-SLAM pipeline. On the algorithm side, we introduce (1) an adaptive Gaussian pruning step to remove the redundant Gaussians by reusing gradients computed during backpropagation; and (2) a dynamic downsampling technique that directly reuses the keyframe identification and alpha computing steps to eliminate redundant pixels. On the hardware side, we propose (1) a subtile-level streaming strategy and a pixel-level pairwise scheduling strategy that mitigates workload imbalance via a Workload Scheduling Unit (WSU) guided by previous iteration information; (2) a Rendering and Backpropagation (R&B) Buffer that accelerates the rendering backpropagation by reusing intermediate data computed during rendering; and (3) a Gradient Merging Unit (GMU) to red...

---

## 38. ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars

- **作者**: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du
- **发布时间**: 2025-10-07
- **arXiv链接**: [arXiv:2510.05488v1](https://arxiv.org/abs/2510.05488v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has enabled photorealistic and real-time rendering of 3D head avatars. Existing 3DGS-based avatars typically rely on tens of thousands of 3D Gaussian points (Gaussians), with the number of Gaussians fixed after training. However, many practical applications require adjustable levels of detail (LOD) to balance rendering efficiency and visual quality. In this work, we propose "ArchitectHead", the first framework for creating 3D Gaussian head avatars that support continuous control over LOD. Our key idea is to parameterize the Gaussians in a 2D UV feature space and propose a UV feature field composed of multi-level learnable feature maps to encode their latent features. A lightweight neural network-based decoder then transforms these latent features into 3D Gaussian attributes for rendering. ArchitectHead controls the number of Gaussians by dynamically resampling feature maps from the UV feature field at the desired resolutions. This method enables efficient and continuous control of LOD without retraining. Experimental results show that ArchitectHead achieves state-of-the-art (SOTA) quality in self and cross-identity reenactment tasks at the highest LOD, while maintaining near SOTA performance at lower LODs. At the lowest LOD, our method uses only 6.2\% of the Gaussians while the quality degrades moderately (L1 Loss +7.9\%, PSNR --0.97\%, SSIM --0.6\%, LPIPS Loss +24.1\%), and the rendering speed nearly doubles.

---

## 39. Optimized Minimal 4D Gaussian Splatting

- **作者**: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee et al.
- **发布时间**: 2025-10-04
- **arXiv链接**: [arXiv:2510.03857v1](https://arxiv.org/abs/2510.03857v1)
- **说明**: 17 pages, 8 figures
- **英文摘要**: 4D Gaussian Splatting has emerged as a new paradigm for dynamic scene representation, enabling real-time rendering of scenes with complex motions. However, it faces a major challenge of storage overhead, as millions of Gaussians are required for high-fidelity reconstruction. While several studies have attempted to alleviate this memory burden, they still face limitations in compression ratio or visual quality. In this work, we present OMG4 (Optimized Minimal 4D Gaussian Splatting), a framework that constructs a compact set of salient Gaussians capable of faithfully representing 4D Gaussian models. Our method progressively prunes Gaussians in three stages: (1) Gaussian Sampling to identify primitives critical to reconstruction fidelity, (2) Gaussian Pruning to remove redundancies, and (3) Gaussian Merging to fuse primitives with similar characteristics. In addition, we integrate implicit appearance compression and generalize Sub-Vector Quantization (SVQ) to 4D representations, further reducing storage while preserving quality. Extensive experiments on standard benchmark datasets demonstrate that OMG4 significantly outperforms recent state-of-the-art methods, reducing model sizes by over 60% while maintaining reconstruction quality. These results position OMG4 as a significant step forward in compact 4D scene representation, opening new possibilities for a wide range of applications. Our source code is available at https://minshirley.github.io/OMG4/.

---

## 40. GS-Share: Enabling High-fidelity Map Sharing with Incremental Gaussian Splatting

- **作者**: Xinran Zhang, Hanqi Zhu, Yifan Duan, Yanyong Zhang
- **发布时间**: 2025-10-03
- **arXiv链接**: [arXiv:2510.02884v1](https://arxiv.org/abs/2510.02884v1)
- **说明**: 11 pages, 11 figures
- **英文摘要**: Constructing and sharing 3D maps is essential for many applications, including autonomous driving and augmented reality. Recently, 3D Gaussian splatting has emerged as a promising approach for accurate 3D reconstruction. However, a practical map-sharing system that features high-fidelity, continuous updates, and network efficiency remains elusive. To address these challenges, we introduce GS-Share, a photorealistic map-sharing system with a compact representation. The core of GS-Share includes anchor-based global map construction, virtual-image-based map enhancement, and incremental map update. We evaluate GS-Share against state-of-the-art methods, demonstrating that our system achieves higher fidelity, particularly for extrapolated views, with improvements of 11%, 22%, and 74% in PSNR, LPIPS, and Depth L1, respectively. Furthermore, GS-Share is significantly more compact, reducing map transmission overhead by 36%.

---

## 41. From Tokens to Nodes: Semantic-Guided Motion Control for Dynamic 3D Gaussian Splatting

- **作者**: Jianing Chen, Zehao Li, Yujun Cai et al.
- **发布时间**: 2025-10-03
- **arXiv链接**: [arXiv:2510.02732v1](https://arxiv.org/abs/2510.02732v1)
- **英文摘要**: Dynamic 3D reconstruction from monocular videos remains difficult due to the ambiguity inferring 3D motion from limited views and computational demands of modeling temporally varying scenes. While recent sparse control methods alleviate computation by reducing millions of Gaussians to thousands of control points, they suffer from a critical limitation: they allocate points purely by geometry, leading to static redundancy and dynamic insufficiency. We propose a motion-adaptive framework that aligns control density with motion complexity. Leveraging semantic and motion priors from vision foundation models, we establish patch-token-node correspondences and apply motion-adaptive compression to concentrate control points in dynamic regions while suppressing redundancy in static backgrounds. Our approach achieves flexible representational density adaptation through iterative voxelization and motion tendency scoring, directly addressing the fundamental mismatch between control point allocation and motion complexity. To capture temporal evolution, we introduce spline-based trajectory parameterization initialized by 2D tracklets, replacing MLP-based deformation fields to achieve smoother motion representation and more stable optimization. Extensive experiments demonstrate significant improvements in reconstruction quality and efficiency over existing state-of-the-art methods.

---

## 42. GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM Reconstruction

- **作者**: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen
- **发布时间**: 2025-09-29
- **arXiv链接**: [arXiv:2509.25075v2](https://arxiv.org/abs/2509.25075v2)
- **英文摘要**: Cryo-electron microscopy (cryo-EM) has become a central tool for high-resolution structural biology, yet the massive scale of datasets (often exceeding 100k particle images) renders 3D reconstruction both computationally expensive and memory intensive. Traditional Fourier-space methods are efficient but lose fidelity due to repeated transforms, while recent real-space approaches based on neural radiance fields (NeRFs) improve accuracy but incur cubic memory and computation overhead. Therefore, we introduce GEM, a novel cryo-EM reconstruction framework built on 3D Gaussian Splatting (3DGS) that operates directly in real-space while maintaining high efficiency. Instead of modeling the entire density volume, GEM represents proteins with compact 3D Gaussians, each parameterized by only 11 values. To further improve the training efficiency, we designed a novel gradient computation to 3D Gaussians that contribute to each voxel. This design substantially reduced both memory footprint and training cost. On standard cryo-EM benchmarks, GEM achieves up to 48% faster training and 12% lower memory usage compared to state-of-the-art methods, while improving local resolution by as much as 38.8%. These results establish GEM as a practical and scalable paradigm for cryo-EM reconstruction, unifying speed, efficiency, and high-resolution accuracy. Our code is available at https://github.com/UNITES-Lab/GEM.

---

## 43. ExGS: Extreme 3D Gaussian Compression with Diffusion Priors

- **作者**: Jiaqi Chen, Xinhao Ji, Yuanyuan Gao et al.
- **发布时间**: 2025-09-29
- **arXiv链接**: [arXiv:2509.24758v4](https://arxiv.org/abs/2509.24758v4)
- **英文摘要**: Neural scene representations, such as 3D Gaussian Splatting (3DGS), have enabled high-quality neural rendering; however, their large storage and transmission costs hinder deployment in resource-constrained environments. Existing compression methods either rely on costly optimization, which is slow and scene-specific, or adopt training-free pruning and quantization, which degrade rendering quality under high compression ratios. In contrast, recent data-driven approaches provide a promising direction to overcome this trade-off, enabling efficient compression while preserving high rendering quality. We introduce ExGS, a novel feed-forward framework that unifies Universal Gaussian Compression (UGC) with GaussPainter for Extreme 3DGS compression. UGC performs re-optimization-free pruning to aggressively reduce Gaussian primitives while retaining only essential information, whereas GaussPainter leverages powerful diffusion priors with mask-guided refinement to restore high-quality renderings from heavily pruned Gaussian scenes. Unlike conventional inpainting, GaussPainter not only fills in missing regions but also enhances visible pixels, yielding substantial improvements in degraded renderings. To ensure practicality, it adopts a lightweight VAE and a one-step diffusion design, enabling real-time restoration. Our framework can even achieve over 100X compression (reducing a typical 354.77 MB model to about 3.31 MB) while preserving fidelity and significantly improving image quality...

---

## 44. Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh

- **作者**: Yuanyuan Gao, Yuning Gong, Yifei Liu et al.
- **发布时间**: 2025-09-29
- **arXiv链接**: [arXiv:2509.24421v2](https://arxiv.org/abs/2509.24421v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for achieving photorealistic rendering. Recent MLP-based variants further improve visual fidelity but introduce substantial decoding overhead during rendering. To alleviate computation cost, several pruning strategies and level-of-detail (LOD) techniques have been introduced, aiming to effectively reduce the number of Gaussian primitives in large-scale scenes. However, our analysis reveals that significant redundancy still remains due to the lack of occlusion awareness. In this work, we propose Proxy-GS, a novel pipeline that exploits a proxy to introduce Gaussian occlusion awareness from any view. At the core of our approach is a fast proxy system capable of producing precise occlusion depth maps at a resolution of 1000x1000 under 1ms. This proxy serves two roles: first, it guides the culling of anchors and Gaussians to accelerate rendering speed. Second, it guides the densification towards surfaces during training, avoiding inconsistencies in occluded regions, and improving the rendering quality. In heavily occluded scenarios, such as the MatrixCity Streets dataset, Proxy-GS not only equips MLP-based Gaussian splatting with stronger rendering capability but also achieves faster rendering speed. Specifically, it achieves more than 2.5x speedup over Octree-GS, and consistently delivers substantially higher rendering quality. Code will be public upon acceptance.

---

## 45. OMeGa: Joint Optimization of Explicit Meshes and Gaussian Splats for Robust Scene-Level Surface Reconstruction

- **作者**: Yuhang Cao, Haojun Yan, Danya Yao
- **发布时间**: 2025-09-29
- **arXiv链接**: [arXiv:2509.24308v1](https://arxiv.org/abs/2509.24308v1)
- **说明**: 12 pages, 9 figures
- **英文摘要**: Neural rendering with Gaussian splatting has advanced novel view synthesis, and most methods reconstruct surfaces via post-hoc mesh extraction. However, existing methods suffer from two limitations: (i) inaccurate geometry in texture-less indoor regions, and (ii) the decoupling of mesh extraction from optimization, thereby missing the opportunity to leverage mesh geometry to guide splat optimization. In this paper, we present OMeGa, an end-to-end framework that jointly optimizes an explicit triangle mesh and 2D Gaussian splats via a flexible binding strategy, where spatial attributes of Gaussian Splats are expressed in the mesh frame and texture attributes are retained on splats. To further improve reconstruction accuracy, we integrate mesh constraints and monocular normal supervision into the optimization, thereby regularizing geometry learning. In addition, we propose a heuristic, iterative mesh-refinement strategy that splits high-error faces and prunes unreliable ones to further improve the detail and accuracy of the reconstructed mesh. OMeGa achieves state-of-the-art performance on challenging indoor reconstruction benchmarks, reducing Chamfer-$L_1$ by 47.3\% over the 2DGS baseline while maintaining competitive novel-view rendering quality. The experimental results demonstrate that OMeGa effectively addresses prior limitations in indoor texture-less reconstruction.

---

## 46. GaussianVision: Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting

- **作者**: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe
- **发布时间**: 2025-09-26
- **arXiv链接**: [arXiv:2509.22615v2](https://arxiv.org/abs/2509.22615v2)
- **英文摘要**: Modern vision language pipelines are driven by RGB vision encoders trained on massive image text corpora. While these pipelines have enabled impressive zero-shot capabilities and strong transfer across tasks, they still inherit two structural inefficiencies from the pixel domain: (i) transmitting dense RGB images from edge devices to the cloud is energy-intensive and costly, and (ii) patch-based tokenization explodes sequence length, stressing attention budgets and context limits. We explore 2D Gaussian Splatting (2DGS) as an alternative visual substrate for alignment: a compact, spatially adaptive representation that parameterizes images by a set of colored anisotropic Gaussians. We develop a scalable 2DGS pipeline with structured initialization, luminance-aware pruning, and batched CUDA kernels, achieving over 90x faster fitting and about 97% GPU utilization compared to prior implementations. We further adapt contrastive language-image pre-training (CLIP) to 2DGS by reusing a frozen RGB-based transformer backbone with a lightweight splat-aware input stem and a perceiver resampler, training only 9.7% to 13.8% of the total parameters. On a 12.8M dataset from DataComp, GS encoders yield competitive zero-shot performance on 38 datasets from the CLIP benchmark while compressing inputs 3x to 23.5x relative to pixels. Our results establish 2DGS as a viable multimodal substrate, pinpoint architectural bottlenecks, and open a path toward representations that are both semantically po...

---

## 47. Gaussian splatting holography

- **作者**: Shuhe Zhang, Liangcai Cao
- **发布时间**: 2025-09-25
- **arXiv链接**: [arXiv:2509.20774v1](https://arxiv.org/abs/2509.20774v1)
- **英文摘要**: In-line holography offers high space-bandwidth product imaging with a simplified lens-free optical system. However, in-line holographic reconstruction is troubled by twin images arising from the Hermitian symmetry of complex fields. Twin images disrupt the reconstruction in solving the ill-posed phase retrieval problem. The known parameters are less than the unknown parameters, causing phase ambiguities. State-of-the-art deep-learning or non-learning methods face challenges in balancing data fidelity with twin-image disturbance. We propose the Gaussian splatting holography (GSH) for twin-image-suppressed holographic reconstruction. GSH uses Gaussian splatting for optical field representation and compresses the number of unknown parameters by a maximum of 15 folds, transforming the original ill-posed phase retrieval into a well-posed one with reduced phase ambiguities. Additionally, the Gaussian splatting tends to form sharp patterns rather than those with noisy twin-image backgrounds as each Gaussian has a spatially slow-varying profile. Experiments show that GSH achieves constraint-free recovery for in-line holography with accuracy comparable to state-of-the-art constraint-based methods, with an average peak signal-to-noise ratio equal to 26 dB, and structure similarity equal to 0.8. Combined with total variation, GSH can be further improved, obtaining a peak signal-to-noise ratio of 31 dB, and a high compression ability of up to 15 folds.

---

## 48. Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction

- **作者**: Sitian Shen, Georgi Pramatarov, Yifu Tao, Daniele De Martini
- **发布时间**: 2025-09-22
- **arXiv链接**: [arXiv:2509.17762v1](https://arxiv.org/abs/2509.17762v1)
- **英文摘要**: This paper proposes Neural-MMGS, a novel neural 3DGS framework for multimodal large-scale scene reconstruction that fuses multiple sensing modalities in a per-gaussian compact, learnable embedding. While recent works focusing on large-scale scene reconstruction have incorporated LiDAR data to provide more accurate geometric constraints, we argue that LiDAR's rich physical properties remain underexplored. Similarly, semantic information has been used for object retrieval, but could provide valuable high-level context for scene reconstruction. Traditional approaches append these properties to Gaussians as separate parameters, increasing memory usage and limiting information exchange across modalities. Instead, our approach fuses all modalities -- image, LiDAR, and semantics -- into a compact, learnable embedding that implicitly encodes optical, physical, and semantic features in each Gaussian. We then train lightweight neural decoders to map these embeddings to Gaussian parameters, enabling the reconstruction of each sensing modality with lower memory overhead and improved scalability. We evaluate Neural-MMGS on the Oxford Spires and KITTI-360 datasets. On Oxford Spires, we achieve higher-quality reconstructions, while on KITTI-360, our method reaches competitive results with less storage consumption compared with current approaches in LiDAR-based novel-view synthesis.

---

## 49. Improving 3D Gaussian Splatting Compression by Scene-Adaptive Lattice Vector Quantization

- **作者**: Hao Xu, Xiaolin Wu, Xi Zhang
- **发布时间**: 2025-09-16
- **arXiv链接**: [arXiv:2509.13482v1](https://arxiv.org/abs/2509.13482v1)
- **说明**: Code available at https://github.com/hxu160/SALVQ
- **英文摘要**: 3D Gaussian Splatting (3DGS) is rapidly gaining popularity for its photorealistic rendering quality and real-time performance, but it generates massive amounts of data. Hence compressing 3DGS data is necessary for the cost effectiveness of 3DGS models. Recently, several anchor-based neural compression methods have been proposed, achieving good 3DGS compression performance. However, they all rely on uniform scalar quantization (USQ) due to its simplicity. A tantalizing question is whether more sophisticated quantizers can improve the current 3DGS compression methods with very little extra overhead and minimal change to the system. The answer is yes by replacing USQ with lattice vector quantization (LVQ). To better capture scene-specific characteristics, we optimize the lattice basis for each scene, improving LVQ's adaptability and R-D efficiency. This scene-adaptive LVQ (SALVQ) strikes a balance between the R-D efficiency of vector quantization and the low complexity of USQ. SALVQ can be seamlessly integrated into existing 3DGS compression architectures, enhancing their R-D performance with minimal modifications and computational overhead. Moreover, by scaling the lattice basis vectors, SALVQ can dynamically adjust lattice density, enabling a single model to accommodate multiple bit rate targets. This flexibility eliminates the need to train separate models for different compression levels, significantly reducing training time and memory consumption.

---

## 50. 3D Gaussian Modeling and Ray Marching of OpenVDB datasets for Scientific Visualization

- **作者**: Isha Sharma, Dieter Schmalstieg
- **发布时间**: 2025-09-14
- **arXiv链接**: [arXiv:2509.11377v1](https://arxiv.org/abs/2509.11377v1)
- **英文摘要**: 3D Gaussians are currently being heavily investigated for their scene modeling and compression abilities. In 3D volumes, their use is being explored for representing dense volumes as sparsely as possible. However, most of these methods begin with a memory inefficient data format. Specially in Scientific Visualization(SciVis), where most popular formats are dense-grid data structures that store every grid cell, irrespective of its contribution. OpenVDB library and data format were introduced for representing sparse volumetric data specifically for visual effects use cases such as clouds, fire, fluids etc. It avoids storing empty cells by masking them during storage. It presents an opportunity for use in SciVis, specifically as a modeling framework for conversion to 3D Gaussian particles for further compression and for a unified modeling approach for different scientific volume types. This compression head-start is non-trivial and this paper would like to present this with a rendering algorithm based on line integration implemented in OptiX8.1 for calculating 3D Gaussians contribution along a ray for optical-depth accumulation. For comparing the rendering results of our ray marching Gaussians renderer, we also implement a SciVis style primary-ray only NanoVDB HDDA based ray marcher for OpenVDB voxel grids. Finally, this paper also explores application of this Gaussian model to formats of volumes other than regular grids, such as AMR volumes and point clouds, using internal repr...

---

## 51. ROSGS: Relightable Outdoor Scenes With Gaussian Splatting

- **作者**: Lianjun Liao, Chunhui Zhang, Tong Wu et al.
- **发布时间**: 2025-09-14
- **arXiv链接**: [arXiv:2509.11275v1](https://arxiv.org/abs/2509.11275v1)
- **英文摘要**: Image data captured outdoors often exhibit unbounded scenes and unconstrained, varying lighting conditions, making it challenging to decompose them into geometry, reflectance, and illumination. Recent works have focused on achieving this decomposition using Neural Radiance Fields (NeRF) or the 3D Gaussian Splatting (3DGS) representation but remain hindered by two key limitations: the high computational overhead associated with neural networks of NeRF and the use of low-frequency lighting representations, which often result in inefficient rendering and suboptimal relighting accuracy. We propose ROSGS, a two-stage pipeline designed to efficiently reconstruct relightable outdoor scenes using the Gaussian Splatting representation. By leveraging monocular normal priors, ROSGS first reconstructs the scene's geometry with the compact 2D Gaussian Splatting (2DGS) representation, providing an efficient and accurate geometric foundation. Building upon this reconstructed geometry, ROSGS then decomposes the scene's texture and lighting through a hybrid lighting model. This model effectively represents typical outdoor lighting by employing a spherical Gaussian function to capture the directional, high-frequency components of sunlight, while learning a radiance transfer function via Spherical Harmonic coefficients to model the remaining low-frequency skylight comprehensively. Both quantitative metrics and qualitative comparisons demonstrate that ROSGS achieves state-of-the-art performance ...

---

## 52. SVR-GS: Spatially Variant Regularization for Probabilistic Masks in 3D Gaussian Splatting

- **作者**: Ashkan Taghipour, Vahid Naghshin, Benjamin Southwell et al.
- **发布时间**: 2025-09-14
- **arXiv链接**: [arXiv:2509.11116v1](https://arxiv.org/abs/2509.11116v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables fast, high-quality novel view synthesis but typically relies on densification followed by pruning to optimize the number of Gaussians. Existing mask-based pruning, such as MaskGS, regularizes the global mean of the mask, which is misaligned with the local per-pixel (per-ray) reconstruction loss that determines image quality along individual camera rays. This paper introduces SVR-GS, a spatially variant regularizer that renders a per-pixel spatial mask from each Gaussian's effective contribution along the ray, thereby applying sparsity pressure where it matters: on low-importance Gaussians. We explore three spatial-mask aggregation strategies, implement them in CUDA, and conduct a gradient analysis to motivate our final design. Extensive experiments on Tanks\&Temples, Deep Blending, and Mip-NeRF360 datasets demonstrate that, on average across the three datasets, the proposed SVR-GS reduces the number of Gaussians by 1.79\(\times\) compared to MaskGS and 5.63\(\times\) compared to 3DGS, while incurring only 0.50 dB and 0.40 dB PSNR drops, respectively. These gains translate into significantly smaller, faster, and more memory-efficient models, making them well-suited for real-time applications such as robotics, AR/VR, and mobile perception.

---

## 53. MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning

- **作者**: Jiarui Chen, Yikeng Chen, Yingshuang Zou et al.
- **发布时间**: 2025-09-07
- **arXiv链接**: [arXiv:2509.07021v2](https://arxiv.org/abs/2509.07021v2)
- **说明**: 20 pages, 8 figures. Project page at https://megs-2.github.io/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a dominant novel-view synthesis technique, but its high memory consumption severely limits its applicability on edge devices. A growing number of 3DGS compression methods have been proposed to make 3DGS more efficient, yet most only focus on storage compression and fail to address the critical bottleneck of rendering memory. To address this problem, we introduce MEGS$^{2}$, a novel memory-efficient framework that tackles this challenge by jointly optimizing two key factors: the total primitive number and the parameters per primitive, achieving unprecedented memory compression. Specifically, we replace the memory-intensive spherical harmonics with lightweight, arbitrarily oriented spherical Gaussian lobes as our color representations. More importantly, we propose a unified soft pruning framework that models primitive-number and lobe-number pruning as a single constrained optimization problem. Experiments show that MEGS$^{2}$ achieves a 50% static VRAM reduction and a 40% rendering VRAM reduction compared to existing methods, while maintaining comparable rendering quality. Project page: https://megs-2.github.io/

---

## 54. ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast, Memory-Efficient Reconstruction

- **作者**: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa et al.
- **发布时间**: 2025-09-03
- **arXiv链接**: [arXiv:2509.03775v1](https://arxiv.org/abs/2509.03775v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a state-of-art technique to model real-world scenes with high quality and real-time rendering. Typically, a higher quality representation can be achieved by using a large number of 3D Gaussians. However, using large 3D Gaussian counts significantly increases the GPU device memory for storing model parameters. A large model thus requires powerful GPUs with high memory capacities for training and has slower training/rendering latencies due to the inefficiencies of memory access and data movement. In this work, we introduce ContraGS, a method to enable training directly on compressed 3DGS representations without reducing the Gaussian Counts, and thus with a little loss in model quality. ContraGS leverages codebooks to compactly store a set of Gaussian parameter vectors throughout the training process, thereby significantly reducing memory consumption. While codebooks have been demonstrated to be highly effective at compressing fully trained 3DGS models, directly training using codebook representations is an unsolved challenge. ContraGS solves the problem of learning non-differentiable parameters in codebook-compressed representations by posing parameter estimation as a Bayesian inference problem. To this end, ContraGS provides a framework that effectively uses MCMC sampling to sample over a posterior distribution of these compressed representations. With ContraGS, we demonstrate that ContraGS significantly reduces the peak memory during training (...

---

## 55. Efficient Geometry Compression and Communication for 3D Gaussian Splatting Point Clouds

- **作者**: Liang Xie, Yanting Li, Luyang Tang, Wei Gao
- **发布时间**: 2025-09-02
- **arXiv链接**: [arXiv:2509.02232v1](https://arxiv.org/abs/2509.02232v1)
- **说明**: 8 pages,5 figures
- **英文摘要**: Storage and transmission challenges in dynamic 3D scene representation based on the i3DV platform, With increasing scene complexity, the explosive growth of 3D Gaussian data volume causes excessive storage space occupancy. To address this issue, we propose adopting the AVS PCRM reference software for efficient compression of Gaussian point cloud geometry data. The strategy deeply integrates the advanced encoding capabilities of AVS PCRM into the i3DV platform, forming technical complementarity with the original rate-distortion optimization mechanism based on binary hash tables. On one hand, the hash table efficiently caches inter-frame Gaussian point transformation relationships, which allows for high-fidelity transmission within a 40 Mbps bandwidth constraint. On the other hand, AVS PCRM performs precise compression on geometry data. Experimental results demonstrate that the joint framework maintains the advantages of fast rendering and high-quality synthesis in 3D Gaussian technology while achieving significant 10\%-25\% bitrate savings on universal test sets. It provides a superior rate-distortion tradeoff solution for the storage, transmission, and interaction of 3D volumetric video.

---

## 56. Image-Conditioned 3D Gaussian Splat Quantization

- **作者**: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen
- **发布时间**: 2025-08-21
- **arXiv链接**: [arXiv:2508.15372v2](https://arxiv.org/abs/2508.15372v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has attracted considerable attention for enabling high-quality real-time rendering. Although 3DGS compression methods have been proposed for deployment on storage-constrained devices, two limitations hinder archival use: (1) they compress medium-scale scenes only to the megabyte range, which remains impractical for large-scale scenes or extensive scene collections; and (2) they lack mechanisms to accommodate scene changes after long-term archival. To address these limitations, we propose an Image-Conditioned Gaussian Splat Quantizer (ICGS-Quantizer) that substantially enhances compression efficiency and provides adaptability to scene changes after archiving. ICGS-Quantizer improves quantization efficiency by jointly exploiting inter-Gaussian and inter-attribute correlations and by using shared codebooks across all training scenes, which are then fixed and applied to previously unseen test scenes, eliminating the overhead of per-scene codebooks. This approach effectively reduces the storage requirements for 3DGS to the kilobyte range while preserving visual fidelity. To enable adaptability to post-archival scene changes, ICGS-Quantizer conditions scene decoding on images captured at decoding time. The encoding, quantization, and decoding processes are trained jointly, ensuring that the codes, which are quantized representations of the scene, are effective for conditional decoding. We evaluate ICGS-Quantizer on 3D scene compression and 3D scene upda...

---

## 57. GeMS: Efficient Gaussian Splatting for Extreme Motion Blur

- **作者**: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra
- **发布时间**: 2025-08-20
- **arXiv链接**: [arXiv:2508.14682v1](https://arxiv.org/abs/2508.14682v1)
- **英文摘要**: We introduce GeMS, a framework for 3D Gaussian Splatting (3DGS) designed to handle severely motion-blurred images. State-of-the-art deblurring methods for extreme blur, such as ExBluRF, as well as Gaussian Splatting-based approaches like Deblur-GS, typically assume access to sharp images for camera pose estimation and point cloud generation, an unrealistic assumption. Methods relying on COLMAP initialization, such as BAD-Gaussians, also fail due to unreliable feature correspondences under severe blur. To address these challenges, we propose GeMS, a 3DGS framework that reconstructs scenes directly from extremely blurred images. GeMS integrates: (1) VGGSfM, a deep learning-based Structure-from-Motion pipeline that estimates poses and generates point clouds directly from blurred inputs; (2) 3DGS-MCMC, which enables robust scene initialization by treating Gaussians as samples from a probability distribution, eliminating heuristic densification and pruning; and (3) joint optimization of camera trajectories and Gaussian parameters for stable reconstruction. While this pipeline produces strong results, inaccuracies may remain when all inputs are severely blurred. To mitigate this, we propose GeMS-E, which integrates a progressive refinement step using events: (4) Event-based Double Integral (EDI) deblurring restores sharper images that are then fed into GeMS, improving pose estimation, point cloud generation, and overall reconstruction. Both GeMS and GeMS-E achieve state-of-the-art ...

---

## 58. IGFuse: Interactive 3D Gaussian Scene Reconstruction via Multi-Scans Fusion

- **作者**: Wenhao Hu, Zesheng Li, Haonan Zhou et al.
- **发布时间**: 2025-08-18
- **arXiv链接**: [arXiv:2508.13153v1](https://arxiv.org/abs/2508.13153v1)
- **说明**: Project page: https://whhu7.github.io/IGFuse
- **英文摘要**: Reconstructing complete and interactive 3D scenes remains a fundamental challenge in computer vision and robotics, particularly due to persistent object occlusions and limited sensor coverage. Multiview observations from a single scene scan often fail to capture the full structural details. Existing approaches typically rely on multi stage pipelines, such as segmentation, background completion, and inpainting or require per-object dense scanning, both of which are error-prone, and not easily scalable. We propose IGFuse, a novel framework that reconstructs interactive Gaussian scene by fusing observations from multiple scans, where natural object rearrangement between captures reveal previously occluded regions. Our method constructs segmentation aware Gaussian fields and enforces bi-directional photometric and semantic consistency across scans. To handle spatial misalignments, we introduce a pseudo-intermediate scene state for unified alignment, alongside collaborative co-pruning strategies to refine geometry. IGFuse enables high fidelity rendering and object level scene manipulation without dense observations or complex pipelines. Extensive experiments validate the framework's strong generalization to novel scene configurations, demonstrating its effectiveness for real world 3D reconstruction and real-to-simulation transfer. Our project page is available online.

---

## 59. Improving Densification in 3D Gaussian Splatting for High-Fidelity Rendering

- **作者**: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu
- **发布时间**: 2025-08-17
- **arXiv链接**: [arXiv:2508.12313v1](https://arxiv.org/abs/2508.12313v1)
- **说明**: Project page: https://xiaobin2001.github.io/improved-gs-web
- **英文摘要**: Although 3D Gaussian Splatting (3DGS) has achieved impressive performance in real-time rendering, its densification strategy often results in suboptimal reconstruction quality. In this work, we present a comprehensive improvement to the densification pipeline of 3DGS from three perspectives: when to densify, how to densify, and how to mitigate overfitting. Specifically, we propose an Edge-Aware Score to effectively select candidate Gaussians for splitting. We further introduce a Long-Axis Split strategy that reduces geometric distortions introduced by clone and split operations. To address overfitting, we design a set of techniques, including Recovery-Aware Pruning, Multi-step Update, and Growth Control. Our method enhances rendering fidelity without introducing additional training or inference overhead, achieving state-of-the-art performance with fewer Gaussians.

---

## 60. Versatile Video Tokenization with Generative 2D Gaussian Splatting

- **作者**: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu
- **发布时间**: 2025-08-15
- **arXiv链接**: [arXiv:2508.11183v1](https://arxiv.org/abs/2508.11183v1)
- **英文摘要**: Video tokenization procedure is critical for a wide range of video processing tasks. Most existing approaches directly transform video into fixed-grid and patch-wise tokens, which exhibit limited versatility. Spatially, uniformly allocating a fixed number of tokens often leads to over-encoding in low-information regions. Temporally, reducing redundancy remains challenging without explicitly distinguishing between static and dynamic content. In this work, we propose the Gaussian Video Transformer (GVT), a versatile video tokenizer built upon a generative 2D Gaussian Splatting (2DGS) strategy. We first extract latent rigid features from a video clip and represent them with a set of 2D Gaussians generated by our proposed Spatio-Temporal Gaussian Embedding (STGE) mechanism in a feed-forward manner. Such generative 2D Gaussians not only enhance spatial adaptability by assigning higher (resp., lower) rendering weights to regions with higher (resp., lower) information content during rasterization, but also improve generalization by avoiding per-video optimization.To enhance the temporal versatility, we introduce a Gaussian Set Partitioning (GSP) strategy that separates the 2D Gaussians into static and dynamic sets, which explicitly model static content shared across different time-steps and dynamic content specific to each time-step, enabling a compact representation.We primarily evaluate GVT on the video reconstruction, while also assessing its performance on action recognition and...

---

## 61. EntropyGS: An Efficient Entropy Coding on 3D Gaussian Splatting

- **作者**: Yuning Huang, Jiahao Pang, Fengqing Zhu, Dong Tian
- **发布时间**: 2025-08-13
- **arXiv链接**: [arXiv:2508.10227v1](https://arxiv.org/abs/2508.10227v1)
- **英文摘要**: As an emerging novel view synthesis approach, 3D Gaussian Splatting (3DGS) demonstrates fast training/rendering with superior visual quality. The two tasks of 3DGS, Gaussian creation and view rendering, are typically separated over time or devices, and thus storage/transmission and finally compression of 3DGS Gaussians become necessary. We begin with a correlation and statistical analysis of 3DGS Gaussian attributes. An inspiring finding in this work reveals that spherical harmonic AC attributes precisely follow Laplace distributions, while mixtures of Gaussian distributions can approximate rotation, scaling, and opacity. Additionally, harmonic AC attributes manifest weak correlations with other attributes except for inherited correlations from a color space. A factorized and parameterized entropy coding method, EntropyGS, is hereinafter proposed. During encoding, distribution parameters of each Gaussian attribute are estimated to assist their entropy coding. The quantization for entropy coding is adaptively performed according to Gaussian attribute types. EntropyGS demonstrates about 30x rate reduction on benchmark datasets while maintaining similar rendering quality compared to input 3DGS data, with a fast encoding and decoding time.

---

## 62. A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation

- **作者**: Shuting He, Peilin Ji, Yitong Yang et al.
- **发布时间**: 2025-08-13
- **arXiv链接**: [arXiv:2508.09977v3](https://arxiv.org/abs/2508.09977v3)
- **说明**: GitHub Repo: https://github.com/heshuting555/Awesome-3DGS-Applications
- **英文摘要**: In the context of novel view synthesis, 3D Gaussian Splatting (3DGS) has recently emerged as an efficient and competitive counterpart to Neural Radiance Field (NeRF), enabling high-fidelity photorealistic rendering in real time. Beyond novel view synthesis, the explicit and compact nature of 3DGS enables a wide range of downstream applications that require geometric and semantic understanding. This survey provides a comprehensive overview of recent progress in 3DGS applications. It first introduces 2D foundation models that support semantic understanding and control in 3DGS applications, followed by a review of NeRF-based methods that inform their 3DGS counterparts. We then categorize 3DGS applications into three foundational tasks: segmentation, editing, and generation, alongside additional functional applications built upon or tightly coupled with these foundational capabilities. For each, we summarize representative methods, supervision strategies, and learning paradigms, highlighting shared design principles and emerging trends. Commonly used datasets and evaluation protocols are also summarized, along with comparative analyses of recent methods across public benchmarks. To support ongoing research and development, a continually updated repository of papers, code, and resources is maintained at https://github.com/heshuting555/Awesome-3DGS-Applications.

---

## 63. Gradient-Direction-Aware Density Control for 3D Gaussian Splatting

- **作者**: Zheng Zhou, Yu-Jie Xiong, Jia-Chen Zhang et al.
- **发布时间**: 2025-08-12
- **arXiv链接**: [arXiv:2508.09239v2](https://arxiv.org/abs/2508.09239v2)
- **英文摘要**: The emergence of 3D Gaussian Splatting (3DGS) has significantly advanced Novel View Synthesis (NVS) through explicit scene representation, enabling real-time photorealistic rendering. However, existing approaches manifest two critical limitations in complex scenarios: (1) Over-reconstruction occurs when persistent large Gaussians cannot meet adaptive splitting thresholds during density control. This is exacerbated by conflicting gradient directions that prevent effective splitting of these Gaussians; (2) Over-densification of Gaussians occurs in regions with aligned gradient aggregation, leading to redundant component proliferation. This redundancy significantly increases memory overhead due to unnecessary data retention. We present Gradient-Direction-Aware Gaussian Splatting (GDAGS) to address these challenges. Our key innovations: the Gradient Coherence Ratio (GCR), computed through normalized gradient vector norms, which explicitly discriminates Gaussians with concordant versus conflicting gradient directions; and a nonlinear dynamic weighting mechanism leverages the GCR to enable gradient-direction-aware density control. Specifically, GDAGS prioritizes conflicting-gradient Gaussians during splitting operations to enhance geometric details while suppressing redundant concordant-direction Gaussians. Conversely, in cloning processes, GDAGS promotes concordant-direction Gaussian densification for structural completion while preventing conflicting-direction Gaussian overpopula...

---

## 64. 3DGS-VBench: A Comprehensive Video Quality Evaluation Benchmark for 3DGS Compression

- **作者**: Yuke Xing, William Gordon, Qi Yang et al.
- **发布时间**: 2025-08-09
- **arXiv链接**: [arXiv:2508.07038v1](https://arxiv.org/abs/2508.07038v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis with high visual fidelity, but its substantial storage requirements hinder practical deployment, prompting state-of-the-art (SOTA) 3DGS methods to incorporate compression modules. However, these 3DGS generative compression techniques introduce unique distortions lacking systematic quality assessment research. To this end, we establish 3DGS-VBench, a large-scale Video Quality Assessment (VQA) Dataset and Benchmark with 660 compressed 3DGS models and video sequences generated from 11 scenes across 6 SOTA 3DGS compression algorithms with systematically designed parameter levels. With annotations from 50 participants, we obtained MOS scores with outlier removal and validated dataset reliability. We benchmark 6 3DGS compression algorithms on storage efficiency and visual quality, and evaluate 15 quality assessment metrics across multiple paradigms. Our work enables specialized VQA model training for 3DGS, serving as a catalyst for compression and quality assessment research. The dataset is available at https://github.com/YukeXing/3DGS-VBench.

---

## 65. UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian Splatting

- **作者**: Wenpeng Xing, Jie Chen, Zaifeng Yang et al.
- **发布时间**: 2025-08-08
- **arXiv链接**: [arXiv:2508.06169v1](https://arxiv.org/abs/2508.06169v1)
- **英文摘要**: Underwater 3D scene reconstruction faces severe challenges from light absorption, scattering, and turbidity, which degrade geometry and color fidelity in traditional methods like Neural Radiance Fields (NeRF). While NeRF extensions such as SeaThru-NeRF incorporate physics-based models, their MLP reliance limits efficiency and spatial resolution in hazy environments. We introduce UW-3DGS, a novel framework adapting 3D Gaussian Splatting (3DGS) for robust underwater reconstruction. Key innovations include: (1) a plug-and-play learnable underwater image formation module using voxel-based regression for spatially varying attenuation and backscatter; and (2) a Physics-Aware Uncertainty Pruning (PAUP) branch that adaptively removes noisy floating Gaussians via uncertainty scoring, ensuring artifact-free geometry. The pipeline operates in training and rendering stages. During training, noisy Gaussians are optimized end-to-end with underwater parameters, guided by PAUP pruning and scattering modeling. In rendering, refined Gaussians produce clean Unattenuated Radiance Images (URIs) free from media effects, while learned physics enable realistic Underwater Images (UWIs) with accurate light transport. Experiments on SeaThru-NeRF and UWBundle datasets show superior performance, achieving PSNR of 27.604, SSIM of 0.868, and LPIPS of 0.104 on SeaThru-NeRF, with ~65% reduction in floating artifacts.

---

## 66. Refining Gaussian Splatting: A Volumetric Densification Approach

- **作者**: Mohamed Abdul Gafoor, Marius Preda, Titus Zaharia
- **发布时间**: 2025-08-07
- **arXiv链接**: [arXiv:2508.05187v1](https://arxiv.org/abs/2508.05187v1)
- **英文摘要**: Achieving high-quality novel view synthesis in 3D Gaussian Splatting (3DGS) often depends on effective point primitive management. The underlying Adaptive Density Control (ADC) process addresses this issue by automating densification and pruning. Yet, the vanilla 3DGS densification strategy shows key shortcomings. To address this issue, in this paper we introduce a novel density control method, which exploits the volumes of inertia associated to each Gaussian function to guide the refinement process. Furthermore, we study the effect of both traditional Structure from Motion (SfM) and Deep Image Matching (DIM) methods for point cloud initialization. Extensive experimental evaluations on the Mip-NeRF 360 dataset demonstrate that our approach surpasses 3DGS in reconstruction quality, delivering encouraging performance across diverse scenes.

---

## 67. Perceive-Sample-Compress: Towards Real-Time 3D Gaussian Splatting

- **作者**: Zijian Wang, Beizhen Zhao, Hao Wang
- **发布时间**: 2025-08-07
- **arXiv链接**: [arXiv:2508.04965v1](https://arxiv.org/abs/2508.04965v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated remarkable capabilities in real-time and photorealistic novel view synthesis. However, traditional 3DGS representations often struggle with large-scale scene management and efficient storage, particularly when dealing with complex environments or limited computational resources. To address these limitations, we introduce a novel perceive-sample-compress framework for 3D Gaussian Splatting. Specifically, we propose a scene perception compensation algorithm that intelligently refines Gaussian parameters at each level. This algorithm intelligently prioritizes visual importance for higher fidelity rendering in critical areas, while optimizing resource usage and improving overall visible quality. Furthermore, we propose a pyramid sampling representation to manage Gaussian primitives across hierarchical levels. Finally, to facilitate efficient storage of proposed hierarchical pyramid representations, we develop a Generalized Gaussian Mixed model compression algorithm to achieve significant compression ratios without sacrificing visual fidelity. The extensive experiments demonstrate that our method significantly improves memory efficiency and high visual quality while maintaining real-time rendering speed.

---

## 68. CryoSplat: Gaussian Splatting for Cryo-EM Homogeneous Reconstruction

- **作者**: Suyi Chen, Haibin Ling
- **发布时间**: 2025-08-06
- **arXiv链接**: [arXiv:2508.04929v3](https://arxiv.org/abs/2508.04929v3)
- **英文摘要**: As a critical modality for structural biology, cryogenic electron microscopy (cryo-EM) facilitates the determination of macromolecular structures at near-atomic resolution. The core computational task in single-particle cryo-EM is to reconstruct the 3D electrostatic potential of a molecule from noisy 2D projections acquired at unknown orientations. Gaussian mixture models (GMMs) provide a continuous, compact, and physically interpretable representation for molecular density and have recently gained interest in cryo-EM reconstruction. However, existing methods rely on external consensus maps or atomic models for initialization, limiting their use in self-contained pipelines. In parallel, differentiable rendering techniques such as Gaussian splatting have demonstrated remarkable scalability and efficiency for volumetric representations, suggesting a natural fit for GMM-based cryo-EM reconstruction. However, off-the-shelf Gaussian splatting methods are designed for photorealistic view synthesis and remain incompatible with cryo-EM due to mismatches in the image formation physics, reconstruction objectives, and coordinate systems. Addressing these issues, we propose cryoSplat, a GMM-based method that integrates Gaussian splatting with the physics of cryo-EM image formation. In particular, we develop an orthogonal projection-aware Gaussian splatting, with adaptations such as a view-dependent normalization term and FFT-aligned coordinate system tailored for cryo-EM imaging. These i...

---

## 69. SA-3DGS: A Self-Adaptive Compression Method for 3D Gaussian Splatting

- **作者**: Liheng Zhang, Weihao Yu, Zubo Lu, Haozhi Gu, Jin Huang
- **发布时间**: 2025-08-05
- **arXiv链接**: [arXiv:2508.03017v2](https://arxiv.org/abs/2508.03017v2)
- **说明**: This paper is being withdrawn as the work is incomplete and requires substantial additional development before it can be presented
- **英文摘要**: Recent advancements in 3D Gaussian Splatting have enhanced efficient and high-quality novel view synthesis. However, representing scenes requires a large number of Gaussian points, leading to high storage demands and limiting practical deployment. The latest methods facilitate the compression of Gaussian models but struggle to identify truly insignificant Gaussian points in the scene, leading to a decline in subsequent Gaussian pruning, compression quality, and rendering performance. To address this issue, we propose SA-3DGS, a method that significantly reduces storage costs while maintaining rendering quality. SA-3DGS learns an importance score to automatically identify the least significant Gaussians in scene reconstruction, thereby enabling effective pruning and redundancy reduction. Next, the importance-aware clustering module compresses Gaussians attributes more accurately into the codebook, improving the codebook's expressive capability while reducing model size. Finally, the codebook repair module leverages contextual scene information to repair the codebook, thereby recovering the original Gaussian point attributes and mitigating the degradation in rendering quality caused by information loss. Experimental results on several benchmark datasets show that our method achieves up to 66x compression while maintaining or even improving rendering quality. The proposed Gaussian pruning approach is not only adaptable to but also improves other pruning-based methods (e.g., Ligh...

---

## 70. AG$^2$aussian: Anchor-Graph Structured Gaussian Splatting for Instance-Level 3D Scene Understanding and Editing

- **作者**: Zhaonan Wang, Manyi Li, Changhe Tu
- **发布时间**: 2025-08-03
- **arXiv链接**: [arXiv:2508.01740v1](https://arxiv.org/abs/2508.01740v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has witnessed exponential adoption across diverse applications, driving a critical need for semantic-aware 3D Gaussian representations to enable scene understanding and editing tasks. Existing approaches typically attach semantic features to a collection of free Gaussians and distill the features via differentiable rendering, leading to noisy segmentation and a messy selection of Gaussians. In this paper, we introduce AG$^2$aussian, a novel framework that leverages an anchor-graph structure to organize semantic features and regulate Gaussian primitives. Our anchor-graph structure not only promotes compact and instance-aware Gaussian distributions, but also facilitates graph-based propagation, achieving a clean and accurate instance-level Gaussian selection. Extensive validation across four applications, i.e. interactive click-based query, open-vocabulary text-driven query, object removal editing, and physics simulation, demonstrates the advantages of our approach and its benefits to various applications. The experiments and ablation studies further evaluate the effectiveness of the key designs of our approach.

---

## 71. Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

- **作者**: Zhensheng Yuan, Haozhi Huang, Zhen Xiong, Di Wang, Guanghua Yang
- **发布时间**: 2025-07-30
- **arXiv链接**: [arXiv:2507.23006v1](https://arxiv.org/abs/2507.23006v1)
- **英文摘要**: We present a framework that enables fast reconstruction and real-time rendering of urban-scale scenes while maintaining robustness against appearance variations across multi-view captures. Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency. A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity. The appearance transformation module mitigates the negative effects of appearance inconsistencies across images while enabling flexible adjustments. Additionally, we utilize enhancement modules, such as depth regularization, scale regularization, and antialiasing, to improve reconstruction fidelity. Experimental results demonstrate that our method effectively reconstructs urban-scale scenes and outperforms previous approaches in both efficiency and quality. The source code is available at: https://yzslab.github.io/REUrbanGS.

---

## 72. GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections

- **作者**: Haiyang Bai, Jiaqi Zhu, Songru Jiang et al.
- **发布时间**: 2025-07-28
- **arXiv链接**: [arXiv:2507.20512v1](https://arxiv.org/abs/2507.20512v1)
- **英文摘要**: We propose a 3D Gaussian splatting-based framework for outdoor relighting that leverages intrinsic image decomposition to precisely integrate sunlight, sky radiance, and indirect lighting from unconstrained photo collections. Unlike prior methods that compress the per-image global illumination into a single latent vector, our approach enables simultaneously diverse shading manipulation and the generation of dynamic shadow effects. This is achieved through three key innovations: (1) a residual-based sun visibility extraction method to accurately separate direct sunlight effects, (2) a region-based supervision framework with a structural consistency loss for physically interpretable and coherent illumination decomposition, and (3) a ray-tracing-based technique for realistic shadow simulation. Extensive experiments demonstrate that our framework synthesizes novel views with competitive fidelity against state-of-the-art relighting solutions and produces more natural and multifaceted illumination and shadow effects.

---

## 73. Decomposing Densification in Gaussian Splatting for Faster 3D Scene Reconstruction

- **作者**: Binxiao Huang, Zhengwu Liu, Ngai Wong
- **发布时间**: 2025-07-27
- **arXiv链接**: [arXiv:2507.20239v1](https://arxiv.org/abs/2507.20239v1)
- **英文摘要**: 3D Gaussian Splatting (GS) has emerged as a powerful representation for high-quality scene reconstruction, offering compelling rendering quality. However, the training process of GS often suffers from slow convergence due to inefficient densification and suboptimal spatial distribution of Gaussian primitives. In this work, we present a comprehensive analysis of the split and clone operations during the densification phase, revealing their distinct roles in balancing detail preservation and computational efficiency. Building upon this analysis, we propose a global-to-local densification strategy, which facilitates more efficient growth of Gaussians across the scene space, promoting both global coverage and local refinement. To cooperate with the proposed densification strategy and promote sufficient diffusion of Gaussian primitives in space, we introduce an energy-guided coarse-to-fine multi-resolution training framework, which gradually increases resolution based on energy density in 2D images. Additionally, we dynamically prune unnecessary Gaussian primitives to speed up the training. Extensive experiments on MipNeRF-360, Deep Blending, and Tanks & Temples datasets demonstrate that our approach significantly accelerates training,achieving over 2x speedup with fewer Gaussian primitives and superior reconstruction performance.

---

## 74. Taking Language Embedded 3D Gaussian Splatting into the Wild

- **作者**: Yuze Wang, Yue Qi
- **发布时间**: 2025-07-26
- **arXiv链接**: [arXiv:2507.19830v2](https://arxiv.org/abs/2507.19830v2)
- **说明**: Visit our project page at https://yuzewang1998.github.io/takinglangsplatw/
- **英文摘要**: Recent advances in leveraging large-scale Internet photo collections for 3D reconstruction have enabled immersive virtual exploration of landmarks and historic sites worldwide. However, little attention has been given to the immersive understanding of architectural styles and structural knowledge, which remains largely confined to browsing static text-image pairs. Therefore, can we draw inspiration from 3D in-the-wild reconstruction techniques and use unconstrained photo collections to create an immersive approach for understanding the 3D structure of architectural components? To this end, we extend language embedded 3D Gaussian splatting (3DGS) and propose a novel framework for open-vocabulary scene understanding from unconstrained photo collections. Specifically, we first render multiple appearance images from the same viewpoint as the unconstrained image with the reconstructed radiance field, then extract multi-appearance CLIP features and two types of language feature uncertainty maps-transient and appearance uncertainty-derived from the multi-appearance features to guide the subsequent optimization process. Next, we propose a transient uncertainty-aware autoencoder, a multi-appearance language field 3DGS representation, and a post-ensemble strategy to effectively compress, learn, and fuse language features from multiple appearances. Finally, to quantitatively evaluate our method, we introduce PT-OVS, a new benchmark dataset for assessing open-vocabulary segmentation perf...

---

## 75. LongSplat: Online Generalizable 3D Gaussian Splatting from Long Sequence Images

- **作者**: Guichen Huang, Ruoyu Wang, Xiangjun Gao et al.
- **发布时间**: 2025-07-22
- **arXiv链接**: [arXiv:2507.16144v1](https://arxiv.org/abs/2507.16144v1)
- **英文摘要**: 3D Gaussian Splatting achieves high-fidelity novel view synthesis, but its application to online long-sequence scenarios is still limited. Existing methods either rely on slow per-scene optimization or fail to provide efficient incremental updates, hindering continuous performance. In this paper, we propose LongSplat, an online real-time 3D Gaussian reconstruction framework designed for long-sequence image input. The core idea is a streaming update mechanism that incrementally integrates current-view observations while selectively compressing redundant historical Gaussians. Crucial to this mechanism is our Gaussian-Image Representation (GIR), a representation that encodes 3D Gaussian parameters into a structured, image-like 2D format. GIR simultaneously enables efficient fusion of current-view and historical Gaussians and identity-aware redundancy compression. These functions enable online reconstruction and adapt the model to long sequences without overwhelming memory or computational costs. Furthermore, we leverage an existing image compression method to guide the generation of more compact and higher-quality 3D Gaussians. Extensive evaluations demonstrate that LongSplat achieves state-of-the-art efficiency-quality trade-offs in real-time novel view synthesis, delivering real-time reconstruction while reducing Gaussian counts by 44\% compared to existing per-pixel Gaussian prediction methods.

---

## 76. GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage Conditional Processing

- **作者**: Minnan Pei, Gang Li, Junwen Si et al.
- **发布时间**: 2025-07-21
- **arXiv链接**: [arXiv:2507.15300v3](https://arxiv.org/abs/2507.15300v3)
- **说明**: Accepted to MICRO 2025
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a leading neural rendering technique for high-fidelity view synthesis, prompting the development of dedicated 3DGS accelerators for resource-constrained platforms. The conventional decoupled preprocessing-rendering dataflow in existing accelerators has two major limitations: 1) a significant portion of preprocessed Gaussians are not used in rendering, and 2) the same Gaussian gets repeatedly loaded across different tile renderings, resulting in substantial computational and data movement overhead. To address these issues, we propose GCC, a novel accelerator designed for fast and energy-efficient 3DGS inference. GCC introduces a novel dataflow featuring: 1) \textit{cross-stage conditional processing}, which interleaves preprocessing and rendering to dynamically skip unnecessary Gaussian preprocessing; and 2) \textit{Gaussian-wise rendering}, ensuring that all rendering operations for a given Gaussian are completed before moving to the next, thereby eliminating duplicated Gaussian loading. We also propose an alpha-based boundary identification method to derive compact and accurate Gaussian regions, thereby reducing rendering costs. We implement our GCC accelerator in 28nm technology. Extensive experiments demonstrate that GCC significantly outperforms the state-of-the-art 3DGS inference accelerator, GSCore, in both performance and energy efficiency.

---

## 77. Adaptive 3D Gaussian Splatting Video Streaming

- **作者**: Han Gong, Qiyue Li, Zhi Liu et al.
- **发布时间**: 2025-07-19
- **arXiv链接**: [arXiv:2507.14432v1](https://arxiv.org/abs/2507.14432v1)
- **英文摘要**: The advent of 3D Gaussian splatting (3DGS) has significantly enhanced the quality of volumetric video representation. Meanwhile, in contrast to conventional volumetric video, 3DGS video poses significant challenges for streaming due to its substantially larger data volume and the heightened complexity involved in compression and transmission. To address these issues, we introduce an innovative framework for 3DGS volumetric video streaming. Specifically, we design a 3DGS video construction method based on the Gaussian deformation field. By employing hybrid saliency tiling and differentiated quality modeling of 3DGS video, we achieve efficient data compression and adaptation to bandwidth fluctuations while ensuring high transmission quality. Then we build a complete 3DGS video streaming system and validate the transmission performance. Through experimental evaluation, our method demonstrated superiority over existing approaches in various aspects, including video quality, compression effectiveness, and transmission rate.

---

## 78. A Mixed-Primitive-based Gaussian Splatting Method for Surface Reconstruction

- **作者**: Haoxuan Qu, Yujun Cai, Hossein Rahmani et al.
- **发布时间**: 2025-07-15
- **arXiv链接**: [arXiv:2507.11321v1](https://arxiv.org/abs/2507.11321v1)
- **英文摘要**: Recently, Gaussian Splatting (GS) has received a lot of attention in surface reconstruction. However, while 3D objects can be of complex and diverse shapes in the real world, existing GS-based methods only limitedly use a single type of splatting primitive (Gaussian ellipse or Gaussian ellipsoid) to represent object surfaces during their reconstruction. In this paper, we highlight that this can be insufficient for object surfaces to be represented in high quality. Thus, we propose a novel framework that, for the first time, enables Gaussian Splatting to incorporate multiple types of (geometrical) primitives during its surface reconstruction process. Specifically, in our framework, we first propose a compositional splatting strategy, enabling the splatting and rendering of different types of primitives in the Gaussian Splatting pipeline. In addition, we also design our framework with a mixed-primitive-based initialization strategy and a vertex pruning mechanism to further promote its surface representation learning process to be well executed leveraging different types of primitives. Extensive experiments show the efficacy of our framework and its accurate surface reconstruction performance.

---

## 79. SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene Reconstruction

- **作者**: Wei Yao, Shuzhao Xie, Letian Li et al.
- **发布时间**: 2025-07-10
- **arXiv链接**: [arXiv:2507.07465v1](https://arxiv.org/abs/2507.07465v1)
- **英文摘要**: Current 4D Gaussian frameworks for dynamic scene reconstruction deliver impressive visual fidelity and rendering speed, however, the inherent trade-off between storage costs and the ability to characterize complex physical motions significantly limits the practical application of these methods. To tackle these problems, we propose SD-GS, a compact and efficient dynamic Gaussian splatting framework for complex dynamic scene reconstruction, featuring two key contributions. First, we introduce a deformable anchor grid, a hierarchical and memory-efficient scene representation where each anchor point derives multiple 3D Gaussians in its local spatiotemporal region and serves as the geometric backbone of the 3D scene. Second, to enhance modeling capability for complex motions, we present a deformation-aware densification strategy that adaptively grows anchors in under-reconstructed high-dynamic regions while reducing redundancy in static areas, achieving superior visual quality with fewer anchors. Experimental results demonstrate that, compared to state-of-the-art methods, SD-GS achieves an average of 60\% reduction in model size and an average of 100\% improvement in FPS, significantly enhancing computational efficiency while maintaining or even surpassing visual quality.

---

## 80. LighthouseGS: Indoor Structure-aware 3D Gaussian Splatting for Panorama-Style Mobile Captures

- **作者**: Seungoh Han, Jaehoon Jang, Hyunsu Kim et al.
- **发布时间**: 2025-07-08
- **arXiv链接**: [arXiv:2507.06109v1](https://arxiv.org/abs/2507.06109v1)
- **说明**: Preprint
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) have enabled real-time novel view synthesis (NVS) with impressive quality in indoor scenes. However, achieving high-fidelity rendering requires meticulously captured images covering the entire scene, limiting accessibility for general users. We aim to develop a practical 3DGS-based NVS framework using simple panorama-style motion with a handheld camera (e.g., mobile device). While convenient, this rotation-dominant motion and narrow baseline make accurate camera pose and 3D point estimation challenging, especially in textureless indoor scenes. To address these challenges, we propose LighthouseGS, a novel framework inspired by the lighthouse-like sweeping motion of panoramic views. LighthouseGS leverages rough geometric priors, such as mobile device camera poses and monocular depth estimation, and utilizes the planar structures often found in indoor environments. We present a new initialization method called plane scaffold assembly to generate consistent 3D points on these structures, followed by a stable pruning strategy to enhance geometry and optimization stability. Additionally, we introduce geometric and photometric corrections to resolve inconsistencies from motion drift and auto-exposure in mobile devices. Tested on collected real and synthetic indoor scenes, LighthouseGS delivers photorealistic rendering, surpassing state-of-the-art methods and demonstrating the potential for panoramic view synthesis and object placement.

---

## 81. D-FCGS: Feedforward Compression of Dynamic Gaussian Splatting for Free-Viewpoint Videos

- **作者**: Wenkang Zhang, Yan Zhao, Qiang Wang et al.
- **发布时间**: 2025-07-08
- **arXiv链接**: [arXiv:2507.05859v4](https://arxiv.org/abs/2507.05859v4)
- **说明**: code:https://github.com/Mr-Zwkid/D-FCGS
- **英文摘要**: Free-Viewpoint Video (FVV) enables immersive 3D experiences, but efficient compression of dynamic 3D representation remains a major challenge. Existing dynamic 3D Gaussian Splatting methods couple reconstruction with optimization-dependent compression and customized motion formats, limiting generalization and standardization. To address this, we propose D-FCGS, a novel Feedforward Compression framework for Dynamic Gaussian Splatting. Key innovations include: (1) a standardized Group-of-Frames (GoF) structure with I-P coding, leveraging sparse control points to extract inter-frame motion tensors; (2) a dual prior-aware entropy model that fuses hyperprior and spatial-temporal priors for accurate rate estimation; (3) a control-point-guided motion compensation mechanism and refinement network to enhance view-consistent fidelity. Trained on Gaussian frames derived from multi-view videos, D-FCGS generalizes across diverse scenes in a zero-shot fashion. Experiments show that it matches the rate-distortion performance of optimization-based methods, achieving over 17 times compression compared to the baseline while preserving visual quality across viewpoints. This work advances feedforward compression of dynamic 3DGS, facilitating scalable FVV transmission and storage for immersive applications.

---

## 82. GaussianVLM: Scene-centric 3D Vision-Language Models using Language-aligned Gaussian Splats for Embodied Reasoning and Beyond

- **作者**: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool
- **发布时间**: 2025-07-01
- **arXiv链接**: [arXiv:2507.00886v1](https://arxiv.org/abs/2507.00886v1)
- **英文摘要**: As multimodal language models advance, their application to 3D scene understanding is a fast-growing frontier, driving the development of 3D Vision-Language Models (VLMs). Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility. To address these limitations, we propose a scene-centric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations. Our approach directly embeds rich linguistic features into the 3D scene representation by associating language with each Gaussian primitive, achieving early modality alignment. To process the resulting dense representations, we introduce a dual sparsifier that distills them into compact, task-relevant tokens via task-guided and location-guided pathways, producing sparse, task-aware global and local scene tokens. Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM five folds, in out-of-the-domain settings.

---

## 83. LOD-GS: Level-of-Detail-Sensitive 3D Gaussian Splatting for Detail Conserved Anti-Aliasing

- **作者**: Zhenya Yang, Bingchen Gong, Kai Chen
- **发布时间**: 2025-07-01
- **arXiv链接**: [arXiv:2507.00554v3](https://arxiv.org/abs/2507.00554v3)
- **英文摘要**: Despite the advancements in quality and efficiency achieved by 3D Gaussian Splatting (3DGS) in 3D scene rendering, aliasing artifacts remain a persistent challenge. Existing approaches primarily rely on low-pass filtering to mitigate aliasing. However, these methods are not sensitive to the sampling rate, often resulting in under-filtering and over-smoothing renderings. To address this limitation, we propose LOD-GS, a Level-of-Detail-sensitive filtering framework for Gaussian Splatting, which dynamically predicts the optimal filtering strength for each 3D Gaussian primitive. Specifically, we introduce a set of basis functions to each Gaussian, which take the sampling rate as input to model appearance variations, enabling sampling-rate-sensitive filtering. These basis function parameters are jointly optimized with the 3D Gaussian in an end-to-end manner. The sampling rate is influenced by both focal length and camera distance. However, existing methods and datasets rely solely on down-sampling to simulate focal length changes for anti-aliasing evaluation, overlooking the impact of camera distance. To enable a more comprehensive assessment, we introduce a new synthetic dataset featuring objects rendered at varying camera distances. Extensive experiments on both public datasets and our newly collected dataset demonstrate that our method achieves SOTA rendering quality while effectively eliminating aliasing. The code and dataset have been open-sourced.

---

## 84. Confident Splatting: Confidence-Based Compression of 3D Gaussian Splatting via Learnable Beta Distributions

- **作者**: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei
- **发布时间**: 2025-06-28
- **arXiv链接**: [arXiv:2506.22973v1](https://arxiv.org/abs/2506.22973v1)
- **英文摘要**: 3D Gaussian Splatting enables high-quality real-time rendering but often produces millions of splats, resulting in excessive storage and computational overhead. We propose a novel lossy compression method based on learnable confidence scores modeled as Beta distributions. Each splat's confidence is optimized through reconstruction-aware losses, enabling pruning of low-confidence splats while preserving visual fidelity. The proposed approach is architecture-agnostic and can be applied to any Gaussian Splatting variant. In addition, the average confidence values serve as a new metric to assess the quality of the scene. Extensive experiments demonstrate favorable trade-offs between compression and fidelity compared to prior work. Our code and data are publicly available at https://github.com/amirhossein-razlighi/Confident-Splatting

---

## 85. Part Segmentation and Motion Estimation for Articulated Objects with Dynamic 3D Gaussians

- **作者**: Jun-Jee Chao, Qingyuan Jiang, Volkan Isler
- **发布时间**: 2025-06-28
- **arXiv链接**: [arXiv:2506.22718v2](https://arxiv.org/abs/2506.22718v2)
- **英文摘要**: Part segmentation and motion estimation are two fundamental problems for articulated object motion analysis. In this paper, we present a method to solve these two problems jointly from a sequence of observed point clouds of a single articulated object. The main challenge in our problem setting is that the point clouds are not assumed to be generated by a fixed set of moving points. Instead, each point cloud in the sequence could be an arbitrary sampling of the object surface at that particular time step. Such scenarios occur when the object undergoes major occlusions, or if the dataset is collected using measurements from multiple sensors asynchronously. In these scenarios, methods that rely on tracking point correspondences are not appropriate. We present an alternative approach based on a compact but effective representation where we represent the object as a collection of simple building blocks modeled as 3D Gaussians. We parameterize the Gaussians with time-dependent rotations, translations, and scales that are shared across all time steps. With our representation, part segmentation can be achieved by building correspondences between the observed points and the Gaussians. Moreover, the transformation of each point across time can be obtained by following the poses of the assigned Gaussian (even when the point is not observed). Experiments show that our method outperforms existing methods that solely rely on finding point correspondences. Additionally, we extend existing d...

---

## 86. 3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting

- **作者**: Yuke Xing, Jiarui Wang, Peizhi Niu et al.
- **发布时间**: 2025-06-17
- **arXiv链接**: [arXiv:2506.14642v2](https://arxiv.org/abs/2506.14642v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a promising approach for novel view synthesis, offering real-time rendering with high visual fidelity. However, its substantial storage requirements present significant challenges for practical applications. While recent state-of-the-art (SOTA) 3DGS methods increasingly incorporate dedicated compression modules, there is a lack of a comprehensive framework to evaluate their perceptual impact. Therefore we present 3DGS-IEval-15K, the first large-scale image quality assessment (IQA) dataset specifically designed for compressed 3DGS representations. Our dataset encompasses 15,200 images rendered from 10 real-world scenes through 6 representative 3DGS algorithms at 20 strategically selected viewpoints, with different compression levels leading to various distortion effects. Through controlled subjective experiments, we collect human perception data from 60 viewers. We validate dataset quality through scene diversity and MOS distribution analysis, and establish a comprehensive benchmark with 30 representative IQA metrics covering diverse types. As the largest-scale 3DGS quality assessment dataset to date, our work provides a foundation for developing 3DGS specialized IQA metrics, and offers essential data for investigating view-dependent quality distribution patterns unique to 3DGS. The database is publicly available at https://github.com/YukeXing/3DGS-IEval-15K.

---

## 87. HRGS: Hierarchical Gaussian Splatting for Memory-Efficient High-Resolution 3D Reconstruction

- **作者**: Changbai Li, Haodong Zhu, Hanlin Chen et al.
- **发布时间**: 2025-06-17
- **arXiv链接**: [arXiv:2506.14229v1](https://arxiv.org/abs/2506.14229v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has made significant strides in real-time 3D scene reconstruction, but faces memory scalability issues in high-resolution scenarios. To address this, we propose Hierarchical Gaussian Splatting (HRGS), a memory-efficient framework with hierarchical block-level optimization. First, we generate a global, coarse Gaussian representation from low-resolution data. Then, we partition the scene into multiple blocks, refining each block with high-resolution data. The partitioning involves two steps: Gaussian partitioning, where irregular scenes are normalized into a bounded cubic space with a uniform grid for task distribution, and training data partitioning, where only relevant observations are retained for each block. By guiding block refinement with the coarse Gaussian prior, we ensure seamless Gaussian fusion across adjacent blocks. To reduce computational demands, we introduce Importance-Driven Gaussian Pruning (IDGP), which computes importance scores for each Gaussian and removes those with minimal contribution, speeding up convergence and reducing memory usage. Additionally, we incorporate normal priors from a pretrained model to enhance surface reconstruction quality. Our method enables high-quality, high-resolution 3D scene reconstruction even under memory constraints. Extensive experiments on three benchmarks show that HRGS achieves state-of-the-art performance in high-resolution novel view synthesis (NVS) and surface reconstruction tasks.

---

## 88. Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting

- **作者**: Mufan Liu, Cixiao Zhang, Qi Yang et al.
- **发布时间**: 2025-06-15
- **arXiv链接**: [arXiv:2506.12787v3](https://arxiv.org/abs/2506.12787v3)
- **英文摘要**: Modeling the wireless radiance field (WRF) is fundamental to modern communication systems, enabling key tasks such as localization, sensing, and channel estimation. Traditional approaches, which rely on empirical formulas or physical simulations, often suffer from limited accuracy or require strong scene priors. Recent neural radiance field (NeRF-based) methods improve reconstruction fidelity through differentiable volumetric rendering, but their reliance on computationally expensive multilayer perceptron (MLP) queries hinders real-time deployment. To overcome these challenges, we introduce Gaussian splatting (GS) to the wireless domain, leveraging its efficiency in modeling optical radiance fields to enable compact and accurate WRF reconstruction. Specifically, we propose SwiftWRF, a deformable 2D Gaussian splatting framework that synthesizes WRF spectra at arbitrary positions under single-sided transceiver mobility. SwiftWRF employs CUDA-accelerated rasterization to render spectra at over 100000 fps and uses a lightweight MLP to model the deformation of 2D Gaussians, effectively capturing mobility-induced WRF variations. In addition to novel spectrum synthesis, the efficacy of SwiftWRF is further underscored in its applications in angle-of-arrival (AoA) and received signal strength indicator (RSSI) prediction. Experiments conducted on both real-world and synthetic indoor scenes demonstrate that SwiftWRF can reconstruct WRF spectra up to 500x faster than existing state-of-th...

---

## 89. GraphGSOcc: Semantic-Geometric Graph Transformer with Dynamic-Static Decoupling for 3D Gaussian Splatting-based Occupancy Prediction

- **作者**: Ke Song, Yunhe Wu, Chunchit Siu, Huiyuan Xiong
- **发布时间**: 2025-06-13
- **arXiv链接**: [arXiv:2506.14825v2](https://arxiv.org/abs/2506.14825v2)
- **英文摘要**: Addressing the task of 3D semantic occupancy prediction for autonomous driving, we tackle two key issues in existing 3D Gaussian Splatting (3DGS) methods: (1) unified feature aggregation neglecting semantic correlations among similar categories and across regions, (2) boundary ambiguities caused by the lack of geometric constraints in MLP iterative optimization and (3) biased issues in dynamic-static object coupling optimization. We propose the GraphGSOcc model, a novel framework that combines semantic and geometric graph Transformer and decouples dynamic-static objects optimization for 3D Gaussian Splatting-based Occupancy Prediction. We propose the Dual Gaussians Graph Attenntion, which dynamically constructs dual graph structures: a geometric graph adaptively calculating KNN search radii based on Gaussian poses, enabling large-scale Gaussians to aggregate features from broader neighborhoods while compact Gaussians focus on local geometric consistency; a semantic graph retaining top-M highly correlated nodes via cosine similarity to explicitly encode semantic relationships within and across instances. Coupled with the Multi-scale Graph Attention framework, fine-grained attention at lower layers optimizes boundary details, while coarsegrained attention at higher layers models object-level topology. On the other hand, we decouple dynamic and static objects by leveraging semantic probability distributions and design a Dynamic-Static Decoupled Gaussian Attention mechanism to op...

---

## 90. DynaSplat: Dynamic-Static Gaussian Splatting with Hierarchical Motion Decomposition for Scene Reconstruction

- **作者**: Junli Deng, Ping Shi, Qipei Li, Jinyang Guo
- **发布时间**: 2025-06-11
- **arXiv链接**: [arXiv:2506.09836v1](https://arxiv.org/abs/2506.09836v1)
- **英文摘要**: Reconstructing intricate, ever-changing environments remains a central ambition in computer vision, yet existing solutions often crumble before the complexity of real-world dynamics. We present DynaSplat, an approach that extends Gaussian Splatting to dynamic scenes by integrating dynamic-static separation and hierarchical motion modeling. First, we classify scene elements as static or dynamic through a novel fusion of deformation offset statistics and 2D motion flow consistency, refining our spatial representation to focus precisely where motion matters. We then introduce a hierarchical motion modeling strategy that captures both coarse global transformations and fine-grained local movements, enabling accurate handling of intricate, non-rigid motions. Finally, we integrate physically-based opacity estimation to ensure visually coherent reconstructions, even under challenging occlusions and perspective shifts. Extensive experiments on challenging datasets reveal that DynaSplat not only surpasses state-of-the-art alternatives in accuracy and realism but also provides a more intuitive, compact, and efficient route to dynamic scene reconstruction.

---

## 91. Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation

- **作者**: Haowen Wang, Xiaoping Yuan, Zhao Jin et al.
- **发布时间**: 2025-06-11
- **arXiv链接**: [arXiv:2506.09663v1](https://arxiv.org/abs/2506.09663v1)
- **英文摘要**: Articulated objects are ubiquitous in everyday life, and accurate 3D representations of their geometry and motion are critical for numerous applications. However, in the absence of human annotation, existing approaches still struggle to build a unified representation for objects that contain multiple movable parts. We introduce DeGSS, a unified framework that encodes articulated objects as deformable 3D Gaussian fields, embedding geometry, appearance, and motion in one compact representation. Each interaction state is modeled as a smooth deformation of a shared field, and the resulting deformation trajectories guide a progressive coarse-to-fine part segmentation that identifies distinct rigid components, all in an unsupervised manner. The refined field provides a spatially continuous, fully decoupled description of every part, supporting part-level reconstruction and precise modeling of their kinematic relationships. To evaluate generalization and realism, we enlarge the synthetic PartNet-Mobility benchmark and release RS-Art, a real-to-sim dataset that pairs RGB captures with accurately reverse-engineered 3D models. Extensive experiments demonstrate that our method outperforms existing methods in both accuracy and stability.

---

## 92. Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS

- **作者**: Tao Wang, Mengyu Li, Geduo Zeng, Cheng Meng, Qiong Zhang
- **发布时间**: 2025-06-11
- **arXiv链接**: [arXiv:2506.09534v2](https://arxiv.org/abs/2506.09534v2)
- **说明**: 26 pages, 15 figures
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for radiance field rendering, but it typically requires millions of redundant Gaussian primitives, overwhelming memory and rendering budgets. Existing compaction approaches address this by pruning Gaussians based on heuristic importance scores, without global fidelity guarantee. To bridge this gap, we propose a novel optimal transport perspective that casts 3DGS compaction as global Gaussian mixture reduction. Specifically, we first minimize the composite transport divergence over a KD-tree partition to produce a compact geometric representation, and then decouple appearance from geometry by fine-tuning color and opacity attributes with far fewer Gaussian primitives. Experiments on benchmark datasets show that our method (i) yields negligible loss in rendering quality (PSNR, SSIM, LPIPS) compared to vanilla 3DGS with only 10% Gaussians; and (ii) consistently outperforms state-of-the-art 3DGS compaction techniques. Notably, our method is applicable to any stage of vanilla or accelerated 3DGS pipelines, providing an efficient and agnostic pathway to lightweight neural rendering. The code is publicly available at https://github.com/DrunkenPoet/GHAP

---

## 93. TinySplat: Feedforward Approach for Generating Compact 3D Scene Representation

- **作者**: Zetian Song, Jiaye Fu, Jiaqi Zhang et al.
- **发布时间**: 2025-06-11
- **arXiv链接**: [arXiv:2506.09479v1](https://arxiv.org/abs/2506.09479v1)
- **英文摘要**: The recent development of feedforward 3D Gaussian Splatting (3DGS) presents a new paradigm to reconstruct 3D scenes. Using neural networks trained on large-scale multi-view datasets, it can directly infer 3DGS representations from sparse input views. Although the feedforward approach achieves high reconstruction speed, it still suffers from the substantial storage cost of 3D Gaussians. Existing 3DGS compression methods relying on scene-wise optimization are not applicable due to architectural incompatibilities. To overcome this limitation, we propose TinySplat, a complete feedforward approach for generating compact 3D scene representations. Built upon standard feedforward 3DGS methods, TinySplat integrates a training-free compression framework that systematically eliminates key sources of redundancy. Specifically, we introduce View-Projection Transformation (VPT) to reduce geometric redundancy by projecting geometric parameters into a more compact space. We further present Visibility-Aware Basis Reduction (VABR), which mitigates perceptual redundancy by aligning feature energy along dominant viewing directions via basis transformation. Lastly, spatial redundancy is addressed through an off-the-shelf video codec. Comprehensive experimental results on multiple benchmark datasets demonstrate that TinySplat achieves over 100x compression for 3D Gaussian data generated by feedforward methods. Compared to the state-of-the-art compression approach, we achieve comparable quality with...

---

## 94. SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping

- **作者**: Allen Tu, Haiyang Ying, Alex Hanson et al.
- **发布时间**: 2025-06-09
- **arXiv链接**: [arXiv:2506.07917v3](https://arxiv.org/abs/2506.07917v3)
- **说明**: Project Page: https://speede3dgs.github.io/
- **英文摘要**: Dynamic extensions of 3D Gaussian Splatting (3DGS) achieve high-quality reconstructions through neural motion fields, but per-Gaussian neural inference makes these models computationally expensive. Building on DeformableGS, we introduce Speedy Deformable 3D Gaussian Splatting (SpeeDe3DGS), which bridges this efficiency-fidelity gap through three complementary modules: Temporal Sensitivity Pruning (TSP) removes low-impact Gaussians via temporally aggregated sensitivity analysis, Temporal Sensitivity Sampling (TSS) perturbs timestamps to suppress floaters and improve temporal coherence, and GroupFlow distills the learned deformation field into shared SE(3) transformations for efficient groupwise motion. On the 50 dynamic scenes in MonoDyGauBench, integrating TSP and TSS into DeformableGS accelerates rendering by 6.78$\times$ on average while maintaining neural-field fidelity and using 10$\times$ fewer primitives. Adding GroupFlow culminates in 13.71$\times$ faster rendering and 2.53$\times$ shorter training, surpassing all baselines in speed while preserving superior image quality.

---

## 95. DSG-World: Learning a 3D Gaussian World Model from Dual State Videos

- **作者**: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang
- **发布时间**: 2025-06-05
- **arXiv链接**: [arXiv:2506.05217v1](https://arxiv.org/abs/2506.05217v1)
- **英文摘要**: Building an efficient and physically consistent world model from limited observations is a long standing challenge in vision and robotics. Many existing world modeling pipelines are based on implicit generative models, which are hard to train and often lack 3D or physical consistency. On the other hand, explicit 3D methods built from a single state often require multi-stage processing-such as segmentation, background completion, and inpainting-due to occlusions. To address this, we leverage two perturbed observations of the same scene under different object configurations. These dual states offer complementary visibility, alleviating occlusion issues during state transitions and enabling more stable and complete reconstruction. In this paper, we present DSG-World, a novel end-to-end framework that explicitly constructs a 3D Gaussian World model from Dual State observations. Our approach builds dual segmentation-aware Gaussian fields and enforces bidirectional photometric and semantic consistency. We further introduce a pseudo intermediate state for symmetric alignment and design collaborative co-pruning trategies to refine geometric completeness. DSG-World enables efficient real-to-simulation transfer purely in the explicit Gaussian representation space, supporting high-fidelity rendering and object-level scene manipulation without relying on dense observations or multi-stage pipelines. Extensive experiments demonstrate strong generalization to novel views and scene states, h...

---

## 96. Multi-Spectral Gaussian Splatting with Neural Color Representation

- **作者**: Lukas Meyer, Josef Grün, Maximilian Weiherer et al.
- **发布时间**: 2025-06-03
- **arXiv链接**: [arXiv:2506.03407v1](https://arxiv.org/abs/2506.03407v1)
- **英文摘要**: We present MS-Splatting -- a multi-spectral 3D Gaussian Splatting (3DGS) framework that is able to generate multi-view consistent novel views from images of multiple, independent cameras with different spectral domains. In contrast to previous approaches, our method does not require cross-modal camera calibration and is versatile enough to model a variety of different spectra, including thermal and near-infra red, without any algorithmic changes.   Unlike existing 3DGS-based frameworks that treat each modality separately (by optimizing per-channel spherical harmonics) and therefore fail to exploit the underlying spectral and spatial correlations, our method leverages a novel neural color representation that encodes multi-spectral information into a learned, compact, per-splat feature embedding. A shallow multi-layer perceptron (MLP) then decodes this embedding to obtain spectral color values, enabling joint learning of all bands within a unified representation.   Our experiments show that this simple yet effective strategy is able to improve multi-spectral rendering quality, while also leading to improved per-spectra rendering quality over state-of-the-art methods. We demonstrate the effectiveness of this new technique in agricultural applications to render vegetation indices, such as normalized difference vegetation index (NDVI).

---

## 97. GSCodec Studio: A Modular Framework for Gaussian Splat Compression

- **作者**: Sicheng Li, Chengzhen Wu, Hao Li et al.
- **发布时间**: 2025-06-02
- **arXiv链接**: [arXiv:2506.01822v1](https://arxiv.org/abs/2506.01822v1)
- **说明**: Repository of the project: https://github.com/JasonLSC/GSCodec_Studio
- **英文摘要**: 3D Gaussian Splatting and its extension to 4D dynamic scenes enable photorealistic, real-time rendering from real-world captures, positioning Gaussian Splats (GS) as a promising format for next-generation immersive media. However, their high storage requirements pose significant challenges for practical use in sharing, transmission, and storage. Despite various studies exploring GS compression from different perspectives, these efforts remain scattered across separate repositories, complicating benchmarking and the integration of best practices. To address this gap, we present GSCodec Studio, a unified and modular framework for GS reconstruction, compression, and rendering. The framework incorporates a diverse set of 3D/4D GS reconstruction methods and GS compression techniques as modular components, facilitating flexible combinations and comprehensive comparisons. By integrating best practices from community research and our own explorations, GSCodec Studio supports the development of compact representation and compression solutions for static and dynamic Gaussian Splats, namely our Static and Dynamic GSCodec, achieving competitive rate-distortion performance in static and dynamic GS compression. The code for our framework is publicly available at https://github.com/JasonLSC/GSCodec_Studio , to advance the research on Gaussian Splats compression.

---

## 98. CountingFruit: Language-Guided 3D Fruit Counting with Semantic Gaussian Splatting

- **作者**: Fengze Li, Yangle Liu, Jieming Ma et al.
- **发布时间**: 2025-06-01
- **arXiv链接**: [arXiv:2506.01109v3](https://arxiv.org/abs/2506.01109v3)
- **英文摘要**: Accurate 3D fruit counting in orchards is challenging due to heavy occlusion, semantic ambiguity between fruits and surrounding structures, and the high computational cost of volumetric reconstruction. Existing pipelines often rely on multi-view 2D segmentation and dense volumetric sampling, which lead to accumulated fusion errors and slow inference. We introduce FruitLangGS, a language-guided 3D fruit counting framework that reconstructs orchard-scale scenes using an adaptive-density Gaussian Splatting pipeline with radius-aware pruning and tile-based rasterization, enabling scalable 3D representation. During inference, compressed CLIP-aligned semantic vectors embedded in each Gaussian are filtered via a dual-threshold cosine similarity mechanism, retrieving Gaussians relevant to target prompts while suppressing common distractors (e.g., foliage), without requiring retraining or image-space masks. The selected Gaussians are then sampled into dense point clouds and clustered geometrically to estimate fruit instances, remaining robust under severe occlusion and viewpoint variation. Experiments on nine different orchard-scale datasets demonstrate that FruitLangGS consistently outperforms existing pipelines in instance counting recall, avoiding multi-view segmentation fusion errors and achieving up to 99.7% recall on Pfuji-Size_Orch2018 orchard dataset. Ablation studies further confirm that language-conditioned semantic embedding and dual-threshold prompt filtering are essential...

---

## 99. Adaptive Voxelization for Transform coding of 3D Gaussian splatting data

- **作者**: Chenjunjie Wang, Shashank N. Sridhara, Eduardo Pavez, Antonio Ortega, Cheng Chang
- **发布时间**: 2025-05-30
- **arXiv链接**: [arXiv:2506.00271v1](https://arxiv.org/abs/2506.00271v1)
- **英文摘要**: We present a novel compression framework for 3D Gaussian splatting (3DGS) data that leverages transform coding tools originally developed for point clouds. Contrary to existing 3DGS compression methods, our approach can produce compressed 3DGS models at multiple bitrates in a computationally efficient way. Point cloud voxelization is a discretization technique that point cloud codecs use to improve coding efficiency while enabling the use of fast transform coding algorithms. We propose an adaptive voxelization algorithm tailored to 3DGS data, to avoid the inefficiencies introduced by uniform voxelization used in point cloud codecs. We ensure the positions of larger volume Gaussians are represented at high resolution, as these significantly impact rendering quality. Meanwhile, a low-resolution representation is used for dense regions with smaller Gaussians, which have a relatively lower impact on rendering quality. This adaptive voxelization approach significantly reduces the number of Gaussians and the bitrate required to encode the 3DGS data. After voxelization, many Gaussians are moved or eliminated. Thus, we propose to fine-tune/recolor the remaining 3DGS attributes with an initialization that can reduce the amount of retraining required. Experimental results on pre-trained datasets show that our proposed compression framework outperforms existing methods.

---

## 100. TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores

- **作者**: Zimu Liao, Jifeng Ding, Siwei Cui et al.
- **发布时间**: 2025-05-30
- **arXiv链接**: [arXiv:2505.24796v2](https://arxiv.org/abs/2505.24796v2)
- **说明**: 15 pages, 6 figures
- **英文摘要**: 3D Gaussian Splatting (3DGS) renders pixels by rasterizing Gaussian primitives, where conditional alpha-blending dominates the computational cost in the rendering pipeline. This paper proposes TC-GS, an algorithm-independent universal module that expands the applicability of Tensor Core (TCU) for 3DGS, leading to substantial speedups and seamless integration into existing 3DGS optimization frameworks. The key innovation lies in mapping alpha computation to matrix multiplication, fully utilizing otherwise idle TCUs in existing 3DGS implementations. TC-GS provides plug-and-play acceleration for existing top-tier acceleration algorithms and integrates seamlessly with rendering pipeline designs, such as Gaussian compression and redundancy elimination algorithms. Additionally, we introduce a global-to-local coordinate transformation to mitigate rounding errors from quadratic terms of pixel coordinates caused by Tensor Core half-precision computation. Extensive experiments demonstrate that our method maintains rendering quality while providing an additional 2.18x speedup over existing Gaussian acceleration algorithms, thereby achieving a total acceleration of up to 5.6x.

---

## 101. Learning Hierarchical Sparse Transform Coding for 3DGS Compression

- **作者**: Hao Xu, Xiaolin Wu, Xi Zhang
- **发布时间**: 2025-05-28
- **arXiv链接**: [arXiv:2505.22908v3](https://arxiv.org/abs/2505.22908v3)
- **说明**: Our code will be released at \href{https://github.com/hxu160/SHTC_for_3DGS_compression}{here}
- **英文摘要**: Current 3DGS compression methods largely forego the neural analysis-synthesis transform, which is a crucial component in learned signal compression systems. As a result, redundancy removal is left solely to the entropy coder, overburdening the entropy coding module and reducing rate-distortion (R-D) performance. To fix this critical omission, we propose a training-time transform coding (TTC) method that adds the analysis-synthesis transform and optimizes it jointly with the 3DGS representation and entropy model. Concretely, we adopt a hierarchical design: a channel-wise KLT for decorrelation and energy compaction, followed by a sparsity-aware neural transform that reconstructs the KLT residuals with minimal parameter and computational overhead. Experiments show that our method delivers strong R-D performance with fast decoding, offering a favorable BD-rate-decoding-time trade-off over SOTA 3DGS compressors.

---

## 102. HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes

- **作者**: Changjian Jiang, Kerui Ren, Linning Xu et al.
- **发布时间**: 2025-05-26
- **arXiv链接**: [arXiv:2505.20267v1](https://arxiv.org/abs/2505.20267v1)
- **英文摘要**: High fidelity 3D reconstruction and rendering hinge on capturing precise geometry while preserving photo realistic detail. Most existing methods either fuse these goals into a single cumbersome model or adopt hybrid schemes whose uniform primitives lead to a trade off between efficiency and fidelity. In this paper, we introduce HaloGS, a dual representation that loosely couples coarse triangles for geometry with Gaussian primitives for appearance, motivated by the lightweight classic geometry representations and their proven efficiency in real world applications. Our design yields a compact yet expressive model capable of photo realistic rendering across both indoor and outdoor environments, seamlessly adapting to varying levels of scene complexity. Experiments on multiple benchmark datasets demonstrate that our method yields both compact, accurate geometry and high fidelity renderings, especially in challenging scenarios where robust geometric structure make a clear difference.

---

## 103. VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes

- **作者**: Tianchen Deng, Wenhua Wu, Junjie He et al.
- **发布时间**: 2025-05-25
- **arXiv链接**: [arXiv:2505.18992v2](https://arxiv.org/abs/2505.18992v2)
- **英文摘要**: 3D Gaussian Splatting has recently shown promising results in dense visual SLAM. However, existing 3DGS-based SLAM methods are all constrained to small-room scenarios and struggle with memory explosion in large-scale scenes and long sequences. To this end, we propose VPGS-SLAM, the first 3DGS-based large-scale RGBD SLAM framework for both indoor and outdoor scenarios. We design a novel voxel-based progressive 3D Gaussian mapping method with multiple submaps for compact and accurate scene representation in large-scale and long-sequence scenes. This allows us to scale up to arbitrary scenes and improves robustness (even under pose drifts). In addition, we propose a 2D-3D fusion camera tracking method to achieve robust and accurate camera tracking in both indoor and outdoor large-scale scenes. Furthermore, we design a 2D-3D Gaussian loop closure method to eliminate pose drift. We further propose a submap fusion method with online distillation to achieve global consistency in large-scale scenes when detecting a loop. Experiments on various indoor and outdoor datasets demonstrate the superiority and generalizability of the proposed framework. The code will be open source on https://github.com/dtc111111/vpgs-slam.

---

## 104. SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes

- **作者**: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang
- **发布时间**: 2025-05-23
- **arXiv链接**: [arXiv:2505.17951v4](https://arxiv.org/abs/2505.17951v4)
- **英文摘要**: We present SplatCo, a structure-view collaborative Gaussian splatting framework for high-fidelity rendering of complex outdoor scenes. SplatCo builds upon three novel components: 1) a cross-structure collaboration module that combines global tri-plane representations, which capture coarse scene layouts, with local context grid features representing fine details. This fusion is achieved through a hierarchical compensation mechanism, ensuring both global spatial awareness and local detail preservation; 2) a cross-view pruning mechanism that removes overfitted or inaccurate Gaussians based on structural consistency, thereby improving storage efficiency and preventing rendering artifacts; 3) a structure view co-learning module that aggregates structural gradients with view gradients,thereby steering the optimization of Gaussian geometric and appearance attributes more robustly. By combining these key components, SplatCo effectively achieves high-fidelity rendering for large-scale scenes. Code and project page are available at https://splatco-tech.github.io.

---

## 105. R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections

- **作者**: Xu yan, Zhaohui Wang, Rong Wei et al.
- **发布时间**: 2025-05-21
- **arXiv链接**: [arXiv:2505.15294v1](https://arxiv.org/abs/2505.15294v1)
- **说明**: 7 pages, 4 figures
- **英文摘要**: We propose R3GS, a robust reconstruction and relocalization framework tailored for unconstrained datasets. Our method uses a hybrid representation during training. Each anchor combines a global feature from a convolutional neural network (CNN) with a local feature encoded by the multiresolution hash grids [2]. Subsequently, several shallow multi-layer perceptrons (MLPs) predict the attributes of each Gaussians, including color, opacity, and covariance. To mitigate the adverse effects of transient objects on the reconstruction process, we ffne-tune a lightweight human detection network. Once ffne-tuned, this network generates a visibility map that efffciently generalizes to other transient objects (such as posters, banners, and cars) with minimal need for further adaptation. Additionally, to address the challenges posed by sky regions in outdoor scenes, we propose an effective sky-handling technique that incorporates a depth prior as a constraint. This allows the inffnitely distant sky to be represented on the surface of a large-radius sky sphere, signiffcantly reducing ffoaters caused by errors in sky reconstruction. Furthermore, we introduce a novel relocalization method that remains robust to changes in lighting conditions while estimating the camera pose of a given image within the reconstructed 3DGS scene. As a result, R3GS significantly enhances rendering ffdelity, improves both training and rendering efffciency, and reduces storage requirements. Our method achieves stat...

---

## 106. A Novel Benchmark and Dataset for Efficient 3D Gaussian Splatting with Gaussian Point Cloud Compression

- **作者**: Kangli Wang, Shihao Li, Qianxi Yi, Wei Gao
- **发布时间**: 2025-05-21
- **arXiv链接**: [arXiv:2505.18197v1](https://arxiv.org/abs/2505.18197v1)
- **说明**: 22 pages, 13 figures
- **英文摘要**: Recently, immersive media and autonomous driving applications have significantly advanced through 3D Gaussian Splatting (3DGS), which offers high-fidelity rendering and computational efficiency. Despite these advantages, 3DGS as a display-oriented representation requires substantial storage due to its numerous Gaussian attributes. Current compression methods have shown promising results but typically neglect the compression of Gaussian spatial positions, creating unnecessary bitstream overhead. We conceptualize Gaussian primitives as point clouds and propose leveraging point cloud compression techniques for more effective storage. AI-based point cloud compression demonstrates superior performance and faster inference compared to MPEG Geometry-based Point Cloud Compression (G-PCC). However, direct application of existing models to Gaussian compression may yield suboptimal results, as Gaussian point clouds tend to exhibit globally sparse yet locally dense geometric distributions that differ from conventional point cloud characteristics. To address these challenges, we introduce GausPcgc for Gaussian point cloud geometry compression along with a specialized training dataset GausPcc-1K. Our work pioneers the integration of AI-based point cloud compression into Gaussian compression pipelines, achieving superior compression ratios. The framework complements existing Gaussian compression methods while delivering significant performance improvements. All code, data, and pre-trained m...

---

## 107. EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes

- **作者**: Jianlin Guo, Haihong Xiao, Wenxiong Kang
- **发布时间**: 2025-05-16
- **arXiv链接**: [arXiv:2505.10787v1](https://arxiv.org/abs/2505.10787v1)
- **英文摘要**: Efficient scene representations are essential for many real-world applications, especially those involving spatial measurement. Although current NeRF-based methods have achieved impressive results in reconstructing building-scale scenes, they still suffer from slow training and inference speeds due to time-consuming stochastic sampling. Recently, 3D Gaussian Splatting (3DGS) has demonstrated excellent performance with its high-quality rendering and real-time speed, especially for objects and small-scale scenes. However, in outdoor scenes, its point-based explicit representation lacks an effective adjustment mechanism, and the millions of Gaussian points required often lead to memory constraints during training. To address these challenges, we propose EA-3DGS, a high-quality real-time rendering method designed for outdoor scenes. First, we introduce a mesh structure to regulate the initialization of Gaussian components by leveraging an adaptive tetrahedral mesh that partitions the grid and initializes Gaussian components on each face, effectively capturing geometric structures in low-texture regions. Second, we propose an efficient Gaussian pruning strategy that evaluates each 3D Gaussian's contribution to the view and prunes accordingly. To retain geometry-critical Gaussian points, we also present a structure-aware densification strategy that densifies Gaussian points in low-curvature regions. Additionally, we employ vector quantization for parameter quantization of Gaussian ...

---

## 108. ControlGS: Consistent Structural Compression Control for Deployment-Aware Gaussian Splatting

- **作者**: Fengdi Zhang, Yibao Sun, Hongkun Cao, Ruqi Huang
- **发布时间**: 2025-05-15
- **arXiv链接**: [arXiv:2505.10473v3](https://arxiv.org/abs/2505.10473v3)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a highly deployable real-time method for novel view synthesis. In practice, it requires a universal, consistent control mechanism that adjusts the trade-off between rendering quality and model compression without scene-specific tuning, enabling automated deployment across different device performances and communication bandwidths. In this work, we present ControlGS, a control-oriented optimization framework that maps the trade-off between Gaussian count and rendering quality to a continuous, scene-agnostic, and highly responsive control axis. Extensive experiments across a wide range of scene scales and types (from small objects to large outdoor scenes) demonstrate that, by adjusting a globally unified control hyperparameter, ControlGS can flexibly generate models biased toward either structural compactness or high fidelity, regardless of the specific scene scale or complexity, while achieving markedly higher rendering quality with the same or fewer Gaussians compared to potential competing methods. Project page: https://zhang-fengdi.github.io/ControlGS/

---

## 109. Neural Video Compression using 2D Gaussian Splatting

- **作者**: Lakshya Gupta, Imran N. Junejo
- **发布时间**: 2025-05-14
- **arXiv链接**: [arXiv:2505.09324v1](https://arxiv.org/abs/2505.09324v1)
- **说明**: 9 pages, 8 figures
- **英文摘要**: The computer vision and image processing research community has been involved in standardizing video data communications for the past many decades, leading to standards such as AVC, HEVC, VVC, AV1, AV2, etc. However, recent groundbreaking works have focused on employing deep learning-based techniques to replace the traditional video codec pipeline to a greater affect. Neural video codecs (NVC) create an end-to-end ML-based solution that does not rely on any handcrafted features (motion or edge-based) and have the ability to learn content-aware compression strategies, offering better adaptability and higher compression efficiency than traditional methods. This holds a great potential not only for hardware design, but also for various video streaming platforms and applications, especially video conferencing applications such as MS-Teams or Zoom that have found extensive usage in classrooms and workplaces. However, their high computational demands currently limit their use in real-time applications like video conferencing. To address this, we propose a region-of-interest (ROI) based neural video compression model that leverages 2D Gaussian Splatting. Unlike traditional codecs, 2D Gaussian Splatting is capable of real-time decoding and can be optimized using fewer data points, requiring only thousands of Gaussians for decent quality outputs as opposed to millions in 3D scenes. In this work, we designed a video pipeline that speeds up the encoding time of the previous Gaussian spl...

---

## 110. ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction

- **作者**: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li
- **发布时间**: 2025-05-13
- **arXiv链接**: [arXiv:2505.08196v1](https://arxiv.org/abs/2505.08196v1)
- **英文摘要**: Existing 4D Gaussian Splatting methods rely on per-Gaussian deformation from a canonical space to target frames, which overlooks redundancy among adjacent Gaussian primitives and results in suboptimal performance. To address this limitation, we propose Anchor-Driven Deformable and Compressed Gaussian Splatting (ADC-GS), a compact and efficient representation for dynamic scene reconstruction. Specifically, ADC-GS organizes Gaussian primitives into an anchor-based structure within the canonical space, enhanced by a temporal significance-based anchor refinement strategy. To reduce deformation redundancy, ADC-GS introduces a hierarchical coarse-to-fine pipeline that captures motions at varying granularities. Moreover, a rate-distortion optimization is adopted to achieve an optimal balance between bitrate consumption and representation fidelity. Experimental results demonstrate that ADC-GS outperforms the per-Gaussian deformation approaches in rendering speed by 300%-800% while achieving state-of-the-art storage efficiency without compromising rendering quality. The code is released at https://github.com/H-Huang774/ADC-GS.git.

---

## 111. Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes

- **作者**: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai
- **发布时间**: 2025-05-10
- **arXiv链接**: [arXiv:2505.06523v1](https://arxiv.org/abs/2505.06523v1)
- **说明**: project page: https://xijie-yang.github.io/V3DG/
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables the reconstruction of intricate digital 3D assets from multi-view images by leveraging a set of 3D Gaussian primitives for rendering. Its explicit and discrete representation facilitates the seamless composition of complex digital worlds, offering significant advantages over previous neural implicit methods. However, when applied to large-scale compositions, such as crowd-level scenes, it can encompass numerous 3D Gaussians, posing substantial challenges for real-time rendering. To address this, inspired by Unreal Engine 5's Nanite system, we propose Virtualized 3D Gaussians (V3DG), a cluster-based LOD solution that constructs hierarchical 3D Gaussian clusters and dynamically selects only the necessary ones to accelerate rendering speed. Our approach consists of two stages: (1) Offline Build, where hierarchical clusters are generated using a local splatting method to minimize visual differences across granularities, and (2) Online Selection, where footprint evaluation determines perceptible clusters for efficient rasterization during rendering. We curate a dataset of synthetic and real-world scenes, including objects, trees, people, and buildings, each requiring 0.1 billion 3D Gaussians to capture fine details. Experiments show that our solution balances rendering efficiency and visual quality across user-defined tolerances, facilitating downstream interactive applications that compose extensive 3DGS assets for consistent rendering perform...

---

## 112. GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes

- **作者**: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang
- **发布时间**: 2025-05-07
- **arXiv链接**: [arXiv:2505.04659v1](https://arxiv.org/abs/2505.04659v1)
- **英文摘要**: The semantic synthesis of unseen scenes from multiple viewpoints is crucial for research in 3D scene understanding. Current methods are capable of rendering novel-view images and semantic maps by reconstructing generalizable Neural Radiance Fields. However, they often suffer from limitations in speed and segmentation performance. We propose a generalizable semantic Gaussian Splatting method (GSsplat) for efficient novel-view synthesis. Our model predicts the positions and attributes of scene-adaptive Gaussian distributions from once input, replacing the densification and pruning processes of traditional scene-specific Gaussian Splatting. In the multi-task framework, a hybrid network is designed to extract color and semantic information and predict Gaussian parameters. To augment the spatial perception of Gaussians for high-quality rendering, we put forward a novel offset learning module through group-based supervision and a point-level interaction module with spatial unit aggregation. When evaluated with varying numbers of multi-view inputs, GSsplat achieves state-of-the-art performance for semantic synthesis at the fastest speed.

---

## 113. 3D Gaussian Splatting Data Compression with Mixture of Priors

- **作者**: Lei Liu, Zhenghao Chen, Dong Xu
- **发布时间**: 2025-05-06
- **arXiv链接**: [arXiv:2505.03310v2](https://arxiv.org/abs/2505.03310v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) data compression is crucial for enabling efficient storage and transmission in 3D scene modeling. However, its development remains limited due to inadequate entropy models and suboptimal quantization strategies for both lossless and lossy compression scenarios, where existing methods have yet to 1) fully leverage hyperprior information to construct robust conditional entropy models, and 2) apply fine-grained, element-wise quantization strategies for improved compression granularity. In this work, we propose a novel Mixture of Priors (MoP) strategy to simultaneously address these two challenges. Specifically, inspired by the Mixture-of-Experts (MoE) paradigm, our MoP approach processes hyperprior information through multiple lightweight MLPs to generate diverse prior features, which are subsequently integrated into the MoP feature via a gating mechanism. To enhance lossless compression, the resulting MoP feature is utilized as a hyperprior to improve conditional entropy modeling. Meanwhile, for lossy compression, we employ the MoP feature as guidance information in an element-wise quantization procedure, leveraging a prior-guided Coarse-to-Fine Quantization (C2FQ) strategy with a predefined quantization step value. Specifically, we expand the quantization step value into a matrix and adaptively refine it from coarse to fine granularity, guided by the MoP feature, thereby obtaining a quantization step matrix that facilitates element-wise quantizatio...

---

## 114. SignSplat: Rendering Sign Language via Gaussian Splatting

- **作者**: Maksym Ivashechkin, Oscar Mendez, Richard Bowden
- **发布时间**: 2025-05-04
- **arXiv链接**: [arXiv:2505.02108v1](https://arxiv.org/abs/2505.02108v1)
- **英文摘要**: State-of-the-art approaches for conditional human body rendering via Gaussian splatting typically focus on simple body motions captured from many views. This is often in the context of dancing or walking. However, for more complex use cases, such as sign language, we care less about large body motion and more about subtle and complex motions of the hands and face. The problems of building high fidelity models are compounded by the complexity of capturing multi-view data of sign. The solution is to make better use of sequence data, ensuring that we can overcome the limited information from only a few views by exploiting temporal variability. Nevertheless, learning from sequence-level data requires extremely accurate and consistent model fitting to ensure that appearance is consistent across complex motions. We focus on how to achieve this, constraining mesh parameters to build an accurate Gaussian splatting framework from few views capable of modelling subtle human motion. We leverage regularization techniques on the Gaussian parameters to mitigate overfitting and rendering artifacts. Additionally, we propose a new adaptive control method to densify Gaussians and prune splat points on the mesh surface. To demonstrate the accuracy of our approach, we render novel sequences of sign language video, building on neural machine translation approaches to sign stitching. On benchmark datasets, our approach achieves state-of-the-art performance; and on highly articulated and complex si...

---

## 115. 4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression

- **作者**: Zicong Chen, Zhenghao Chen, Wei Jiang et al.
- **发布时间**: 2025-04-26
- **arXiv链接**: [arXiv:2504.18925v2](https://arxiv.org/abs/2504.18925v2)
- **英文摘要**: Storage is a significant challenge in reconstructing dynamic scenes with 4D Gaussian Splatting (4DGS) data. In this work, we introduce 4DGS-CC, a contextual coding framework that compresses 4DGS data to meet specific storage constraints. Building upon the established deformable 3D Gaussian Splatting (3DGS) method, our approach decomposes 4DGS data into 4D neural voxels and a canonical 3DGS component, which are then compressed using Neural Voxel Contextual Coding (NVCC) and Vector Quantization Contextual Coding (VQCC), respectively. Specifically, we first decompose the 4D neural voxels into distinct quantized features by separating the temporal and spatial dimensions. To losslessly compress each quantized feature, we leverage the previously compressed features from the temporal and spatial dimensions as priors and apply NVCC to generate the spatiotemporal context for contextual coding. Next, we employ a codebook to store spherical harmonics information from canonical 3DGS as quantized vectors, which are then losslessly compressed by using VQCC with the auxiliary learned hyperpriors for contextual coding, thereby reducing redundancy within the codebook. By integrating NVCC and VQCC, our contextual coding framework, 4DGS-CC, enables multi-rate 4DGS data compression tailored to specific storage requirements. Extensive experiments on three 4DGS data compression benchmarks demonstrate that our method achieves an average storage reduction of approximately 12 times while maintaining ...

---

## 116. 3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations

- **作者**: Yating Wang, Xuan Wang, Ran Yi et al.
- **发布时间**: 2025-04-21
- **arXiv链接**: [arXiv:2504.14967v1](https://arxiv.org/abs/2504.14967v1)
- **英文摘要**: Recent studies have combined 3D Gaussian and 3D Morphable Models (3DMM) to construct high-quality 3D head avatars. In this line of research, existing methods either fail to capture the dynamic textures or incur significant overhead in terms of runtime speed or storage space. To this end, we propose a novel method that addresses all the aforementioned demands. In specific, we introduce an expressive and compact representation that encodes texture-related attributes of the 3D Gaussians in the tensorial format. We store appearance of neutral expression in static tri-planes, and represents dynamic texture details for different expressions using lightweight 1D feature lines, which are then decoded into opacity offset relative to the neutral face. We further propose adaptive truncated opacity penalty and class-balanced sampling to improve generalization across different expressions. Experiments show this design enables accurate face dynamic details capturing while maintains real-time rendering and significantly reduces storage costs, thus broadening the applicability to more scenarios.

---

## 117. Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs

- **作者**: Shaohui Dai, Yansong Qu, Zheyan Li et al.
- **发布时间**: 2025-04-17
- **arXiv链接**: [arXiv:2504.13153v1](https://arxiv.org/abs/2504.13153v1)
- **英文摘要**: Bridging natural language and 3D geometry is a crucial step toward flexible, language-driven scene understanding. While recent advances in 3D Gaussian Splatting (3DGS) have enabled fast and high-quality scene reconstruction, research has also explored incorporating open-vocabulary understanding into 3DGS. However, most existing methods require iterative optimization over per-view 2D semantic feature maps, which not only results in inefficiencies but also leads to inconsistent 3D semantics across views. To address these limitations, we introduce a training-free framework that constructs a superpoint graph directly from Gaussian primitives. The superpoint graph partitions the scene into spatially compact and semantically coherent regions, forming view-consistent 3D entities and providing a structured foundation for open-vocabulary understanding. Based on the graph structure, we design an efficient reprojection strategy that lifts 2D semantic features onto the superpoints, avoiding costly multi-view iterative training. The resulting representation ensures strong 3D semantic coherence and naturally supports hierarchical understanding, enabling both coarse- and fine-grained open-vocabulary perception within a unified semantic field. Extensive experiments demonstrate that our method achieves state-of-the-art open-vocabulary segmentation performance, with semantic field reconstruction completed over $30\times$ faster. Our code will be available at https://github.com/Atrovast/THGS.

---

## 118. CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene Representation

- **作者**: Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong
- **发布时间**: 2025-04-17
- **arXiv链接**: [arXiv:2504.13022v1](https://arxiv.org/abs/2504.13022v1)
- **说明**: Submitted to a journal
- **英文摘要**: Gaussian splatting demonstrates proficiency for 3D scene modeling but suffers from substantial data volume due to inherent primitive redundancy. To enable future photorealistic 3D immersive visual communication applications, significant compression is essential for transmission over the existing Internet infrastructure. Hence, we propose Compressed Gaussian Splatting (CompGS++), a novel framework that leverages compact Gaussian primitives to achieve accurate 3D modeling with substantial size reduction for both static and dynamic scenes. Our design is based on the principle of eliminating redundancy both between and within primitives. Specifically, we develop a comprehensive prediction paradigm to address inter-primitive redundancy through spatial and temporal primitive prediction modules. The spatial primitive prediction module establishes predictive relationships for scene primitives and enables most primitives to be encoded as compact residuals, substantially reducing the spatial redundancy. We further devise a temporal primitive prediction module to handle dynamic scenes, which exploits primitive correlations across timestamps to effectively reduce temporal redundancy. Moreover, we devise a rate-constrained optimization module that jointly minimizes reconstruction error and rate consumption. This module effectively eliminates parameter redundancy within primitives and enhances the overall compactness of scene representations. Comprehensive evaluations across multiple bench...

---

## 119. Micro-splatting: Multistage Isotropy-informed Covariance Regularization Optimization for High-Fidelity 3D Gaussian Splatting

- **作者**: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Brad Choi
- **发布时间**: 2025-04-08
- **arXiv链接**: [arXiv:2504.05740v2](https://arxiv.org/abs/2504.05740v2)
- **说明**: This work has been submitted to journal for potential publication
- **英文摘要**: High-fidelity 3D Gaussian Splatting methods excel at capturing fine textures but often overlook model compactness, resulting in massive splat counts, bloated memory, long training, and complex post-processing. We present Micro-Splatting: Two-Stage Adaptive Growth and Refinement, a unified, in-training pipeline that preserves visual detail while drastically reducing model complexity without any post-processing or auxiliary neural modules. In Stage I (Growth), we introduce a trace-based covariance regularization to maintain near-isotropic Gaussians, mitigating low-pass filtering in high-frequency regions and improving spherical-harmonic color fitting. We then apply gradient-guided adaptive densification that subdivides splats only in visually complex regions, leaving smooth areas sparse. In Stage II (Refinement), we prune low-impact splats using a simple opacity-scale importance score and merge redundant neighbors via lightweight spatial and feature thresholds, producing a lean yet detail-rich model. On four object-centric benchmarks, Micro-Splatting reduces splat count and model size by up to 60% and shortens training by 20%, while matching or surpassing state-of-the-art PSNR, SSIM, and LPIPS in real-time rendering. These results demonstrate that Micro-Splatting delivers both compactness and high fidelity in a single, efficient, end-to-end framework.

---

## 120. L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery

- **作者**: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen
- **发布时间**: 2025-04-07
- **arXiv链接**: [arXiv:2504.05517v1](https://arxiv.org/abs/2504.05517v1)
- **英文摘要**: Traditional 3D content representations include dense point clouds that consume large amounts of data and hence network bandwidth, while newer representations such as neural radiance fields suffer from poor frame rates due to their non-standard volumetric rendering pipeline. 3D Gaussian splats (3DGS) can be seen as a generalization of point clouds that meet the best of both worlds, with high visual quality and efficient rendering for real-time frame rates. However, delivering 3DGS scenes from a hosting server to client devices is still challenging due to high network data consumption (e.g., 1.5 GB for a single scene). The goal of this work is to create an efficient 3D content delivery framework that allows users to view high quality 3D scenes with 3DGS as the underlying data representation. The main contributions of the paper are: (1) Creating new layered 3DGS scenes for efficient delivery, (2) Scheduling algorithms to choose what splats to download at what time, and (3) Trace-driven experiments from users wearing virtual reality headsets to evaluate the visual quality and latency. Our system for Layered 3D Gaussian Splats delivery L3GS demonstrates high visual quality, achieving 16.9% higher average SSIM compared to baselines, and also works with other compressed 3DGS representations.

---

## 121. 3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization

- **作者**: Isha Sharma, Dieter Schmalstieg
- **发布时间**: 2025-04-07
- **arXiv链接**: [arXiv:2504.04857v2](https://arxiv.org/abs/2504.04857v2)
- **英文摘要**: The complexity and scale of Volumetric and Simulation datasets for Scientific Visualization(SciVis) continue to grow. And the approaches and advantages of memory-efficient data formats and storage techniques for such datasets vary. OpenVDB library and its VDB data format excels in memory efficiency through its hierarchical and dynamic tree structure, with active and inactive sub-trees for data storage. It is heavily used in current production renderers for both animation and rendering stages in VFX pipelines and photorealistic rendering of volumes and fluids. However, it still remains to be fully leveraged in SciVis where domains dealing with sparse scalar fields like porous media, time varying volumes such as tornado and weather simulation or high resolution simulation of Computational Fluid Dynamics present ample number of large challenging data sets. The goal of this paper hence is not only to explore the use of OpenVDB in SciVis but also to explore a level of detail(LOD) technique using 3D Gaussian particles approximating voxel regions. For rendering, we utilize NVIDIA OptiX library for ray marching through the Gaussians particles. Data modeling using 3D Gaussians has been very popular lately due to success in stereoscopic image to 3D scene conversion using Gaussian Splatting and Gaussian approximation and mixture models aren't entirely new in SciVis as well. Our work explores the integration with rendering software libraries like OpenVDB and OptiX to take advantage of th...

---

## 122. Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization

- **作者**: Haishan Wang, Mohammad Hassan Vali, Arno Solin
- **发布时间**: 2025-04-03
- **arXiv链接**: [arXiv:2504.03059v2](https://arxiv.org/abs/2504.03059v2)
- **说明**: Appearing in Scandinavian Conference on Image Analysis (SCIA) 2025
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated remarkable effectiveness in 3D reconstruction, achieving high-quality results with real-time radiance field rendering. However, a key challenge is the substantial storage cost: reconstructing a single scene typically requires millions of Gaussian splats, each represented by 59 floating-point parameters, resulting in approximately 1 GB of memory. To address this challenge, we propose a compression method by building separate attribute codebooks and storing only discrete code indices. Specifically, we employ noise-substituted vector quantization technique to jointly train the codebooks and model features, ensuring consistency between gradient descent optimization and parameter discretization. Our method reduces the memory consumption efficiently (around $45\times$) while maintaining competitive reconstruction quality on standard 3D benchmark scenes. Experiments on different codebook sizes show the trade-off between compression ratio and image quality. Furthermore, the trained compressed model remains fully compatible with popular 3DGS viewers and enables faster rendering speed, making it well-suited for practical applications.

---

## 123. NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations

- **作者**: Zhenyu Tang, Chaoran Feng, Xinhua Cheng et al.
- **发布时间**: 2025-03-29
- **arXiv链接**: [arXiv:2503.23162v2](https://arxiv.org/abs/2503.23162v2)
- **说明**: Project page: https://pku-yuangroup.github.io/NeuralGS/
- **英文摘要**: 3D Gaussian Splatting (3DGS) achieves impressive quality and rendering speed, but with millions of 3D Gaussians and significant storage and transmission costs. In this paper, we aim to develop a simple yet effective method called NeuralGS that compresses the original 3DGS into a compact representation. Our observation is that neural fields like NeRF can represent complex 3D scenes with Multi-Layer Perceptron (MLP) neural networks using only a few megabytes. Thus, NeuralGS effectively adopts the neural field representation to encode the attributes of 3D Gaussians with MLPs, only requiring a small storage size even for a large-scale scene. To achieve this, we adopt a clustering strategy and fit the Gaussians within each cluster using different tiny MLPs, based on importance scores of Gaussians as fitting weights. We experiment on multiple datasets, achieving a 91-times average model size reduction without harming the visual quality.

---

## 124. Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis

- **作者**: Shuai Shen, Wanhua Li, Yunpeng Zhang, Yap-Peng Tan, Jiwen Lu
- **发布时间**: 2025-03-28
- **arXiv链接**: [arXiv:2503.22605v2](https://arxiv.org/abs/2503.22605v2)
- **说明**: Demo video at \url{https://sstzal.github.io/Audio-Plane/}
- **英文摘要**: Talking head synthesis has emerged as a prominent research topic in computer graphics and multimedia, yet most existing methods often struggle to strike a balance between generation quality and computational efficiency, particularly under real-time constraints. In this paper, we propose a novel framework that integrates Gaussian Splatting with a structured Audio Factorization Plane (Audio-Plane) to enable high-quality, audio-synchronized, and real-time talking head generation. For modeling a dynamic talking head, a 4D volume representation, which consists of three axes in 3D space and one temporal axis aligned with audio progression, is typically required. However, directly storing and processing a dense 4D grid is impractical due to the high memory and computation cost, and lack of scalability for longer durations. We address this challenge by decomposing the 4D volume representation into a set of audio-independent spatial planes and audio-dependent planes, forming a compact and interpretable representation for talking head modeling that we refer to as the Audio-Plane. This factorized design allows for efficient and fine-grained audio-aware spatial encoding, and significantly enhances the model's ability to capture complex lip dynamics driven by speech signals. To further improve region-specific motion modeling, we introduce an audio-guided saliency splatting mechanism based on region-aware modulation, which adaptively emphasizes highly dynamic regions such as the mouth area...

---

## 125. GS-LTS: 3D Gaussian Splatting-Based Adaptive Modeling for Long-Term Service Robots

- **作者**: Bin Fu, Jialin Li, Bin Zhang, Ruiping Wang, Xilin Chen
- **发布时间**: 2025-03-22
- **arXiv链接**: [arXiv:2503.17733v1](https://arxiv.org/abs/2503.17733v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has garnered significant attention in robotics for its explicit, high fidelity dense scene representation, demonstrating strong potential for robotic applications. However, 3DGS-based methods in robotics primarily focus on static scenes, with limited attention to the dynamic scene changes essential for long-term service robots. These robots demand sustained task execution and efficient scene updates-challenges current approaches fail to meet. To address these limitations, we propose GS-LTS (Gaussian Splatting for Long-Term Service), a 3DGS-based system enabling indoor robots to manage diverse tasks in dynamic environments over time. GS-LTS detects scene changes (e.g., object addition or removal) via single-image change detection, employs a rule-based policy to autonomously collect multi-view observations, and efficiently updates the scene representation through Gaussian editing. Additionally, we propose a simulation-based benchmark that automatically generates scene change data as compact configuration scripts, providing a standardized, user-friendly evaluation benchmark. Experimental results demonstrate GS-LTS's advantages in reconstruction, navigation, and superior scene updates-faster and higher quality than the image training baseline-advancing 3DGS for long-term robotic operations. Code and benchmark are available at: https://vipl-vsu.github.io/3DGS-LTS.

---

## 126. ProtoGS: Efficient and High-Quality Rendering with 3D Gaussian Prototypes

- **作者**: Zhengqing Gao, Dongting Hu, Jia-Wang Bian et al.
- **发布时间**: 2025-03-21
- **arXiv链接**: [arXiv:2503.17486v3](https://arxiv.org/abs/2503.17486v3)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has made significant strides in novel view synthesis but is limited by the substantial number of Gaussian primitives required, posing challenges for deployment on lightweight devices. Recent methods address this issue by compressing the storage size of densified Gaussians, yet fail to preserve rendering quality and efficiency. To overcome these limitations, we propose ProtoGS to learn Gaussian prototypes to represent Gaussian primitives, significantly reducing the total Gaussian amount without sacrificing visual quality. Our method directly uses Gaussian prototypes to enable efficient rendering and leverage the resulting reconstruction loss to guide prototype learning. To further optimize memory efficiency during training, we incorporate structure-from-motion (SfM) points as anchor points to group Gaussian primitives. Gaussian prototypes are derived within each group by clustering of K-means, and both the anchor points and the prototypes are optimized jointly. Our experiments on real-world and synthetic datasets prove that we outperform existing methods, achieving a substantial reduction in the number of Gaussians, and enabling high rendering speed while maintaining or even enhancing rendering fidelity.

---

## 127. Optimized Minimal 3D Gaussian Splatting

- **作者**: Joo Chan Lee, Jong Hwan Ko, Eunbyung Park
- **发布时间**: 2025-03-21
- **arXiv链接**: [arXiv:2503.16924v2](https://arxiv.org/abs/2503.16924v2)
- **说明**: Project page: https://maincold2.github.io/omg/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for real-time, high-performance rendering, enabling a wide range of applications. However, representing 3D scenes with numerous explicit Gaussian primitives imposes significant storage and memory overhead. Recent studies have shown that high-quality rendering can be achieved with a substantially reduced number of Gaussians when represented with high-precision attributes. Nevertheless, existing 3DGS compression methods still rely on a relatively large number of Gaussians, focusing primarily on attribute compression. This is because a smaller set of Gaussians becomes increasingly sensitive to lossy attribute compression, leading to severe quality degradation. Since the number of Gaussians is directly tied to computational costs, it is essential to reduce the number of Gaussians effectively rather than only optimizing storage. In this paper, we propose Optimized Minimal Gaussians representation (OMG), which significantly reduces storage while using a minimal number of primitives. First, we determine the distinct Gaussian from the near ones, minimizing redundancy without sacrificing quality. Second, we propose a compact and precise attribute representation that efficiently captures both continuity and irregularity among primitives. Additionally, we propose a sub-vector quantization technique for improved irregularity representation, maintaining fast training with a negligible codebook size. Extensive experiment...

---

## 128. SAGE: Semantic-Driven Adaptive Gaussian Splatting in Extended Reality

- **作者**: Chiara Schiavo, Elena Camuffo, Leonardo Badia, Simone Milani
- **发布时间**: 2025-03-20
- **arXiv链接**: [arXiv:2503.16747v1](https://arxiv.org/abs/2503.16747v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has significantly improved the efficiency and realism of three-dimensional scene visualization in several applications, ranging from robotics to eXtended Reality (XR). This work presents SAGE (Semantic-Driven Adaptive Gaussian Splatting in Extended Reality), a novel framework designed to enhance the user experience by dynamically adapting the Level of Detail (LOD) of different 3DGS objects identified via a semantic segmentation. Experimental results demonstrate how SAGE effectively reduces memory and computational overhead while keeping a desired target visual quality, thus providing a powerful optimization for interactive XR applications.

---

## 129. 1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering

- **作者**: Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang
- **发布时间**: 2025-03-20
- **arXiv链接**: [arXiv:2503.16422v1](https://arxiv.org/abs/2503.16422v1)
- **英文摘要**: 4D Gaussian Splatting (4DGS) has recently gained considerable attention as a method for reconstructing dynamic scenes. Despite achieving superior quality, 4DGS typically requires substantial storage and suffers from slow rendering speed. In this work, we delve into these issues and identify two key sources of temporal redundancy. (Q1) \textbf{Short-Lifespan Gaussians}: 4DGS uses a large portion of Gaussians with short temporal span to represent scene dynamics, leading to an excessive number of Gaussians. (Q2) \textbf{Inactive Gaussians}: When rendering, only a small subset of Gaussians contributes to each frame. Despite this, all Gaussians are processed during rasterization, resulting in redundant computation overhead. To address these redundancies, we present \textbf{4DGS-1K}, which runs at over 1000 FPS on modern GPUs. For Q1, we introduce the Spatial-Temporal Variation Score, a new pruning criterion that effectively removes short-lifespan Gaussians while encouraging 4DGS to capture scene dynamics using Gaussians with longer temporal spans. For Q2, we store a mask for active Gaussians across consecutive frames, significantly reducing redundant computations in rendering. Compared to vanilla 4DGS, our method achieves a $41\times$ reduction in storage and $9\times$ faster rasterization speed on complex dynamic scenes, while maintaining comparable visual quality. Please see our project page at https://4DGS-1K.github.io.

---

## 130. Improving Adaptive Density Control for 3D Gaussian Splatting

- **作者**: Glenn Grubert, Florian Barthel, Anna Hilsmann, Peter Eisert
- **发布时间**: 2025-03-18
- **arXiv链接**: [arXiv:2503.14274v1](https://arxiv.org/abs/2503.14274v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has become one of the most influential works in the past year. Due to its efficient and high-quality novel view synthesis capabilities, it has been widely adopted in many research fields and applications. Nevertheless, 3DGS still faces challenges to properly manage the number of Gaussian primitives that are used during scene reconstruction. Following the adaptive density control (ADC) mechanism of 3D Gaussian Splatting, new Gaussians in under-reconstructed regions are created, while Gaussians that do not contribute to the rendering quality are pruned. We observe that those criteria for densifying and pruning Gaussians can sometimes lead to worse rendering by introducing artifacts. We especially observe under-reconstructed background or overfitted foreground regions. To encounter both problems, we propose three new improvements to the adaptive density control mechanism. Those include a correction for the scene extent calculation that does not only rely on camera positions, an exponentially ascending gradient threshold to improve training convergence, and significance-aware pruning strategy to avoid background artifacts. With these adaptions, we show that the rendering quality improves while using the same number of Gaussians primitives. Furthermore, with our improvements, the training converges considerably faster, allowing for more than twice as fast training times while yielding better quality than 3DGS. Finally, our contributions are easily comp...

---

## 131. Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model

- **作者**: Mufan Liu, Qi Yang, He Huang et al.
- **发布时间**: 2025-03-18
- **arXiv链接**: [arXiv:2503.13948v2](https://arxiv.org/abs/2503.13948v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as an efficient and high-fidelity paradigm for novel view synthesis. To adapt 3DGS for dynamic content, deformable 3DGS incorporates temporally deformable primitives with learnable latent embeddings to capture complex motions. Despite its impressive performance, the high-dimensional embeddings and vast number of primitives lead to substantial storage requirements. In this paper, we introduce a \textbf{Light}weight \textbf{4}D\textbf{GS} framework, called Light4GS, that employs significance pruning with a deep context model to provide a lightweight storage-efficient dynamic 3DGS representation. The proposed Light4GS is based on 4DGS that is a typical representation of deformable 3DGS. Specifically, our framework is built upon two core components: (1) a spatio-temporal significance pruning strategy that eliminates over 64\% of the deformable primitives, followed by an entropy-constrained spherical harmonics compression applied to the remainder; and (2) a deep context model that integrates intra- and inter-prediction with hyperprior into a coarse-to-fine context structure to enable efficient multiscale latent embedding compression. Our approach achieves over 120x compression and increases rendering FPS up to 20\% compared to the baseline 4DGS, and also superior to frame-wise state-of-the-art 3DGS compression methods, revealing the effectiveness of our Light4GS in terms of both intra- and inter-prediction methods without sacrificing render...

---

## 132. CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression

- **作者**: Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng
- **发布时间**: 2025-03-17
- **arXiv链接**: [arXiv:2503.12862v1](https://arxiv.org/abs/2503.12862v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has shown immense potential for novel view synthesis. However, achieving rate-distortion-optimized compression of 3DGS representations for transmission and/or storage applications remains a challenge. CAT-3DGS introduces a context-adaptive triplane hyperprior for end-to-end optimized compression, delivering state-of-the-art coding performance. Despite this, it requires prolonged training and decoding time. To address these limitations, we propose CAT-3DGS Pro, an enhanced version of CAT-3DGS that improves both compression performance and computational efficiency. First, we introduce a PCA-guided vector-matrix hyperprior, which replaces the triplane-based hyperprior to reduce redundant parameters. To achieve a more balanced rate-distortion trade-off and faster encoding, we propose an alternate optimization strategy (A-RDO). Additionally, we refine the sampling rate optimization method in CAT-3DGS, leading to significant improvements in rate-distortion performance. These enhancements result in a 46.6% BD-rate reduction and 3x speedup in training time on BungeeNeRF, while achieving 5x acceleration in decoding speed for the Amsterdam scene compared to CAT-3DGS.

---

## 133. CompMarkGS: Robust Watermarking for Compressed 3D Gaussian Splatting

- **作者**: Sumin In, Youngdong Jang, Utae Jeong et al.
- **发布时间**: 2025-03-17
- **arXiv链接**: [arXiv:2503.12836v6](https://arxiv.org/abs/2503.12836v6)
- **说明**: 33 pages, 19 figures
- **英文摘要**: As 3D Gaussian Splatting (3DGS) is increasingly adopted in various academic and commercial applications due to its high-quality and real-time rendering capabilities, the need for copyright protection is growing. At the same time, its large model size requires efficient compression for storage and transmission. However, compression techniques, especially quantization-based methods, degrade the integrity of existing 3DGS watermarking methods, thus creating the need for a novel methodology that is robust against compression. To ensure reliable watermark detection under compression, we propose a compression-tolerant 3DGS watermarking method that preserves watermark integrity and rendering quality. Our approach utilizes an anchor-based 3DGS, embedding the watermark into anchor attributes, particularly the anchor feature, to enhance security and rendering quality. We also propose a quantization distortion layer that injects quantization noise during training, preserving the watermark after quantization-based compression. Moreover, we employ a frequency-aware anchor growing strategy that enhances rendering quality by effectively identifying Gaussians in high-frequency regions, and an HSV loss to mitigate color artifacts for further rendering quality improvement. Extensive experiments demonstrate that our proposed method preserves the watermark even under compression and maintains high rendering quality.

---

## 134. PCGS: Progressive Compression of 3D Gaussian Splatting

- **作者**: Yihang Chen, Mengyao Li, Qianyi Wu et al.
- **发布时间**: 2025-03-11
- **arXiv链接**: [arXiv:2503.08511v1](https://arxiv.org/abs/2503.08511v1)
- **说明**: Project Page: https://yihangchen-ee.github.io/project_pcgs/ Code: https://github.com/YihangChen-ee/PCGS
- **英文摘要**: 3D Gaussian Splatting (3DGS) achieves impressive rendering fidelity and speed for novel view synthesis. However, its substantial data size poses a significant challenge for practical applications. While many compression techniques have been proposed, they fail to efficiently utilize existing bitstreams in on-demand applications due to their lack of progressivity, leading to a waste of resource. To address this issue, we propose PCGS (Progressive Compression of 3D Gaussian Splatting), which adaptively controls both the quantity and quality of Gaussians (or anchors) to enable effective progressivity for on-demand applications. Specifically, for quantity, we introduce a progressive masking strategy that incrementally incorporates new anchors while refining existing ones to enhance fidelity. For quality, we propose a progressive quantization approach that gradually reduces quantization step sizes to achieve finer modeling of Gaussian attributes. Furthermore, to compact the incremental bitstreams, we leverage existing quantization results to refine probability prediction, improving entropy coding efficiency across progressive levels. Overall, PCGS achieves progressivity while maintaining compression performance comparable to SoTA non-progressive methods. Code available at: github.com/YihangChen-ee/PCGS.

---

## 135. MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction

- **作者**: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo et al.
- **发布时间**: 2025-03-11
- **arXiv链接**: [arXiv:2503.08093v2](https://arxiv.org/abs/2503.08093v2)
- **说明**: project page https://mvgsr.github.io
- **英文摘要**: 3D Gaussian Splatting (3DGS) has gained significant attention for its high-quality rendering capabilities, ultra-fast training, and inference speeds. However, when we apply 3DGS to surface reconstruction tasks, especially in environments with dynamic objects and distractors, the method suffers from floating artifacts and color errors due to inconsistency from different viewpoints. To address this challenge, we propose Multi-View Consistency Gaussian Splatting for the domain of Robust Surface Reconstruction (\textbf{MVGSR}), which takes advantage of lightweight Gaussian models and a {heuristics-guided distractor masking} strategy for robust surface reconstruction in non-static environments. Compared to existing methods that rely on MLPs for distractor segmentation strategies, our approach separates distractors from static scene elements by comparing multi-view feature consistency, allowing us to obtain precise distractor masks early in training. Furthermore, we introduce a pruning measure based on multi-view contributions to reset transmittance, effectively reducing floating artifacts. Finally, a multi-view consistency loss is applied to achieve high-quality performance in surface reconstruction tasks. Experimental results demonstrate that MVGSR achieves competitive geometric accuracy and rendering fidelity compared to the state-of-the-art surface reconstruction algorithms. More information is available on our project page (https://mvgsr.github.io).

---

## 136. Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction

- **作者**: Kai Li, Junhao Wang, William Han, Ding Zhao
- **发布时间**: 2025-03-08
- **arXiv链接**: [arXiv:2503.06161v2](https://arxiv.org/abs/2503.06161v2)
- **说明**: 17 pages, 5 figures; Accepted to ML4H 2025
- **英文摘要**: Minimally invasive surgery (MIS) requires high-fidelity, real-time visual feedback of dynamic and low-texture surgical scenes. To address these requirements, we introduce FeatureEndo-4DGS (FE-4DGS), the first real time pipeline leveraging feature-distilled 4D Gaussian Splatting for simultaneous reconstruction and semantic segmentation of deformable surgical environments. Unlike prior feature-distilled methods restricted to static scenes, and existing 4D approaches that lack semantic integration, FE-4DGS seamlessly leverages pre-trained 2D semantic embeddings to produce a unified 4D representation-where semantics also deform with tissue motion. This unified approach enables the generation of real-time RGB and semantic outputs through a single, parallelized rasterization process. Despite the additional complexity from feature distillation, FE-4DGS sustains real-time rendering (61 FPS) with a compact footprint, achieves state-of-the-art rendering fidelity on EndoNeRF (39.1 PSNR) and SCARED (27.3 PSNR), and delivers competitive EndoVis18 segmentation, matching or exceeding strong 2D baselines for binary segmentation tasks (0.93 DSC) and remaining competitive for multi-label segmentation (0.77 DSC).

---

## 137. Progressively Deformable 2D Gaussian Splatting for Video Representation at Arbitrary Resolutions

- **作者**: Mufan Liu, Qi Yang, Miaoran Zhao et al.
- **发布时间**: 2025-03-07
- **arXiv链接**: [arXiv:2503.05600v2](https://arxiv.org/abs/2503.05600v2)
- **英文摘要**: Implicit neural representations (INRs) enable fast video compression and effective video processing, but a single model rarely offers scalable decoding across rates and resolutions. In practice, multi-resolution typically relies on retraining or multi-branch designs, and structured pruning failed to provide a permutation-invariant progressive transmission order. Motivated by the explicit structure and efficiency of Gaussian splatting, we propose D2GV-AR, a deformable 2D Gaussian video representation that enables \emph{arbitrary-scale} rendering and \emph{any-ratio} progressive coding within a single model. We partition each video into fixed-length Groups of Pictures and represent each group with a canonical set of 2D Gaussian primitives, whose temporal evolution is modeled by a neural ordinary differential equation. During training and rendering, we apply scale-aware grouping according to Nyquist sampling theorem to form a nested hierarchy across resolutions. Once trained, primitives can be pruned via a D-optimal subset objective to enable any-ratio progressive coding. Extensive experiments show that D2GV-AR renders at over 250 FPS while matching or surpassing recent INR baselines, enabling multiscale continuous rate--quality adaptation.

---

## 138. EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation

- **作者**: Chao Zhang, Yifeng Zhou, Shuheng Wang et al.
- **发布时间**: 2025-03-07
- **arXiv链接**: [arXiv:2503.05162v1](https://arxiv.org/abs/2503.05162v1)
- **英文摘要**: We have recently seen great progress in 3D scene reconstruction through explicit point-based 3D Gaussian Splatting (3DGS), notable for its high quality and fast rendering speed. However, reconstructing dynamic scenes such as complex human performances with long durations remains challenging. Prior efforts fall short of modeling a long-term sequence with drastic motions, frequent topology changes or interactions with props, and resort to segmenting the whole sequence into groups of frames that are processed independently, which undermines temporal stability and thereby leads to an unpleasant viewing experience and inefficient storage footprint. In view of this, we introduce EvolvingGS, a two-stage strategy that first deforms the Gaussian model to coarsely align with the target frame, and then refines it with minimal point addition/subtraction, particularly in fast-changing areas. Owing to the flexibility of the incrementally evolving representation, our method outperforms existing approaches in terms of both per-frame and temporal quality metrics while maintaining fast rendering through its purely explicit representation. Moreover, by exploiting temporal coherence between successive frames, we propose a simple yet effective compression algorithm that achieves over 50x compression rate. Extensive experiments on both public benchmarks and challenging custom datasets demonstrate that our method significantly advances the state-of-the-art in dynamic scene reconstruction, particula...

---

## 139. GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting

- **作者**: Inseo Lee, Youngyoon Choi, Joonseok Lee
- **发布时间**: 2025-03-06
- **arXiv链接**: [arXiv:2503.04333v1](https://arxiv.org/abs/2503.04333v1)
- **英文摘要**: Implicit Neural Representation for Videos (NeRV) has introduced a novel paradigm for video representation and compression, outperforming traditional codecs. As model size grows, however, slow encoding and decoding speed and high memory consumption hinder its application in practice. To address these limitations, we propose a new video representation and compression method based on 2D Gaussian Splatting to efficiently handle video data. Our proposed deformable 2D Gaussian Splatting dynamically adapts the transformation of 2D Gaussians at each frame, significantly reducing memory cost. Equipped with a multi-plane-based spatiotemporal encoder and a lightweight decoder, it predicts changes in color, coordinates, and shape of initialized Gaussians, given the time step. By leveraging temporal gradients, our model effectively captures temporal redundancy at negligible cost, significantly enhancing video representation efficiency. Our method reduces GPU memory usage by up to 78.4%, and significantly expedites video processing, achieving 5.5x faster training and 12.5x faster decoding compared to the state-of-the-art NeRV methods.

---

## 140. GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding

- **作者**: Xihan Wang, Dianyi Yang, Yu Gao et al.
- **发布时间**: 2025-03-06
- **arXiv链接**: [arXiv:2503.04034v1](https://arxiv.org/abs/2503.04034v1)
- **英文摘要**: Recent advancements in 3D Gaussian Splatting(3DGS) have significantly improved semantic scene understanding, enabling natural language queries to localize objects within a scene. However, existing methods primarily focus on embedding compressed CLIP features to 3D Gaussians, suffering from low object segmentation accuracy and lack spatial reasoning capabilities. To address these limitations, we propose GaussianGraph, a novel framework that enhances 3DGS-based scene understanding by integrating adaptive semantic clustering and scene graph generation. We introduce a "Control-Follow" clustering strategy, which dynamically adapts to scene scale and feature distribution, avoiding feature compression and significantly improving segmentation accuracy. Additionally, we enrich scene representation by integrating object attributes and spatial relations extracted from 2D foundation models. To address inaccuracies in spatial relationships, we propose 3D correction modules that filter implausible relations through spatial consistency verification, ensuring reliable scene graph construction. Extensive experiments on three datasets demonstrate that GaussianGraph outperforms state-of-the-art methods in both semantic segmentation and object grounding tasks, providing a robust solution for complex scene understanding and interaction.

---

## 141. OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding

- **作者**: Dianyi Yang, Yu Gao, Xihan Wang et al.
- **发布时间**: 2025-03-03
- **arXiv链接**: [arXiv:2503.01646v1](https://arxiv.org/abs/2503.01646v1)
- **英文摘要**: Recent advancements in 3D Gaussian Splatting have significantly improved the efficiency and quality of dense semantic SLAM. However, previous methods are generally constrained by limited-category pre-trained classifiers and implicit semantic representation, which hinder their performance in open-set scenarios and restrict 3D object-level scene understanding. To address these issues, we propose OpenGS-SLAM, an innovative framework that utilizes 3D Gaussian representation to perform dense semantic SLAM in open-set environments. Our system integrates explicit semantic labels derived from 2D foundational models into the 3D Gaussian framework, facilitating robust 3D object-level scene understanding. We introduce Gaussian Voting Splatting to enable fast 2D label map rendering and scene updating. Additionally, we propose a Confidence-based 2D Label Consensus method to ensure consistent labeling across multiple views. Furthermore, we employ a Segmentation Counter Pruning strategy to improve the accuracy of semantic scene representation. Extensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of our method in scene understanding, tracking, and mapping, achieving 10 times faster semantic rendering and 2 times lower storage costs compared to existing methods. Project page: https://young-bit.github.io/opengs-github.github.io/.

---

## 142. LiteGS: A High-performance Framework to Train 3DGS in Subminutes via System and Algorithm Codesign

- **作者**: Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang
- **发布时间**: 2025-03-03
- **arXiv链接**: [arXiv:2503.01199v3](https://arxiv.org/abs/2503.01199v3)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as promising alternative in 3D representation. However, it still suffers from high training cost. This paper introduces LiteGS, a high performance framework that systematically optimizes the 3DGS training pipeline from multiple aspects. At the low-level computation layer, we design a ``warp-based raster'' associated with two hardware-aware optimizations to significantly reduce gradient reduction overhead. At the mid-level data management layer, we introduce dynamic spatial sorting based on Morton coding to enable a performant ``Cluster-Cull-Compact'' pipeline and improve data locality, therefore reducing cache misses. At the top-level algorithm layer, we establish a new robust densification criterion based on the variance of the opacity gradient, paired with a more stable opacity control mechanism, to achieve more precise parameter growth. Experimental results demonstrate that LiteGS accelerates the original 3DGS training by up to 13.4x with comparable or superior quality and surpasses the current SOTA in lightweight models by up to 1.4x speedup. For high-quality reconstruction tasks, LiteGS sets a new accuracy record and decreases the training time by an order of magnitude.

---

## 143. Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions

- **作者**: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo et al.
- **发布时间**: 2025-02-26
- **arXiv链接**: [arXiv:2502.19457v1](https://arxiv.org/abs/2502.19457v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a pioneering approach in explicit scene rendering and computer graphics. Unlike traditional neural radiance field (NeRF) methods, which typically rely on implicit, coordinate-based models to map spatial coordinates to pixel values, 3DGS utilizes millions of learnable 3D Gaussians. Its differentiable rendering technique and inherent capability for explicit scene representation and manipulation positions 3DGS as a potential game-changer for the next generation of 3D reconstruction and representation technologies. This enables 3DGS to deliver real-time rendering speeds while offering unparalleled editability levels. However, despite its advantages, 3DGS suffers from substantial memory and storage requirements, posing challenges for deployment on resource-constrained devices. In this survey, we provide a comprehensive overview focusing on the scalability and compression of 3DGS. We begin with a detailed background overview of 3DGS, followed by a structured taxonomy of existing compression methods. Additionally, we analyze and compare current methods from the topological perspective, evaluating their strengths and limitations in terms of fidelity, compression ratios, and computational efficiency. Furthermore, we explore how advancements in efficient NeRF representations can inspire future developments in 3DGS optimization. Finally, we conclude with current research challenges and highlight key directions for future exploration.

---

## 144. Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field

- **作者**: Wenhao Hu, Wenhao Chai, Shengyu Hao et al.
- **发布时间**: 2025-02-22
- **arXiv链接**: [arXiv:2502.16303v1](https://arxiv.org/abs/2502.16303v1)
- **英文摘要**: Achieving a consistent and compact 3D segmentation field is crucial for maintaining semantic coherence across views and accurately representing scene structures. Previous 3D scene segmentation methods rely on video segmentation models to address inconsistencies across views, but the absence of spatial information often leads to object misassociation when object temporarily disappear and reappear. Furthermore, in the process of 3D scene reconstruction, segmentation and optimization are often treated as separate tasks. As a result, optimization typically lacks awareness of semantic category information, which can result in floaters with ambiguous segmentation. To address these challenges, we introduce CCGS, a method designed to achieve both view consistent 2D segmentation and a compact 3D Gaussian segmentation field. CCGS incorporates pointmap association and a piecewise-plane constraint. First, we establish pixel correspondence between adjacent images by minimizing the Euclidean distance between their pointmaps. We then redefine object mask overlap accordingly. The Hungarian algorithm is employed to optimize mask association by minimizing the total matching cost, while allowing for partial matches. To further enhance compactness, the piecewise-plane constraint restricts point displacement within local planes during optimization, thereby preserving structural integrity. Experimental results on ScanNet and Replica datasets demonstrate that CCGS outperforms existing methods in bo...

---

## 145. Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting

- **作者**: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi
- **发布时间**: 2025-02-20
- **arXiv链接**: [arXiv:2502.14931v2](https://arxiv.org/abs/2502.14931v2)
- **说明**: 18 pages. Under review
- **英文摘要**: We propose Hier-SLAM++, a comprehensive Neuro-Symbolic semantic 3D Gaussian Splatting SLAM method with both RGB-D and monocular input featuring an advanced hierarchical categorical representation, which enables accurate pose estimation as well as global 3D semantic mapping. The parameter usage in semantic SLAM systems increases significantly with the growing complexity of the environment, making scene understanding particularly challenging and costly. To address this problem, we introduce a novel hierarchical representation that encodes both semantic and geometric information in a compact form into 3D Gaussian Splatting, leveraging the capabilities of large language models (LLMs) as well as the 3D generative model. By utilizing the proposed hierarchical tree structure, semantic information is symbolically represented and learned in an end-to-end manner. We further introduce an advanced semantic loss designed to optimize hierarchical semantic information through both Intra-level and Inter-level optimizations. Additionally, we propose an improved SLAM system to support both RGB-D and monocular inputs using a feed-forward model. To the best of our knowledge, this is the first semantic monocular Gaussian Splatting SLAM system, significantly reducing sensor requirements for 3D semantic understanding and broadening the applicability of semantic Gaussian SLAM system. We conduct experiments on both synthetic and real-world datasets, demonstrating superior or on-par performance with s...

---

## 146. GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting

- **作者**: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang
- **发布时间**: 2025-02-16
- **arXiv链接**: [arXiv:2502.10975v1](https://arxiv.org/abs/2502.10975v1)
- **英文摘要**: Recently, the emergence of 3D Gaussian Splatting (3DGS) has drawn significant attention in the area of 3D map reconstruction and visual SLAM. While extensive research has explored 3DGS for indoor trajectory tracking using visual sensor alone or in combination with Light Detection and Ranging (LiDAR) and Inertial Measurement Unit (IMU), its integration with GNSS for large-scale outdoor navigation remains underexplored. To address these concerns, we proposed GS-GVINS: a tightly-integrated GNSS-Visual-Inertial Navigation System augmented by 3DGS. This system leverages 3D Gaussian as a continuous differentiable scene representation in largescale outdoor environments, enhancing navigation performance through the constructed 3D Gaussian map. Notably, GS-GVINS is the first GNSS-Visual-Inertial navigation application that directly utilizes the analytical jacobians of SE3 camera pose with respect to 3D Gaussians. To maintain the quality of 3DGS rendering in extreme dynamic states, we introduce a motionaware 3D Gaussian pruning mechanism, updating the map based on relative pose translation and the accumulated opacity along the camera ray. For validation, we test our system under different driving environments: open-sky, sub-urban, and urban. Both self-collected and public datasets are used for evaluation. The results demonstrate the effectiveness of GS-GVINS in enhancing navigation accuracy across diverse driving environments.

---

## 147. DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior

- **作者**: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang
- **发布时间**: 2025-02-13
- **arXiv链接**: [arXiv:2502.09111v2](https://arxiv.org/abs/2502.09111v2)
- **说明**: IEEE Transactions on Visualization and Computer Graphics
- **英文摘要**: Gaussian SLAM systems excel in real-time rendering and fine-grained reconstruction compared to NeRF-based systems. However, their reliance on extensive keyframes is impractical for deployment in real-world robotic systems, which typically operate under sparse-view conditions that can result in substantial holes in the map. To address these challenges, we introduce DenseSplat, the first SLAM system that effectively combines the advantages of NeRF and 3DGS. DenseSplat utilizes sparse keyframes and NeRF priors for initializing primitives that densely populate maps and seamlessly fill gaps. It also implements geometry-aware primitive sampling and pruning strategies to manage granularity and enhance rendering efficiency. Moreover, DenseSplat integrates loop closure and bundle adjustment, significantly enhancing frame-to-frame tracking accuracy. Extensive experiments on multiple large-scale datasets demonstrate that DenseSplat achieves superior performance in tracking and mapping compared to current state-of-the-art methods.

---

## 148. PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map

- **作者**: Yue Pan, Xingguang Zhong, Liren Jin et al.
- **发布时间**: 2025-02-09
- **arXiv链接**: [arXiv:2502.05752v2](https://arxiv.org/abs/2502.05752v2)
- **说明**: 15 pages, 8 figures, presented at RSS 2025
- **英文摘要**: Robots benefit from high-fidelity reconstructions of their environment, which should be geometrically accurate and photorealistic to support downstream tasks. While this can be achieved by building distance fields from range sensors and radiance fields from cameras, realising scalable incremental mapping of both fields consistently and at the same time with high quality is challenging. In this paper, we propose a novel map representation that unifies a continuous signed distance field and a Gaussian splatting radiance field within an elastic and compact point-based implicit neural map. By enforcing geometric consistency between these fields, we achieve mutual improvements by exploiting both modalities. We present a novel LiDAR-visual SLAM system called PINGS using the proposed map representation and evaluate it on several challenging large-scale datasets. Experimental results demonstrate that PINGS can incrementally build globally consistent distance and radiance fields encoded with a compact set of neural points. Compared to state-of-the-art methods, PINGS achieves superior photometric and geometric rendering at novel views by constraining the radiance field with the distance field. Furthermore, by utilizing dense photometric cues and multi-view consistency from the radiance field, PINGS produces more accurate distance fields, leading to improved odometry estimation and mesh reconstruction. We also provide an open-source implementation of PING at: https://github.com/PRBonn/P...

---

## 149. UVGS: Reimagining Unstructured 3D Gaussian Splatting using UV Mapping

- **作者**: Aashish Rai, Dilin Wang, Mihir Jain et al.
- **发布时间**: 2025-02-03
- **arXiv链接**: [arXiv:2502.01846v4](https://arxiv.org/abs/2502.01846v4)
- **说明**: https://ivl.cs.brown.edu/uvgs
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated superior quality in modeling 3D objects and scenes. However, generating 3DGS remains challenging due to their discrete, unstructured, and permutation-invariant nature. In this work, we present a simple yet effective method to overcome these challenges. We utilize spherical mapping to transform 3DGS into a structured 2D representation, termed UVGS. UVGS can be viewed as multi-channel images, with feature dimensions as a concatenation of Gaussian attributes such as position, scale, color, opacity, and rotation. We further find that these heterogeneous features can be compressed into a lower-dimensional (e.g., 3-channel) shared feature space using a carefully designed multi-branch network. The compressed UVGS can be treated as typical RGB images. Remarkably, we discover that typical VAEs trained with latent diffusion models can directly generalize to this new representation without additional training. Our novel representation makes it effortless to leverage foundational 2D models, such as diffusion models, to directly model 3DGS. Additionally, one can simply increase the 2D UV resolution to accommodate more Gaussians, making UVGS a scalable solution compared to typical 3D backbones. This approach immediately unlocks various novel generation applications of 3DGS by inherently utilizing the already developed superior 2D generation capabilities. In our experiments, we demonstrate various unconditional, conditional generation, and inpai...

---

## 150. CrowdSplat: Exploring Gaussian Splatting For Crowd Rendering

- **作者**: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan
- **发布时间**: 2025-01-29
- **arXiv链接**: [arXiv:2501.17792v3](https://arxiv.org/abs/2501.17792v3)
- **说明**: 4 pages, 4 figures
- **英文摘要**: We present CrowdSplat, a novel approach that leverages 3D Gaussian Splatting for real-time, high-quality crowd rendering. Our method utilizes 3D Gaussian functions to represent animated human characters in diverse poses and outfits, which are extracted from monocular videos. We integrate Level of Detail (LoD) rendering to optimize computational efficiency and quality. The CrowdSplat framework consists of two stages: (1) avatar reconstruction and (2) crowd synthesis. The framework is also optimized for GPU memory usage to enhance scalability. Quantitative and qualitative evaluations show that CrowdSplat achieves good levels of rendering quality, memory efficiency, and computational performance. Through the.se experiments, we demonstrate that CrowdSplat is a viable solution for dynamic, realistic crowd simulation in real-time applications.

---

## 151. GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting

- **作者**: Jiajun Dong, Chengkun Wang, Wenzhao Zheng et al.
- **发布时间**: 2025-01-26
- **arXiv链接**: [arXiv:2501.15619v1](https://arxiv.org/abs/2501.15619v1)
- **英文摘要**: Effective image tokenization is crucial for both multi-modal understanding and generation tasks due to the necessity of the alignment with discrete text data. To this end, existing approaches utilize vector quantization (VQ) to project pixels onto a discrete codebook and reconstruct images from the discrete representation. However, compared with the continuous latent space, the limited discrete codebook space significantly restrict the representational ability of these image tokenizers. In this paper, we propose GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting as a solution. We first represent the encoded samples as multiple flexible featured 2D Gaussians characterized by positions, rotation angles, scaling factors, and feature coefficients. We adopt the standard quantization for the Gaussian features and then concatenate the quantization results with the other intrinsic Gaussian parameters before the corresponding splatting operation and the subsequent decoding module. In general, GaussianToken integrates the local influence of 2D Gaussian distribution into the discrete space and thus enhances the representation capability of the image tokenizer. Competitive reconstruction performances on CIFAR, Mini-ImageNet, and ImageNet-1K demonstrate the effectiveness of our framework. Our code is available at: https://github.com/ChrisDong-THU/GaussianToken.

---

## 152. GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression

- **作者**: Francesco Di Sario, Riccardo Renzulli, Marco Grangetto, Akihiro Sugimoto, Enzo Tartaglione
- **发布时间**: 2025-01-23
- **arXiv链接**: [arXiv:2501.13558v2](https://arxiv.org/abs/2501.13558v2)
- **英文摘要**: 3D Gaussian Splatting enhances real-time performance in novel view synthesis by representing scenes with mixtures of Gaussians and utilizing differentiable rasterization. However, it typically requires large storage capacity and high VRAM, demanding the design of effective pruning and compression techniques. Existing methods, while effective in some scenarios, struggle with scalability and fail to adapt models based on critical factors such as computing capabilities or bandwidth, requiring to re-train the model under different configurations. In this work, we propose a novel, model-agnostic technique that organizes Gaussians into several hierarchical layers, enabling progressive Level of Detail (LoD) strategy. This method, combined with recent approach of compression of 3DGS, allows a single model to instantly scale across several compression ratios, with minimal to none impact to quality compared to a single non-scalable model and without requiring re-training. We validate our approach on typical datasets and benchmarks, showcasing low distortion and substantial gains in terms of scalability and adaptability.

---

## 153. Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes

- **作者**: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi
- **发布时间**: 2025-01-22
- **arXiv链接**: [arXiv:2501.13045v1](https://arxiv.org/abs/2501.13045v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a promising representation for photorealistic rendering of 3D scenes. However, its high storage requirements pose significant challenges for practical applications. We observe that Gaussians exhibit distinct roles and characteristics that are analogous to traditional artistic techniques -- Like how artists first sketch outlines before filling in broader areas with color, some Gaussians capture high-frequency features like edges and contours; While other Gaussians represent broader, smoother regions, that are analogous to broader brush strokes that add volume and depth to a painting. Based on this observation, we propose a novel hybrid representation that categorizes Gaussians into (i) Sketch Gaussians, which define scene boundaries, and (ii) Patch Gaussians, which cover smooth regions. Sketch Gaussians are efficiently encoded using parametric models, leveraging their geometric coherence, while Patch Gaussians undergo optimized pruning, retraining, and vector quantization to maintain volumetric consistency and storage efficiency. Our comprehensive evaluation across diverse indoor and outdoor scenes demonstrates that this structure-aware approach achieves up to 32.62% improvement in PSNR, 19.12% in SSIM, and 45.41% in LPIPS at equivalent model sizes, and correspondingly, for an indoor scene, our model maintains the visual quality with 2.3% of the original model size.

---

## 154. GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting

- **作者**: Longan Wang, Yuang Shi, Wei Tsang Ooi
- **发布时间**: 2025-01-21
- **arXiv链接**: [arXiv:2501.12060v2](https://arxiv.org/abs/2501.12060v2)
- **英文摘要**: 3D Gaussian splats have emerged as a revolutionary, effective, learned representation for static 3D scenes. In this work, we explore using 2D Gaussian splats as a new primitive for representing videos. We propose GSVC, an approach to learning a set of 2D Gaussian splats that can effectively represent and compress video frames. GSVC incorporates the following techniques: (i) To exploit temporal redundancy among adjacent frames, which can speed up training and improve the compression efficiency, we predict the Gaussian splats of a frame based on its previous frame; (ii) To control the trade-offs between file size and quality, we remove Gaussian splats with low contribution to the video quality; (iii) To capture dynamics in videos, we randomly add Gaussian splats to fit content with large motion or newly-appeared objects; (iv) To handle significant changes in the scene, we detect key frames based on loss differences during the learning process. Experiment results show that GSVC achieves good rate-distortion trade-offs, comparable to state-of-the-art video codecs such as AV1 and VVC, and a rendering speed of 1500 fps for a 1920x1080 video.

---

## 155. Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models

- **作者**: Marcel Rogge, Didier Stricker
- **发布时间**: 2025-01-14
- **arXiv链接**: [arXiv:2501.08174v2](https://arxiv.org/abs/2501.08174v2)
- **说明**: ICPRAM 2025. Implementation details (no code): https://github.com/MarcelRogge/object-centric-2dgs
- **英文摘要**: Current Gaussian Splatting approaches are effective for reconstructing entire scenes but lack the option to target specific objects, making them computationally expensive and unsuitable for object-specific applications. We propose a novel approach that leverages object masks to enable targeted reconstruction, resulting in object-centric models. Additionally, we introduce an occlusion-aware pruning strategy to minimize the number of Gaussians without compromising quality. Our method reconstructs compact object models, yielding object-centric Gaussian and mesh representations that are up to 96% smaller and up to 71% faster to train compared to the baseline while retaining competitive quality. These representations are immediately usable for downstream applications such as appearance editing and physics simulation without additional processing.

---

## 156. GaussianVideo: Efficient Video Representation via Hierarchical Gaussian Splatting

- **作者**: Andrew Bond, Jui-Hsien Wang, Long Mai, Erkut Erdem, Aykut Erdem
- **发布时间**: 2025-01-08
- **arXiv链接**: [arXiv:2501.04782v1](https://arxiv.org/abs/2501.04782v1)
- **说明**: 10 pages, 10 figures
- **英文摘要**: Efficient neural representations for dynamic video scenes are critical for applications ranging from video compression to interactive simulations. Yet, existing methods often face challenges related to high memory usage, lengthy training times, and temporal consistency. To address these issues, we introduce a novel neural video representation that combines 3D Gaussian splatting with continuous camera motion modeling. By leveraging Neural ODEs, our approach learns smooth camera trajectories while maintaining an explicit 3D scene representation through Gaussians. Additionally, we introduce a spatiotemporal hierarchical learning strategy, progressively refining spatial and temporal features to enhance reconstruction quality and accelerate convergence. This memory-efficient approach achieves high-quality rendering at impressive speeds. Experimental results show that our hierarchical learning, combined with robust camera motion modeling, captures complex dynamic scenes with strong temporal consistency, achieving state-of-the-art performance across diverse video datasets in both high- and low-motion scenarios.

---

## 157. Compression of 3D Gaussian Splatting with Optimized Feature Planes and Standard Video Codecs

- **作者**: Soonbin Lee, Fangwen Shu, Yago Sanchez, Thomas Schierl, Cornelius Hellge
- **发布时间**: 2025-01-06
- **arXiv链接**: [arXiv:2501.03399v1](https://arxiv.org/abs/2501.03399v1)
- **英文摘要**: 3D Gaussian Splatting is a recognized method for 3D scene representation, known for its high rendering quality and speed. However, its substantial data requirements present challenges for practical applications. In this paper, we introduce an efficient compression technique that significantly reduces storage overhead by using compact representation. We propose a unified architecture that combines point cloud data and feature planes through a progressive tri-plane structure. Our method utilizes 2D feature planes, enabling continuous spatial representation. To further optimize these representations, we incorporate entropy modeling in the frequency domain, specifically designed for standard video codecs. We also propose channel-wise bit allocation to achieve a better trade-off between bitrate consumption and feature plane representation. Consequently, our model effectively leverages spatial correlations within the feature planes to enhance rate-distortion performance using standard, non-differentiable video codecs. Experimental results demonstrate that our method outperforms existing methods in data compactness while maintaining high rendering quality. Our project page is available at https://fraunhoferhhi.github.io/CodecGS

---

## 158. 4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images

- **作者**: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui
- **发布时间**: 2024-12-17
- **arXiv链接**: [arXiv:2412.12919v2](https://arxiv.org/abs/2412.12919v2)
- **说明**: IPMI 2025 Oral; Zhentao Liu and Ruyi Zha made equal contributions
- **英文摘要**: Reconstructing 3D vessel structures from sparse-view dynamic digital subtraction angiography (DSA) images enables accurate medical assessment while reducing radiation exposure. Existing methods often produce suboptimal results or require excessive computation time. In this work, we propose 4D radiative Gaussian splatting (4DRGS) to achieve high-quality reconstruction efficiently. In detail, we represent the vessels with 4D radiative Gaussian kernels. Each kernel has time-invariant geometry parameters, including position, rotation, and scale, to model static vessel structures. The time-dependent central attenuation of each kernel is predicted from a compact neural network to capture the temporal varying response of contrast agent flow. We splat these Gaussian kernels to synthesize DSA images via X-ray rasterization and optimize the model with real captured ones. The final 3D vessel volume is voxelized from the well-trained kernels. Moreover, we introduce accumulated attenuation pruning and bounded scaling activation to improve reconstruction quality. Extensive experiments on real-world patient data demonstrate that 4DRGS achieves impressive results in 5 minutes training, which is 32x faster than the state-of-the-art method. This underscores the potential of 4DRGS for real-world clinics.

---

## 159. CLIP-GS: CLIP-Informed Gaussian Splatting for View-Consistent 3D Indoor Semantic Understanding

- **作者**: Guibiao Liao, Jiankun Li, Zhenyu Bao et al.
- **发布时间**: 2024-04-22
- **arXiv链接**: [arXiv:2404.14249v2](https://arxiv.org/abs/2404.14249v2)
- **说明**: ACM TOMM 2025
- **英文摘要**: Exploiting 3D Gaussian Splatting (3DGS) with Contrastive Language-Image Pre-Training (CLIP) models for open-vocabulary 3D semantic understanding of indoor scenes has emerged as an attractive research focus. Existing methods typically attach high-dimensional CLIP semantic embeddings to 3D Gaussians and leverage view-inconsistent 2D CLIP semantics as Gaussian supervision, resulting in efficiency bottlenecks and deficient 3D semantic consistency. To address these challenges, we present CLIP-GS, efficiently achieving a coherent semantic understanding of 3D indoor scenes via the proposed Semantic Attribute Compactness (SAC) and 3D Coherent Regularization (3DCR). SAC approach exploits the naturally unified semantics within objects to learn compact, yet effective, semantic Gaussian representations, enabling highly efficient rendering (>100 FPS). 3DCR enforces semantic consistency in 2D and 3D domains: In 2D, 3DCR utilizes refined view-consistent semantic outcomes derived from 3DGS to establish cross-view coherence constraints; in 3D, 3DCR encourages features similar among 3D Gaussian primitives associated with the same object, leading to more precise and coherent segmentation results. Extensive experimental results demonstrate that our method remarkably suppresses existing state-of-the-art approaches, achieving mIoU improvements of 21.20% and 13.05% on ScanNet and Replica datasets, respectively, while maintaining real-time rendering speed. Furthermore, our approach exhibits superior...

---

