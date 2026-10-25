# SIGGRAPH 2026

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2026 年 SIGGRAPH 会议的论文列表。

## 1. X-Splat: Unified Gaussian Splatting for Joint RGB and X-ray 3D Reconstruction

- **作者**: Wangze Xu, Chu Zhou, Mae Yamaguchi et al.
- **发布时间**: 2026-10-16
- **arXiv链接**: [arXiv:2610.23237v1](https://arxiv.org/abs/2610.23237v1)
- **说明**: SIGGRAPH Asia 2026 Conference Papers. 19 pages (12 main paper + 7 supplementary), 13 figures. Project page: https://zezeaaa.github.io/X-Splat/
- **英文摘要**: Jointly reconstructing RGB and X-ray provides new insights by connecting external appearance with internal structure, enabling a more complete understanding of real-world objects than single modality. Yet existing methods train separate models per modality and suffer from redundant geometry, alignment artifacts, and loose coupling that limits cross-modal insight discovery. We propose a unified representation in which all Gaussian primitives share a single set of geometric parameters, with only surface-proximal primitives additionally carrying appearance attributes. We perform cross-modal registration through clean multi-view stereo and X-ray geometric proxies instead of aligning two sets of optimized Gaussians, improving alignment stability. We then jointly optimize the unified representation via supervision from both modalities, complemented by a surface-depth consistency loss derived from X-ray geometry to guide RGB reconstruction. Experiments on the InsideOut dataset and our Flower & Insect dataset show that our framework achieves more robust cross-modal alignment, higher RGB rendering quality without compromising X-ray reconstruction, and a more compact representation than maintaining two independent geometries.

---

## 2. OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning

- **作者**: Haoran Wang, Shaoyu Cai, Adrian Azzarelli et al.
- **发布时间**: 2026-09-24
- **arXiv链接**: [arXiv:2609.29985v1](https://arxiv.org/abs/2609.29985v1)
- **说明**: SIGGRAPH ASIA 2026
- **英文摘要**: Underwater 3D reconstruction is critical for marine exploration, ecological monitoring, and subsea infrastructure inspection, yet remains challenging at large scale due to light attenuation, scattering, and limited capture coverage. While 3D Gaussian Splatting (3DGS) enables high-quality real-time rendering, its application to large underwater scenes is constrained by high memory consumption and inefficient optimization over extensive areas. We propose OceanXL, a fast and scalable 3DGS-based framework for large-scale underwater reconstruction. OceanXL adopts a divide-and-conquer strategy, partitioning scenes into spatially coherent blocks to enable efficient optimization while preserving global geometric consistency. We further introduce an adaptive pruning scheme tailored to underwater conditions that removes redundant primitives, producing compact representations without sacrificing visual fidelity. Together, these components improve training efficiency and rendering performance for large scenes. We also introduce a large-scale underwater dataset covering diverse marine environments. Experiments on five large-scale scenes demonstrate favorable scalability, compactness, and efficiency--quality trade-offs over large-scene baselines. Controlled comparisons on the small-scale SeaThru-NeRF dataset further show competitive reconstruction quality with substantially smaller model sizes than underwater-specific methods.

---

## 3. ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation

- **作者**: Jiahao Wu, Jie Liang, Die Hu et al.
- **发布时间**: 2026-08-31
- **arXiv链接**: [arXiv:2608.30184v1](https://arxiv.org/abs/2608.30184v1)
- **说明**: ACM ToG(SIGGRAPH'2026)
- **英文摘要**: Volumetric video enables immersive free viewpoint rendering of dynamic real world scenes, yet existing methods struggle with long sequences and complex motions, often leading to temporal instability and visual artifacts. To address these challenges, we propose \ourname, a Gaussian splatting based framework for volumetric video reconstruction. Our key insight is that explicitly tracking long term complex motion with individual Gaussian primitives is inherently unstable. Instead, we organize Gaussians around time conditioned anchors that localize their spatial and temporal support, thereby reducing long range motion complexity. We further introduce a temporal windowing strategy to activate only anchors relevant to the queried time, which improves scalability and temporal coherence. In addition, to ensure spatial and temporal stability, we design a compact set of multi level anchor features that encode global features, local spatial features, and local temporal features, jointly constraining Gaussian generation. Extensive experiments demonstrate that \ourname \ consistently outperforms prior methods on long sequence volumetric videos with complex motions. Project page: https://github.com/WuJH2001/ATGS.

---

## 4. CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting

- **作者**: Daheng Yin, Yili Jin, Jianxin Shi et al.
- **发布时间**: 2026-05-10
- **arXiv链接**: [arXiv:2605.09279v1](https://arxiv.org/abs/2605.09279v1)
- **说明**: SIGGRAPH 2026 Conference Paper. Code is available at https://github.com/yindaheng98/ColorAdaptiveGaussianSplatting
- **英文摘要**: Volumetric video (VV) streaming enables real-time, immersive access to remote 3D environments, powering telepresence, ecological monitoring, and robotic teleoperation. These applications turn VV streaming into a real-time interface to remote physical environments, imposing new system-level demands for photorealistic scene representation, low-latency interaction, and robust performance under heterogeneous networks. 3D Gaussian Splatting (3DGS) has been widely used for real-time photorealistic rendering, offering superior visual quality and rendering performance, but it faces challenges due to bandwidth consumption. Furthermore, as the foundation of adaptive VV streaming, existing Levels of Detail (LoD) methods based on density are not well-suited to Gaussian representations, leading to visible gaps and severe quality degradation. Recent studies have also explored attribute compression techniques to reduce bandwidth consumption. Our preliminary studies reveal that aggressive attribute compression primarily causes color distortion, which can be effectively corrected in the rendered image using a reference image. Motivated by these findings, we propose a novel Color-Adaptive scheme for adaptive VV streaming that uses vector quantization (VQ) to establish LoDs and correct color distortions with low-resolution reference images. We further present CAGS, an adaptive VV streaming system compatible with diverse Gaussian representations, which integrates the Color-Adaptive scheme by ren...

---

## 5. Generative 3D Gaussians with Learned Density Control

- **作者**: Runjie Yan, Yan-Pei Cao, Peng Wang, Ding Liang, Yuan-Chen Guo
- **发布时间**: 2026-05-08
- **arXiv链接**: [arXiv:2605.16355v1](https://arxiv.org/abs/2605.16355v1)
- **说明**: 19 pages, 16 figures, SIGGRAPH Conference Papers '26
- **英文摘要**: We present Density-Sampled Gaussians (DeG), a novel 3D representation designed to bridge the gap between adaptive rendering primitives and scalable generative modeling. Unlike existing approaches that constrain 3D Gaussians to fixed voxel grids or arrays, DeG models Gaussian centers as samples from a learnable probability density function defined over an octree. This formulation provides a rigorous mathematical framework for adaptive density control: by jointly optimizing the spatial density and Gaussian attributes under rendering supervision, our model naturally concentrates primitives in regions of high geometric complexity. We achieve this via a new render loss contribution gradient that serves as a fully differentiable analogue to the discrete densification and pruning heuristics used in standard Gaussian Splatting. The resulting representation is highly flexible, supporting variable-resolution decoding from a single latent code by simply adjusting the sampling budget. To enable generative synthesis, we train a latent diffusion model on DeG. We identify a critical challenge in applying diffusion to unordered set-structured latents, which can significantly slow convergence, and propose VecSeq, a canonical re-indexing mechanism that anchors latent tokens to a deterministic 3D Sobol sequence. This transforms the ambiguous set-generation problem into a robust sequence modeling task. Extensive experiments demonstrate that our pipeline achieves state-of-the-art quality in singl...

---

