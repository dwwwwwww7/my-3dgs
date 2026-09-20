# BMVC 2026

> **最后更新**： 2026-09-20 03:21:03

本页面包含 2026 年 BMVC 会议的论文列表。

## 1. LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting

- **作者**: Donghun Ryu, Minhyeok Lee
- **发布时间**: 2026-09-09
- **arXiv链接**: [arXiv:2609.10095v1](https://arxiv.org/abs/2609.10095v1)
- **说明**: Accepted to BMVC 2026. 17 pages main paper + 17 pages supplementary material, 3 figures, 4 tables in the main paper
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis but produces millions of primitives through adaptive densification, leading to significant storage overhead. Learned-mask pruning methods such as LP-3DGS address this by assigning each Gaussian a learnable mask to identify and prune redundant primitives. However, we identify a limitation of this paradigm: the steep slope of the Gumbel-Sigmoid activation drives mask values to the extremes within the short mask-training window, before the importance ranking has stabilized, producing a sharply bimodal distribution from which that ranking can no longer be reliably recovered. We propose LinearMask-GS, which replaces Gumbel-Sigmoid with a linear increment activation that keeps mask values in a mid-confidence regime throughout mask training, producing a stable, unimodal mask distribution whose ranking tracks importance. On Mip-NeRF 360, our method achieves 3.6x and 1.6x Gaussian reductions over 3DGS and LP-3DGS, respectively, while maintaining or improving rendering quality. For outdoor scenes, it yields a 1.6x reduction (from 2.18M to 1.36M) with notable gains in PSNR (+0.38 dB), SSIM (+0.025), and LPIPS (-0.029).

---

## 2. FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence

- **作者**: Amir Sabbaghziarani, Hanting Ye, Maria Gorlatova, Yi Ding
- **发布时间**: 2026-08-08
- **arXiv链接**: [arXiv:2608.07937v1](https://arxiv.org/abs/2608.07937v1)
- **说明**: Accepted to the British Machine Vision Conference (BMVC) 2026. Code: https://github.com/amir-sbg/FlexSplat
- **英文摘要**: We present FlexSplat, a feed-forward framework for novel view synthesis (NVS) from uncalibrated, object-centric multi-view image collections. A recent line of query-based methods reconstructs a compact set of 3D Gaussians by treating them as transformer queries that are refined with multi-view deformable attention; these methods, however, assume that camera poses are given. FlexSplat removes this assumption: a geometry transformer is trained jointly with the Gaussian decoder to predict per-image camera parameters and depth, which in turn ground a depth-guided Gaussian parameterization and a multi-view deformable cross-attention that aggregates evidence across all input views into a single, view-consistent set of primitives. An uncertainty-weighted depth-consistency objective lets the jointly trained geometry adapt to the reconstruction task, while the cross-view consensus formed during decoding absorbs the residual error of the estimated cameras and depth. The representation uses a compact Gaussian budget that is decoupled from the input resolution - unlike pixel-aligned methods, the primitive count does not grow with the image grid - and is not dictated by the number of views. On ShapeNet-SRN and Google Scanned Objects (GSO), FlexSplat matches or approaches posed state-of-the-art reconstructors while requiring neither camera poses nor ground-truth depth, and matches the best perceptual (LPIPS) quality among the compared methods on GSO. Our results indicate that a jointly tra...

---

## 3. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

- **作者**: Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, Hamed Rezazadegan Tavakoli
- **发布时间**: 2026-03-23
- **arXiv链接**: [arXiv:2603.21933v3](https://arxiv.org/abs/2603.21933v3)
- **说明**: 16 pages, 3 figures, 3 tables. Accepted for publication in the Proceedings of the British Machine Vision Conference (BMVC), 2026
- **英文摘要**: The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training pruning method for 3D Gaussian splats that relies solely on attribute-derived neighbourhood descriptors. As our primary contribution, we introduce a hybrid descriptor framework that captures structural and appearance consistency directly from the splat representation. Building on these descriptors, we formulate pruning as a statistical evidence estimation problem and introduce a Beta evidence model that quantifies per-splat reliability through a probabilistic confidence score.   Experiments conducted on standardized test sequences defined by the ISO/IEC MPEG Common Test Conditions (CTC) demonstrate that our approach achieves substantial pruning while preserving reconstruction quality, establishing a practical and generalizable alternative to existing camera-dependent pruning strategies.

---

