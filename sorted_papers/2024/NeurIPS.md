# NeurIPS 2024

> **最后更新**： 2026-02-22 01:52:30

本页面包含 2024 年 NeurIPS 会议的论文列表。

## 1. HiCoM: Hierarchical Coherent Motion for Streamable Dynamic Scene with 3D Gaussian Splatting

- **作者**: Qiankun Gao, Jiarui Meng, Chengxiang Wen, Jie Chen, Jian Zhang
- **发布时间**: 2024-11-12
- **arXiv链接**: [arXiv:2411.07541v2](https://arxiv.org/abs/2411.07541v2)
- **说明**: Accepted to NeurIPS 2024; Code is avaliable at https://github.com/gqk/HiCoM
- **英文摘要**: The online reconstruction of dynamic scenes from multi-view streaming videos faces significant challenges in training, rendering and storage efficiency. Harnessing superior learning speed and real-time rendering capabilities, 3D Gaussian Splatting (3DGS) has recently demonstrated considerable potential in this field. However, 3DGS can be inefficient in terms of storage and prone to overfitting by excessively growing Gaussians, particularly with limited views. This paper proposes an efficient framework, dubbed HiCoM, with three key components. First, we construct a compact and robust initial 3DGS representation using a perturbation smoothing strategy. Next, we introduce a Hierarchical Coherent Motion mechanism that leverages the inherent non-uniform distribution and local consistency of 3D Gaussians to swiftly and accurately learn motions across frames. Finally, we continually refine the 3DGS with additional Gaussians, which are later merged into the initial 3DGS to maintain consistency with the evolving scene. To preserve a compact representation, an equivalent number of low-opacity Gaussians that minimally impact the representation are removed before processing subsequent frames. Extensive experiments conducted on two widely used datasets show that our framework improves learning efficiency of the state-of-the-art methods by about $20\%$ and reduces the data storage by $85\%$, achieving competitive free-viewpoint video synthesis quality but with higher robustness and stabili...

---

## 2. Dynamic 3D Gaussian Fields for Urban Areas

- **作者**: Tobias Fischer, Jonas Kulhanek, Samuel Rota Bulò et al.
- **发布时间**: 2024-06-05
- **arXiv链接**: [arXiv:2406.03175v2](https://arxiv.org/abs/2406.03175v2)
- **说明**: NeurIPS'24 spotlight. Project page is available at https://tobiasfshr.github.io/pub/4dgf/
- **英文摘要**: We present an efficient neural 3D scene representation for novel-view synthesis (NVS) in large-scale, dynamic urban areas. Existing works are not well suited for applications like mixed-reality or closed-loop simulation due to their limited visual quality and non-interactive rendering speeds. Recently, rasterization-based approaches have achieved high-quality NVS at impressive speeds. However, these methods are limited to small-scale, homogeneous data, i.e. they cannot handle severe appearance and geometry variations due to weather, season, and lighting and do not scale to larger, dynamic areas with thousands of images. We propose 4DGF, a neural scene representation that scales to large-scale dynamic urban areas, handles heterogeneous input data, and substantially improves rendering speeds. We use 3D Gaussians as an efficient geometry scaffold while relying on neural fields as a compact and flexible appearance model. We integrate scene dynamics via a scene graph at global scale while modeling articulated motions on a local level via deformations. This decomposed approach enables flexible scene composition suitable for real-world applications. In experiments, we surpass the state-of-the-art by over 3 dB in PSNR and more than 200 times in rendering speed.

---

## 3. LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS

- **作者**: Zhiwen Fan, Kevin Wang, Kairun Wen et al.
- **发布时间**: 2023-11-28
- **arXiv链接**: [arXiv:2311.17245v6](https://arxiv.org/abs/2311.17245v6)
- **说明**: NeurIPS 2024, Project page: https://lightgaussian.github.io/
- **英文摘要**: Recent advances in real-time neural rendering using point-based techniques have enabled broader adoption of 3D representations. However, foundational approaches like 3D Gaussian Splatting impose substantial storage overhead, as Structure-from-Motion (SfM) points can grow to millions, often requiring gigabyte-level disk space for a single unbounded scene. This growth presents scalability challenges and hinders splatting efficiency. To address this, we introduce LightGaussian, a method for transforming 3D Gaussians into a more compact format. Inspired by Network Pruning, LightGaussian identifies Gaussians with minimal global significance on scene reconstruction, and applies a pruning and recovery process to reduce redundancy while preserving visual quality. Knowledge distillation and pseudo-view augmentation then transfer spherical harmonic coefficients to a lower degree, yielding compact representations. Gaussian Vector Quantization, based on each Gaussian's global significance, further lowers bitwidth with minimal accuracy loss. LightGaussian achieves an average 15x compression rate while boosting FPS from 144 to 237 within the 3D-GS framework, enabling efficient complex scene representation on the Mip-NeRF 360 and Tank & Temple datasets. The proposed Gaussian pruning approach is also adaptable to other 3D representations (e.g., Scaffold-GS), demonstrating strong generalization capabilities.

---

