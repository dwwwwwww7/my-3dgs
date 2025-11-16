# 未知会议 2021

> **最后更新**： 2025-11-16 09:25:49

本页面包含 2021 年 未知会议 会议的论文列表。

## 1. 3D Scene Compression through Entropy Penalized Neural Representation Functions

- **作者**: Thomas Bird, Johannes Ballé, Saurabh Singh, Philip A. Chou
- **发布时间**: 2021-04-26
- **arXiv链接**: [arXiv:2104.12456v1](https://arxiv.org/abs/2104.12456v1)
- **说明**: accepted (in an abridged format) as a contribution to the Learning-based Image Coding special session of the Picture Coding Symposium 2021
- **英文摘要**: Some forms of novel visual media enable the viewer to explore a 3D scene from arbitrary viewpoints, by interpolating between a discrete set of original views. Compared to 2D imagery, these types of applications require much larger amounts of storage space, which we seek to reduce. Existing approaches for compressing 3D scenes are based on a separation of compression and rendering: each of the original views is compressed using traditional 2D image formats; the receiver decompresses the views and then performs the rendering. We unify these steps by directly compressing an implicit representation of the scene, a function that maps spatial coordinates to a radiance vector field, which can then be queried to render arbitrary viewpoints. The function is implemented as a neural network and jointly trained for reconstruction as well as compressibility, in an end-to-end manner, with the use of an entropy penalty on the parameters. Our method significantly outperforms a state-of-the-art conventional approach for scene compression, achieving simultaneously higher quality reconstructions and lower bitrates. Furthermore, we show that the performance at lower bitrates can be improved by jointly representing multiple scenes using a soft form of parameter sharing.

---

