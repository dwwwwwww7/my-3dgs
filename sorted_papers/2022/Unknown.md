# 未知会议 2022

> **最后更新**： 2026-03-22 01:55:49

本页面包含 2022 年 未知会议 会议的论文列表。

## 1. 3DG-STFM: 3D Geometric Guided Student-Teacher Feature Matching

- **作者**: Runyu Mao, Chen Bai, Yatong An, Fengqing Zhu, Cheng Lu
- **发布时间**: 2022-07-06
- **arXiv链接**: [arXiv:2207.02375v2](https://arxiv.org/abs/2207.02375v2)
- **英文摘要**: We tackle the essential task of finding dense visual correspondences between a pair of images. This is a challenging problem due to various factors such as poor texture, repetitive patterns, illumination variation, and motion blur in practical scenarios. In contrast to methods that use dense correspondence ground-truths as direct supervision for local feature matching training, we train 3DG-STFM: a multi-modal matching model (Teacher) to enforce the depth consistency under 3D dense correspondence supervision and transfer the knowledge to 2D unimodal matching model (Student). Both teacher and student models consist of two transformer-based matching modules that obtain dense correspondences in a coarse-to-fine manner. The teacher model guides the student model to learn RGB-induced depth information for the matching purpose on both coarse and fine branches. We also evaluate 3DG-STFM on a model compression task. To the best of our knowledge, 3DG-STFM is the first student-teacher learning method for the local feature matching task. The experiments show that our method outperforms state-of-the-art methods on indoor and outdoor camera pose estimations, and homography estimation problems. Code is available at: https://github.com/Ryan-prime/3DG-STFM.

---

