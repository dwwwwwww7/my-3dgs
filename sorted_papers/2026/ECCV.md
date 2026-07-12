# ECCV 2026

> **最后更新**： 2026-07-12 02:26:50

本页面包含 2026 年 ECCV 会议的论文列表。

## 1. AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction

- **作者**: Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan
- **发布时间**: 2026-07-05
- **arXiv链接**: [arXiv:2607.04256v1](http://arxiv.org/abs/2607.04256v1)
- **说明**: Accepted at ECCV 2026. Project page: https://badrinaths.github.io/projects/adaptive-splat/
- **英文摘要**: Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by this, we propose a novel approach to explicitly control the number of Gaussians by leveraging local texture information. Our approach achieves this through three key components: (1) texture estimation to capture spatial variation in scene detail, (2) texture-aware pruning that removes redundant Gaussians from low frequency regions, and (3) an adaptive Gaussian head that predicts the modified attributes of the retained primitives without breaking the feed-forward paradigm. Experiments on RE10K, ACID, DL3DV, Tanks and Temples, and DTU demonstrate the effectiveness of our approach, while ablation studies validate the contributions of its key components.

---

## 2. PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation

- **作者**: Cao Duy, Phong Nguyen-Ha
- **发布时间**: 2026-07-02
- **arXiv链接**: [arXiv:2607.01803v2](http://arxiv.org/abs/2607.01803v2)
- **说明**: Accepted at ECCV 2026
- **英文摘要**: Recent advances in 3D content generation from text or images have achieved impressive results, yet view inconsistency from 2D generators and the scarcity of high-quality 3D data remain significant bottlenecks. Existing solutions typically adapt large-scale pre-trained text-to-image latent diffusion models to generate 3D Gaussian Splats (3DGS). However, these approaches often rely on training complex cascade pipelines that are computationally expensive and scalability-limited. Most critically, the quality of generated 3D assets is inherently constrained by each component capacity and compressed latent space, leading to decoding artifacts and accumulated errors. To address these limitations, we propose PixGS, a single-stage pipeline for direct high-quality 3DGS generation, which leverages recent advances in pixel-space diffusion to bypass lossy latent compression while still benefiting from the vast 2D generative priors. By directly denoising 3D Gaussian attributes at each timestep, our method enables precise, splat-level regularization of both appearance and geometry. Furthermore, we introduce a comprehensive supervision strategy that incorporates surface normals, depth, and high-frequency structural information, which is often overlooked in prior works. Experiments demonstrate that PixGS outperforms current state-of-the-art methods while maintaining a fast inference speed (1s on a single A100 GPU), offering a robust and efficient alternative to multi-stage generation pipeline...

---

## 3. Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting

- **作者**: Xiaobiao Du, YuAn Wang, Hao Li et al.
- **发布时间**: 2026-06-29
- **arXiv链接**: [arXiv:2606.30017v1](http://arxiv.org/abs/2606.30017v1)
- **说明**: ECCV 2026, Project Page:https://xiaobiaodu.github.io/flux-gs-project/
- **英文摘要**: Recent advances in 3D Gaussian Splatting have demonstrated unprecedented success in novel view synthesis. However, the substantial inference and storage overhead driven by high-order Spherical Harmonics (SH) are primary bottlenecks for mobile platforms. In this paper, we present Flux-GS, a real-time Gaussian Splatting method designed to achieve high-fidelity rendering with significantly reduced overhead for resource-constrained mobile platforms. We first propose a Monte Carlo Specular Energy Aggregator, sampling third-order radiance residuals and aggregating specular energy into a compact latent space. In this way, our method effectively preserves visually salient lighting features in lower-order bands without expensive distillation or pre-training. To mitigate the high-frequency details lost during compression, we introduce an Attribute-Conditioned SH Enhancement module. This module predicts Gaussian-aware offsets based on intrinsic Gaussian attributes, which enhance the first-order SH representation prior to inference, without extra inference costs. Furthermore, the original single-view gradient-based densification is prone to producing excessive Gaussians and overfitting to a certain view. We address these limitations by proposing a Multi-view Alpha-based Densification and Pruning strategy. By leveraging multi-view guidance, we ensure multi-view structure consistency and the precise removal of redundant primitives. Extensive experiments demonstrate that Flux-GS achieves su...

---

## 4. Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation

- **作者**: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt
- **发布时间**: 2026-06-20
- **arXiv链接**: [arXiv:2606.22197v1](http://arxiv.org/abs/2606.22197v1)
- **说明**: Accepted by ECCV 2026, project page:https://batfacewayne.github.io/Multi4D.io/
- **英文摘要**: Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: https://batfacewayne.github.io/Multi4D.io/

---

## 5. Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures

- **作者**: Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi et al.
- **发布时间**: 2026-05-05
- **arXiv链接**: [arXiv:2605.04035v3](http://arxiv.org/abs/2605.04035v3)
- **说明**: Accepted to ECCV 2026. Project website: https://apple.github.io/ml-headsup/
- **英文摘要**: We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

---

## 6. GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation

- **作者**: Nicolas von Lützow, Barbara Rössle, Katharina Schmid, Matthias Nießner
- **发布时间**: 2026-03-27
- **arXiv链接**: [arXiv:2603.26661v2](http://arxiv.org/abs/2603.26661v2)
- **说明**: Project page: https://nicolasvonluetzow.github.io/GaussianGPT/ - Project video: https://youtu.be/zVnMHkFzHDg - Accepted at ECCV 2026
- **英文摘要**: Most recent advances in 3D generative modeling rely on diffusion or flow-matching formulations. We instead explore a fully autoregressive alternative and introduce GaussianGPT, a transformer-based model that directly generates 3D Gaussians via next-token prediction, thus facilitating full 3D scene generation. We first compress Gaussian primitives into a discrete latent grid using a sparse 3D convolutional autoencoder with vector quantization. The resulting tokens are serialized and modeled using a causal transformer with 3D rotary positional embedding, enabling sequential generation of spatial structure and appearance. Unlike diffusion-based methods that refine scenes holistically, our formulation constructs scenes step-by-step, naturally supporting completion, outpainting, controllable sampling via temperature, and flexible generation horizons. This formulation leverages the compositional inductive biases and scalability of autoregressive modeling while operating on explicit representations compatible with modern neural rendering pipelines, positioning autoregressive transformers as a complementary paradigm for controllable and context-aware 3D generation.

---

## 7. Drop-In Perceptual Optimization for 3D Gaussian Splatting

- **作者**: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.23297v2](http://arxiv.org/abs/2603.23297v2)
- **说明**: Accepted as a conference paper at ECCV'26. Project page: https://apple.github.io/ml-perceptual-3dgs
- **英文摘要**: Despite their output being ultimately consumed by human viewers, 3D Gaussian Splatting (3DGS) methods often rely on ad-hoc combinations of pixel-level losses, resulting in blurry renderings. To address this, we systematically explore perceptual optimization strategies for 3DGS by searching over a diverse set of distortion losses. We conduct the first-of-its-kind large-scale human subjective study on 3DGS, involving 39,320 pairwise ratings across several datasets and 3DGS frameworks. A regularized version of Wasserstein Distortion, which we call WD-R, emerges as the clear winner, excelling at recovering fine textures without incurring a higher splat count. WD-R is preferred by raters more than $2.3\times$ over the original 3DGS loss, and $1.5\times$ over the current best method Perceptual-GS. WD-R also consistently achieves state-of-the-art LPIPS, DISTS, and FID scores across various datasets, and generalizes across recent frameworks, such as Mip-Splatting and Scaffold-GS, where replacing the original loss with WD-R consistently enhances perceptual quality within a similar resource budget (number of splats for Mip-Splatting, model size for Scaffold-GS), and leads to reconstructions being preferred by human raters $1.8\times$ and $3.6\times$, respectively. We also find that this carries over to the task of 3DGS scene compression, with $\approx 50\%$ bitrate savings for comparable perceptual metric performance.

---

