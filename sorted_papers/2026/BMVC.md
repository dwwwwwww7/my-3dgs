# BMVC 2026

> **最后更新**： 2026-08-16 01:20:46

本页面包含 2026 年 BMVC 会议的论文列表。

## 1. FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence

- **作者**: Amir Sabbaghziarani, Hanting Ye, Maria Gorlatova, Yi Ding
- **发布时间**: 2026-08-08
- **arXiv链接**: [arXiv:2608.07937v1](https://arxiv.org/abs/2608.07937v1)
- **说明**: Accepted to the British Machine Vision Conference (BMVC) 2026. Code: https://github.com/amir-sbg/FlexSplat
- **英文摘要**: We present FlexSplat, a feed-forward framework for novel view synthesis (NVS) from uncalibrated, object-centric multi-view image collections. A recent line of query-based methods reconstructs a compact set of 3D Gaussians by treating them as transformer queries that are refined with multi-view deformable attention; these methods, however, assume that camera poses are given. FlexSplat removes this assumption: a geometry transformer is trained jointly with the Gaussian decoder to predict per-image camera parameters and depth, which in turn ground a depth-guided Gaussian parameterization and a multi-view deformable cross-attention that aggregates evidence across all input views into a single, view-consistent set of primitives. An uncertainty-weighted depth-consistency objective lets the jointly trained geometry adapt to the reconstruction task, while the cross-view consensus formed during decoding absorbs the residual error of the estimated cameras and depth. The representation uses a compact Gaussian budget that is decoupled from the input resolution - unlike pixel-aligned methods, the primitive count does not grow with the image grid - and is not dictated by the number of views. On ShapeNet-SRN and Google Scanned Objects (GSO), FlexSplat matches or approaches posed state-of-the-art reconstructors while requiring neither camera poses nor ground-truth depth, and matches the best perceptual (LPIPS) quality among the compared methods on GSO. Our results indicate that a jointly tra...

---

