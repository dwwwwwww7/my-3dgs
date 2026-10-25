# 未知会议 2027

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2027 年 未知会议 会议的论文列表。

## 1. Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD

- **作者**: Haipeng Wang
- **发布时间**: 2026-10-02
- **arXiv链接**: [arXiv:2610.03162v1](https://arxiv.org/abs/2610.03162v1)
- **说明**: 28 pages, 21 figures. Preprint of the EG 2027 submission (paper1075)
- **英文摘要**: 3D Gaussian Splatting achieves excellent visual quality with real-time rendering, but at the scale of entire cities it does not fit: a trained model carries millions of primitives and gigabytes of memory, and real-time rendering at high quality on a consumer GPU remains out of reach. We introduce Budgeted-GS, a post-hoc method that turns any trained 3DGS model into a factoring tree, a multi-resolution hierarchy of moment-matched aggregates. After a construction pass of a few seconds, a single quality parameter selects, for each view, the level of detail that fits the memory of the target device, so the same city-scale model serves GPUs with widely different memory capacities. When a new scene is to be trained, the same theory applies: instead of growing a full-sized model and compressing it afterwards, budget-centered training first measures how many primitives the scene needs and then trains the model directly at that size, avoiding the wasted effort of optimizing primitives that are later discarded. Both methods are grounded in a measurable capacity floor, a budget-error law derived from optimal transport in phase space; selection rules certified by recent covering theorems decide which primitives are redundant. The floor answers how many primitives a scene actually needs and how many can safely be given up. We validate the floor on 13 public scenes under a preregistered protocol, and exercise both methods from object scenes to an official city capture, rendering it at nati...

---

