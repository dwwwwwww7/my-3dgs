# NeurIPS 2026

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2026 年 NeurIPS 会议的论文列表。

## 1. SplatLab: Autonomous Scientific Discovery for 3DGS Research

- **作者**: Seemandhar Jain, Manmohan Chandraker
- **发布时间**: 2026-10-21
- **arXiv链接**: [arXiv:2610.30468v1](https://arxiv.org/abs/2610.30468v1)
- **说明**: Accepted at NeurIPS 2026. 14 pages, 4 figures. Project page: https://seemandhar.github.io/splatlab
- **英文摘要**: Reproducing a published 3DGS paper takes weeks of expert engineering before any extension can be proposed. Prior autonomous-research systems read papers, draft hypotheses, and write code, but are limited by short fixed templates, low executability, and weak traceability, and none has been demonstrated end-to-end in a live computer-vision subfield with intense activity. SplatLab is an autonomous research system for 3D Gaussian Splatting that addresses these limitations. Given a research prompt, a target-paper URL, or no input at all, it reproduces a published baseline, proposes an extension, trains and ablates across Mip-NeRF 360 and LLFF, writes the manuscript, and binds every reported number to a logged training run. Five design choices distinguish it: (i) candidates mutate plugins from a verified-reproduction backbone matched to published baselines; (ii) a cascade-weighted Elo tournament across eight islands scores candidates on measured GPU PSNR with verbal-gradient feedback; (iii) a standing falsifier subtracts Elo on failure, integrating stress-test survival into selection; (iv) every reported number is bound to a logged training run, and the run cannot terminate while any claim is unbacked; (v) a seven-category 3DGS taxonomy wraps EVOLVE-BLOCK markers in domain-aligned scaffolds transferable across 3DGS repositories. On PSNR-targeted runs, SplatLab's manuscripts beat their reproduced targets by +0.18 to +3.78 dB, including +3.78 dB on astrophotographic nebula rendering,...

---

## 2. KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting

- **作者**: Radu Beche, Raoul de Charette
- **发布时间**: 2026-10-20
- **arXiv链接**: [arXiv:2610.28615v1](https://arxiv.org/abs/2610.28615v1)
- **说明**: NeurIPS 2026 (Spotlight). Project page https://rdbch.github.io/koalags
- **英文摘要**: Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (LoD) setting, the challenge is to decide which Gaussians should retain capacity as the budget decreases. A pilot study on 3DGS-MCMC reconstructions shows that image complexity, computed from the input views before optimization, predicts where reconstruction error concentrates in image and 3D space. It also reveals that simple regions contain too many Gaussians and degrade as much as complex ones at lower budgets, despite being inherently cheaper to represent. Subsequently, in KoalaGS, during training we use this complexity prior to bias relocation toward poorly reconstructed areas while ensuring smooth degradation across LoDs. A primitive importance score then enables inference at low-capacity, while preserving the scene structure. Tested across three datasets, KoalaGS maintains competitive full-capacity quality while significantly improving quality across the budget spectrum, yielding smoother transitions across LoDs, and enabling faster progressive streaming.

---

## 3. Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation

- **作者**: Sheng Ye, Jiangke Lin, Fudong Wang et al.
- **发布时间**: 2026-10-15
- **arXiv链接**: [arXiv:2610.21634v1](https://arxiv.org/abs/2610.21634v1)
- **说明**: NeurIPS 2026
- **英文摘要**: Recent feed-forward 3D Gaussian Splatting (3DGS) methods have enabled effective multi-view 3D reconstruction by predicting Gaussian primitives in a single forward pass. However, existing approaches predominantly adopt a pixel-aligned paradigm that predicts one Gaussian per input pixel, coupling the Gaussian count to the input resolution and number of views. This also leads to redundant primitives in textureless regions and insufficient coverage in geometrically complex areas. We present Anchor3DGS, a pose-free feed-forward 3DGS framework that replaces pixel-aligned prediction with a compact anchor-based representation. Guided by information entropy, our method places a set of 3D anchors in the scene, concentrating them in regions of higher visual complexity while maintaining broad spatial coverage. Each anchor performs occlusion-aware aggregation of multi-view image features, exchanges information with other anchors, and is decoded into a set of local Gaussians. A lightweight feature enhancement module further refines the coarse RGB output from Gaussian splatting and improves rendering fidelity. Extensive experiments on diverse benchmark datasets demonstrate that our Anchor3DGS achieves state-of-the-art novel view synthesis quality while only using an order of magnitude fewer Gaussian primitives.

---

## 4. GS-Codec: A Gaussian-Splatting Bottleneck for Neural Audio Coding

- **作者**: Ron Aluf, Alon Canfi, Eliya Nachmani
- **发布时间**: 2026-10-03
- **arXiv链接**: [arXiv:2610.04651v1](https://arxiv.org/abs/2610.04651v1)
- **说明**: Accepted to Neurips 2026
- **英文摘要**: Neural audio codecs compress waveforms into compact discrete tokens that underpin speech language models, real-time communication, and large-scale audio storage. Almost every dominant design, including residual vector quantization, finite scalar quantization, and single-codebook variants, follows the VQ-VAE template by partitioning the encoder latent through a learned codebook or a fixed scalar grid. We ask whether this partition is necessary. We introduce GS-Codec, a neural speech codec whose bottleneck is a parametric signal decomposition rather than a quantizer. We adapt Gaussian splatting from 3D scene reconstruction to one-dimensional latents. An inner optimization loop fits each encoder segment as a weighted sum of 1D Gaussian primitives. The decoder then reconstructs the waveform from the rendered sum. To avoid the cost of this iterative inner loop at inference time, we additionally train a lightweight GS Predictor Net that regresses the primitive parameters in a single forward pass. The encoder and decoder are trained end-to-end through the inner loop, with no quantizer anywhere in the training pipeline: the bottleneck is the decomposition itself, and scalar quantization is applied only post-training to the fitted parameters. Rather than relying on discrete codebook stages for bitrate control, our representation exposes a fine-grained rate-quality tradeoff: a single trained checkpoint supports post-training bitrate control by varying the number of primitives and the p...

---

## 5. NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting

- **作者**: Pratik Singh Bisht, Andreas Kolb
- **发布时间**: 2026-09-29
- **arXiv链接**: [arXiv:2609.37115v1](https://arxiv.org/abs/2609.37115v1)
- **说明**: Accepted at NeurIPS 2026
- **英文摘要**: We revisit the role of appearance modeling in 3D Gaussian Splatting (3DGS) and show that limited expressiveness in view-dependent reflectance is a key driver of representation redundancy. In standard 3DGS, low-order spherical harmonics (SH) are used, restricting the splats' ability to model high-frequency directional effects, which is typically compensated by increasing the number of splats. We propose \emph{NRF-GS: Neural Residual Fields for Gaussian Splatting}, a hybrid representation that replaces per-splat SH-bases with a shared neural residual field. Each Gaussian encodes a compact set of appearance features and a lambertian base color, while a lightweight \emph{global scene-level MLP} predicts view-dependent residuals conditioned on viewing direction, distance, and per-splat features. This formulation enhances directional reflectance modeling by combining diffuse per-splat reflectance representations with a shared global function for high-frequency details, enabling both higher expressiveness and parameter sharing across splats. Our key insight is that by accurately capturing high-frequency directional reflectance, especially in specular regions, the GS-representation becomes more expressive, reducing the need for geometrically redundant splats. As a result, NRF-GS achieves comparable or better rendering quality while reducing the number of Gaussians by up to 50\%, and produces visibly improved specular and high-frequency details.

---

## 6. CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting

- **作者**: Pengpeng Yu, Runqing Jiang, Qi Zhang et al.
- **发布时间**: 2026-05-25
- **arXiv链接**: [arXiv:2605.25563v2](https://arxiv.org/abs/2605.25563v2)
- **说明**: Accepted to NeurIPS 2026
- **英文摘要**: While feed-forward 3D Gaussian splatting reconstructs renderable Gaussian primitives from sparse context views without per-scene optimization, existing pipelines do not provide a compact scene representation for storage or transmission. A natural solution is to apply existing 3DGS compression methods to the generated Gaussian primitives. However, this approach operates on the final irregular 3D representation and is decoupled from the internal feature-to-Gaussian generation process, which limits compression efficiency. To address this, we introduce CodecSplat, an ultra-compact latent coding framework for feed-forward 3D Gaussian splatting. CodecSplat first encodes an intermediate 2D Gaussian-generation feature into an entropy-coded scene bitstream. At the decoder, the latent feature is reconstructed and used to predict depth and Gaussian parameters, which are then mapped to 3D Gaussian primitives. By integrating compression into the feed-forward Gaussian generation pipeline, CodecSplat avoids inefficient compression over irregular 3D Gaussian primitives and allows the codec to exploit the structured intermediate feature representation. We instantiate CodecSplat on a feed-forward Gaussian splatting backbone with depth-guided multi-view feature refinement and a hierarchical learned feature codec. On DL3DV and RealEstate10K datasets, CodecSplat achieves 23.56-26.36 dB and 24.76-27.05 dB PSNR with only 20.00-107.77 KiB and 3.37-12.51 KiB per scene, respectively. This is roughly o...

---

