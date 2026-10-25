# WACV 2025

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2025 年 WACV 会议的论文列表。

## 1. GoDe: Gaussians on Demand for Backbone-Agnostic Progressive Compression

- **作者**: Francesco Di Sario, Riccardo Renzulli, Marco Grangetto, Akihiro Sugimoto, Enzo Tartaglione
- **发布时间**: 2025-01-23
- **arXiv链接**: [arXiv:2501.13558v4](https://arxiv.org/abs/2501.13558v4)
- **说明**: Accepted at WACV27. Previously titled "GoDe: Gaussians on Demand for Progressive Level-of-Detail and Scalable Compression"
- **英文摘要**: Splat-based radiance fields have rapidly diversified in primitive type, kernel support, and appearance parameterization. This diversity makes compression difficult: most codecs are single-rate, requiring a separately optimized model for each target bitrate, while progressive codecs remain tied to representation-specific assumptions that do not transfer across backbones. We introduce GoDe (Gaussians on Demand), a progressive compression framework whose central contribution is backbone agnosticism. It reorganizes any trained differentiable splat representation into a single scalable bitstream without modifying the backbone or re-deriving the compression structure for each new primitive type. GoDe builds a nested level-of-detail hierarchy via masked-gradient importance ranking, refines all levels with one quantization-aware fine-tuning stage, and stores the base layer and enhancement layers as progressive chunks compressed with shared entropy dictionaries. Any decoded prefix is directly renderable, so one training pipeline provides multiple rate-distortion operating points without per-rate retraining. Across five heterogeneous backbones and three standard benchmarks, GoDe achieves competitive rate-distortion performance while enabling faster rendering and substantially faster progressive decoding than existing methods. Project page: https://gaussians-on-demand.github.io/

---

