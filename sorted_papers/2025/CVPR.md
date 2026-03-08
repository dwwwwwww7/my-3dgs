# CVPR 2025

> **最后更新**： 2026-03-08 01:50:50

本页面包含 2025 年 CVPR 会议的论文列表。

## 1. FlexGS: Train Once, Deploy Everywhere with Many-in-One Flexible 3D Gaussian Splatting

- **作者**: Hengyu Liu, Yuehao Wang, Chenxin Li et al.
- **发布时间**: 2025-06-04
- **arXiv链接**: [arXiv:2506.04174v1](https://arxiv.org/abs/2506.04174v1)
- **说明**: CVPR 2025; Project Page: https://flexgs.github.io
- **英文摘要**: 3D Gaussian splatting (3DGS) has enabled various applications in 3D scene representation and novel view synthesis due to its efficient rendering capabilities. However, 3DGS demands relatively significant GPU memory, limiting its use on devices with restricted computational resources. Previous approaches have focused on pruning less important Gaussians, effectively compressing 3DGS but often requiring a fine-tuning stage and lacking adaptability for the specific memory needs of different devices. In this work, we present an elastic inference method for 3DGS. Given an input for the desired model size, our method selects and transforms a subset of Gaussians, achieving substantial rendering performance without additional fine-tuning. We introduce a tiny learnable module that controls Gaussian selection based on the input percentage, along with a transformation module that adjusts the selected Gaussians to complement the performance of the reduced model. Comprehensive experiments on ZipNeRF, MipNeRF and Tanks\&Temples scenes demonstrate the effectiveness of our approach. Code is available at https://flexgs.github.io.

---

## 2. Steepest Descent Density Control for Compact 3D Gaussian Splatting

- **作者**: Peihao Wang, Yuehao Wang, Dilin Wang et al.
- **发布时间**: 2025-05-08
- **arXiv链接**: [arXiv:2505.05587v1](https://arxiv.org/abs/2505.05587v1)
- **说明**: CVPR 2025, Project page: https://vita-group.github.io/SteepGS/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for real-time, high-resolution novel view synthesis. By representing scenes as a mixture of Gaussian primitives, 3DGS leverages GPU rasterization pipelines for efficient rendering and reconstruction. To optimize scene coverage and capture fine details, 3DGS employs a densification algorithm to generate additional points. However, this process often leads to redundant point clouds, resulting in excessive memory usage, slower performance, and substantial storage demands - posing significant challenges for deployment on resource-constrained devices. To address this limitation, we propose a theoretical framework that demystifies and improves density control in 3DGS. Our analysis reveals that splitting is crucial for escaping saddle points. Through an optimization-theoretic approach, we establish the necessary conditions for densification, determine the minimal number of offspring Gaussians, identify the optimal parameter update direction, and provide an analytical solution for normalizing off-spring opacity. Building on these insights, we introduce SteepGS, incorporating steepest density control, a principled strategy that minimizes loss while maintaining a compact point cloud. SteepGS achieves a ~50% reduction in Gaussian points without compromising rendering quality, significantly enhancing both efficiency and scalability.

---

## 3. NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting

- **作者**: Yulong Zheng, Zicheng Jiang, Shengfeng He et al.
- **发布时间**: 2025-03-24
- **arXiv链接**: [arXiv:2503.18794v1](https://arxiv.org/abs/2503.18794v1)
- **说明**: This paper is accepted by CVPR 2025
- **英文摘要**: Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have noticeably advanced photo-realistic novel view synthesis using images from densely spaced camera viewpoints. However, these methods struggle in few-shot scenarios due to limited supervision. In this paper, we present NexusGS, a 3DGS-based approach that enhances novel view synthesis from sparse-view images by directly embedding depth information into point clouds, without relying on complex manual regularizations. Exploiting the inherent epipolar geometry of 3DGS, our method introduces a novel point cloud densification strategy that initializes 3DGS with a dense point cloud, reducing randomness in point placement while preventing over-smoothing and overfitting. Specifically, NexusGS comprises three key steps: Epipolar Depth Nexus, Flow-Resilient Depth Blending, and Flow-Filtered Depth Pruning. These steps leverage optical flow and camera poses to compute accurate depth maps, while mitigating the inaccuracies often associated with optical flow. By incorporating epipolar depth priors, NexusGS ensures reliable dense point cloud coverage and supports stable 3DGS training under sparse-view conditions. Experiments demonstrate that NexusGS significantly enhances depth accuracy and rendering quality, surpassing state-of-the-art methods by a considerable margin. Furthermore, we validate the superiority of our generated point clouds by substantially boosting the performance of competing methods. Project page: https://usm...

---

## 4. DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation

- **作者**: Xiaoliang Ju, Hongsheng Li
- **发布时间**: 2025-03-10
- **arXiv链接**: [arXiv:2503.06900v1](https://arxiv.org/abs/2503.06900v1)
- **说明**: Accepted by CVPR 2025
- **英文摘要**: We present DirectTriGS, a novel framework designed for 3D object generation with Gaussian Splatting (GS). GS-based rendering for 3D content has gained considerable attention recently. However, there has been limited exploration in directly generating 3D Gaussians compared to traditional generative modeling approaches. The main challenge lies in the complex data structure of GS represented by discrete point clouds with multiple channels. To overcome this challenge, we propose employing the triplane representation, which allows us to represent Gaussian Splatting as an image-like continuous field. This representation effectively encodes both the geometry and texture information, enabling smooth transformation back to Gaussian point clouds and rendering into images by a TriRenderer, with only 2D supervisions. The proposed TriRenderer is fully differentiable, so that the rendering loss can supervise both texture and geometry encoding. Furthermore, the triplane representation can be compressed using a Variational Autoencoder (VAE), which can subsequently be utilized in latent diffusion to generate 3D objects. The experiments demonstrate that the proposed generation framework can produce high-quality 3D object geometry and rendering results in the text-to-3D task.

---

## 5. MoDec-GS: Global-to-Local Motion Decomposition and Temporal Interval Adjustment for Compact Dynamic 3D Gaussian Splatting

- **作者**: Sangwoon Kwak, Joonsoo Kim, Jun Young Jeong et al.
- **发布时间**: 2025-01-07
- **arXiv链接**: [arXiv:2501.03714v3](https://arxiv.org/abs/2501.03714v3)
- **说明**: CVPR2025 (camera ready ver.). The last two authors are co-corresponding authors. Please visit our project page at https://kaist-viclab.github.io/MoDecGS-site/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has made significant strides in scene representation and neural rendering, with intense efforts focused on adapting it for dynamic scenes. Despite delivering remarkable rendering quality and speed, existing methods struggle with storage demands and representing complex real-world motions. To tackle these issues, we propose MoDecGS, a memory-efficient Gaussian splatting framework designed for reconstructing novel views in challenging scenarios with complex motions. We introduce GlobaltoLocal Motion Decomposition (GLMD) to effectively capture dynamic motions in a coarsetofine manner. This approach leverages Global Canonical Scaffolds (Global CS) and Local Canonical Scaffolds (Local CS), extending static Scaffold representation to dynamic video reconstruction. For Global CS, we propose Global Anchor Deformation (GAD) to efficiently represent global dynamics along complex motions, by directly deforming the implicit Scaffold attributes which are anchor position, offset, and local context features. Next, we finely adjust local motions via the Local Gaussian Deformation (LGD) of Local CS explicitly. Additionally, we introduce Temporal Interval Adjustment (TIA) to automatically control the temporal coverage of each Local CS during training, allowing MoDecGS to find optimal interval assignments based on the specified number of temporal segments. Extensive evaluations demonstrate that MoDecGS achieves an average 70% reduction in model size over stateofthear...

---

## 6. MaskGaussian: Adaptive 3D Gaussian Representation from Probabilistic Masks

- **作者**: Yifei Liu, Zhihang Zhong, Yifan Zhan, Sheng Xu, Xiao Sun
- **发布时间**: 2024-12-29
- **arXiv链接**: [arXiv:2412.20522v3](https://arxiv.org/abs/2412.20522v3)
- **说明**: CVPR 2025; Project page:https://maskgaussian.github.io/
- **英文摘要**: While 3D Gaussian Splatting (3DGS) has demonstrated remarkable performance in novel view synthesis and real-time rendering, the high memory consumption due to the use of millions of Gaussians limits its practicality. To mitigate this issue, improvements have been made by pruning unnecessary Gaussians, either through a hand-crafted criterion or by using learned masks. However, these methods deterministically remove Gaussians based on a snapshot of the pruning moment, leading to sub-optimized reconstruction performance from a long-term perspective. To address this issue, we introduce MaskGaussian, which models Gaussians as probabilistic entities rather than permanently removing them, and utilize them according to their probability of existence. To achieve this, we propose a masked-rasterization technique that enables unused yet probabilistically existing Gaussians to receive gradients, allowing for dynamic assessment of their contribution to the evolving scene and adjustment of their probability of existence. Hence, the importance of Gaussians iteratively changes and the pruned Gaussians are selected diversely. Extensive experiments demonstrate the superiority of the proposed method in achieving better rendering quality with fewer Gaussians than previous pruning methods, pruning over 60% of Gaussians on average with only a 0.02 PSNR decline. Our code can be found at: https://github.com/kaikai23/MaskGaussian

---

## 7. Speedy-Splat: Fast 3D Gaussian Splatting with Sparse Pixels and Sparse Primitives

- **作者**: Alex Hanson, Allen Tu, Geng Lin et al.
- **发布时间**: 2024-11-30
- **arXiv链接**: [arXiv:2412.00578v3](https://arxiv.org/abs/2412.00578v3)
- **说明**: CVPR 2025, Project Page: https://speedysplat.github.io/
- **英文摘要**: 3D Gaussian Splatting (3D-GS) is a recent 3D scene reconstruction technique that enables real-time rendering of novel views by modeling scenes as parametric point clouds of differentiable 3D Gaussians. However, its rendering speed and model size still present bottlenecks, especially in resource-constrained settings. In this paper, we identify and address two key inefficiencies in 3D-GS to substantially improve rendering speed. These improvements also yield the ancillary benefits of reduced model size and training time. First, we optimize the rendering pipeline to precisely localize Gaussians in the scene, boosting rendering speed without altering visual fidelity. Second, we introduce a novel pruning technique and integrate it into the training pipeline, significantly reducing model size and training time while further raising rendering speed. Our Speedy-Splat approach combines these techniques to accelerate average rendering speed by a drastic $\mathit{6.71\times}$ across scenes from the Mip-NeRF 360, Tanks & Temples, and Deep Blending datasets.

---

## 8. GaussianSpa: An "Optimizing-Sparsifying" Simplification Framework for Compact and High-Quality 3D Gaussian Splatting

- **作者**: Yangming Zhang, Wenqi Jia, Wei Niu, Miao Yin
- **发布时间**: 2024-11-09
- **arXiv链接**: [arXiv:2411.06019v3](https://arxiv.org/abs/2411.06019v3)
- **说明**: CVPR 2025. Project page at https://noodle-lab.github.io/gaussianspa/
- **英文摘要**: 3D Gaussian Splatting (3DGS) has emerged as a mainstream for novel view synthesis, leveraging continuous aggregations of Gaussian functions to model scene geometry. However, 3DGS suffers from substantial memory requirements to store the multitude of Gaussians, hindering its practicality. To address this challenge, we introduce GaussianSpa, an optimization-based simplification framework for compact and high-quality 3DGS. Specifically, we formulate the simplification as an optimization problem associated with the 3DGS training. Correspondingly, we propose an efficient "optimizing-sparsifying" solution that alternately solves two independent sub-problems, gradually imposing strong sparsity onto the Gaussians in the training process. Our comprehensive evaluations on various datasets show the superiority of GaussianSpa over existing state-of-the-art approaches. Notably, GaussianSpa achieves an average PSNR improvement of 0.9 dB on the real-world Deep Blending dataset with 10$\times$ fewer Gaussians compared to the vanilla 3DGS. Our project page is available at https://noodle-lab.github.io/gaussianspa/.

---

## 9. PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting

- **作者**: Alex Hanson, Allen Tu, Vasu Singla et al.
- **发布时间**: 2024-06-14
- **arXiv链接**: [arXiv:2406.10219v3](https://arxiv.org/abs/2406.10219v3)
- **说明**: CVPR 2025, Project Page: https://pup3dgs.github.io/
- **英文摘要**: Recent advances in novel view synthesis have enabled real-time rendering speeds with high reconstruction accuracy. 3D Gaussian Splatting (3D-GS), a foundational point-based parametric 3D scene representation, models scenes as large sets of 3D Gaussians. However, complex scenes can consist of millions of Gaussians, resulting in high storage and memory requirements that limit the viability of 3D-GS on devices with limited resources. Current techniques for compressing these pretrained models by pruning Gaussians rely on combining heuristics to determine which Gaussians to remove. At high compression ratios, these pruned scenes suffer from heavy degradation of visual fidelity and loss of foreground details. In this paper, we propose a principled sensitivity pruning score that preserves visual fidelity and foreground details at significantly higher compression ratios than existing approaches. It is computed as a second-order approximation of the reconstruction error on the training views with respect to the spatial parameters of each Gaussian. Additionally, we propose a multi-round prune-refine pipeline that can be applied to any pretrained 3D-GS model without changing its training pipeline. After pruning 90% of Gaussians, a substantially higher percentage than previous methods, our PUP 3D-GS pipeline increases average rendering speed by 3.56$\times$ while retaining more salient foreground information and achieving higher image quality metrics than existing techniques on scenes fr...

---

## 10. Generative Gaussian Splatting for Unbounded 3D City Generation

- **作者**: Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu
- **发布时间**: 2024-06-10
- **arXiv链接**: [arXiv:2406.06526v3](https://arxiv.org/abs/2406.06526v3)
- **说明**: CVPR 2025. Project Page: https://haozhexie.com/project/gaussian-city
- **英文摘要**: 3D city generation with NeRF-based methods shows promising generation results but is computationally inefficient. Recently 3D Gaussian Splatting (3D-GS) has emerged as a highly efficient alternative for object-level 3D generation. However, adapting 3D-GS from finite-scale 3D objects and humans to infinite-scale 3D cities is non-trivial. Unbounded 3D city generation entails significant storage overhead (out-of-memory issues), arising from the need to expand points to billions, often demanding hundreds of Gigabytes of VRAM for a city scene spanning 10km^2. In this paper, we propose GaussianCity, a generative Gaussian Splatting framework dedicated to efficiently synthesizing unbounded 3D cities with a single feed-forward pass. Our key insights are two-fold: 1) Compact 3D Scene Representation: We introduce BEV-Point as a highly compact intermediate representation, ensuring that the growth in VRAM usage for unbounded scenes remains constant, thus enabling unbounded city generation. 2) Spatial-aware Gaussian Attribute Decoder: We present spatial-aware BEV-Point decoder to produce 3D Gaussian attributes, which leverages Point Serializer to integrate the structural and contextual characteristics of BEV points. Extensive experiments demonstrate that GaussianCity achieves state-of-the-art results in both drone-view and street-view 3D city generation. Notably, compared to CityDreamer, GaussianCity exhibits superior performance with a speedup of 60 times (10.72 FPS v.s. 0.18 FPS).

---

## 11. Improving Gaussian Splatting with Localized Points Management

- **作者**: Haosen Yang, Chenhao Zhang, Wenqing Wang et al.
- **发布时间**: 2024-06-06
- **arXiv链接**: [arXiv:2406.04251v3](https://arxiv.org/abs/2406.04251v3)
- **说明**: CVPR 2025 (Highlight). Github: https://happy-hsy.github.io/projects/LPM/
- **英文摘要**: Point management is critical for optimizing 3D Gaussian Splatting models, as point initiation (e.g., via structure from motion) is often distributionally inappropriate. Typically, Adaptive Density Control (ADC) algorithm is adopted, leveraging view-averaged gradient magnitude thresholding for point densification, opacity thresholding for pruning, and regular all-points opacity reset. We reveal that this strategy is limited in tackling intricate/special image regions (e.g., transparent) due to inability of identifying all 3D zones requiring point densification, and lacking an appropriate mechanism to handle ill-conditioned points with negative impacts (e.g., occlusion due to false high opacity). To address these limitations, we propose a Localized Point Management (LPM) strategy, capable of identifying those error-contributing zones in greatest need for both point addition and geometry calibration. Zone identification is achieved by leveraging the underlying multiview geometry constraints, subject to image rendering errors. We apply point densification in the identified zones and then reset the opacity of the points in front of these regions, creating a new opportunity to correct poorly conditioned points. Serving as a versatile plugin, LPM can be seamlessly integrated into existing static 3D and dynamic 4D Gaussian Splatting models with minimal additional cost. Experimental evaluations validate the efficacy of our LPM in boosting a variety of existing 3D/4D models both quanti...

---

