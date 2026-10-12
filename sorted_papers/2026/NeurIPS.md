# NeurIPS 2026

> **最后更新**： 2026-10-12 10:46:20

本页面包含 2026 年 NeurIPS 会议的论文列表。

## 1. GS-Codec: A Gaussian-Splatting Bottleneck for Neural Audio Coding

- **作者**: Ron Aluf, Alon Canfi, Eliya Nachmani
- **发布时间**: 2026-10-03
- **arXiv链接**: [arXiv:2610.04651v1](https://arxiv.org/abs/2610.04651v1)
- **说明**: Accepted to Neurips 2026
- **英文摘要**: Neural audio codecs compress waveforms into compact discrete tokens that underpin speech language models, real-time communication, and large-scale audio storage. Almost every dominant design, including residual vector quantization, finite scalar quantization, and single-codebook variants, follows the VQ-VAE template by partitioning the encoder latent through a learned codebook or a fixed scalar grid. We ask whether this partition is necessary. We introduce GS-Codec, a neural speech codec whose bottleneck is a parametric signal decomposition rather than a quantizer. We adapt Gaussian splatting from 3D scene reconstruction to one-dimensional latents. An inner optimization loop fits each encoder segment as a weighted sum of 1D Gaussian primitives. The decoder then reconstructs the waveform from the rendered sum. To avoid the cost of this iterative inner loop at inference time, we additionally train a lightweight GS Predictor Net that regresses the primitive parameters in a single forward pass. The encoder and decoder are trained end-to-end through the inner loop, with no quantizer anywhere in the training pipeline: the bottleneck is the decomposition itself, and scalar quantization is applied only post-training to the fitted parameters. Rather than relying on discrete codebook stages for bitrate control, our representation exposes a fine-grained rate-quality tradeoff: a single trained checkpoint supports post-training bitrate control by varying the number of primitives and the p...

---

## 2. NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting

- **作者**: Pratik Singh Bisht, Andreas Kolb
- **发布时间**: 2026-09-29
- **arXiv链接**: [arXiv:2609.37115v1](https://arxiv.org/abs/2609.37115v1)
- **说明**: Accepted at NeurIPS 2026
- **英文摘要**: We revisit the role of appearance modeling in 3D Gaussian Splatting (3DGS) and show that limited expressiveness in view-dependent reflectance is a key driver of representation redundancy. In standard 3DGS, low-order spherical harmonics (SH) are used, restricting the splats' ability to model high-frequency directional effects, which is typically compensated by increasing the number of splats. We propose \emph{NRF-GS: Neural Residual Fields for Gaussian Splatting}, a hybrid representation that replaces per-splat SH-bases with a shared neural residual field. Each Gaussian encodes a compact set of appearance features and a lambertian base color, while a lightweight \emph{global scene-level MLP} predicts view-dependent residuals conditioned on viewing direction, distance, and per-splat features. This formulation enhances directional reflectance modeling by combining diffuse per-splat reflectance representations with a shared global function for high-frequency details, enabling both higher expressiveness and parameter sharing across splats. Our key insight is that by accurately capturing high-frequency directional reflectance, especially in specular regions, the GS-representation becomes more expressive, reducing the need for geometrically redundant splats. As a result, NRF-GS achieves comparable or better rendering quality while reducing the number of Gaussians by up to 50\%, and produces visibly improved specular and high-frequency details.

---

