# NeurIPS 2024

> **最后更新**： 2026-03-29 02:19:01

本页面包含 2024 年 NeurIPS 会议的论文列表。

## 1. HiCoM: Hierarchical Coherent Motion for Streamable Dynamic Scene with 3D Gaussian Splatting

- **作者**: Qiankun Gao, Jiarui Meng, Chengxiang Wen, Jie Chen, Jian Zhang
- **发布时间**: 2024-11-12
- **arXiv链接**: [arXiv:2411.07541v2](http://arxiv.org/abs/2411.07541v2)
- **说明**: Accepted to NeurIPS 2024; Code is avaliable at https://github.com/gqk/HiCoM
- **英文摘要**: The online reconstruction of dynamic scenes from multi-view streaming videos faces significant challenges in training, rendering and storage efficiency. Harnessing superior learning speed and real-time rendering capabilities, 3D Gaussian Splatting (3DGS) has recently demonstrated considerable potential in this field. However, 3DGS can be inefficient in terms of storage and prone to overfitting by excessively growing Gaussians, particularly with limited views. This paper proposes an efficient framework, dubbed HiCoM, with three key components. First, we construct a compact and robust initial 3DGS representation using a perturbation smoothing strategy. Next, we introduce a Hierarchical Coherent Motion mechanism that leverages the inherent non-uniform distribution and local consistency of 3D Gaussians to swiftly and accurately learn motions across frames. Finally, we continually refine the 3DGS with additional Gaussians, which are later merged into the initial 3DGS to maintain consistency with the evolving scene. To preserve a compact representation, an equivalent number of low-opacity Gaussians that minimally impact the representation are removed before processing subsequent frames. Extensive experiments conducted on two widely used datasets show that our framework improves learning efficiency of the state-of-the-art methods by about $20\%$ and reduces the data storage by $85\%$, achieving competitive free-viewpoint video synthesis quality but with higher robustness and stabili...

---

