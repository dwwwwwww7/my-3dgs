# 未知会议 2026

> **最后更新**： 2026-06-07 03:05:52

本页面包含 2026 年 未知会议 会议的论文列表。

## 1. GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds

- **作者**: Rajrup Ghosh, Haodong Wang, Haoran Hong et al.
- **发布时间**: 2026-06-04
- **arXiv链接**: [arXiv:2606.05650v1](https://arxiv.org/abs/2606.05650v1)
- **英文摘要**: Dynamic 3D Gaussian Splatting (3DGS) holds great promise as a 3D video streaming technology since it can represent complex 3D scenes with high fidelity. In this approach, every frame in a 3D video represents the environment as a collection of Gaussians with position and other attributes such as scale, rotation, opacity, and color. Frames capture fine details, permit views from any arbitrary perspective, but are an order of magnitude, or more, larger than 2D video frames. A line of recent work has explored how to compress dynamic 3DGS frames, but these approaches are often slow, in part because their compression techniques are not amenable to efficient acceleration. GS-NFS accelerates dynamic 3DGS compression and decompression on a GPU, to the point where it can encode and decode at full frame rate. It achieves this by developing novel GPU-based parallelizations of existing algorithms for encoding both positions and attributes of Gaussians. As a result, it is 1-2 orders of magnitude faster than the state-of-the-art in encoding and decoding a frame, while offering competitive compression performance and rendering quality.

---

## 2. SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation

- **作者**: Qingpo Wuwu, Xiaobao Wei, Peng Chen et al.
- **发布时间**: 2026-06-02
- **arXiv链接**: [arXiv:2606.03909v1](https://arxiv.org/abs/2606.03909v1)
- **英文摘要**: While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general compression framework specifically designed for street scenes. First, we introduce a node-based learnable pruning strategy that systematically removes low-contributing Gaussian primitives while preserving visually critical regions. Second, after the scene representation stabilizes, we apply background compression, further reducing redundancy in static regions. Our method effectively preserves the geometry and appearance of dynamic objects while significantly reducing the total number of Gaussian primitives. Extensive experiments on the Waymo and nuScenes demonstrate that SparseStreet achieves up to 80% compression ratio with minimal quality degradation, enabling resource-efficient, high-fidelity dynamic scene reconstruction. Project website: https://sparsestreet.github.io/.

---

## 3. VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning

- **作者**: Aoduo Li, Jiancheng Li, Huan Ye et al.
- **发布时间**: 2026-06-01
- **arXiv链接**: [arXiv:2606.02346v1](https://arxiv.org/abs/2606.02346v1)
- **说明**: 12 pages, 5 figures. Accepted by CGI 2026
- **英文摘要**: 3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

---

## 4. Smaller and Faster 3DGS via Post-Training Dictionary Learning

- **作者**: Jiarong Gong, Jonas Unger, Ehsan Miandji
- **发布时间**: 2026-05-28
- **arXiv链接**: [arXiv:2605.30396v1](https://arxiv.org/abs/2605.30396v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a promising neural scene representation for real-time rendering, but trained models often suffer from large memory footprints, limiting deployment on less powerful devices. Existing compression techniques often lead to architectures with several additional trainable parameters. While achieving outstanding compression ratios, they introduce noticeable drops in image quality. In this work, we introduce the first dictionary-learning-based compression framework for 3DGS. The proposed post-training compression pipeline can be deployed in virtually any 3DGS model without the need for re-training or modifications to existing 3DGS models. Our compression framework is straightforward to implement, yet provides significant compression capabilities, preserves image quality, and improves real-time rendering performance. Across 13 benchmark scenes, our approach achieves an average compression ratio of 3.95x, 3.10x, and 4.55x when applied to 3DGS, 3DGS-MCMC, and PixelGS, respectively. This yields consistent rendering speedups of 23.3%, 24.3%, and 25.3%, while maintaining image quality.

---

## 5. BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression

- **作者**: Yuquan Bi, Baosheng Yu, Yingke Lei et al.
- **发布时间**: 2026-05-28
- **arXiv链接**: [arXiv:2605.29583v1](https://arxiv.org/abs/2605.29583v1)
- **英文摘要**: High-capacity watermarking is necessary for 3D Gaussian Splatting (3DGS) assets to embed rich information (e.g., ownership, provenance, and authentication codes), enabling reliable identification and integrity verification in large-scale 3D asset pipelines. Existing bit-to-token watermarking methods based on a pre-trained text encoder are limited to 77-bit messages due to CLIP's fixed 77-token context length, as tokens beyond this limit are unsupported by learned positional embeddings. To address this limitation, we introduce BitC-3DGS, a bit-compression framework that encodes multiple message bits per token. It employs a bit-compressed tokenization scheme that encodes multiple bits within the same chunk into a single semantic token. To enable recovery of the compressed information, it further introduces a dual-branch architecture for joint chunk decompression and bit decoding, along with a hard-message sampling strategy to improve combinatorial coverage during decoder training. Extensive experiments on the Blender and LLFF datasets demonstrate the effectiveness of BitC-3DGS for high-capacity watermarking, achieving high message recovery accuracy and rendering fidelity. For example, it supports 128-bit message capacity with recovery accuracy comparable to that of 64-bit messages in recent state-of-the-art methods.

---

## 6. GScomp-QA: A Subjective Dataset for Quality Assessment of Compressed Gaussian Splatting

- **作者**: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz
- **发布时间**: 2026-05-26
- **arXiv链接**: [arXiv:2605.26880v1](https://arxiv.org/abs/2605.26880v1)
- **英文摘要**: Gaussian Splatting (GS) has emerged as an efficient representation for high-quality 3D reconstruction and novel view synthesis. However, its large model size poses challenges for storage and transmission. While several GS compression solutions have been proposed, their perceptual impact remains poorly understood due to the lack of dedicated evaluation datasets. To address this gap, this paper introduces GScomp-QA, a subjective quality assessment dataset for evaluating synthesis quality from compressed GS models. The dataset comprises 331 video stimuli from 13 real-world scenes, covering 9 state-of-the-art GS compression solutions. By using videos synthesized from uncompressed models as reference, GScomp-QA isolates compression-induced distortions from synthesis artifacts. A subjective study with 20 participants was conducted, providing reliable perceptual scores. Based on these data, GS compression solutions are evaluated through perceptual rate-distortion analysis. In addition, 18 objective quality metrics are evaluated, showing that they do not fully capture GS-specific distortions. GScomp-QA will be publicly available and provide a benchmark for evaluating GS compression solutions and supporting the development of quality metrics tailored to GS compression.

---

## 7. R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction

- **作者**: Denis Gridusov, Maxim Popov, Sergey Kolyubin
- **发布时间**: 2026-05-25
- **arXiv链接**: [arXiv:2605.25909v1](https://arxiv.org/abs/2605.25909v1)
- **说明**: Code: https://github.com/be2rlab/r5dgs
- **英文摘要**: Reconstructing and predicting dynamic 3D scenes from multi-view videos is a foundational task for robotics, AR/VR, and digital twins. Recent physics-informed Gaussian Splatting methods achieve impressive future frame extrapolation but lack semantic awareness and suffer from large computational overhead. We introduce $\textbf{R5DGS}$, a framework that augments a physics-driven 4D Gaussian representation with compact Identity Encoding vectors, enabling precise Gaussian-to-object association. By constructing an offline CLIP-based object lookup table, we support open-vocabulary text prompting to retrieve and render object-specific Gaussians across arbitrary timestamps and viewpoints. Furthermore, we propose a rigid-body inference constraint that predicts and integrates physical dynamics exclusively for object centroids, propagating motion to associated Gaussians via relative transformations. This optimization yields a 11 FPS speedup during extrapolation without compromising trajectories plausibility.

---

## 8. CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting

- **作者**: Pengpeng Yu, Runqing Jiang, Qi Zhang et al.
- **发布时间**: 2026-05-25
- **arXiv链接**: [arXiv:2605.25563v1](https://arxiv.org/abs/2605.25563v1)
- **英文摘要**: While feed-forward 3D Gaussian splatting reconstructs renderable Gaussian primitives from sparse context views without per-scene optimization, existing pipelines do not provide a compact scene representation for storage or transmission. A natural solution is to apply existing 3DGS compression methods to the generated Gaussian primitives. However, this approach operates on the final irregular 3D representation and is decoupled from the internal feature-to-Gaussian generation process, which limits compression efficiency. To address this, we introduce CodecSplat, an ultra-compact latent coding framework for feed-forward 3D Gaussian splatting. CodecSplat first encodes an intermediate 2D Gaussian-generation feature into an entropy-coded scene bitstream. At the decoder, the latent feature is reconstructed and used to predict depth and Gaussian parameters, which are then mapped to 3D Gaussian primitives. Note that, by integrating compression into the feed-forward Gaussian generation pipeline, CodecSplat avoids inefficient compression over irregular 3D Gaussian primitives and allows the codec to exploit the structured intermediate feature representation. We instantiate CodecSplat on a feed-forward Gaussian splatting backbone with depth-guided multi-view feature refinement and a hierarchical learned feature codec. On DL3DV and RealEstate10K datasets, CodecSplat achieves 23.56-26.36 dB and 24.76-27.05 dB PSNR with only 20.00-107.77 KiB and 3.37-12.51 KiB per scene, respectively. This i...

---

## 9. OctCGS: Octree-Contextual Gaussian Splatting with Explicit Multi-Order Propagation Modeling for Channel Knowledge Map Construction

- **作者**: Jinghan Zhang, Xitao Gong, Qi Wang, Richard A. Stirling-Gallacher, Giuseppe Caire
- **发布时间**: 2026-05-21
- **arXiv链接**: [arXiv:2605.22961v1](https://arxiv.org/abs/2605.22961v1)
- **说明**: Submitted to IEEE GLOBECOM 2026
- **英文摘要**: Channel knowledge maps (CKMs) learn the relation between transmitter (Tx) and receiver (Rx) positions and channel knowledge to support environment-aware wireless communications. Implicit neural methods can model continuous channel variation but often incur high training and inference cost, while existing Gaussian-splatting-based CKM methods improve efficiency yet still compress wireless multipath interactions into aggregated scattering representations. Consequently, explicit modeling of multi-bounce wireless propagation remains absent from CKM construction. We propose OctCGS, an octree-contextual Gaussian splatting framework that explicitly models the order of bounce jointly over Tx/Rx positions and carrier frequencies. OctCGS partitions the environment into a multi-resolution octree and anchors one Gaussian primitive to each leaf node. Rather than having each Gaussian independently encode all multi-path propagations, it models complex electromagnetic interactions among scatterers through tree attention over the octree hierarchy with controlled complexity. Experiments on simulated benchmarks show that OctCGS achieves a 2.99 dB channel-gain mean absolute error (MAE) and 0.065 channel gain normalized mean absolute error (NMAE), outperforming the strongest baseline by 0.88 dB MAE and 0.021 NMAE.

---

## 10. ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting

- **作者**: Yuke Li, Weihang Liu, Cheng Zhang et al.
- **发布时间**: 2026-05-21
- **arXiv链接**: [arXiv:2605.22020v2](https://arxiv.org/abs/2605.22020v2)
- **英文摘要**: Feed-forward 3D Gaussian Splatting models offer fast single-pass reconstruction,but scaling them to match per-scene optimization quality is fundamentally hindered by the scarcity of large-scale 3D annotations. A practical compromise is predict-then-refine,where post-prediction optimization compensates for the limited capacity of the feed-forward network. However,standard feed-forward 3DGS is trained solely for zero-step rendering error,ignoring whether its output constitutes a good initialization for the downstream optimizer. We present ForeSplat,an optimization-aware training framework that equips feed-forward 3DGS models to produce initializations explicitly designed for rapid,effective refinement. By offloading part of the scene-modeling burden to the optimizer,ForeSplat substantially reduces the capacity pressure on the feed-forward model,making high-quality reconstruction feasible even with compact networks. At its core is MetaGrad,a lightweight multi-anchor meta-gradient training rule that bypasses costly higher-order differentiation through the 3DGS optimizer. MetaGrad unrolls a short inner-loop refinement trajectory,samples anchor states,and back-propagates aggregated first-order gradients to the prediction head as a surrogate optimization-aware signal. This fine-tuning adds no inference cost and enables high-quality reconstruction within seconds after a few refinement steps. We instantiate ForeSplat on diverse backbones,including AnySplat,Pi3X,and a distilled variant...

---

## 11. AIR: Amortized Image Reconstruction Framework for Self-Supervised Feed-Forward 2D Gaussian Splatting

- **作者**: Zhaojie Zeng, Yuesong Wang, Yawei Luo, Tao Guan
- **发布时间**: 2026-05-20
- **arXiv链接**: [arXiv:2605.20820v1](https://arxiv.org/abs/2605.20820v1)
- **说明**: preprint version
- **英文摘要**: 2D Gaussian splatting provides an efficient explicit representation for image reconstruction, but existing methods still require costly per-image iterative optimization or rely on handcrafted priors for primitive allocation. We present AIR, a self-supervised feed-forward framework that amortizes iterative Gaussian fitting into a single network pass, eliminating per-image test-time optimization. AIR adopts a stage-wise residual architecture that progressively predicts additional Gaussian primitives from reconstruction residuals, together with an explicit Stage Control mechanism that activates new primitives only in under-reconstructed regions. A Predict--Optimize--Distill training strategy stabilizes multi-stage prediction by distilling short-horizon optimized Gaussian increments back into the predictor. The stabilized predictor is then jointly finetuned across stages and equipped with an image-adaptive quantizer for compact Gaussian storage. Experiments on Kodak and DIV2K show that AIR achieves better reconstruction quality than representative Gaussian-based baselines while reducing encoding time to 160--300\,ms. Code: https://github.com/whoiszzj/AIR.git

---

## 12. GLUT: 3D Gaussian Lookup Table for Continuous Color Transformation

- **作者**: Danna Xue, David Serrano-Lozano, Shaolin Su, Javier Vazquez-Corral
- **发布时间**: 2026-05-19
- **arXiv链接**: [arXiv:2605.19889v1](https://arxiv.org/abs/2605.19889v1)
- **说明**: Project page: https://color.cvc.uab.cat/glut/
- **英文摘要**: 3D Lookup Tables (3D LUTs) are widely used for color mapping, but their grid-based representation requires discretizing the RGB space, leading to a capacity-memory trade-off that becomes prohibitive when storing large numbers of LUTs. Recent approaches adopt implicit neural representations to improve scalability, yet their black-box nature limits interpretability and hinders intuitive, localized editing. In this paper, we propose Gaussian LUT (GLUT), a continuous and explicit color representation that models color transformations using a set of learnable 3D Gaussian primitives. By avoiding fixed-resolution grids, GLUT achieves flexible representational capacity while maintaining a compact memory footprint. Its explicit, spatially localized formulation further enables both accurate modeling and interpretability. Building on this representation, we introduce a compact conditional generator (CGLUT) that predicts GLUT parameters for multiple LUT instances, encoding diverse color styles in a single framework to enable smooth and controllable LUT style blending. Moreover, GLUT supports efficient, user-friendly editing by allowing localized adjustments to specific color regions without global retraining. Experimental results demonstrate that our approach outperforms prior neural LUT representations in both accuracy and efficiency, while offering improved interpretability and interactive control.

---

## 13. MMGS: 10$\times$ Compressed 3DGS through Optimal Transport Aggregation based on Multi-view Ranking

- **作者**: Beizhen Zhao, Sicheng Yu, Ziran Yin, Dongxu Shen, Hao Wang
- **发布时间**: 2026-05-19
- **arXiv链接**: [arXiv:2605.19304v1](https://arxiv.org/abs/2605.19304v1)
- **说明**: 19 pages
- **英文摘要**: While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction, it suffers from significant overhead due to massive redundant primitives. Existing compression methods typically rely on local sampling or fixed pruning thresholds, which often struggle to balance redundancy reduction with high-fidelity rendering. To address this, we propose a novel framework that formulates Gaussian optimization as a global geometric distribution matching problem. Specifically, our approach integrates three components: (1) we introduce a multi-view 3D Gaussian contribution ranking mechanism that filters primitives using geometric consistency instead of local heuristics; (2) we propose a global Optimal Transport (OT)-based aggregation algorithm that merges redundant primitives while preserving the underlying geometry; and (3) we design an OT-based densification operator that maintains the Gaussian's distributional properties for stable optimization. Our approach achieves state-of-the-art rendering quality with only \textbf{10$\%$} primitives and \textbf{10$\times$} accelerated training speeds compared to vanilla 3DGS.

---

## 14. 3D Skew Gaussian Splatting with Any Camera Trajectory Visualization Engine

- **作者**: Beizhen Zhao, Yifan Zhou, Gaochao Song, Ziran Yin, Hao Wang
- **发布时间**: 2026-05-18
- **arXiv链接**: [arXiv:2605.18334v1](https://arxiv.org/abs/2605.18334v1)
- **说明**: 16 pages
- **英文摘要**: While 3D Gaussian Splatting (3DGS) has revolutionized real-time photorealistic view synthesis, its fundamental reliance on symmetric Gaussian distributions introduces visual artifacts that hinder accurate spatial data exploration. Specifically, symmetric kernels struggle to capture shape and color discontinuities , which cause blurriness and primitive redundancy that mislead human perception during visual analysis. To address these visualization barriers, we introduce 3D Skew Gaussian Splatting (3DSGS), a novel framework that significantly enhances the structural fidelity and compactness of explicit scene representations. Our key insight lies in extending the standard primitive to a general Skew Gaussian counterpart. This generalized primitive inherits the highly efficient rasterization properties of standard Gaussians while gaining intrinsic asymmetric modeling capabilities. We couple this with an enhanced opacity representation to better handle complex transparency, alongside a depth-aware densification strategy that intelligently manages primitive allocation. Furthermore, to make these advancements actionable for real-world visual analytics, we re-derive the CUDA rasterization pipeline to universally support both symmetric and skew Gaussians, integrating it into a decoupled, free-camera interactive visualization engine. Extensive experiments demonstrate that 3DSGS achieves superior rendering quality and structural compactness, particularly in regions with intricate details...

---

## 15. A Single Atlas is All You Need: Decoder-Side Gaussian Splatting for Immersive Video

- **作者**: Dawid Mieloch, Stuart Perry
- **发布时间**: 2026-05-16
- **arXiv链接**: [arXiv:2605.17002v1](https://arxiv.org/abs/2605.17002v1)
- **英文摘要**: Immersive video delivery is bottlenecked by pixel-rate constraints, making the transmission of high-resolution depth maps or explicit 3D volumetric data expensive. Decoder-Side Depth Estimation (DSDE) shifts depth computation to the client, but struggles with complex geometries, inter-view flickering, and non-Lambertian reflections. Conversely, 3D Gaussian Splatting (3DGS) offers state-of-the-art view synthesis, but transmitting splats (or their projected 2D maps) incurs prohibitive bandwidth costs and is poorly aligned with standard video codecs. We propose Decoder-Side Gaussian Splatting (DSGS), a framework that natively replaces the depth-estimation stage of DSDE with feed-forward 3DGS inference, optimizing volumetric scenes entirely on the decoder side from compressed textures and metadata. A central, counterintuitive finding is that lossy compression acts as an implicit low-pass filter stabilizing feed-forward splat prediction: compressed bitstreams exceed lossless quality while shrinking tenfold. Under extreme view sparsity (one 2D atlas comprising 4 input views), DSGS achieves a +5.79 dB BD-PSNR and +0.054 BD-SSIM gain over the DSDE anchor while reducing maximum inter-view Delta IV-PSNR from 17.2 dB to 6.4 dB, minimizing the domain shift between transmitted and virtual viewports.

---

## 16. Smart target point control for Gaussian Splatting methods

- **作者**: Pratik Singh Bisht, Andreas Kolb
- **发布时间**: 2026-05-15
- **arXiv链接**: [arXiv:2605.16158v1](https://arxiv.org/abs/2605.16158v1)
- **英文摘要**: Standard Gaussian splatting methods rely on heuristic densification and pruning to adaptively allocate primitives during training, and the resulting Gaussian count strongly influences both reconstruction quality and runtime. This makes comparisons across methods fragile: improvements can stem from higher representational capacity rather than algorithmic design. A common and naive workaround for this is hard-stopping or budgeting densification/pruning once a target count is reached, which biases training because different methods hit the cap at different times, yielding non-uniform densify/prune exposure across views and uneven point distributions. We propose a target point control scheme that preserves the standard densification window and cadence, but adjusts only the existing densification and opacity-culling hyper-parameters to track a quadratic target count trajectory. This quota-governor reaches the desired count by 15k iterations without abrupt cutoffs, ensuring that all methods and views receive equal densification and pruning cycles, enabling fairer, capacity-matched evaluation.

---

## 17. Eff-WRFGS: Efficient Wireless Radiance Field Using 3D Gaussian Splatting

- **作者**: Chenghong Bian, Meng Hua, Deniz Gunduz
- **发布时间**: 2026-05-14
- **arXiv链接**: [arXiv:2605.15324v1](https://arxiv.org/abs/2605.15324v1)
- **说明**: 5 pages, for possible IEEE journal publication
- **英文摘要**: Wireless channel modeling is a key building block for next-generation wireless systems. Predicting the channel state information (CSI) across different transmitter locations can substantially reduce the pilot and feedback overhead of conventional channel estimation. We propose Eff-WRFGS, an efficient wireless radiance field modeling framework built upon 3D Gaussian Splatting. Eff-WRFGS introduces a learnable mask for each 3D Gaussian primitive to indicate its importance, which guides the pruning of less significant primitives for more efficient rendering. The model is trained using a weighted combination of rendering and regularization losses, allowing a flexible trade-off between rendering quality and efficiency. Numerical results on the $\text{NeRF}^2$ dataset demonstrate that Eff-WRFGS achieves up to 44$\times$ storage reduction and 7$\times$ rendering speed-up with only marginal quality degradation. Moreover, initializing the Gaussian primitives from a 3D point cloud of the scene further improves the entire quality-efficiency trade-off.

---

## 18. Denoising-GS: Gaussian Splatting with Spatial-aware Denoising

- **作者**: Qingyuan Zhou, Xinyi Liu, Weidong Yang et al.
- **发布时间**: 2026-05-14
- **arXiv链接**: [arXiv:2605.14880v1](https://arxiv.org/abs/2605.14880v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable success in high-fidelity Novel View Synthesis (NVS), yet the optimization process inevitably introduces noisy Gaussian primitives due to the sparse and incomplete initialization from Structure-from-Motion (SfM) point clouds. Most existing methods focus solely on adjusting the positions of primitives during optimization, while neglecting the underlying spatial structure. To this end, we introduce a new perspective by formulating the optimization of 3DGS as a primitive denoising process and propose Denoising-GS, a spatial-aware denoising framework for Gaussian primitives by taking both the positions and spatial structure into consideration. Specifically, we design an optimizer that preserves the spatial optimization flow of primitives, facilitating coherent and directed denoising rather than random perturbations. Building upon this, the Spatial Gradient-based Denoising strategy jointly considers the spatial supports of primitives to ensure gradient-consistent updates. Furthermore, the Uncertainty-based Denoising module estimates primitive-wise uncertainty to prune redundant or noisy primitives, while the Spatial Coherence Refinement strategy selectively splits primitives in sparse regions to maintain structural completeness. Experiments conducted on three benchmark datasets demonstrate that Denoising-GS consistently enhances NVS fidelity while maintaining representation compactness, achieving state-of-the-...

---

## 19. BlitzGS: City-Scale Gaussian Splatting at Lightning Speed

- **作者**: Zhongtao Wang, Huishan Au, Yilong Li et al.
- **发布时间**: 2026-05-13
- **arXiv链接**: [arXiv:2605.13794v1](https://arxiv.org/abs/2605.13794v1)
- **英文摘要**: We present BlitzGS, a distributed 3DGS framework that reduces active Gaussian workload for fast city-scale reconstruction. BlitzGS manages this workload at three coupled levels. At the system level, the framework shards Gaussians across GPUs by index parity rather than spatial blocks. This approach mitigates the cross-block visibility redundancy inherent in spatial partitioning. Furthermore, it distributes each rendering step through a single cross-GPU exchange that routes projected Gaussians to their tile owners. At the model level, scheduled importance-scoring passes shrink the global Gaussian population. During these passes, the framework generates a per-Gaussian visibility weight to bias density-control updates toward contributing primitives and a per-view importance mask for the view-level renderer. At the view level, BlitzGS trims each camera's active set with a distance-based LOD gate to exclude excessively fine primitives for the current frustum and the importance-based culling mask to skip Gaussians with negligible cross-view contribution.   On large-scale benchmarks, BlitzGS matches the rendering quality of recent large-scale baselines while delivering an order-of-magnitude speedup, training city-scale scenes in tens of minutes. Our code is available at https: //github.com/AkierRaee/BlitzGS.

---

## 20. Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting

- **作者**: Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar
- **发布时间**: 2026-05-13
- **arXiv链接**: [arXiv:2605.13600v1](https://arxiv.org/abs/2605.13600v1)
- **说明**: 18 pages (9 pages main paper), 10 figures, preprint
- **英文摘要**: 3D Language Gaussian Splatting (3DLGS) augments 3D Gaussian Splatting with language-aligned visual features for open-vocabulary 3D scene understanding. A core challenge is efficiently associating high-dimensional vision-language embeddings with millions of 3D Gaussians while preserving efficient feature rendering for text-based querying. Existing methods either store dense features directly on Gaussians, causing high storage costs and slow rendering, or learn compact representations through expensive per-scene optimization with repeated feature rasterization. No existing method simultaneously achieves fast 3D semantic reconstruction, efficient storage, and fast rendering. We propose SCOUP (Sparse COde UPlifting), which addresses all three by decoupling language representation learning from 3D Gaussian optimization. Rather than working directly in 3D, we learn sparse codebook-based representations entirely using features associated with 2D image regions, associating each region with a sparse set of codebook coefficients. We then uplift these coefficients to 3D Gaussians with our weighted sparse aggregation using Gaussian-to-pixel associations, where each Gaussian accumulates coefficients over codebook atoms across views. Top-$K$ filtering then extracts the most dominant multi-view coefficients per Gaussian, enabling efficient storage and fast rendering. Our method achieves up to $400\times$ training speedup while being $3\times$ more memory efficient during training compared t...

---

## 21. HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization

- **作者**: Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng
- **发布时间**: 2026-05-13
- **arXiv链接**: [arXiv:2605.13073v2](https://arxiv.org/abs/2605.13073v2)
- **英文摘要**: In-the-wild 3D Gaussian Splatting remains challenging due to transient distractors and illumination-induced cross-view appearance inconsistencies. Existing methods mainly rely on image-level masking to suppress unreliable supervision, but masking alone cannot fully eliminate residual occlusions or resolve illumination-induced inconsistencies, both of which can introduce conflicting cross-view gradients. These unresolved conflicts may destabilize Gaussian optimization and lead to visible reconstruction artifacts. We propose a conflict-aware 3DGS framework that addresses this problem from both image-space supervision and gradient-level optimization. Semantic Consistency-Guided Masking learns pixel-wise consistency scores to adaptively refine prior masks and suppress unreliable supervision before gradient formation. A dual-view Conflict-Aware Gradient Harmonization strategy further reconciles view-specific gradients by mutually rotating them into an orthogonal configuration, reducing negative directional interference across views. We also introduce conflict-aware densification and pruning to stabilize Gaussian growth and remove persistently conflicting primitives. Extensive experiments on standard in-the-wild benchmarks demonstrate that our method achieves state-of-the-art rendering quality under complex transient distractors and cross-view inconsistencies.

---

## 22. 3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering

- **作者**: Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu
- **发布时间**: 2026-05-12
- **arXiv链接**: [arXiv:2605.11489v1](https://arxiv.org/abs/2605.11489v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables high-quality real-time 3D rendering but faces challenges in efficiently scaling to ultra-dense scenes and high-resolution due to computational bottlenecks that limit its use in latency-sensitive applications. Instead of optimizing the splatting pipeline itself, we propose \textbf{3DGS$^3$}, a unified post-rendering framework that jointly performs super sampling and frame interpolation through differentiable processing of low-resolution outputs to achieve both high-resolution and high-frame-rate rendering. Our \textbf{Gradient\- \-Aware Super Sampling (GASS)} module leverages the continuous differentiability of 3DGS to extract image gradients that guide a GRU-based refinement network to enable high-fidelity super sampling. Furthermore, a \textbf{Lightweight Temporal Frame Interpolation (LTFI)} module based on a compact U-Net-like backbone fuses temporal and differentiable spatial cues from consecutive frames to synthesize temporally coherent intermediate frames. Experiments on public datasets demonstrate that 3DGS$^3$ achieves superior rendering efficiency and visual quality when compared with state-of-the-art methods and remains compatible with existing 3DGS acceleration techniques. The code will be publicly released upon acceptance.

---

## 23. PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming

- **作者**: Jiachen Li, Guangzhi Han, Jin Wan et al.
- **发布时间**: 2026-05-12
- **arXiv链接**: [arXiv:2605.11427v1](https://arxiv.org/abs/2605.11427v1)
- **英文摘要**: 4D Gaussian Splatting (4DGS) enables high-quality dynamic novel view synthesis, yet current models remain monolithic bitstreams that clients must download in full before any frame can be rendered, causing black-screen waits of tens to hundreds of seconds on mobile bandwidth and leaving 4DGS incompatible with modern adaptive-bitrate delivery. Progressive 3DGS compression alleviates this for static scenes, but it acts only on spatial anchors and cannot partition the temporal deformation networks that dominate dynamic-scene size. We present PD-4DGS, the first framework for progressive compression and on-demand transmission of 4DGS. Hierarchical Deformation Decomposition (HDD) externalises the coarse-to-fine motion hierarchy already latent in 4DGS into three independently transmittable layers -- a static scaffold, a global deformation, and a local refinement -- so that any prefix of the bitstream is already renderable, turning a single training run into a scalable, DASH/HLS-compatible bitstream. A Gaussian-entropy attribute rate-distortion loss together with a temporal mask consistency regulariser shrink the base layer while suppressing low-bitrate flicker; a capacity-weighted rollout schedule, gated online by a learnt activation rate rho, then prevents deformation-network under-training without any per-scene hyperparameter. On the Dycheck iPhone benchmark, PD-4DGS cuts the streamed bitstream by >60% at matched rendering fidelity and reduces first-frame latency from 73--930 s to ...

---

## 24. MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction

- **作者**: Zhihao Cao, Qi Shao, Shuhao Zhai et al.
- **发布时间**: 2026-05-11
- **arXiv链接**: [arXiv:2605.10760v1](https://arxiv.org/abs/2605.10760v1)
- **英文摘要**: Collaborative photorealistic 3D reconstruction from multiple agents enables rapid large-scale scene capture for virtual production and cooperative multi-robot exploration. While recent 3D Gaussian Splatting (3DGS) SLAM algorithms can generate high-fidelity real-time mapping, most of the existing multi-agent Gaussian SLAM methods still rely on RGB-D sensors to obtain metric depth and simplify cross-agent alignment, which limits the deployment on lightweight, low-cost, or power-constrained robotic platforms. To address this challenge, we propose MAGS-SLAM, the first RGB-only multi-agent 3DGS SLAM framework for collaborative scene reconstruction. Each agent independently builds local monocular Gaussian submaps and transmits compact submap summaries rather than raw observations or dense maps. To facilitate robust collaboration in the presence of monocular scale ambiguity, our framework integrates compact submap communication, geometry- and appearance-aware loop verification, and occupancy-aware Gaussian fusion, enabling coherent global reconstruction without active depth sensors. We further introduce ReplicaMultiagent Plus benchmark for evaluating collaborative Gaussian SLAM. Intensive experiments on synthetic and real-world datasets show that MAGS-SLAM achieves competitive tracking accuracy and comparable or superior rendering quality to state-of-the-art RGB-D collaborative Gaussian SLAM methods while relying only RGB images.

---

## 25. Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization

- **作者**: Miso Lee, Sangeek Hyun, Yerim Jeon, Jae-Pil Heo
- **发布时间**: 2026-05-08
- **arXiv链接**: [arXiv:2605.07351v1](https://arxiv.org/abs/2605.07351v1)
- **英文摘要**: While Gaussian Splatting-based Feature Fields (GSFFs) have shown promise for visual localization, this paper highlights that photometrically optimized GSFFs are inherently ill-suited for 2D-3D matching. The volumetric extent of each Gaussian induces many-to-one pixel-to-point mappings that destabilize PnP-based pose estimation, while photometric optimization gives rise to superfluous Gaussians devoid of multi-view consistency. To address these issues, we propose SplitGS-Loc, a localization-specialized GSFFs construction framework that disambiguates 2D-3D correspondences by exploiting Gaussian attributes. Our key design, Mixture-of-Gaussians-based splitting, decomposes each Gaussian into smaller Gaussians, replacing ambiguous many-to-one with precise one-to-one correspondences. In parallel, we exploit composition weights from GS rasterization to select Gaussians that significantly and consistently contribute across multiple views and aggregate discriminative features through strong pixel-Gaussian associations, enforcing multi-view consistency. The resulting compact yet discriminative feature fields enable stable PnP convergence, achieving state-of-the-art performance on localization benchmarks. Extensive experiments validate that SplitGS-Loc extends the utility of photometric GSFFs to accurate and efficient localization by exploiting Gaussian attributes, without per-scene training or iterative pose refinement.

---

## 26. Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures

- **作者**: Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi et al.
- **发布时间**: 2026-05-05
- **arXiv链接**: [arXiv:2605.04035v2](https://arxiv.org/abs/2605.04035v2)
- **说明**: Project page: https://apple.github.io/ml-headsup/
- **英文摘要**: We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

---

## 27. GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting

- **作者**: Baobing Zhang, Wanxin Sui
- **发布时间**: 2026-05-03
- **arXiv链接**: [arXiv:2605.02086v1](https://arxiv.org/abs/2605.02086v1)
- **英文摘要**: 3D Gaussian splatting (3DGS) is a state-of-the-art representation for real-time photorealistic novel-view synthesis, yet a single high-fidelity scene typically occupies hundreds of megabytes to several gigabytes, exceeding the budgets of mobile, immersive, and volumetric video platforms. Existing 3DGS compression methods (e.g., HAC++, FlexGaussian, LP-3DGS) treat pruning, quantization, and entropy coding as separate stages and rely on hand-tuned heuristics (opacity thresholds, fixed bit-widths, SH truncation), limiting cross-scene generalization and preventing users from specifying a target rate or quality budget. We propose GETA-3DGS, to our knowledge the first end-to-end automatic joint structured pruning and quantization framework for 3DGS. Building on GETA for joint pruning-quantization of deep networks, we contribute: (i) a 3DGS-aware quantization-aware dependency graph (QADG) treating each Gaussian primitive as a group with five attribute sub-nodes and degree-aware SH sub-nodes; (ii) a render-aware saliency fusing transmittance-weighted contribution, screen-space gradient, and pixel coverage into a Gaussian-level importance score; and (iii) a heterogeneous per-attribute mixed-precision scheme co-optimized with structural sparsity under a projected partial saliency-guided (PPSG) descent guarantee. On Mip-NeRF 360, Tanks and Temples, and Deep Blending, GETA-3DGS operates directly on raw Gaussian primitives rather than a post-hoc anchor representation, delivering ~5x stora...

---

## 28. 2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction

- **作者**: Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies
- **发布时间**: 2026-05-01
- **arXiv链接**: [arXiv:2605.00569v1](https://arxiv.org/abs/2605.00569v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for generating photorealistic renderings of a scene in real-time. However, the volumetric nature of 3DGS limits its ability to accurately capture surface geometry. To address this, 2D Gaussian Splatting (2DGS) was proposed to enable view-consistent and geometrically accurate surface reconstruction from multi-view images. However, 2DGS can be sensitive to the initialization of the Gaussian primitives. Reliance on Structure-from-Motion (SfM) initializations, which can produce poor estimates on challenging image sets, may lead to subpar results. In this work, we enhance 2DGS by incorporating monocular depth and normal priors to improve both geometric accuracy and robustness. We propose a depth-guided initialization strategy for Gaussians and introduce a clustering-based technique for pruning degenerate Gaussians. We evaluate our method on the DTU dataset, where it achieves state-of-the-art results in mesh reconstruction while preserving high-quality novel view synthesis.

---

## 29. MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching

- **作者**: Shuzhao Xie, Junchen Ge, Weixiang Zhang et al.
- **发布时间**: 2026-04-29
- **arXiv链接**: [arXiv:2604.26799v2](https://arxiv.org/abs/2604.26799v2)
- **说明**: https://github.com/mmlab-sigs/mesongs_plus
- **英文摘要**: 3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is avai...

---

## 30. Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications

- **作者**: Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin
- **发布时间**: 2026-04-28
- **arXiv链接**: [arXiv:2604.25330v1](https://arxiv.org/abs/2604.25330v1)
- **说明**: Under review
- **英文摘要**: Real-time immersive video communications, particularly high-fidelity 3D telepresence, necessitates a synergistic balance between instantaneous dynamic scene reconstruction and high-efficiency data transmission. While recent advancements in feed-forward 3D Gaussian Splatting (3DGS) have enabled real-time rendering, performing multi-view video coding and 3D reconstruction in a decoupled manner leads to suboptimal compression efficiency and high computational complexity. To address this, we propose GS-SCNet, the first unified end-to-end framework that seamlessly integrates generalizable 3DGS reconstruction with a dedicated deep Semantic Coding pipeline. Our architecture is underpinned by two core technical contributions: (i) we introduce a Disparity-Guided Parallel Semantic Codec that exploits epipolar geometric priors to facilitate cross-view contextual interaction via disparity compensation and semantic fusion, thereby enabling real-time parallel processing of stereo streams while significantly enhancing rate-distortion performance, and (ii) we develop a Lightweight Gaussian Parameter Predictor which directly projects decoded semantic latents into 3DGS attributes, obviating the need for intermediate pixel-domain reconstruction. By coupling the codec with the task-specific predictor, our framework extracts geometric correlations only once, effectively eliminating the redundant computational bottleneck inherent in conventional decoupled paradigms. Extensive evaluations on both s...

---

## 31. Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training

- **作者**: Yangming Zhang, Jian Xu, Chaojian Li et al.
- **发布时间**: 2026-04-21
- **arXiv链接**: [arXiv:2604.20046v2](https://arxiv.org/abs/2604.20046v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has revolutionized novel view synthesis with high-quality rendering through continuous aggregations of millions of 3D Gaussian primitives. However, it suffers from a substantial memory footprint, particularly during training due to uncontrolled densification, posing a critical bottleneck for deployment on memory-constrained edge devices. While existing methods prune redundant Gaussians post-training, they fail to address the peak memory spikes caused by the abrupt growth of Gaussians early in the training process. To solve the training memory consumption problem, we propose a systematic memory-bounded training framework that dynamically optimizes Gaussians through iterative growth and pruning. In other words, the proposed framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation, maintaining a near-constant low memory usage while progressively refining rendering fidelity. We comprehensively evaluate the proposed training framework on various real-world datasets under strict memory constraints, showing significant improvements over existing state-of-the-art methods. Particularly, our proposed method practically enables memory-efficient 3DGS training on NVIDIA Jetson AGX Xavier, achieving similar visual quality with up to 80% lower peak training memory consumption than the original 3DGS.

---

## 32. OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem

- **作者**: Byunghyun Kim
- **发布时间**: 2026-04-21
- **arXiv链接**: [arXiv:2604.19127v1](https://arxiv.org/abs/2604.19127v1)
- **说明**: Accepted to Eurographics 2026 Short Papers
- **英文摘要**: UV-parameterized Gaussian Splatting (UVGS) maps an unstructured set of 3D Gaussians to a regular UV tensor, enabling compact storage and explicit control of representation capacity. Existing UVGS, however, uses a deterministic spherical pro- jection to assign Gaussians to UV locations. Because this mapping ignores the global Gaussian distribution, it often leaves many UV slots empty while causing frequent collisions in dense regions. We reinterpret UV mapping as a capacity-allocation problem under a fixed UV budget and propose OT-UVGS, a lightweight, separable one-dimensional optimal-transport-inspired mapping that globally couples assignments while preserving the original UVGS representation. The method is implemented with rank-based sorting, has O(N log N) complexity for N Gaussians, and can be used as a drop-in replacement for spherical UVGS. Across 184 object-centric scenes and the Mip-NeRF dataset, OT-UVGS consistently improves peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) under the same UV resolution and per-slot capacity (K=1). These gains are accompanied by substantially better UV utilization, including higher non-empty slot ratios, fewer collisions, and higher Gaussian retention. Our results show that revisiting the mapping alone can unlock a significant fraction of the latent capacity of UVGS.

---

## 33. Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting

- **作者**: Ahmad Droby
- **发布时间**: 2026-04-17
- **arXiv链接**: [arXiv:2604.16747v2](https://arxiv.org/abs/2604.16747v2)
- **说明**: 10 pages, 6 figures, 2 tables
- **英文摘要**: Dynamic 3D Gaussian Splatting methods achieve strong training-view PSNR on monocular video but generalize poorly: on the D-NeRF benchmark we measure an average train-test PSNR gap of 6.18 dB, rising to 11 dB on individual scenes. We report two findings that together account for most of that gap.   Finding 1 (the role of splitting). A systematic ablation of the Adaptive Density Control pipeline (split, clone, prune, frequency, threshold, schedule) shows that splitting is responsible for over 80% of the gap: disabling split collapses the cloud from 44K to 3K Gaussians and the gap from 6.18 dB to 1.15 dB. Across all threshold-varying ablations, gap is log-linear in count (r = 0.995, bootstrap 95% CI [0.99, 1.00]), which suggests a capacity-based explanation.   Finding 2 (the role of deformation coherence). We show that the capacity explanation is incomplete. A local-smoothness penalty on the per-Gaussian deformation field -- Elastic Energy Regularization (EER) -- reduces the gap by 40.8% while growing the cloud by 85%. Measuring per-Gaussian strain directly on trained checkpoints, EER reduces mean strain by 99.72% (median 99.80%) across all 8 scenes; on 8/8 scenes the median Gaussian under EER is less strained than the 1st-percentile (best-behaved) Gaussian under baseline. Alongside EER, we evaluate two further regularizers: GAD, a loss-rate-aware densification threshold, and PTDrop, a jitter-weighted Gaussian dropout. GAD+EER reduces the gap by 48%; adding PTDrop and a soft gro...

---

## 34. Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography

- **作者**: Yijia Guo, Wenkai Huang, Tong Hu et al.
- **发布时间**: 2026-04-17
- **arXiv链接**: [arXiv:2604.15862v1](https://arxiv.org/abs/2604.15862v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently redefined the paradigm of 3D reconstruction, striking an unprecedented balance between visual fidelity and computational efficiency. As its adoption proliferates, safeguarding the copyright of explicit 3DGS assets has become paramount. However, existing invisible message embedding frameworks struggle to reconcile secure and high-capacity data embedding with intrinsic asset utility, often disrupting the native rendering pipeline or exhibiting vulnerability to structural perturbations. In this work, we present \textbf{\textit{Splats in Splats++}}, a unified and pipeline-agnostic steganography framework that seamlessly embeds high-capacity 3D/4D content directly within the native 3DGS representation. Grounded in a principled analysis of the frequency distribution of Spherical Harmonics (SH), we propose an importance-graded SH coefficient encryption scheme that achieves imperceptible embedding without compromising the original expressive power. To fundamentally resolve the geometric ambiguities that lead to message leakage, we introduce a \textbf{Hash-Grid Guided Opacity Mapping} mechanism. Coupled with a novel \textbf{Gradient-Gated Opacity Consistency Loss}, our formulation enforces a stringent spatial-attribute coupling between the original and hidden scenes, effectively projecting the discrete attribute mapping into a continuous, attack-resilient latent manifold. Extensive experiments demonstrate that our method substantially outperfo...

---

## 35. GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow

- **作者**: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung
- **发布时间**: 2026-04-17
- **arXiv链接**: [arXiv:2604.15612v1](https://arxiv.org/abs/2604.15612v1)
- **说明**: 8 pages, 5 figures, 7 tables, accepted to IEEE RA-L
- **英文摘要**: Gaussian splatting has recently gained traction as a compelling map representation for SLAM systems, enabling dense and photo-realistic scene modeling. However, its application to monocular SLAM remains challenging due to the lack of reliable geometric cues from monocular input. Without geometric supervision, mapping or tracking could fall in local-minima, resulting in structural degeneracies and inaccuracies. To address this challenge, we propose GaussianFlow SLAM, a monocular 3DGS-SLAM that leverages optical flow as a geometry-aware cue to guide the optimization of both the scene structure and camera poses. By encouraging the projected motion of Gaussians, termed GaussianFlow, to align with the optical flow, our method introduces consistent structural cues to regularize both map reconstruction and pose estimation. Furthermore, we introduce normalized error-based densification and pruning modules to refine inactive and unstable Gaussians, thereby contributing to improved map quality and pose accuracy. Experiments conducted on public datasets demonstrate that our method achieves superior rendering quality and tracking accuracy compared with state-of-the-art algorithms. The source code is available at: https://github.com/url-kaist/gaussianflow-slam.

---

## 36. GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens

- **作者**: Roni Itkin, Noam Issachar, Yehonatan Keypur et al.
- **发布时间**: 2026-04-16
- **arXiv链接**: [arXiv:2604.15284v2](https://arxiv.org/abs/2604.15284v2)
- **英文摘要**: The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussi...

---

## 37. Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis

- **作者**: Yuqin Lu, Yang Zhou, Yihua Dai, Guiqing Li, Shengfeng He
- **发布时间**: 2026-04-13
- **arXiv链接**: [arXiv:2604.11685v1](https://arxiv.org/abs/2604.11685v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has become a state-of-the-art framework for real-time, high-fidelity novel view synthesis. However, its substantial storage requirements and inherently unstructured representation pose challenges for deployment in streaming and resource-constrained environments. Existing Level-of-Detail (LOD) strategies, particularly those based on bottom-up construction, often introduce redundancy or lead to fidelity degradation. To overcome these limitations, we propose Iterative Gaussian Synopsis, a novel framework for compact and progressive rendering through a top-down "unfolding" scheme. Our approach begins with a full-resolution 3DGS model and iteratively derives coarser LODs using an adaptive, learnable mask-based pruning mechanism. This process constructs a multi-level hierarchy that preserves visual quality while improving efficiency. We integrate hierarchical spatial grids, which capture the global scene structure, with a shared Anchor Codebook that models localized details. This combination produces a compact yet expressive feature representation, designed to minimize redundancy and support efficient, level-specific adaptation. The unfolding mechanism promotes inter-layer reusability and requires only minimal data overhead for progressive refinement. Experiments show that our method maintains high rendering quality across all LODs while achieving substantial storage reduction. These results demonstrate the practicality and scalability of our approach f...

---

## 38. GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors

- **作者**: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi
- **发布时间**: 2026-04-13
- **arXiv链接**: [arXiv:2604.11401v1](https://arxiv.org/abs/2604.11401v1)
- **英文摘要**: Recent semantic 3D Gaussian Splatting (3DGS) methods primarily rely on 2D foundation models, often yielding ambiguous boundaries and limited support for structured urban semantics. While city models such as CityGML encode hierarchically organized semantics together with building geometry, these labels cannot be directly mapped to Gaussian primitives. We present GS4City, a hierarchical semantic Gaussian Splatting method that incorporates city-model priors for urban scene understanding. GS4City derives reliable image-aligned masks from Level of Detail (LoD) 3 CityGML models via two-pass raycasting, explicitly using parent-child relations to validate and recover fine-grained facade elements. It then fuses these geometry-grounded masks with foundation-model predictions to establish scene-consistent instance correspondences, and learns a compact identity encoding for each Gaussian under joint 2D identity supervision and 3D spatial regularization. Experiments on the TUM2TWIN and Gold Coast datasets show that GS4City effectively incorporates structured building semantics into Gaussian scene representations, outperforming existing 2D-driven semantic 3DGS baselines, including LangSplat and Gaga, by up to 15.8 IoU points in coarse building segmentation and 14.2 mIoU points in fine-grained semantic segmentation. By bridging structured city models and photorealistic Gaussian scene representations, GS4City enables semantically queryable and structure-aware urban reconstruction. Code is av...

---

## 39. Naka-GS: A Bionics-inspired Dual-Branch Naka Correction and Progressive Point Pruning for Low-Light 3DGS

- **作者**: Runyu Zhu, SiXun Dong, Zhiqiang Zhang, Qingxia Ye, Zhihua Xu
- **发布时间**: 2026-04-13
- **arXiv链接**: [arXiv:2604.11142v1](https://arxiv.org/abs/2604.11142v1)
- **英文摘要**: Low-light conditions severely hinder 3D restoration and reconstruction by degrading image visibility, introducing color distortions, and contaminating geometric priors for downstream optimization. We present NAKA-GS, a bionics-inspired framework for low-light 3D Gaussian Splatting that jointly improves photometric restoration and geometric initialization. Our method starts with a Naka-guided chroma-correction network, which combines physics-prior low-light enhancement, dual-branch input modeling, frequency-decoupled correction, and mask-guided optimization to suppress bright-region chromatic artifacts and edge-structure errors. The enhanced images are then fed into a feed-forward multi-view reconstruction model to produce dense scene priors. To further improve Gaussian initialization, we introduce a lightweight Point Preprocessing Module (PPM) that performs coordinate alignment, voxel pooling, and distance-adaptive progressive pruning to remove noisy and redundant points while preserving representative structures. Without introducing heavy inference overhead, NAKA-GS improves restoration quality, training stability, and optimization efficiency for low-light 3D reconstruction. The proposed method was presented in the NTIRE 3D Restoration and Reconstruction (3DRR) Challenge, and outperformed the baseline methods by a large margin. The code is available at https://github.com/RunyuZhu/Naka-GS

---

## 40. A 129FPS Full HD Real-Time Accelerator for 3D Gaussian Splatting

- **作者**: Fang-Chi Chang, Tian-Sheuan Chang
- **发布时间**: 2026-04-11
- **arXiv链接**: [arXiv:2604.10223v1](https://arxiv.org/abs/2604.10223v1)
- **英文摘要**: Rendering large-scale, unbounded scenes on AR/VR-class devices is constrained by the computation, bandwidth, and storage cost of 3D Gaussian Splatting (3DGS). We propose a low-power, low-cost 3DGS hardware accelerator that renders full-HD images in real time, together with a hardware-friendly compression pipeline that combines iterative Gaussian pruning and fine-tuning, progressive spherical harmonics (SH) degree reduction, and vector quantization of all SH coefficients and colors. The scheme achieves a $51.6\times$ model-size reduction with a 0.743 dB PSNR loss. The accelerator uses a frame-level pipeline that integrates point-based culling and projection with tile-based sorting and rasterization, skips zero-Jacobian matrix multiplications (reducing processing elements by 63\% and computation by 53\%), and adopts comparison-free tile-based sorting with deterministic latency. Implemented in a TSMC 28-nm process at 800 MHz, the design occupies $0.66~\text{mm}^2$ with 1.1438 M gates and 120 kB SRAM, consumes 0.219 W, and delivers 1219 Mpixels/J at 267.5 Mpixels/s, enabling 1080p at 129 FPS. Overall, it is $5.98\times$ smaller in area, $5.94\times$ higher throughput, and delivers $7.5\times$ higher energy efficiency than prior 3DGS accelerators.

---

## 41. DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting

- **作者**: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan
- **发布时间**: 2026-04-08
- **arXiv链接**: [arXiv:2604.06739v1](https://arxiv.org/abs/2604.06739v1)
- **说明**: 10 pages, 5 figures
- **英文摘要**: Sparse-view reconstruction with 3D Gaussian Splatting (3DGS) is fundamentally ill-posed due to insufficient geometric supervision, often leading to severe overfitting and the emergence of structural distortions and translucent haze-like artifacts. While existing approaches attempt to alleviate this issue via dropout-based regularization, they are largely heuristic and lack a unified understanding of artifact formation. In this paper, we revisit sparse-view 3DGS reconstruction from a new perspective and identify the core challenge as the unobservability of Gaussian primitive reliability. Unreliable Gaussians are insufficiently constrained during optimization and accumulate as haze-like degradations in rendered images. Motivated by this observation, we propose a unified Dual-domain Observation and Calibration (DOC-GS) framework that models and corrects Gaussian reliability through the synergy of optimization-domain inductive bias and observation-domain evidence. Specifically, in the optimization domain, we characterize Gaussian reliability by the degree to which each primitive is constrained during training, and instantiate this signal via a Continuous Depth-Guided Dropout (CDGD) strategy, where the dropout probability serves as an explicit proxy for primitive reliability. This imposes a smooth depth-aware inductive bias to suppress weakly constrained Gaussians and improve optimization stability. In the observation domain, we establish a connection between floater artifacts and...

---

## 42. GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields

- **作者**: Yuhang Zhang, Mingsheng Li, Yujing Shang et al.
- **发布时间**: 2026-04-06
- **arXiv链接**: [arXiv:2604.05062v1](https://arxiv.org/abs/2604.05062v1)
- **英文摘要**: Learning visuomotor policies for Autonomous Aerial Vehicles (AAVs) relying solely on monocular vision is an attractive yet highly challenging paradigm. Existing end-to-end learning approaches directly map high-dimensional RGB observations to action commands, which frequently suffer from low sample efficiency and severe sim-to-real gaps due to the visual discrepancy between simulation and physical domains. To address these long-standing challenges, we propose GaussFly, a novel framework that explicitly decouples representation learning from policy optimization through a cohesive real-to-sim-to-real paradigm. First, to achieve a high-fidelity real-to-sim transition, we reconstruct training scenes using 3D Gaussian Splatting (3DGS) augmented with explicit geometric constraints. Second, to ensure robust sim-to-real transfer, we leverage these photorealistic simulated environments and employ contrastive representation learning to extract compact, noise-resilient latent features from the rendered RGB images. By utilizing this pre-trained encoder to provide low-dimensional feature inputs, the computational burden on the visuomotor policy is significantly reduced while its resistance against visual noise is inherently enhanced. Extensive experiments in simulated and real-world environments demonstrate that GaussFly achieves superior sample efficiency and asymptotic performance compared to baselines. Crucially, it enables robust and zero-shot policy transfer to unseen real-world envir...

---

## 43. Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM

- **作者**: Zicheng Zhang, Ke Wu, Xiangting Meng et al.
- **发布时间**: 2026-04-03
- **arXiv链接**: [arXiv:2604.03092v1](https://arxiv.org/abs/2604.03092v1)
- **英文摘要**: Monocular 3D Gaussian Splatting SLAM suffers from critical limitations in time efficiency, geometric accuracy, and multi-view consistency. These issues stem from the time-consuming $\textit{Train-from-Scratch}$ optimization and the lack of inter-frame scale consistency from single-frame geometry priors. We contend that a feed-forward paradigm, leveraging multi-frame context to predict Gaussian attributes directly, is crucial for addressing these challenges. We present Flash-Mono, a system composed of three core modules: a feed-forward prediction frontend, a 2D Gaussian Splatting mapping backend, and an efficient hidden-state-based loop closure module. We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses and per-pixel Gaussian properties. By directly predicting Gaussian attributes, our method bypasses the burdensome per-frame optimization required in optimization-based GS-SLAM, achieving a $\textbf{10x}$ speedup while ensuring high-quality rendering. The power of our recurrent architecture extends beyond efficient prediction. The hidden states act as compact submap descriptors, facilitating efficient loop closure and global $\mathrm{Sim}(3)$ optimization to mitigate the long-standing challenge of drift. For enhanced geometric fidelity, we replace conventional 3D Gaussian ellipsoids with 2D Gaussian surfels. Extensive experiments demonstrate that Fla...

---

## 44. SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction

- **作者**: Zicheng Zhang, Xiangting Meng, Ke Wu, Wenchao Ding
- **发布时间**: 2026-04-03
- **arXiv链接**: [arXiv:2604.03069v1](https://arxiv.org/abs/2604.03069v1)
- **英文摘要**: Recent progress in feed-forward 3D Gaussian Splatting (3DGS) has notably improved rendering quality. However, the spatially uniform and highly redundant 3DGS map generated by previous feed-forward 3DGS methods limits their integration into downstream reconstruction tasks. We propose SparseSplat, the first feed-forward 3DGS model that adaptively adjusts Gaussian density according to scene structure and information richness of local regions, yielding highly compact 3DGS maps. To achieve this, we propose entropy-based probabilistic sampling, generating large, sparse Gaussians in textureless areas and assigning small, dense Gaussians to regions with rich information. Additionally, we designed a specialized point cloud network that efficiently encodes local context and decodes it into 3DGS attributes, addressing the receptive field mismatch between the general 3DGS optimization pipeline and feed-forward models. Extensive experimental results demonstrate that SparseSplat can achieve state-of-the-art rendering quality with only 22% of the Gaussians and maintain reasonable rendering quality with only 1.5% of the Gaussians. Project page: https://victkk.github.io/SparseSplat-page/.

---

## 45. GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting

- **作者**: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling
- **发布时间**: 2026-04-02
- **arXiv链接**: [arXiv:2604.01884v1](https://arxiv.org/abs/2604.01884v1)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has demonstrated breakthrough performance in novel view synthesis and real-time rendering. Nevertheless, its practicality is constrained by the high memory cost due to a huge number of Gaussian points. Many pruning-based 3DGS variants have been proposed for memory saving, but often compromise spatial consistency and may lead to rendering artifacts. To address this issue, we propose graph-based spatial distribution optimization for compact 3D Gaussian Splatting (GS\textasciicircum2), which enhances reconstruction quality by optimizing the spatial distribution of Gaussian points. Specifically, we introduce an evidence lower bound (ELBO)-based adaptive densification strategy that automatically controls the densification process. In addition, an opacity-aware progressive pruning strategy is proposed to further reduce memory consumption by dynamically removing low-opacity Gaussian points. Furthermore, we propose a graph-based feature encoding module to adjust the spatial distribution via feature-guided point shifting. Extensive experiments validate that GS\textasciicircum2 achieves a compact Gaussian representation while delivering superior rendering quality. Compared with 3DGS, it achieves higher PSNR with only about 12.5\% Gaussian points. Furthermore, it outperforms all compared baselines in both rendering quality and memory efficiency.

---

## 46. FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting

- **作者**: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi et al.
- **发布时间**: 2026-04-02
- **arXiv链接**: [arXiv:2604.01844v1](https://arxiv.org/abs/2604.01844v1)
- **英文摘要**: Gaussian Splatting (GS) has emerged as a dominating technique for image rendering and has quickly been adapted for the X-ray Computed Tomography (CT) reconstruction task. However, despite being on par or better than many of its predecessors, the benefits of GS are typically not substantial enough to motivate a transition from well-established reconstruction algorithms. This paper addresses the most significant remaining limitations of the GS-based approach by introducing FaCT-GS, a framework for fast and flexible CT reconstruction. Enabled by an in-depth optimization of the voxelization and rasterization pipelines, our new method is significantly faster than its predecessors and scales well with projection and output volume size. Furthermore, the improved voxelization enables rapid fitting of Gaussians to pre-existing volumes, which can serve as a prior for warm-starting the reconstruction, or simply as an alternative, compressed representation. FaCT-GS is over 4X faster than the State of the Art GS CT reconstruction on standard 512x512 projections, and over 13X faster on 2k projections. Implementation available at: https://github.com/PaPieta/fact-gs.

---

## 47. Autoregressive Appearance Prediction for 3D Gaussian Avatars

- **作者**: Michael Steiner, Zhang Chen, Alexander Richard et al.
- **发布时间**: 2026-04-01
- **arXiv链接**: [arXiv:2604.00928v1](https://arxiv.org/abs/2604.00928v1)
- **说明**: Project Page: https://steimich96.github.io/AAP-3DGA/
- **英文摘要**: A photorealistic and immersive human avatar experience demands capturing fine, person-specific details such as cloth and hair dynamics, subtle facial expressions, and characteristic motion patterns. Achieving this requires large, high-quality datasets, which often introduce ambiguities and spurious correlations when very similar poses correspond to different appearances. Models that fit these details during training can overfit and produce unstable, abrupt appearance changes for novel poses. We propose a 3D Gaussian Splatting avatar model with a spatial MLP backbone that is conditioned on both pose and an appearance latent. The latent is learned during training by an encoder, yielding a compact representation that improves reconstruction quality and helps disambiguate pose-driven renderings. At driving time, our predictor autoregressively infers the latent, producing temporally smooth appearance evolution and improved stability. Overall, our method delivers a robust and practical path to high-fidelity, stable avatar driving.

---

## 48. Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM

- **作者**: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame
- **发布时间**: 2026-04-01
- **arXiv链接**: [arXiv:2604.00804v1](https://arxiv.org/abs/2604.00804v1)
- **英文摘要**: Efficient multi-agent 3D mapping is essential for robotic teams operating in unknown environments, but dense representations hinder real-time exchange over constrained communication links. In multi-agent Simultaneous Localization and Mapping (SLAM), systems typically rely on a centralized server to merge and optimize the local maps produced by individual agents. However, sharing these large map representations, particularly those generated by recent methods such as Gaussian Splatting, becomes a bottleneck in real-world scenarios with limited bandwidth. We present an improved multi-agent RGB-D Gaussian Splatting SLAM framework that reduces communication load while preserving map fidelity. First, we incorporate a compaction step into our SLAM system to remove redundant 3D Gaussians, without degrading the rendering quality. Second, our approach performs centralized loop closure computation without initial guess, operating in two modes: a pure rendered-depth mode that requires no data beyond the 3D Gaussians, and a camera-depth mode that includes lightweight depth images for improved registration accuracy and additional Gaussian pruning. Evaluation on both synthetic and real-world datasets shows up to 85-95\% reduction in transmitted data compared to state-of-the-art approaches in both modes, bringing 3D Gaussian multi-agent SLAM closer to practical deployment in real-world scenarios. Code: https://github.com/lemonci/coko-slam

---

## 49. Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping

- **作者**: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze
- **发布时间**: 2026-03-30
- **arXiv链接**: [arXiv:2603.29005v1](https://arxiv.org/abs/2603.29005v1)
- **说明**: Accepted to IEEE Symposium on VLSI Technology & Circuits (VLSI), 2026. To appear
- **英文摘要**: High-fidelity 3D occupancy mapping is essential for many edge-based applications (such as AR/VR and autonomous navigation) but is limited by power constraints. We present Gleanmer, a system on chip (SoC) with an accelerator for GMMap, a 3D occupancy map using Gaussians. Through algorithm-hardware co-optimizations for direct computation and efficient reuse of these compact Gaussians, Gleanmer reduces construction and query energy by up to 63% and 81%, respectively. Approximate computation on Gaussians reduces accelerator area by 38%. Using 16nm CMOS, Gleanmer processes 640x480 images in real time beyond 88 fps during map construction and processes over 540K coordinates per second during map query. To our knowledge, Gleanmer is the first fabricated SoC to achieve real-time 3D occupancy mapping under 6 mW for edge-based applications.

---

## 50. LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting

- **作者**: Xuan Deng, Xiandong Meng, Hengyu Man et al.
- **发布时间**: 2026-03-30
- **arXiv链接**: [arXiv:2603.28431v3](https://arxiv.org/abs/2603.28431v3)
- **说明**: 10
- **英文摘要**: Although 3D Gaussian Splatting (3DGS) enables high-fidelity real-time rendering, its prohibitive storage overhead severely hinders practical deployment. Recent anchor-based 3DGS compression schemes reduce gaussian redundancy through some advanced context models. However, they overlook explicit geometric dependencies, leading to structural degradation and suboptimal ratedistortion performance. In this paper, we propose a Local Geometry-aware Hierarchical Context Compression framework for 3DGS(LG-HCC) that incorporates inter-anchor geometric correlations into anchor pruning and entropy coding for compact representation. Specifically, we introduce an Neighborhood-Aware Anchor Pruning (NAAP) strategy, which evaluates anchor importance via weighted neighborhood feature aggregation and then merges low-contribution anchors into salient neighbors, yielding a compact yet geometry-consistent anchor set. Moreover, we further develop a hierarchical entropy coding scheme, in which coarse-to-fine priors are exploited through a lightweight Geometry-Guided Convolution(GG-Conv) operator to enable spatially adaptive context modeling and rate-distortion optimization. Extensive experiments show that LG-HCC effectively alleviates structural preservation issues,achieving superior geometric integrity and rendering fidelity while reducing storage by up to 30.85x compared to the Scaffold-GS baseline on the Mip-NeRF360 dataset

---

## 51. GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation

- **作者**: Nicolas von Lützow, Barbara Rössle, Katharina Schmid, Matthias Nießner
- **发布时间**: 2026-03-27
- **arXiv链接**: [arXiv:2603.26661v1](https://arxiv.org/abs/2603.26661v1)
- **说明**: Project page: https://nicolasvonluetzow.github.io/GaussianGPT/ - Project video: https://youtu.be/zVnMHkFzHDg
- **英文摘要**: Most recent advances in 3D generative modeling rely on diffusion or flow-matching formulations. We instead explore a fully autoregressive alternative and introduce GaussianGPT, a transformer-based model that directly generates 3D Gaussians via next-token prediction, thus facilitating full 3D scene generation. We first compress Gaussian primitives into a discrete latent grid using a sparse 3D convolutional autoencoder with vector quantization. The resulting tokens are serialized and modeled using a causal transformer with 3D rotary positional embedding, enabling sequential generation of spatial structure and appearance. Unlike diffusion-based methods that refine scenes holistically, our formulation constructs scenes step-by-step, naturally supporting completion, outpainting, controllable sampling via temperature, and flexible generation horizons. This formulation leverages the compositional inductive biases and scalability of autoregressive modeling while operating on explicit representations compatible with modern neural rendering pipelines, positioning autoregressive transformers as a complementary paradigm for controllable and context-aware 3D generation.

---

## 52. FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting

- **作者**: Yixian Wang, Haolin Yu, Jiadong Tang et al.
- **发布时间**: 2026-03-25
- **arXiv链接**: [arXiv:2603.23891v1](https://arxiv.org/abs/2603.23891v1)
- **英文摘要**: 3D Gaussian Splatting has revolutionized neural rendering with real-time performance. However, scaling this approach to large scenes using Level-of-Detail methods faces critical challenges: inefficient serial traversal consuming over 60\% of rendering time, and redundant Gaussian-tile pairs that incur unnecessary processing overhead. To address these limitations, we introduce FilterGS, featuring a parallel filtering mechanism with two complementary filters that select Gaussian elements efficiently without tree traversal. Additionally, we propose a novel GTC metric that quantifies the redundancy of Gaussian-tile key-value pairs. Based on this metric, we introduce a scene-adaptive Gaussian shrinking strategy that effectively reduces redundant pairs. Extensive experiments demonstrate that FilterGS achieves state-of-the-art rendering speeds while maintaining competitive visual quality across multiple large-scale datasets. Project page: https://github.com/xenon-w/FilterGS

---

## 53. Drop-In Perceptual Optimization for 3D Gaussian Splatting

- **作者**: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.23297v1](https://arxiv.org/abs/2603.23297v1)
- **说明**: Project page: https://apple.github.io/ml-perceptual-3dgs
- **英文摘要**: Despite their output being ultimately consumed by human viewers, 3D Gaussian Splatting (3DGS) methods often rely on ad-hoc combinations of pixel-level losses, resulting in blurry renderings. To address this, we systematically explore perceptual optimization strategies for 3DGS by searching over a diverse set of distortion losses. We conduct the first-of-its-kind large-scale human subjective study on 3DGS, involving 39,320 pairwise ratings across several datasets and 3DGS frameworks. A regularized version of Wasserstein Distortion, which we call WD-R, emerges as the clear winner, excelling at recovering fine textures without incurring a higher splat count. WD-R is preferred by raters more than $2.3\times$ over the original 3DGS loss, and $1.5\times$ over current best method Perceptual-GS. WD-R also consistently achieves state-of-the-art LPIPS, DISTS, and FID scores across various datasets, and generalizes across recent frameworks, such as Mip-Splatting and Scaffold-GS, where replacing the original loss with WD-R consistently enhances perceptual quality within a similar resource budget (number of splats for Mip-Splatting, model size for Scaffold-GS), and leads to reconstructions being preferred by human raters $1.8\times$ and $3.6\times$, respectively. We also find that this carries over to the task of 3DGS scene compression, with $\approx 50\%$ bitrate savings for comparable perceptual metric performance.

---

## 54. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

- **作者**: Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, Hamed Rezazadegan Tavakoli
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.21933v1](https://arxiv.org/abs/2603.21933v1)
- **说明**: 14 pages, 3 figures, 2 tables
- **英文摘要**: The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training pruning method for 3D Gaussian splats that relies solely on attribute-derived neighbourhood descriptors. As our primary contribution, we introduce a hybrid descriptor framework that captures structural and appearance consistency directly from the splat representation. Building on these descriptors, we formulate pruning as a statistical evidence estimation problem and introduce a Beta evidence model that quantifies per-splat reliability through a probabilistic confidence score.   Experiments conducted on standardized test sequences defined by the ISO/IEC MPEG Common Test Conditions (CTC) demonstrate that our approach achieves substantial pruning while preserving reconstruction quality, establishing a practical and generalizable alternative to existing camera-dependent pruning strategies.

---

## 55. F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting

- **作者**: Injae Kim, Chaehyeon Kim, Minseong Bae, Minseok Joo, Hyunwoo J. Kim
- **发布时间**: 2026-03-22
- **arXiv链接**: [arXiv:2603.21304v2](https://arxiv.org/abs/2603.21304v2)
- **说明**: Project Page: $\href{https://mlvlab.github.io/F4Splat}{\text{this http URL}}$
- **英文摘要**: Feed-forward 3D Gaussian Splatting methods enable single-pass reconstruction and real-time rendering. However, they typically adopt rigid pixel-to-Gaussian or voxel-to-Gaussian pipelines that uniformly allocate Gaussians, leading to redundant Gaussians across views. Moreover, they lack an effective mechanism to control the total number of Gaussians while maintaining reconstruction fidelity. To address these limitations, we present F4Splat, which performs Feed-Forward predictive densification for Feed-Forward 3D Gaussian Splatting, introducing a densification-score-guided allocation strategy that adaptively distributes Gaussians according to spatial complexity and multi-view overlap. Our model predicts per-region densification scores to estimate the required Gaussian density and allows explicit control over the final Gaussian budget without retraining. This spatially adaptive allocation reduces redundancy in simple regions and minimizes duplicate Gaussians across overlapping views, producing compact yet high-quality 3D representations. Extensive experiments demonstrate that our model achieves superior novel-view synthesis performance compared to prior uncalibrated feed-forward methods, while using significantly fewer Gaussians.

---

## 56. Matryoshka Gaussian Splatting

- **作者**: Zhilin Guo, Boqiao Zhang, Hakan Aktas et al.
- **发布时间**: 2026-03-19
- **arXiv链接**: [arXiv:2603.19234v2](https://arxiv.org/abs/2603.19234v2)
- **说明**: project page: https://zhilinguo.github.io/MGS
- **英文摘要**: The ability to render scenes at adjustable fidelity from a single model, known as level of detail (LoD), is crucial for practical deployment of 3D Gaussian Splatting (3DGS). Existing discrete LoD methods expose only a limited set of operating points, while concurrent continuous LoD approaches enable smoother scaling but often suffer noticeable quality degradation at full capacity, making LoD a costly design decision. We introduce Matryoshka Gaussian Splatting (MGS), a training framework that enables continuous LoD for standard 3DGS pipelines without sacrificing full-capacity rendering quality. MGS learns a single ordered set of Gaussians such that rendering any prefix, the first k splats, produces a coherent reconstruction whose fidelity improves smoothly with increasing budget. Our key idea is stochastic budget training: each iteration samples a random splat budget and optimises both the corresponding prefix and the full set. This strategy requires only two forward passes and introduces no architectural modifications. Experiments across four benchmarks and six baselines show that MGS matches the full-capacity performance of its backbone while enabling a continuous speed-quality trade-off from a single model. Extensive ablations on ordering strategies, training objectives, and model capacity further validate the designs.

---

## 57. NanoGS: Training-Free Gaussian Splat Simplification

- **作者**: Butian Xiong, Rong Liu, Tiantian Zhou et al.
- **发布时间**: 2026-03-17
- **arXiv链接**: [arXiv:2603.16103v1](https://arxiv.org/abs/2603.16103v1)
- **英文摘要**: 3D Gaussian Splat (3DGS) enables high-fidelity, real-time novel view synthesis by representing scenes with large sets of anisotropic primitives, but often requires millions of Splats, incurring significant storage and transmission costs. Most existing compression methods rely on GPU-intensive post-training optimization with calibrated images, limiting practical deployment. We introduce NanoGS, a training-free and lightweight framework for Gaussian Splat simplification. Instead of relying on image-based rendering supervision, NanoGS formulates simplification as local pairwise merging over a sparse spatial graph. The method approximates a pair of Gaussians with a single primitive using mass preserved moment matching and evaluates merge quality through a principled merge cost between the original mixture and its approximation. By restricting merge candidates to local neighborhoods and selecting compatible pairs efficiently, NanoGS produces compact Gaussian representations while preserving scene structure and appearance. NanoGS operates directly on existing Gaussian Splat models, runs efficiently on CPU, and preserves the standard 3DGS parameterization, enabling seamless integration with existing rendering pipelines. Experiments demonstrate that NanoGS substantially reduces primitive count while maintaining high rendering fidelity, providing an efficient and practical solution for Gaussian Splat simplification. Our project website is available at https://saliteta.github.io/NanoGS...

---

## 58. Direct Object-Level Reconstruction via Probabilistic Gaussian Splatting

- **作者**: Shuai Guo, Ao Guo, Junchao Zhao et al.
- **发布时间**: 2026-03-15
- **arXiv链接**: [arXiv:2603.14316v1](https://arxiv.org/abs/2603.14316v1)
- **英文摘要**: Object-level 3D reconstruction play important roles across domains such as cultural heritage digitization, industrial manufacturing, and virtual reality. However, existing Gaussian Splatting-based approaches generally rely on full-scene reconstruction, in which substantial redundant background information is introduced, leading to increased computational and storage overhead. To address this limitation, we propose an efficient single-object 3D reconstruction method based on 2D Gaussian Splatting. By directly integrating foreground-background probability cues into Gaussian primitives and dynamically pruning low-probability Gaussians during training, the proposed method fundamentally focuses on an object of interest and improves the memory and computational efficiency. Our pipeline leverages probability masks generated by YOLO and SAM to supervise probabilistic Gaussian attributes, replacing binary masks with continuous probability values to mitigate boundary ambiguity. Additionally, we propose a dual-stage filtering strategy for training's startup to suppress background Gaussians. And, during training, rendered probability masks are conversely employed to refine supervision and enhance boundary consistency across views. Experiments conducted on the MIP-360, T&T, and NVOS datasets demonstrate that our method exhibits strong self-correction capability in the presence of mask errors and achieves reconstruction quality comparable to standard 3DGS approaches, while requiring only a...

---

## 59. Spectral Defense Against Resource-Targeting Attack in 3D Gaussian Splatting

- **作者**: Yang Chen, Yi Yu, Jiaming He et al.
- **发布时间**: 2026-03-13
- **arXiv链接**: [arXiv:2603.12796v1](https://arxiv.org/abs/2603.12796v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting (3DGS) deliver high-quality rendering, yet the Gaussian representation exposes a new attack surface, the resource-targeting attack. This attack poisons training images, excessively inducing Gaussian growth to cause resource exhaustion. Although efficiency-oriented methods such as smoothing, thresholding, and pruning have been explored, these spatial-domain strategies operate on visible structures but overlook how stealthy perturbations distort the underlying spectral behaviors of training data. As a result, poisoned inputs introduce abnormal high-frequency amplifications that mislead 3DGS into interpreting noisy patterns as detailed structures, ultimately causing unstable Gaussian overgrowth and degraded scene fidelity. To address this, we propose \textbf{Spectral Defense} in Gaussian and image fields. We first design a 3D frequency filter to selectively prune Gaussians exhibiting abnormally high frequencies. Since natural scenes also contain legitimate high-frequency structures, directly suppressing high frequencies is insufficient, and we further develop a 2D spectral regularization on renderings, distinguishing naturally isotropic frequencies while penalizing anisotropic angular energy to constrain noisy patterns. Experiments show that our defense builds robust, accurate, and secure 3DGS, suppressing overgrowth by up to $5.92\times$, reducing memory by up to $3.66\times$, and improving speed by up to $4.34\times$ under attacks.

---

## 60. Mobile-GS: Real-time Gaussian Splatting for Mobile Devices

- **作者**: Xiaobiao Du, Yida Wang, Kun Zhan, Xin Yu
- **发布时间**: 2026-03-12
- **arXiv链接**: [arXiv:2603.11531v1](https://arxiv.org/abs/2603.11531v1)
- **说明**: Project Page: https://xiaobiaodu.github.io/mobile-gs-project/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for high-quality rendering across a wide range of applications.However, its high computational demands and large storage costs pose significant challenges for deployment on mobile devices. In this work, we propose a mobile-tailored real-time Gaussian Splatting method, dubbed Mobile-GS, enabling efficient inference of Gaussian Splatting on edge devices. Specifically, we first identify alpha blending as the primary computational bottleneck, since it relies on the time-consuming Gaussian depth sorting process. To solve this issue, we propose a depth-aware order-independent rendering scheme that eliminates the need for sorting, thereby substantially accelerating rendering. Although this order-independent rendering improves rendering speed, it may introduce transparency artifacts in regions with overlapping geometry due to the scarcity of rendering order. To address this problem, we propose a neural view-dependent enhancement strategy, enabling more accurate modeling of view-dependent effects conditioned on viewing direction, 3D Gaussian geometry, and appearance attributes. In this way, Mobile-GS can achieve both high-quality and real-time rendering. Furthermore, to facilitate deployment on memory-constrained mobile platforms, we also introduce first-order spherical harmonics distillation, a neural vector quantization technique, and a contribution-based pruning strategy to reduce the number of Gaussian primitive...

---

## 61. ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare

- **作者**: Freeman Cheng, Botao Ye, Xueting Li et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09968v1](https://arxiv.org/abs/2603.09968v1)
- **英文摘要**: Online novel view synthesis remains challenging, requiring robust scene reconstruction from sequential, often unposed, observations. We present ReCoSplat, an autoregressive feed-forward Gaussian Splatting model supporting posed or unposed inputs, with or without camera intrinsics. While assembling local Gaussians using camera poses scales better than canonical-space prediction, it creates a dilemma during training: using ground-truth poses ensures stability but causes a distribution mismatch when predicted poses are used at inference. To address this, we introduce a Render-and-Compare (ReCo) module. ReCo renders the current reconstruction from the predicted viewpoint and compares it with the incoming observation, providing a stable conditioning signal that compensates for pose errors. To support long sequences, we propose a hybrid KV cache compression strategy combining early-layer truncation with chunk-level selective retention, reducing the KV cache size by over 90% for 100+ frames. ReCoSplat achieves state-of-the-art performance across different input settings on both in- and out-of-distribution benchmarks. Code and pretrained models will be released. Our project page is at https://freemancheng.com/ReCoSplat .

---

## 62. GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System

- **作者**: Zhiye Tang, Qiudan Zhang, Lei Zhang et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09718v1](https://arxiv.org/abs/2603.09718v1)
- **英文摘要**: Recently, the 3D Gaussian splatting (3DGS) technique for real-time radiance field rendering has revolutionized the field of volumetric scene representation, providing users with an immersive experience. But in return, it also poses a large amount of data volume, which is extremely bandwidth-intensive. Cutting-edge researchers have tried to introduce different approaches and construct multiple variants for 3DGS to obtain a more compact scene representation, but it is still challenging for real-time distribution. In this paper, we propose GSStream, a novel volumetric scene streaming system to support 3DGS data format. Specifically, GSStream integrates a collaborative viewport prediction module to better predict users' future behaviors by learning collaborative priors and historical priors from multiple users and users' viewport sequences and a deep reinforcement learning (DRL)-based bitrate adaptation module to tackle the state and action space variability challenge of the bitrate adaptation problem, achieving efficient volumetric scene delivery. Besides, we first build a user viewport trajectory dataset for volumetric scenes to support the training and streaming simulation. Extensive experiments prove that our proposed GSStream system outperforms existing representative volumetric scene streaming systems in visual quality and network usage. Demo video: https://youtu.be/3WEe8PN8yvA.

---

## 63. ProGS: Towards Progressive Coding for 3D Gaussian Splatting

- **作者**: Zhiye Tang, Lingzhuo Liu, Shengjie Jiao et al.
- **发布时间**: 2026-03-10
- **arXiv链接**: [arXiv:2603.09703v1](https://arxiv.org/abs/2603.09703v1)
- **英文摘要**: With the emergence of 3D Gaussian Splatting (3DGS), numerous pioneering efforts have been made to address the effective compression issue of massive 3DGS data. 3DGS offers an efficient and scalable representation of 3D scenes by utilizing learnable 3D Gaussians, but the large size of the generated data has posed significant challenges for storage and transmission. Existing methods, however, have been limited by their inability to support progressive coding, a crucial feature in streaming applications with varying bandwidth. To tackle this limitation, this paper introduce a novel approach that organizes 3DGS data into an octree structure, enabling efficient progressive coding. The proposed ProGS is a streaming-friendly codec that facilitates progressive coding for 3D Gaussian splatting, and significantly improves both compression efficiency and visual fidelity. The proposed method incorporates mutual information enhancement mechanisms to mitigate structural redundancy, leveraging the relevance between nodes in the octree hierarchy. By adapting the octree structure and dynamically adjusting the anchor nodes, ProGS ensures scalable data compression without compromising the rendering quality. ProGS achieves a remarkable 45X reduction in file storage compared to the original 3DGS format, while simultaneously improving visual performance by over 10%. This demonstrates that ProGS can provide a robust solution for real-time applications with varying network conditions.

---

## 64. Improving Continual Learning for Gaussian Splatting based Environments Reconstruction on Commercial Off-the-Shelf Edge Devices

- **作者**: Ivan Zaino, Matteo Risso, Daniele Jahier Pagliari et al.
- **发布时间**: 2026-03-09
- **arXiv链接**: [arXiv:2603.08499v1](https://arxiv.org/abs/2603.08499v1)
- **英文摘要**: Novel view synthesis (NVS) is increasingly relevant for edge robotics, where compact and incrementally updatable 3D scene models are needed for SLAM, navigation, and inspection under tight memory and latency budgets. Variational Bayesian Gaussian Splatting (VBGS) enables replay-free continual updates for the 3DGS algorithm by maintaining a probabilistic scene model, but its high-precision computations and large intermediate tensors make on-device training impractical. We present a precision-adaptive optimization framework that enables VBGS training on resource-constrained hardware without altering its variational formulation. We (i) profile VBGS to identify memory/latency hotspots, (ii) fuse memory-dominant kernels to reduce materialized intermediate tensors, and (iii) automatically assign operation-level precisions via a mixed-precision search with bounded relative error. Across the Blender, Habitat, and Replica datasets, our optimised pipeline reduces peak memory from 9.44 GB to 1.11 GB and training time from ~234 min to ~61 min on an A5000 GPU, while preserving (and in some cases improving) reconstruction quality of the state-of-the-art VBGS baseline. We also enable for the first time NVS training on a commercial embedded platform, the Jetson Orin Nano, reducing per-frame latency by 19x compared to 3DGS.

---

## 65. Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis

- **作者**: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang
- **发布时间**: 2026-03-03
- **arXiv链接**: [arXiv:2603.02866v1](https://arxiv.org/abs/2603.02866v1)
- **英文摘要**: We present multimodal-prior-guided importance sampling as the central mechanism for hierarchical 3D Gaussian Splatting (3DGS) in sparse-view novel view synthesis. Our sampler fuses complementary cues { -- } photometric rendering residuals, semantic priors, and geometric priors { -- } to produce a robust, local recoverability estimate that directly drives where to inject fine Gaussians. Built around this sampling core, our framework comprises (1) a coarse-to-fine Gaussian representation that encodes global shape with a stable coarse layer and selectively adds fine primitives where the multimodal metric indicates recoverable detail; and (2) a geometric-aware sampling and retention policy that concentrates refinement on geometrically critical and complex regions while protecting newly added primitives in underconstrained areas from premature pruning. By prioritizing regions supported by consistent multimodal evidence rather than raw residuals alone, our method alleviates overfitting texture-induced errors and suppresses noise from pose/appearance inconsistencies. Experiments on diverse sparse-view benchmarks demonstrate state-of-the-art reconstructions, with up to +0.3 dB PSNR on DTU.

---

## 66. HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views

- **作者**: Jiashu Li, Xumeng Han, Zhaoyang Wei et al.
- **发布时间**: 2026-03-01
- **arXiv链接**: [arXiv:2603.01099v2](https://arxiv.org/abs/2603.01099v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a promising approach in novel view synthesis, combining photorealistic rendering with real-time efficiency. However, its success heavily relies on dense camera coverage; under sparse-view conditions, insufficient supervision leads to irregular Gaussian distributions, characterized by globally sparse coverage, blurred background, and distorted high-frequency areas. To address this, we propose HeroGS, Hierarchical Guidance for Robust 3D Gaussian Splatting, a unified framework that establishes hierarchical guidance across the image, feature, and parameter levels. At the image level, sparse supervision is converted into pseudo-dense guidance, globally regularizing the Gaussian distributions and forming a consistent foundation for subsequent optimization. Building upon this, Feature-Adaptive Densification and Pruning (FADP) at the feature level leverages low-level features to refine high-frequency details and adaptively densifies Gaussians in background regions. The optimized distributions then support Co-Pruned Geometry Consistency (CPG) at parameter level, which guides geometric consistency through parameter freezing and co-pruning, effectively removing inconsistent splats. The hierarchical guidance strategy effectively constrains and optimizes the overall Gaussian distributions, thereby enhancing both structural fidelity and rendering quality. Extensive experiments demonstrate that HeroGS achieves high-fidelity reconstruction...

---

## 67. Semantic-Guided 3D Gaussian Splatting for Transient Object Removal

- **作者**: Aditi Prabakaran, Priyesh Shukla
- **发布时间**: 2026-02-17
- **arXiv链接**: [arXiv:2602.15516v1](https://arxiv.org/abs/2602.15516v1)
- **英文摘要**: Transient objects in casual multi-view captures cause ghosting artifacts in 3D Gaussian Splatting (3DGS) reconstruction. Existing solutions relied on scene decomposition at significant memory cost or on motion-based heuristics that were vulnerable to parallax ambiguity. A semantic filtering framework was proposed for category-aware transient removal using vision-language models. CLIP similarity scores between rendered views and distractor text prompts were accumulated per-Gaussian across training iterations. Gaussians exceeding a calibrated threshold underwent opacity regularization and periodic pruning. Unlike motion-based approaches, semantic classification resolved parallax ambiguity by identifying object categories independently of motion patterns. Experiments on the RobustNeRF benchmark demonstrated consistent improvement in reconstruction quality over vanilla 3DGS across four sequences, while maintaining minimal memory overhead and real-time rendering performance. Threshold calibration and comparisons with baselines validated semantic guidance as a practical strategy for transient removal in scenarios with predictable distractor categories.

---

## 68. CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video

- **作者**: Hojun Song, Heejung Choi, Aro Kim et al.
- **发布时间**: 2026-02-10
- **arXiv链接**: [arXiv:2602.09816v1](https://arxiv.org/abs/2602.09816v1)
- **说明**: Preprint. Under review
- **英文摘要**: High-quality novel view synthesis (NVS) from real-world videos is crucial for applications such as cultural heritage preservation, digital twins, and immersive media. However, real-world videos typically contain long sequences with irregular camera trajectories and unknown poses, leading to pose drift, feature misalignment, and geometric distortion during reconstruction. Moreover, lossy compression amplifies these issues by introducing inconsistencies that gradually degrade geometry and rendering quality. While recent studies have addressed either long-sequence NVS or unposed reconstruction, compression-aware approaches still focus on specific artifacts or limited scenarios, leaving diverse compression patterns in long videos insufficiently explored. In this paper, we propose CompSplat, a compression-aware training framework that explicitly models frame-wise compression characteristics to mitigate inter-frame inconsistency and accumulated geometric errors. CompSplat incorporates compression-aware frame weighting and an adaptive pruning strategy to enhance robustness and geometric consistency, particularly under heavy compression. Extensive experiments on challenging benchmarks, including Tanks and Temples, Free, and Hike, demonstrate that CompSplat achieves state-of-the-art rendering quality and pose accuracy, significantly surpassing most recent state-of-the-art NVS approaches under severe compression conditions.

---

## 69. Forecasting as Rendering: A 2D Gaussian Splatting Framework for Time Series Forecasting

- **作者**: Yixin Wang, Yifan Hu, Peiyuan Liu et al.
- **发布时间**: 2026-02-10
- **arXiv链接**: [arXiv:2603.02220v1](https://arxiv.org/abs/2603.02220v1)
- **英文摘要**: Time series forecasting (TSF) remains a challenging problem due to the intricate entanglement of intraperiod-fluctuations and interperiod-trends. While recent advances have attempted to reshape 1D sequences into 2D period-phase representations, they suffer from two principal limitations.Firstly, treating reshaped tensors as static images results in a topological mismatch, as standard spatial operators sever chronological continuity at grid boundaries. Secondly, relying on uniform fixed-size representations allocates modeling capacity inefficiently and fails to provide the adaptive resolution required for compressible, non-stationary temporal patterns. To address these limitations, we introduce TimeGS, a novel framework that fundamentally shifts the forecasting paradigm from regression to 2D generative rendering. By reconceptualizing the future sequence as a continuous latent surface, TimeGS utilizes the inherent anisotropy of Gaussian kernels to adaptively model complex variations with flexible geometric alignment. To realize this, we introduce a Multi-Basis Gaussian Kernel Generation (MB-GKG) block that synthesizes kernels from a fixed dictionary to stabilize optimization, and a Multi-Period Chronologically Continuous Rasterization (MP-CCR) block that enforces strict temporal continuity across periodic boundaries. Comprehensive experiments on standard benchmark datasets demonstrate that TimeGS attains state-of-the-art performance.

---

## 70. GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification

- **作者**: Soonbin Lee, Yeong-Gyu Kim, Simon Sasse et al.
- **发布时间**: 2026-02-06
- **arXiv链接**: [arXiv:2602.06830v1](https://arxiv.org/abs/2602.06830v1)
- **英文摘要**: Existing 3D Gaussian Splatting simplification methods commonly use importance scores, such as blending weights or sensitivity, to identify redundant Gaussians. However, these scores are not driven by visual error metrics, often leading to suboptimal trade-offs between compactness and rendering fidelity. We present GaussianPOP, a principled simplification framework based on analytical Gaussian error quantification. Our key contribution is a novel error criterion, derived directly from the 3DGS rendering equation, that precisely measures each Gaussian's contribution to the rendered image. By introducing a highly efficient algorithm, our framework enables practical error calculation in a single forward pass. The framework is both accurate and flexible, supporting on-training pruning as well as post-training simplification via iterative error re-quantification for improved stability. Experimental results show that our method consistently outperforms existing state-of-the-art pruning methods across both application scenarios, achieving a superior trade-off between model compactness and high rendering quality.

---

## 71. Nix and Fix: Targeting 1000x Compression of 3D Gaussian Splatting with Diffusion Models

- **作者**: Cem Eteke, Enzo Tartaglione
- **发布时间**: 2026-02-04
- **arXiv链接**: [arXiv:2602.04549v2](https://arxiv.org/abs/2602.04549v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) revolutionized novel view rendering. Instead of inferring from dense spatial points, as implicit representations do, 3DGS uses sparse Gaussians. This enables real-time performance but increases space requirements, hindering rate-constrained applications. 3DGS compression emerged as a field aimed at alleviating this issue. While impressive progress has been made, at low rates, compression introduces artifacts that degrade visual quality significantly. We introduce NiFi, a method for extreme 3DGS compression through restoration via artifact-aware, diffusion-based one-step distillation. We show that our method achieves state-of-the-art perceptual quality at extremely low rates, down to 0.1 MB, and towards 1000x rate improvement over 3DGS at comparable perceptual performance. Code is available at: https://github.com/ceteke/nifi

---

## 72. Constrained Dynamic Gaussian Splatting

- **作者**: Zihan Zheng, Zhenglong Wu, Xuanxuan Wang et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.03538v1](https://arxiv.org/abs/2602.03538v1)
- **英文摘要**: While Dynamic Gaussian Splatting enables high-fidelity 4D reconstruction, its deployment is severely hindered by a fundamental dilemma: unconstrained densification leads to excessive memory consumption incompatible with edge devices, whereas heuristic pruning fails to achieve optimal rendering quality under preset Gaussian budgets. In this work, we propose Constrained Dynamic Gaussian Splatting (CDGS), a novel framework that formulates dynamic scene reconstruction as a budget-constrained optimization problem to enforce a strict, user-defined Gaussian budget during training. Our key insight is to introduce a differentiable budget controller as the core optimization driver. Guided by a multi-modal unified importance score, this controller fuses geometric, motion, and perceptual cues for precise capacity regulation. To maximize the utility of this fixed budget, we further decouple the optimization of static and dynamic elements, employing an adaptive allocation mechanism that dynamically distributes capacity based on motion complexity. Furthermore, we implement a three-phase training strategy to seamlessly integrate these constraints, ensuring precise adherence to the target count. Coupled with a dual-mode hybrid compression scheme, CDGS not only strictly adheres to hardware constraints (error < 2%}) but also pushes the Pareto frontier of rate-distortion performance. Extensive experiments demonstrate that CDGS delivers optimal rendering quality under varying capacity limits, ach...

---

## 73. WebSplatter: Enabling Cross-Device Efficient Gaussian Splatting in Web Browsers via WebGPU

- **作者**: Yudong Han, Chao Xu, Xiaodan Ye et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.03207v1](https://arxiv.org/abs/2602.03207v1)
- **英文摘要**: We present WebSplatter, an end-to-end GPU rendering pipeline for the heterogeneous web ecosystem. Unlike naive ports, WebSplatter introduces a wait-free hierarchical radix sort that circumvents the lack of global atomics in WebGPU, ensuring deterministic execution across diverse hardware. Furthermore, we propose an opacity-aware geometry culling stage that dynamically prunes splats before rasterization, significantly reducing overdraw and peak memory footprint. Evaluation demonstrates that WebSplatter consistently achieves 1.2$\times$ to 4.5$\times$ speedups over state-of-the-art web viewers.

---

## 74. SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation

- **作者**: Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu et al.
- **发布时间**: 2026-02-03
- **arXiv链接**: [arXiv:2602.02989v2](https://arxiv.org/abs/2602.02989v2)
- **英文摘要**: Novel view synthesis of dynamic scenes is fundamental to achieving photorealistic 4D reconstruction and immersive visual experiences. Recent progress in Gaussian-based representations has significantly improved real-time rendering quality, yet existing methods still struggle to maintain a balance between long-term static and short-term dynamic regions in both representation and optimization. To address this, we present SharpTimeGS, a lifespan-aware 4D Gaussian framework that achieves temporally adaptive modeling of both static and dynamic regions under a unified representation. Specifically, we introduce a learnable lifespan parameter that reformulates temporal visibility from a Gaussian-shaped decay into a flat-top profile, allowing primitives to remain consistently active over their intended duration and avoiding redundant densification. In addition, the learned lifespan modulates each primitives' motion, reducing drift in long-lived static points while retaining unrestricted motion for short-lived dynamic ones. This effectively decouples motion magnitude from temporal duration, improving long-term stability without compromising dynamic fidelity. Moreover, we design a lifespan-velocity-aware densification strategy that mitigates optimization imbalance between static and dynamic regions by allocating more capacity to regions with pronounced motion while keeping static areas compact and stable. Extensive experiments on multiple benchmarks demonstrate that our method achieves ...

---

## 75. HPC: Hierarchical Point-based Latent Representation for Streaming Dynamic Gaussian Splatting Compression

- **作者**: Yangzhi Ma, Bojun Liu, Wenting Liao et al.
- **发布时间**: 2026-01-31
- **arXiv链接**: [arXiv:2602.00671v1](https://arxiv.org/abs/2602.00671v1)
- **英文摘要**: While dynamic Gaussian Splatting has driven significant advances in free-viewpoint video, maintaining its rendering quality with a small memory footprint for efficient streaming transmission still presents an ongoing challenge. Existing streaming dynamic Gaussian Splatting compression methods typically leverage a latent representation to drive the neural network for predicting Gaussian residuals between frames. Their core latent representations can be categorized into structured grid-based and unstructured point-based paradigms. However, the former incurs significant parameter redundancy by inevitably modeling unoccupied space, while the latter suffers from limited compactness as it fails to exploit local correlations. To relieve these limitations, we propose HPC, a novel streaming dynamic Gaussian Splatting compression framework. It employs a hierarchical point-based latent representation that operates on a per-Gaussian basis to avoid parameter redundancy in unoccupied space. Guided by a tailored aggregation scheme, these latent points achieve high compactness with low spatial redundancy. To improve compression efficiency, we further undertake the first investigation to compress neural networks for streaming dynamic Gaussian Splatting through mining and exploiting the inter-frame correlation of parameters. Combined with latent compression, this forms a fully end-to-end compression framework. Comprehensive experimental evaluations demonstrate that HPC substantially outperform...

---

## 76. LangGS-SLAM: Real-Time Language-Feature Gaussian Splatting SLAM

- **作者**: Seongbo Ha, Sibaek Lee, Kyungsu Kang et al.
- **发布时间**: 2026-01-28
- **arXiv链接**: [arXiv:2602.06991v1](https://arxiv.org/abs/2602.06991v1)
- **说明**: 17 pages, 4 figures
- **英文摘要**: In this paper, we propose a RGB-D SLAM system that reconstructs a language-aligned dense feature field while sustaining low-latency tracking and mapping. First, we introduce a Top-K Rendering pipeline, a high-throughput and semantic-distortion-free method for efficiently rendering high-dimensional feature maps. To address the resulting semantic-geometric discrepancy and mitigate the memory consumption, we further design a multi-criteria map management strategy that prunes redundant or inconsistent Gaussians while preserving scene integrity. Finally, a hybrid field optimization framework jointly refines the geometric and semantic fields under real-time constraints by decoupling their optimization frequencies according to field characteristics. The proposed system achieves superior geometric fidelity compared to geometric-only baselines and comparable semantic fidelity to offline approaches while operating at 15 FPS. Our results demonstrate that online SLAM with dense, uncompressed language-aligned feature fields is both feasible and effective, bridging the gap between 3D perception and language-based reasoning.

---

## 77. LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction

- **作者**: Xinhui Liu, Can Wang, Lei Liu et al.
- **发布时间**: 2026-01-26
- **arXiv链接**: [arXiv:2601.18475v1](https://arxiv.org/abs/2601.18475v1)
- **英文摘要**: Free-Viewpoint Video (FVV) reconstruction enables photorealistic and interactive 3D scene visualization; however, real-time streaming is often bottlenecked by sparse-view inputs, prohibitive training costs, and bandwidth constraints. While recent 3D Gaussian Splatting (3DGS) has advanced FVV due to its superior rendering speed, Streaming Free-Viewpoint Video (SFVV) introduces additional demands for rapid optimization, high-fidelity reconstruction under sparse constraints, and minimal storage footprints. To bridge this gap, we propose StreamLoD-GS, an LoD-based Gaussian Splatting framework designed specifically for SFVV. Our approach integrates three core innovations: 1) an Anchor- and Octree-based LoD-structured 3DGS with a hierarchical Gaussian dropout technique to ensure efficient and stable optimization while maintaining high-quality rendering; 2) a GMM-based motion partitioning mechanism that separates dynamic and static content, refining dynamic regions while preserving background stability; and 3) a quantized residual refinement framework that significantly reduces storage requirements without compromising visual fidelity. Extensive experiments demonstrate that StreamLoD-GS achieves competitive or state-of-the-art performance in terms of quality, efficiency, and storage.

---

## 78. PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling

- **作者**: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang
- **发布时间**: 2026-01-24
- **arXiv链接**: [arXiv:2601.17354v5](https://arxiv.org/abs/2601.17354v5)
- **英文摘要**: While 3D Gaussian Splatting (3DGS) enables real-time rendering, its training demands workstation-level compute and memory, making mobile deployment impractical under minute-scale time budgets and limited peak memory. We present PocketGS, a mobile scene modeling paradigm that enables on-device 3DGS training under these tightly coupled constraints while preserving high-fidelity reconstruction. PocketGS resolves the fundamental tension between training efficiency, memory compactness, and modeling quality through three co-designed operators: $\mathcal{G}$ builds geometry-faithful point-cloud priors; $\mathcal{I}$ injects local surface statistics to seed anisotropic Gaussians, thereby reducing early conditioning gaps; and $\mathcal{T}$ unrolls alpha compositing with cached intermediates and index-mapped gradient scattering for stable mobile backpropagation. Extensive experiments demonstrate that PocketGS outperforms the powerful mainstream workstation 3DGS baseline under mobile budgets, delivering high-quality reconstructions and enabling a fully on-device, practical capture-to-rendering workflow.

---

## 79. LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting

- **作者**: Yuhan Chen, Wenxuan Yu, Guofa Li et al.
- **发布时间**: 2026-01-22
- **arXiv链接**: [arXiv:2601.15772v1](https://arxiv.org/abs/2601.15772v1)
- **英文摘要**: 2D Gaussian Splatting (2DGS) is an emerging explicit scene representation method with significant potential for image compression due to high fidelity and high compression ratios. However, existing low-light enhancement algorithms operate predominantly within the pixel domain. Processing 2DGS-compressed images necessitates a cumbersome decompression-enhancement-recompression pipeline, which compromises efficiency and introduces secondary degradation. To address these limitations, we propose LL-GaussianImage, the first zero-shot unsupervised framework designed for low-light enhancement directly within the 2DGS compressed representation domain. Three primary advantages are offered by this framework. First, a semantic-guided Mixture-of-Experts enhancement framework is designed. Dynamic adaptive transformations are applied to the sparse attribute space of 2DGS using rendered images as guidance to enable compression-as-enhancement without full decompression to a pixel grid. Second, a multi-objective collaborative loss function system is established to strictly constrain smoothness and fidelity during enhancement, suppressing artifacts while improving visual quality. Third, a two-stage optimization process is utilized to achieve reconstruction-as-enhancement. The accuracy of the base representation is ensured through single-scale reconstruction and network robustness is enhanced. High-quality enhancement of low-light images is achieved while high compression ratios are maintained. ...

---

## 80. POTR: Post-Training 3DGS Compression

- **作者**: Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael
- **发布时间**: 2026-01-21
- **arXiv链接**: [arXiv:2601.14821v1](https://arxiv.org/abs/2601.14821v1)
- **说明**: 15 pages, 12 figures. Submitted to IEEE TCSVT, under review
- **英文摘要**: 3D Gaussian Splatting (3DGS) has recently emerged as a promising contender to Neural Radiance Fields (NeRF) in 3D scene reconstruction and real-time novel view synthesis. 3DGS outperforms NeRF in training and inference speed but has substantially higher storage requirements. To remedy this downside, we propose POTR, a post-training 3DGS codec built on two novel techniques. First, POTR introduces a novel pruning approach that uses a modified 3DGS rasterizer to efficiently calculate every splat's individual removal effect simultaneously. This technique results in 2-4x fewer splats than other post-training pruning techniques and as a result also significantly accelerates inference with experiments demonstrating 1.5-2x faster inference than other compressed models. Second, we propose a novel method to recompute lighting coefficients, significantly reducing their entropy without using any form of training. Our fast and highly parallel approach especially increases AC lighting coefficient sparsity, with experiments demonstrating increases from 70% to 97%, with minimal loss in quality. Finally, we extend POTR with a simple fine-tuning scheme to further enhance pruning, inference, and rate-distortion performance. Experiments demonstrate that POTR, even without fine-tuning, consistently outperforms all other post-training compression techniques in both rate-distortion performance and inference speed.

---

## 81. Structured Image-based Coding for Efficient Gaussian Splatting Compression

- **作者**: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz
- **发布时间**: 2026-01-20
- **arXiv链接**: [arXiv:2601.14510v3](https://arxiv.org/abs/2601.14510v3)
- **英文摘要**: Gaussian Splatting (GS) has recently emerged as a state-of-the-art representation for radiance fields, combining real-time rendering with high visual fidelity. However, GS models require storing millions of parameters, leading to large file sizes that impair their use in practical multimedia systems. To address this limitation, this paper introduces GS Image-based Compression (GSICO), a novel GS codec that efficiently compresses pre-trained GS models while preserving perceptual fidelity. The core contribution lies in a mapping procedure that arranges GS parameters into structured images, guided by a novel algorithm that enhances spatial coherence. These GS parameter images are then encoded using a conventional image codec. Experimental evaluations on Tanks and Temples, Deep Blending, and Mip-NeRF360 datasets show that GSICO achieves average compression factors of 20.2x with minimal loss in visual quality, as measured by PSNR, SSIM, and LPIPS. Compared with state-of-the-art GS compression methods, the proposed codec consistently yields superior rate-distortion (RD) trade-offs.

---

## 82. TIDI-GS: Floater Suppression in 3D Gaussian Splatting for Enhanced Indoor Scene Fidelity

- **作者**: Sooyeun Yang, Cheyul Im, Jee Won Lee, Jongseong Brad Choi
- **发布时间**: 2026-01-14
- **arXiv链接**: [arXiv:2601.09291v2](https://arxiv.org/abs/2601.09291v2)
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a technique to create high-quality, real-time 3D scenes from images. This method often produces visual artifacts known as floaters--nearly transparent, disconnected elements that drift in space away from the actual surface. This geometric inaccuracy undermines the reliability of these models for practical applications, which is critical. To address this issue, we introduce TIDI-GS, a new training framework designed to eliminate these floaters. A key benefit of our approach is that it functions as a lightweight plugin for the standard 3DGS pipeline, requiring no major architectural changes and adding minimal overhead to the training process. The core of our method is a floater pruning algorithm--TIDI--that identifies and removes floaters based on several criteria: their consistency across multiple viewpoints, their spatial relationship to other elements, and an importance score learned during training. The framework includes a mechanism to preserve fine details, ensuring that important high-frequency elements are not mistakenly removed. This targeted cleanup is supported by a monocular depth-based loss function that helps improve the overall geometric structure of the scene. Our experiments demonstrate that TIDI-GS improves both the perceptual quality and geometric integrity of reconstructions, transforming them into robust digital assets, suitable for high-fidelity applications.

---

## 83. Sketch&Patch++: Efficient Structure-Aware 3D Gaussian Representation

- **作者**: Yuang Shi, Géraldine Morin, Simone Gasparini, Wei Tsang Ooi
- **发布时间**: 2026-01-08
- **arXiv链接**: [arXiv:2601.05394v2](https://arxiv.org/abs/2601.05394v2)
- **英文摘要**: We observe that Gaussians exhibit distinct roles and characteristics analogous to traditional artistic techniques -- like how artists first sketch outlines before filling in broader areas with color, some Gaussians capture high-frequency features such as edges and contours, while others represent broader, smoother regions analogous to brush strokes that add volume and depth. Based on this observation, we propose a hybrid representation that categorizes Gaussians into (i) Sketch Gaussians, which represent high-frequency, boundary-defining features, and (ii) Patch Gaussians, which cover low-frequency, smooth regions. This semantic separation naturally enables layered progressive streaming, where the compact Sketch Gaussians establish the structural skeleton before Patch Gaussians incrementally refine volumetric detail.   In this work, we extend our previous method to arbitrary 3D scenes by proposing a novel hierarchical adaptive categorization framework that operates directly on the 3DGS representation. Our approach employs multi-criteria density-based clustering, combined with adaptive quality-driven refinement. This method eliminates dependency on external 3D line primitives while ensuring optimal parametric encoding effectiveness. Our comprehensive evaluation across diverse scenes, including both man-made and natural environments, demonstrates that our method achieves up to 1.74 dB improvement in PSNR, 6.7% in SSIM, and 41.4% in LPIPS at equivalent model sizes compared to un...

---

## 84. SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting

- **作者**: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang
- **发布时间**: 2026-01-07
- **arXiv链接**: [arXiv:2601.04348v1](https://arxiv.org/abs/2601.04348v1)
- **英文摘要**: Recent advances in 3D Gaussian Splatting have allowed for real-time, high-fidelity novel view synthesis. Nonetheless, these models have significant storage requirements for large and medium-sized scenes, hindering their deployment over cloud and streaming services. Some of the most recent progressive compression techniques for these models rely on progressive masking and scalar quantization techniques to reduce the bitrate of Gaussian attributes using spatial context models. While effective, scalar quantization may not optimally capture the correlations of high-dimensional feature vectors, which can potentially limit the rate-distortion performance.   In this work, we introduce a novel progressive codec for 3D Gaussian Splatting that replaces traditional methods with a more powerful Residual Vector Quantization approach to compress the primitive features. Our key contribution is an auto-regressive entropy model, guided by a multi-resolution hash grid, that accurately predicts the conditional probability of each successive transmitted index, allowing for coarse and refinement layers to be compressed with high efficiency.

---

## 85. Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting

- **作者**: Subhankar Mishra
- **发布时间**: 2026-01-01
- **arXiv链接**: [arXiv:2601.00913v1](https://arxiv.org/abs/2601.00913v1)
- **英文摘要**: 3D Gaussian Splatting produces high-quality scene reconstructions but generates hundreds of thousands of spurious Gaussians (floaters) scattered throughout the environment. These artifacts obscure objects of interest and inflate model sizes, hindering deployment in bandwidth-constrained applications. We present Clean-GS, a method for removing background clutter and floaters from 3DGS reconstructions using sparse semantic masks. Our approach combines whitelist-based spatial filtering with color-guided validation and outlier removal to achieve 60-80\% model compression while preserving object quality. Unlike existing 3DGS pruning methods that rely on global importance metrics, Clean-GS uses semantic information from as few as 3 segmentation masks (1\% of views) to identify and remove Gaussians not belonging to the target object. Our multi-stage approach consisting of (1) whitelist filtering via projection to masked regions, (2) depth-buffered color validation, and (3) neighbor-based outlier removal isolates monuments and objects from complex outdoor scenes. Experiments on Tanks and Temples show that Clean-GS reduces file sizes from 125MB to 47MB while maintaining rendering quality, making 3DGS models practical for web deployment and AR/VR applications. Our code is available at https://github.com/smlab-niser/clean-gs

---

## 86. Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding

- **作者**: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li
- **发布时间**: 2025-12-19
- **arXiv链接**: [arXiv:2512.17528v1](https://arxiv.org/abs/2512.17528v1)
- **说明**: Accepted by DCC 2026
- **英文摘要**: Substantial Gaussian splatting format point clouds require effective compression. In this paper, we propose Voxel-GS, a simple yet highly effective framework that departs from the complex neural entropy models of prior work, instead achieving competitive performance using only a lightweight rate proxy and run-length coding. Specifically, we employ a differentiable quantization to discretize the Gaussian attributes of Scaffold-GS. Subsequently, a Laplacian-based rate proxy is devised to impose an entropy constraint, guiding the generation of high-fidelity and compact reconstructions. Finally, this integer-type Gaussian point cloud is compressed losslessly using Octree and run-length coding. Experiments validate that the proposed rate proxy accurately estimates the bitrate of run-length coding, enabling Voxel-GS to eliminate redundancy and optimize for a more compact representation. Consequently, our method achieves a remarkable compression ratio with significantly faster coding speeds than prior art. The code is available at https://github.com/zb12138/VoxelGS.

---

## 87. Lightweight 3D Gaussian Splatting Compression via Video Codec

- **作者**: Qi Yang, Geert Van Der Auwera, Zhu Li
- **发布时间**: 2025-12-12
- **arXiv链接**: [arXiv:2512.11186v1](https://arxiv.org/abs/2512.11186v1)
- **说明**: Accepted by DCC2026 Oral
- **英文摘要**: Current video-based GS compression methods rely on using Parallel Linear Assignment Sorting (PLAS) to convert 3D GS into smooth 2D maps, which are computationally expensive and time-consuming, limiting the application of GS on lightweight devices. In this paper, we propose a Lightweight 3D Gaussian Splatting (GS) Compression method based on Video codec (LGSCV). First, a two-stage Morton scan is proposed to generate blockwise 2D maps that are friendly for canonical video codecs in which the coding units (CU) are square blocks. A 3D Morton scan is used to permute GS primitives, followed by a 2D Morton scan to map the ordered GS primitives to 2D maps in a blockwise style. However, although the blockwise 2D maps report close performance to the PLAS map in high-bitrate regions, they show a quality collapse at medium-to-low bitrates. Therefore, a principal component analysis (PCA) is used to reduce the dimensionality of spherical harmonics (SH), and a MiniPLAS, which is flexible and fast, is designed to permute the primitives within certain block sizes. Incorporating SH PCA and MiniPLAS leads to a significant gain in rate-distortion (RD) performance, especially at medium and low bitrates. MiniPLAS can also guide the setting of the codec CU size configuration and significantly reduce encoding time. Experimental results on the MPEG dataset demonstrate that the proposed LGSCV achieves over 20% RD gain compared with state-of-the-art methods, while reducing 2D map generation time to app...

---

## 88. SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting

- **作者**: Zihan Li, Tengfei Wang, Wentian Gan et al.
- **发布时间**: 2025-11-17
- **arXiv链接**: [arXiv:2511.13278v2](https://arxiv.org/abs/2511.13278v2)
- **说明**: This paper has been submitted to the 2026 ISPRS Congress
- **英文摘要**: Lightweight building surface models are crucial for digital city, navigation, and fast geospatial analytics, yet conventional multi-view geometry pipelines remain cumbersome and quality-sensitive due to their reliance on dense reconstruction, meshing, and subsequent simplification. This work presents SF-Recon, a method that directly reconstructs lightweight building surfaces from multi-view images without post-hoc mesh simplification. We first train an initial 3D Gaussian Splatting (3DGS) field to obtain a view-consistent representation. Building structure is then distilled by a normal-gradient-guided Gaussian optimization that selects primitives aligned with roof and wall boundaries, followed by multi-view edge-consistency pruning to enhance structural sharpness and suppress non-structural artifacts without external supervision. Finally, a multi-view depth-constrained Delaunay triangulation converts the structured Gaussian field into a lightweight, structurally faithful building mesh. Based on a proposed SF dataset, the experimental results demonstrate that our SF-Recon can directly reconstruct lightweight building models from multi-view imagery, achieving substantially fewer faces and vertices while maintaining computational efficiency. Website:https://lzh282140127-cell.github.io/SF-Recon-project/

---

## 89. Compact 3D Gaussian Splatting For Dense Visual SLAM

- **作者**: Tianchen Deng, Chang Nie, Shuhong Liu et al.
- **发布时间**: 2024-03-17
- **arXiv链接**: [arXiv:2403.11247v3](https://arxiv.org/abs/2403.11247v3)
- **说明**: Accepted by IJCV 2026
- **英文摘要**: Recent work has shown that 3D Gaussian-based SLAM enables high-quality reconstruction, accurate pose estimation, and real-time rendering of scenes. However, these approaches are built on a tremendous number of redundant 3D Gaussian ellipsoids, leading to high memory and storage costs, and slow training speed. To address the limitation, we propose a compact 3D Gaussian Splatting SLAM system that reduces the number and the parameter size of Gaussian ellipsoids. A sliding window-based masking strategy is first proposed to reduce the redundant ellipsoids. Then we observe that the covariance matrix (geometry) of most 3D Gaussian ellipsoids are extremely similar, which motivates a novel geometry codebook to compress 3D Gaussian geometric attributes, i.e., the parameters. Robust and accurate pose estimation is achieved by a global bundle adjustment method with reprojection loss. Extensive experiments demonstrate that our method achieves faster training and rendering speed while maintaining the state-of-the-art (SOTA) quality of the scene representation.

---

