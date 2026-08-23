# TVCG 2026

> **最后更新**： 2026-08-23 01:22:53

本页面包含 2026 年 TVCG 会议的论文列表。

## 1. AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting

- **作者**: ByungHyun Kim, Jinwoo Jeon, Woontack Woo
- **发布时间**: 2026-07-29
- **arXiv链接**: [arXiv:2607.26525v1](https://arxiv.org/abs/2607.26525v1)
- **说明**: Accepted to IEEE ISMAR 2026 (TVCG)
- **英文摘要**: 3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis with real-time rendering, but deploying compressed object-centric 3DGS in XR requires more than image-space rate-distortion. In practical XR asset pipelines, reusable objects are repeatedly packaged, transmitted, decoded, and instantiated, making asset-preparation cost, codec compatibility, decoding latency, and preservation of depth and silhouette cues first-class concerns. Existing 3DGS compression methods are largely developed for scene-scale captures and often rely on heavy layout generation or aggressive global pruning, assumptions that transfer poorly to semantically concentrated foreground objects. We present AtlasLC, a source-free, training-free compression pipeline for object-centric 3DGS that operates directly on released Gaussian assets, without original images, camera poses, or per-asset optimization. AtlasLC couples local-competition pruning with deterministic atlas packing to remove the mapping/remapping bottleneck while preserving object-wide foreground support; a lightweight single-pass sort-based conditional transport is used as a shared coordinate backbone for these stages. Across the evaluated assets, AtlasLC reduces atlas-preparation time by up to a factor of 25 and end-to-end compression time by up to a factor of 5, while offering a favorable deployment-aware balance of payload, decode latency, runtime FPS, and 3D geometry relative to the evaluated compressed baselines. Relative to s...

---

