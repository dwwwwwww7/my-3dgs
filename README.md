# 3D Gaussian Splatting 论文列表

> **最后更新**： 2025-08-21 05:19:58

> **翻译说明**： 中文摘要由Edge浏览器翻译API自动生成，可能存在不准确之处。如需查看精确表达请参考原文摘要。


## August 2025

### [1] GeMS: Efficient Gaussian Splatting for Extreme Motion Blur  
- **⏳发布**：2025-08-20  
- **🧑‍🔬作者**：Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2508.14682v1)    
- **📝摘要**：We introduce GeMS, a framework for 3D Gaussian Splatting (3DGS) designed to handle severely motion-blurred images. State-of-the-art deblurring methods for extreme blur, such as ExBluRF, as well as Gaussian Splatting-based approaches like Deblur-GS, typically assume access to sharp images for camera pose estimation and point cloud generation, an unrealistic assumption. Methods relying on COLMAP initialization, such as BAD-Gaussians, also fail due to unreliable feature correspondences under severe blur. To address these challenges, we propose GeMS, a 3DGS framework that reconstructs scenes directly from extremely blurred images. GeMS integrates: (1) VGGSfM, a deep learning-based Structure-from-Motion pipeline that estimates poses and generates point clouds directly from blurred inputs; (2) 3DGS-MCMC, which enables robust scene initialization by treating Gaussians as samples from a probability distribution, eliminating heuristic densification and pruning; and (3) joint optimization of camera trajectories and Gaussian parameters for stable reconstruction. While this pipeline produces strong results, inaccuracies may remain when ...  
- **📝翻译未启用或未翻译**  

### [2] EntropyGS: An Efficient Entropy Coding on 3D Gaussian Splatting  
- **⏳发布**：2025-08-13  
- **🧑‍🔬作者**：Yuning Huang, Jiahao Pang, Fengqing Zhu, Dong Tian  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2508.10227v1)    
- **📝摘要**：As an emerging novel view synthesis approach, 3D Gaussian Splatting (3DGS) demonstrates fast training/rendering with superior visual quality. The two tasks of 3DGS, Gaussian creation and view rendering, are typically separated over time or devices, and thus storage/transmission and finally compression of 3DGS Gaussians become necessary. We begin with a correlation and statistical analysis of 3DGS Gaussian attributes. An inspiring finding in this work reveals that spherical harmonic AC attributes precisely follow Laplace distributions, while mixtures of Gaussian distributions can approximate rotation, scaling, and opacity. Additionally, harmonic AC attributes manifest weak correlations with other attributes except for inherited correlations from a color space. A factorized and parameterized entropy coding method, EntropyGS, is hereinafter proposed. During encoding, distribution parameters of each Gaussian attribute are estimated to assist their entropy coding. The quantization for entropy coding is adaptively performed according to Gaussian attribute types. EntropyGS demonstrates about 30x rate reduction on benchmark ...  
- **📝翻译未启用或未翻译**  

### [3] Communication Efficient Robotic Mixed Reality with Gaussian Splatting  Cross-Layer Optimization  
- **⏳发布**：2025-08-12  
- **🧑‍🔬作者**：Chenxuan Liu, He Li, Zongze Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2508.08624v1)    
- **📝摘要**：Realizing low-cost communication in robotic mixed reality (RoboMR) systems presents a challenge, due to the necessity of uploading high-resolution images through wireless channels. This paper proposes Gaussian splatting (GS) RoboMR (GSMR), which enables the simulator to opportunistically render a photo-realistic view from the robot's pose by calling ``memory'' from a GS model, thus reducing the need for excessive image uploads. However, the GS model may involve discrepancies compared to the actual environments. To this end, a GS cross-layer optimization (GSCLO) framework is further proposed, which jointly optimizes content switching (i.e., deciding whether to upload image or not) and power allocation (i.e., adjusting to content profiles) across different frames by minimizing a newly derived GSMR loss function. The GSCLO problem is addressed by an accelerated penalty optimization (APO) algorithm that reduces computational complexity by over $10$x compared to traditional branch-and-bound and search algorithms. Moreover, variants of GSCLO are presented to achieve ...  
- **📝翻译未启用或未翻译**  

### [4] 3DGS-VBench: A Comprehensive Video Quality Evaluation Benchmark for 3DGS  Compression  
- **⏳发布**：2025-08-09  
- **🧑‍🔬作者**：Yuke Xing, William Gordon, Qi Yang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2508.07038v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) enables real-time novel view synthesis with high visual fidelity, but its substantial storage requirements hinder practical deployment, prompting state-of-the-art (SOTA) 3DGS methods to incorporate compression modules. However, these 3DGS generative compression techniques introduce unique distortions lacking systematic quality assessment research. To this end, we establish 3DGS-VBench, a large-scale Video Quality Assessment (VQA) Dataset and Benchmark with 660 compressed 3DGS models and video sequences generated from 11 scenes across 6 SOTA 3DGS compression algorithms with systematically designed parameter levels. With annotations from 50 participants, we obtained MOS scores with outlier removal and validated dataset reliability. We benchmark 6 3DGS compression algorithms on storage efficiency and visual quality, and evaluate 15 quality assessment metrics across multiple paradigms. Our work enables specialized VQA model training for 3DGS, serving as a catalyst for compression and quality assessment research. The dataset is available at https://github.com/YukeXing/3DGS-VBench.  
- **📝翻译未启用或未翻译**  

### [5] SA-3DGS: A Self-Adaptive Compression Method for 3D Gaussian Splatting  
- **⏳发布**：2025-08-05  
- **🧑‍🔬作者**：Liheng Zhang, Weihao Yu, Zubo Lu, Haozhi Gu, Jin Huang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2508.03017v1)    
- **📝摘要**：Recent advancements in 3D Gaussian Splatting have enhanced efficient and high-quality novel view synthesis. However, representing scenes requires a large number of Gaussian points, leading to high storage demands and limiting practical deployment. The latest methods facilitate the compression of Gaussian models but struggle to identify truly insignificant Gaussian points in the scene, leading to a decline in subsequent Gaussian pruning, compression quality, and rendering performance. To address this issue, we propose SA-3DGS, a method that significantly reduces storage costs while maintaining rendering quality. SA-3DGS learns an importance score to automatically identify the least significant Gaussians in scene reconstruction, thereby enabling effective pruning and redundancy reduction. Next, the importance-aware clustering module compresses Gaussians attributes more accurately into the codebook, improving the codebook's expressive capability while reducing model size. Finally, the codebook repair module leverages contextual scene information to repair the codebook, thereby recovering the original Gaussian point attributes and mitigating ...  
- **📝翻译未启用或未翻译**  


## July 2025

### [1] Robust and Efficient 3D Gaussian Splatting for Urban Scene  Reconstruction  
- **⏳发布**：2025-07-30  
- **🧑‍🔬作者**：Zhensheng Yuan, Haozhi Huang, Zhen Xiong, Di Wang, Guanghua Yang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2507.23006v1)   · [Project](https://yzslab.github.io/REUrbanGS.)  
- **📝摘要**：We present a framework that enables fast reconstruction and real-time rendering of urban-scale scenes while maintaining robustness against appearance variations across multi-view captures. Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency. A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity. The appearance transformation module mitigates the negative effects of appearance inconsistencies across images while enabling flexible adjustments. Additionally, we utilize enhancement modules, such as depth regularization, scale regularization, and antialiasing, to improve reconstruction fidelity. Experimental results demonstrate that our method effectively reconstructs urban-scale scenes and outperforms previous approaches in both efficiency and quality. The source code is available at: https://yzslab.github.io/REUrbanGS.  
- **📝翻译未启用或未翻译**  

### [2] SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene  Reconstruction  
- **⏳发布**：2025-07-10  
- **🧑‍🔬作者**：Wei Yao, Shuzhao Xie, Letian Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2507.07465v1)    
- **📝摘要**：Current 4D Gaussian frameworks for dynamic scene reconstruction deliver impressive visual fidelity and rendering speed, however, the inherent trade-off between storage costs and the ability to characterize complex physical motions significantly limits the practical application of these methods. To tackle these problems, we propose SD-GS, a compact and efficient dynamic Gaussian splatting framework for complex dynamic scene reconstruction, featuring two key contributions. First, we introduce a deformable anchor grid, a hierarchical and memory-efficient scene representation where each anchor point derives multiple 3D Gaussians in its local spatiotemporal region and serves as the geometric backbone of the 3D scene. Second, to enhance modeling capability for complex motions, we present a deformation-aware densification strategy that adaptively grows anchors in under-reconstructed high-dynamic regions while reducing redundancy in static areas, achieving superior visual quality with fewer anchors. Experimental results demonstrate that, compared to state-of-the-art methods, SD-GS achieves an average of 60\% reduction in model ...  
- **📝翻译未启用或未翻译**  

### [3] FlexGaussian: Flexible and Cost-Effective Training-Free Compression for  3D Gaussian Splatting  
- **⏳发布**：2025-07-09  
- **🧑‍🔬作者**：Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2507.06671v1)    
- **📝摘要**：3D Gaussian splatting has become a prominent technique for representing and rendering complex 3D scenes, due to its high fidelity and speed advantages. However, the growing demand for large-scale models calls for effective compression to reduce memory and computation costs, especially on mobile and edge devices with limited resources. Existing compression methods effectively reduce 3D Gaussian parameters but often require extensive retraining or fine-tuning, lacking flexibility under varying compression constraints. In this paper, we introduce FlexGaussian, a flexible and cost-effective method that combines mixed-precision quantization with attribute-discriminative pruning for training-free 3D Gaussian compression. FlexGaussian eliminates the need for retraining and adapts easily to diverse compression targets. Evaluation results show that FlexGaussian achieves up to 96.4% compression while maintaining high rendering quality (<1 dB drop in PSNR), and is deployable on mobile devices. FlexGaussian delivers high compression ratios within seconds, being 1.7-2.1x faster than state-of-the-art training-free methods and 10-100x faster than ...  
- **📝翻译未启用或未翻译**  

### [4] D-FCGS: Feedforward Compression of Dynamic Gaussian Splatting for  Free-Viewpoint Videos  
- **⏳发布**：2025-07-08  
- **🧑‍🔬作者**：Wenkang Zhang, Yan Zhao, Qiang Wang, Li Song, Zhengxue Cheng  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2507.05859v1)    
- **📝摘要**：Free-viewpoint video (FVV) enables immersive 3D experiences, but efficient compression of dynamic 3D representations remains a major challenge. Recent advances in 3D Gaussian Splatting (3DGS) and its dynamic extensions have enabled high-fidelity scene modeling. However, existing methods often couple scene reconstruction with optimization-dependent coding, which limits generalizability. This paper presents Feedforward Compression of Dynamic Gaussian Splatting (D-FCGS), a novel feedforward framework for compressing temporally correlated Gaussian point cloud sequences. Our approach introduces a Group-of-Frames (GoF) structure with I-P frame coding, where inter-frame motions are extracted via sparse control points. The resulting motion tensors are compressed in a feedforward manner using a dual prior-aware entropy model that combines hyperprior and spatial-temporal priors for accurate rate estimation. For reconstruction, we perform control-point-guided motion compensation and employ a refinement network to enhance view-consistent fidelity. Trained on multi-view video-derived Gaussian frames, D-FCGS generalizes across scenes without per-scene optimization. Experiments show that it matches the ...  
- **📝翻译未启用或未翻译**  


## June 2025

### [1] MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient  Surface Reconstruction  
- **⏳发布**：2025-06-30  
- **🧑‍🔬作者**：Antoine Guédon, Diego Gomez, Nissim Maruani et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.24096v1)    
- **📝摘要**：While recent advances in Gaussian Splatting have enabled fast reconstruction of high-quality 3D scenes from images, extracting accurate surface meshes remains a challenge. Current approaches extract the surface through costly post-processing steps, resulting in the loss of fine geometric details or requiring significant time and leading to very dense meshes with millions of vertices. More fundamentally, the a posteriori conversion from a volumetric to a surface representation limits the ability of the final mesh to preserve all geometric structures captured during training. We present MILo, a novel Gaussian Splatting framework that bridges the gap between volumetric and surface representations by differentiably extracting a mesh from the 3D Gaussians. We design a fully differentiable procedure that constructs the mesh-including both vertex locations and connectivity-at every iteration directly from the parameters of the Gaussians, which are the only quantities optimized during training. Our method introduces three key technical contributions: a bidirectional consistency ...  
- **📝翻译未启用或未翻译**  

### [2] From Coarse to Fine: Learnable Discrete Wavelet Transforms for Efficient  3D Gaussian Splatting  
- **⏳发布**：2025-06-29  
- **🧑‍🔬作者**：Hung Nguyen, An Le, Runfa Li, Truong Nguyen  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.23042v1)    
- **📝摘要**：3D Gaussian Splatting has emerged as a powerful approach in novel view synthesis, delivering rapid training and rendering but at the cost of an ever-growing set of Gaussian primitives that strains memory and bandwidth. We introduce AutoOpti3DGS, a training-time framework that automatically restrains Gaussian proliferation without sacrificing visual fidelity. The key idea is to feed the input images to a sequence of learnable Forward and Inverse Discrete Wavelet Transforms, where low-pass filters are kept fixed, high-pass filters are learnable and initialized to zero, and an auxiliary orthogonality loss gradually activates fine frequencies. This wavelet-driven, coarse-to-fine process delays the formation of redundant fine Gaussians, allowing 3DGS to capture global structure first and refine detail only when necessary. Through extensive experiments, AutoOpti3DGS requires just a single filter learning-rate hyper-parameter, integrates seamlessly with existing efficient 3DGS frameworks, and consistently produces sparser scene representations more compatible with memory or storage-constrained hardware.  
- **📝翻译未启用或未翻译**  

### [3] Confident Splatting: Confidence-Based Compression of 3D Gaussian  Splatting via Learnable Beta Distributions  
- **⏳发布**：2025-06-28  
- **🧑‍🔬作者**：AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.22973v1)    
- **📝摘要**：3D Gaussian Splatting enables high-quality real-time rendering but often produces millions of splats, resulting in excessive storage and computational overhead. We propose a novel lossy compression method based on learnable confidence scores modeled as Beta distributions. Each splat's confidence is optimized through reconstruction-aware losses, enabling pruning of low-confidence splats while preserving visual fidelity. The proposed approach is architecture-agnostic and can be applied to any Gaussian Splatting variant. In addition, the average confidence values serve as a new metric to assess the quality of the scene. Extensive experiments demonstrate favorable trade-offs between compression and fidelity compared to prior work. Our code and data are publicly available at https://github.com/amirhossein-razlighi/Confident-Splatting  
- **📝翻译未启用或未翻译**  

### [4] SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads  Synthesis Using Gaussian Splatting  
- **⏳发布**：2025-06-17  
- **🧑‍🔬作者**：Ziqiao Peng, Wentao Hu, Junyuan Ma et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.14742v1)   · [Project](https://ziqiaopeng.github.io/synctalk++.)  
- **📝摘要**：Achieving high synchronization in the synthesis of realistic, speech-driven talking head videos presents a significant challenge. A lifelike talking head requires synchronized coordination of subject identity, lip movements, facial expressions, and head poses. The absence of these synchronizations is a fundamental flaw, leading to unrealistic results. To address the critical issue of synchronization, identified as the ''devil'' in creating realistic talking heads, we introduce SyncTalk++, which features a Dynamic Portrait Renderer with Gaussian Splatting to ensure consistent subject identity preservation and a Face-Sync Controller that aligns lip movements with speech while innovatively using a 3D facial blendshape model to reconstruct accurate facial expressions. To ensure natural head movements, we propose a Head-Sync Stabilizer, which optimizes head poses for greater stability. Additionally, SyncTalk++ enhances robustness to out-of-distribution (OOD) audio by incorporating an Expression Generator and a Torso Restorer, which generate speech-matched facial expressions and seamless torso regions. Our approach maintains consistency ...  
- **📝翻译未启用或未翻译**  

### [5] HRGS: Hierarchical Gaussian Splatting for Memory-Efficient  High-Resolution 3D Reconstruction  
- **⏳发布**：2025-06-17  
- **🧑‍🔬作者**：Changbai Li, Haodong Zhu, Hanlin Chen et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.14229v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has made significant strides in real-time 3D scene reconstruction, but faces memory scalability issues in high-resolution scenarios. To address this, we propose Hierarchical Gaussian Splatting (HRGS), a memory-efficient framework with hierarchical block-level optimization. First, we generate a global, coarse Gaussian representation from low-resolution data. Then, we partition the scene into multiple blocks, refining each block with high-resolution data. The partitioning involves two steps: Gaussian partitioning, where irregular scenes are normalized into a bounded cubic space with a uniform grid for task distribution, and training data partitioning, where only relevant observations are retained for each block. By guiding block refinement with the coarse Gaussian prior, we ensure seamless Gaussian fusion across adjacent blocks. To reduce computational demands, we introduce Importance-Driven Gaussian Pruning (IDGP), which computes importance scores for each Gaussian and removes those with minimal contribution, speeding up convergence and reducing memory usage. Additionally, we incorporate normal ...  
- **📝翻译未启用或未翻译**  

### [6] Efficient multi-view training for 3D Gaussian Splatting  
- **⏳发布**：2025-06-15（更新：2025-06-17）  
- **🧑‍🔬作者**：Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.12727v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a preferred choice alongside Neural Radiance Fields (NeRF) in inverse rendering due to its superior rendering speed. Currently, the common approach in 3DGS is to utilize "single-view" mini-batch training, where only one image is processed per iteration, in contrast to NeRF's "multi-view" mini-batch training, which leverages multiple images. We observe that such single-view training can lead to suboptimal optimization due to increased variance in mini-batch stochastic gradients, highlighting the necessity for multi-view training. However, implementing multi-view training in 3DGS poses challenges. Simply rendering multiple images per iteration incurs considerable overhead and may result in suboptimal Gaussian densification due to its reliance on single-view assumptions. To address these issues, we modify the rasterization process to minimize the overhead associated with multi-view training and propose a 3D distance-aware D-SSIM loss and multi-view adaptive density control that better suits multi-view scenarios. Our experiments demonstrate that the ...  
- **📝翻译未启用或未翻译**  

### [7] Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression  of Dynamic Scenes  
- **⏳发布**：2025-06-09  
- **🧑‍🔬作者**：Allen Tu, Haiyang Ying, Alex Hanson et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.07917v1)    
- **📝摘要**：Recent extensions of 3D Gaussian Splatting (3DGS) to dynamic scenes achieve high-quality novel view synthesis by using neural networks to predict the time-varying deformation of each Gaussian. However, performing per-Gaussian neural inference at every frame poses a significant bottleneck, limiting rendering speed and increasing memory and compute requirements. In this paper, we present Speedy Deformable 3D Gaussian Splatting (SpeeDe3DGS), a general pipeline for accelerating the rendering speed of dynamic 3DGS and 4DGS representations by reducing neural inference through two complementary techniques. First, we propose a temporal sensitivity pruning score that identifies and removes Gaussians with low contribution to the dynamic scene reconstruction. We also introduce an annealing smooth pruning mechanism that improves pruning robustness in real-world scenes with imprecise camera poses. Second, we propose GroupFlow, a motion analysis technique that clusters Gaussians by trajectory similarity and predicts a single rigid transformation per group instead of separate deformations for each Gaussian. ...  
- **📝翻译未启用或未翻译**  

### [8] GSCodec Studio: A Modular Framework for Gaussian Splat Compression  
- **⏳发布**：2025-06-02  
- **🧑‍🔬作者**：Sicheng Li, Chengzhen Wu, Hao Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2506.01822v1)    
- **📝摘要**：3D Gaussian Splatting and its extension to 4D dynamic scenes enable photorealistic, real-time rendering from real-world captures, positioning Gaussian Splats (GS) as a promising format for next-generation immersive media. However, their high storage requirements pose significant challenges for practical use in sharing, transmission, and storage. Despite various studies exploring GS compression from different perspectives, these efforts remain scattered across separate repositories, complicating benchmarking and the integration of best practices. To address this gap, we present GSCodec Studio, a unified and modular framework for GS reconstruction, compression, and rendering. The framework incorporates a diverse set of 3D/4D GS reconstruction methods and GS compression techniques as modular components, facilitating flexible combinations and comprehensive comparisons. By integrating best practices from community research and our own explorations, GSCodec Studio supports the development of compact representation and compression solutions for static and dynamic Gaussian Splats, namely our Static and Dynamic GSCodec, achieving competitive rate-distortion performance ...  
- **📝翻译未启用或未翻译**  


## May 2025

### [1] 3DGEER: Exact and Efficient Volumetric Rendering with 3D Gaussians  
- **⏳发布**：2025-05-29  
- **🧑‍🔬作者**：Zixun Huang, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Liu Ren  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.24053v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) marks a significant milestone in balancing the quality and efficiency of differentiable rendering. However, its high efficiency stems from an approximation of projecting 3D Gaussians onto the image plane as 2D Gaussians, which inherently limits rendering quality--particularly under large Field-of-View (FoV) camera inputs. While several recent works have extended 3DGS to mitigate these approximation errors, none have successfully achieved both exactness and high efficiency simultaneously. In this work, we introduce 3DGEER, an Exact and Efficient Volumetric Gaussian Rendering method. Starting from first principles, we derive a closed-form expression for the density integral along a ray traversing a 3D Gaussian distribution. This formulation enables precise forward rendering with arbitrary camera models and supports gradient-based optimization of 3D Gaussian parameters. To ensure both exactness and real-time performance, we propose an efficient method for computing a tight Particle Bounding Frustum (PBF) for each 3D Gaussian, enabling accurate and efficient ...  
- **📝翻译未启用或未翻译**  

### [2] ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS  
- **⏳发布**：2025-05-29（更新：2025-05-30）  
- **🧑‍🔬作者**：Weijie Wang, Donny Y. Chen, Zeyu Zhang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.23734v2)   · [Project](https://lhmd.top/zpressor.)  
- **📝摘要**：Feed-forward 3D Gaussian Splatting (3DGS) models have recently emerged as a promising solution for novel view synthesis, enabling one-pass inference without the need for per-scene 3DGS optimization. However, their scalability is fundamentally constrained by the limited capacity of their encoders, leading to degraded performance or excessive memory consumption as the number of input views increases. In this work, we analyze feed-forward 3DGS frameworks through the lens of the Information Bottleneck principle and introduce ZPressor, a lightweight architecture-agnostic module that enables efficient compression of multi-view inputs into a compact latent state $Z$ that retains essential scene information while discarding redundancy. Concretely, ZPressor enables existing feed-forward 3DGS models to scale to over 100 input views at 480P resolution on an 80GB GPU, by partitioning the views into anchor and support sets and using cross attention to compress the information from the support views into anchor views, forming the compressed latent state $Z$. ...  
- **📝翻译未启用或未翻译**  

### [3] LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient  Rendering  
- **⏳发布**：2025-05-29  
- **🧑‍🔬作者**：Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.23158v1)    
- **📝摘要**：In this work, we present a novel level-of-detail (LOD) method for 3D Gaussian Splatting that enables real-time rendering of large-scale scenes on memory-constrained devices. Our approach introduces a hierarchical LOD representation that iteratively selects optimal subsets of Gaussians based on camera distance, thus largely reducing both rendering time and GPU memory usage. We construct each LOD level by applying a depth-aware 3D smoothing filter, followed by importance-based pruning and fine-tuning to maintain visual fidelity. To further reduce memory overhead, we partition the scene into spatial chunks and dynamically load only relevant Gaussians during rendering, employing an opacity-blending mechanism to avoid visual artifacts at chunk boundaries. Our method achieves state-of-the-art performance on both outdoor (Hierarchical 3DGS) and indoor (Zip-NeRF) datasets, delivering high-quality renderings with reduced latency and memory requirements.  
- **📝翻译未启用或未翻译**  

### [4] 3DGS Compression with Sparsity-guided Hierarchical Transform Coding  
- **⏳发布**：2025-05-28  
- **🧑‍🔬作者**：Hao Xu, Xiaolin Wu, Xi Zhang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.22908v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has gained popularity for its fast and high-quality rendering, but it has a very large memory footprint incurring high transmission and storage overhead. Recently, some neural compression methods, such as Scaffold-GS, were proposed for 3DGS but they did not adopt the approach of end-to-end optimized analysis-synthesis transforms which has been proven highly effective in neural signal compression. Without an appropriate analysis transform, signal correlations cannot be removed by sparse representation. Without such transforms the only way to remove signal redundancies is through entropy coding driven by a complex and expensive context modeling, which results in slower speed and suboptimal rate-distortion (R-D) performance. To overcome this weakness, we propose Sparsity-guided Hierarchical Transform Coding (SHTC), the first end-to-end optimized transform coding framework for 3DGS compression. SHTC jointly optimizes the 3DGS, transforms and a lightweight context model. This joint optimization enables the transform to produce representations that approach the ...  
- **📝翻译未启用或未翻译**  

### [5] HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D  Scenes  
- **⏳发布**：2025-05-26  
- **🧑‍🔬作者**：Changjian Jiang, Kerui Ren, Linning Xu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.20267v1)    
- **📝摘要**：High fidelity 3D reconstruction and rendering hinge on capturing precise geometry while preserving photo realistic detail. Most existing methods either fuse these goals into a single cumbersome model or adopt hybrid schemes whose uniform primitives lead to a trade off between efficiency and fidelity. In this paper, we introduce HaloGS, a dual representation that loosely couples coarse triangles for geometry with Gaussian primitives for appearance, motivated by the lightweight classic geometry representations and their proven efficiency in real world applications. Our design yields a compact yet expressive model capable of photo realistic rendering across both indoor and outdoor environments, seamlessly adapting to varying levels of scene complexity. Experiments on multiple benchmark datasets demonstrate that our method yields both compact, accurate geometry and high fidelity renderings, especially in challenging scenarios where robust geometric structure make a clear difference.  
- **📝翻译未启用或未翻译**  

### [6] Efficient Differentiable Hardware Rasterization for 3D Gaussian  Splatting  
- **⏳发布**：2025-05-24（更新：2025-08-13）  
- **🧑‍🔬作者**：Yitian Yuan, Qianyue He  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.18764v2)    
- **📝摘要**：Recent works demonstrate the advantages of hardware rasterization for 3D Gaussian Splatting (3DGS) in forward-pass rendering through fast GPU-optimized graphics and fixed memory footprint. However, extending these benefits to backward-pass gradient computation remains challenging due to graphics pipeline constraints. We present a differentiable hardware rasterizer for 3DGS that overcomes the memory and performance limitations of tile-based software rasterization. Our solution employs programmable blending for per-pixel gradient computation combined with a hybrid gradient reduction strategy (quad-level + subgroup) in fragment shaders, achieving over 10x faster backward rasterization versus naive atomic operations and 3x speedup over the canonical tile-based rasterizer. Systematic evaluation reveals 16-bit render targets (float16 and unorm16) as the optimal accuracy-efficiency trade-off, achieving higher gradient accuracy among mixed-precision rendering formats with execution speeds second only to unorm8, while float32 texture incurs severe forward pass performance degradation due to suboptimal hardware optimizations. Our method with float16 formats demonstrates 3.07x acceleration in ...  
- **📝翻译未启用或未翻译**  

### [7] A Novel Benchmark and Dataset for Efficient 3D Gaussian Splatting with  Gaussian Point Cloud Compression  
- **⏳发布**：2025-05-21  
- **🧑‍🔬作者**：Kangli Wang, Shihao Li, Qianxi Yi, Wei Gao  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.18197v1)    
- **📝摘要**：Recently, immersive media and autonomous driving applications have significantly advanced through 3D Gaussian Splatting (3DGS), which offers high-fidelity rendering and computational efficiency. Despite these advantages, 3DGS as a display-oriented representation requires substantial storage due to its numerous Gaussian attributes. Current compression methods have shown promising results but typically neglect the compression of Gaussian spatial positions, creating unnecessary bitstream overhead. We conceptualize Gaussian primitives as point clouds and propose leveraging point cloud compression techniques for more effective storage. AI-based point cloud compression demonstrates superior performance and faster inference compared to MPEG Geometry-based Point Cloud Compression (G-PCC). However, direct application of existing models to Gaussian compression may yield suboptimal results, as Gaussian point clouds tend to exhibit globally sparse yet locally dense geometric distributions that differ from conventional point cloud characteristics. To address these challenges, we introduce GausPcgc for Gaussian point cloud geometry compression along with a specialized training dataset GausPcc-1K. Our ...  
- **📝翻译未启用或未翻译**  

### [8] EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced  Quality for outdoor scenes  
- **⏳发布**：2025-05-16  
- **🧑‍🔬作者**：Jianlin Guo, Haihong Xiao, Wenxiong Kang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.10787v1)    
- **📝摘要**：Efficient scene representations are essential for many real-world applications, especially those involving spatial measurement. Although current NeRF-based methods have achieved impressive results in reconstructing building-scale scenes, they still suffer from slow training and inference speeds due to time-consuming stochastic sampling. Recently, 3D Gaussian Splatting (3DGS) has demonstrated excellent performance with its high-quality rendering and real-time speed, especially for objects and small-scale scenes. However, in outdoor scenes, its point-based explicit representation lacks an effective adjustment mechanism, and the millions of Gaussian points required often lead to memory constraints during training. To address these challenges, we propose EA-3DGS, a high-quality real-time rendering method designed for outdoor scenes. First, we introduce a mesh structure to regulate the initialization of Gaussian components by leveraging an adaptive tetrahedral mesh that partitions the grid and initializes Gaussian components on each face, effectively capturing geometric structures in low-texture regions. Second, we propose an efficient Gaussian pruning strategy ...  
- **📝翻译未启用或未翻译**  

### [9] Neural Video Compression using 2D Gaussian Splatting  
- **⏳发布**：2025-05-14  
- **🧑‍🔬作者**：Lakshya Gupta, Imran N. Junejo  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.09324v1)    
- **📝摘要**：The computer vision and image processing research community has been involved in standardizing video data communications for the past many decades, leading to standards such as AVC, HEVC, VVC, AV1, AV2, etc. However, recent groundbreaking works have focused on employing deep learning-based techniques to replace the traditional video codec pipeline to a greater affect. Neural video codecs (NVC) create an end-to-end ML-based solution that does not rely on any handcrafted features (motion or edge-based) and have the ability to learn content-aware compression strategies, offering better adaptability and higher compression efficiency than traditional methods. This holds a great potential not only for hardware design, but also for various video streaming platforms and applications, especially video conferencing applications such as MS-Teams or Zoom that have found extensive usage in classrooms and workplaces. However, their high computational demands currently limit their use in real-time applications like video conferencing. To address this, we propose ...  
- **📝翻译未启用或未翻译**  

### [10] ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for  Dynamic Scene Reconstruction  
- **⏳发布**：2025-05-13  
- **🧑‍🔬作者**：He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.08196v1)    
- **📝摘要**：Existing 4D Gaussian Splatting methods rely on per-Gaussian deformation from a canonical space to target frames, which overlooks redundancy among adjacent Gaussian primitives and results in suboptimal performance. To address this limitation, we propose Anchor-Driven Deformable and Compressed Gaussian Splatting (ADC-GS), a compact and efficient representation for dynamic scene reconstruction. Specifically, ADC-GS organizes Gaussian primitives into an anchor-based structure within the canonical space, enhanced by a temporal significance-based anchor refinement strategy. To reduce deformation redundancy, ADC-GS introduces a hierarchical coarse-to-fine pipeline that captures motions at varying granularities. Moreover, a rate-distortion optimization is adopted to achieve an optimal balance between bitrate consumption and representation fidelity. Experimental results demonstrate that ADC-GS outperforms the per-Gaussian deformation approaches in rendering speed by 300%-800% while achieving state-of-the-art storage efficiency without compromising rendering quality. The code is released at https://github.com/H-Huang774/ADC-GS.git.  
- **📝翻译未启用或未翻译**  

### [11] Steepest Descent Density Control for Compact 3D Gaussian Splatting  
- **⏳发布**：2025-05-08  
- **🧑‍🔬作者**：Peihao Wang, Yuehao Wang, Dilin Wang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.05587v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a powerful technique for real-time, high-resolution novel view synthesis. By representing scenes as a mixture of Gaussian primitives, 3DGS leverages GPU rasterization pipelines for efficient rendering and reconstruction. To optimize scene coverage and capture fine details, 3DGS employs a densification algorithm to generate additional points. However, this process often leads to redundant point clouds, resulting in excessive memory usage, slower performance, and substantial storage demands - posing significant challenges for deployment on resource-constrained devices. To address this limitation, we propose a theoretical framework that demystifies and improves density control in 3DGS. Our analysis reveals that splitting is crucial for escaping saddle points. Through an optimization-theoretic approach, we establish the necessary conditions for densification, determine the minimal number of offspring Gaussians, identify the optimal parameter update direction, and provide an analytical solution for normalizing off-spring opacity. Building on these insights, we introduce SteepGS, incorporating ...  
- **📝翻译未启用或未翻译**  

### [12] 3D Gaussian Splatting Data Compression with Mixture of Priors  
- **⏳发布**：2025-05-06（更新：2025-08-11）  
- **🧑‍🔬作者**：Lei Liu, Zhenghao Chen, Dong Xu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.03310v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) data compression is crucial for enabling efficient storage and transmission in 3D scene modeling. However, its development remains limited due to inadequate entropy models and suboptimal quantization strategies for both lossless and lossy compression scenarios, where existing methods have yet to 1) fully leverage hyperprior information to construct robust conditional entropy models, and 2) apply fine-grained, element-wise quantization strategies for improved compression granularity. In this work, we propose a novel Mixture of Priors (MoP) strategy to simultaneously address these two challenges. Specifically, inspired by the Mixture-of-Experts (MoE) paradigm, our MoP approach processes hyperprior information through multiple lightweight MLPs to generate diverse prior features, which are subsequently integrated into the MoP feature via a gating mechanism. To enhance lossless compression, the resulting MoP feature is utilized as a hyperprior to improve conditional entropy modeling. Meanwhile, for lossy compression, we employ the MoP feature as guidance information in ...  
- **📝翻译未启用或未翻译**  

### [13] HybridGS: High-Efficiency Gaussian Splatting Data Compression using  Dual-Channel Sparse Representation and Point Cloud Encoder  
- **⏳发布**：2025-05-03  
- **🧑‍🔬作者**：Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2505.01938v1)    
- **📝摘要**：Most existing 3D Gaussian Splatting (3DGS) compression schemes focus on producing compact 3DGS representation via implicit data embedding. They have long coding times and highly customized data format, making it difficult for widespread deployment. This paper presents a new 3DGS compression framework called HybridGS, which takes advantage of both compact generation and standardized point cloud data encoding. HybridGS first generates compact and explicit 3DGS data. A dual-channel sparse representation is introduced to supervise the primitive position and feature bit depth. It then utilizes a canonical point cloud encoder to perform further data compression and form standard output bitstreams. A simple and effective rate control scheme is proposed to pivot the interpretable data compression scheme. At the current stage, HybridGS does not include any modules aimed at improving 3DGS quality during generation. But experiment results show that it still provides comparable reconstruction performance against state-of-the-art methods, with evidently higher encoding and ...  
- **📝翻译未启用或未翻译**  


## April 2025

### [1] 4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data  Compression  
- **⏳发布**：2025-04-26（更新：2025-04-30）  
- **🧑‍🔬作者**：Zicong Chen, Zhenghao Chen, Wei Jiang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.18925v2)    
- **📝摘要**：Storage is a significant challenge in reconstructing dynamic scenes with 4D Gaussian Splatting (4DGS) data. In this work, we introduce 4DGS-CC, a contextual coding framework that compresses 4DGS data to meet specific storage constraints. Building upon the established deformable 3D Gaussian Splatting (3DGS) method, our approach decomposes 4DGS data into 4D neural voxels and a canonical 3DGS component, which are then compressed using Neural Voxel Contextual Coding (NVCC) and Vector Quantization Contextual Coding (VQCC), respectively. Specifically, we first decompose the 4D neural voxels into distinct quantized features by separating the temporal and spatial dimensions. To losslessly compress each quantized feature, we leverage the previously compressed features from the temporal and spatial dimensions as priors and apply NVCC to generate the spatiotemporal context for contextual coding. Next, we employ a codebook to store spherical harmonics information from canonical 3DGS as quantized vectors, which are then losslessly compressed by using VQCC with ...  
- **📝翻译未启用或未翻译**  

### [2] 3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact  Tensorial Representations  
- **⏳发布**：2025-04-21  
- **🧑‍🔬作者**：Yating Wang, Xuan Wang, Ran Yi et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.14967v1)    
- **📝摘要**：Recent studies have combined 3D Gaussian and 3D Morphable Models (3DMM) to construct high-quality 3D head avatars. In this line of research, existing methods either fail to capture the dynamic textures or incur significant overhead in terms of runtime speed or storage space. To this end, we propose a novel method that addresses all the aforementioned demands. In specific, we introduce an expressive and compact representation that encodes texture-related attributes of the 3D Gaussians in the tensorial format. We store appearance of neutral expression in static tri-planes, and represents dynamic texture details for different expressions using lightweight 1D feature lines, which are then decoded into opacity offset relative to the neutral face. We further propose adaptive truncated opacity penalty and class-balanced sampling to improve generalization across different expressions. Experiments show this design enables accurate face dynamic details capturing while maintains real-time rendering and significantly reduces storage costs, thus broadening the ...  
- **📝翻译未启用或未翻译**  

### [3] CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene  Representation  
- **⏳发布**：2025-04-17  
- **🧑‍🔬作者**：Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.13022v1)    
- **📝摘要**：Gaussian splatting demonstrates proficiency for 3D scene modeling but suffers from substantial data volume due to inherent primitive redundancy. To enable future photorealistic 3D immersive visual communication applications, significant compression is essential for transmission over the existing Internet infrastructure. Hence, we propose Compressed Gaussian Splatting (CompGS++), a novel framework that leverages compact Gaussian primitives to achieve accurate 3D modeling with substantial size reduction for both static and dynamic scenes. Our design is based on the principle of eliminating redundancy both between and within primitives. Specifically, we develop a comprehensive prediction paradigm to address inter-primitive redundancy through spatial and temporal primitive prediction modules. The spatial primitive prediction module establishes predictive relationships for scene primitives and enables most primitives to be encoded as compact residuals, substantially reducing the spatial redundancy. We further devise a temporal primitive prediction module to handle dynamic scenes, which exploits primitive correlations across timestamps to effectively reduce temporal ...  
- **📝翻译未启用或未翻译**  

### [4] EDGS: Eliminating Densification for Efficient Convergence of 3DGS  
- **⏳发布**：2025-04-15  
- **🧑‍🔬作者**：Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.13204v1)    
- **📝摘要**：3D Gaussian Splatting reconstructs scenes by starting from a sparse Structure-from-Motion initialization and iteratively refining under-reconstructed regions. This process is inherently slow, as it requires multiple densification steps where Gaussians are repeatedly split and adjusted, following a lengthy optimization path. Moreover, this incremental approach often leads to suboptimal renderings, particularly in high-frequency regions where detail is critical. We propose a fundamentally different approach: we eliminate densification process with a one-step approximation of scene geometry using triangulated pixels from dense image correspondences. This dense initialization allows us to estimate rough geometry of the scene while preserving rich details from input RGB images, providing each Gaussian with well-informed colors, scales, and positions. As a result, we dramatically shorten the optimization path and remove the need for densification. Unlike traditional methods that rely on sparse keypoints, our dense initialization ensures uniform detail across the scene, even in high-frequency regions where 3DGS and other ...  
- **📝翻译未启用或未翻译**  

### [5] 3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians  
- **⏳发布**：2025-04-15（更新：2025-04-16）  
- **🧑‍🔬作者**：Zeming Wei, Junyi Lin, Yang Liu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.11218v2)    
- **📝摘要**：3D affordance reasoning is essential in associating human instructions with the functional regions of 3D objects, facilitating precise, task-oriented manipulations in embodied AI. However, current methods, which predominantly depend on sparse 3D point clouds, exhibit limited generalizability and robustness due to their sensitivity to coordinate variations and the inherent sparsity of the data. By contrast, 3D Gaussian Splatting (3DGS) delivers high-fidelity, real-time rendering with minimal computational overhead by representing scenes as dense, continuous distributions. This positions 3DGS as a highly effective approach for capturing fine-grained affordance details and improving recognition accuracy. Nevertheless, its full potential remains largely untapped due to the absence of large-scale, 3DGS-specific affordance datasets. To overcome these limitations, we present 3DAffordSplat, the first large-scale, multi-modal dataset tailored for 3DGS-based affordance reasoning. This dataset includes 23,677 Gaussian instances, 8,354 point cloud instances, and 6,631 manually annotated affordance labels, encompassing 21 object categories and 18 affordance types. Building upon ...  
- **📝翻译未启用或未翻译**  

### [6] BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via  Adaptive Block-Based Gaussian Splatting  
- **⏳发布**：2025-04-12（更新：2025-04-15）  
- **🧑‍🔬作者**：Yongchang Wu, Zipeng Qi, Zhenwei Shi, Zhengxia Zou  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.09048v2)    
- **📝摘要**：The recent advancements in 3D Gaussian Splatting (3DGS) have demonstrated remarkable potential in novel view synthesis tasks. The divide-and-conquer paradigm has enabled large-scale scene reconstruction, but significant challenges remain in scene partitioning, optimization, and merging processes. This paper introduces BlockGaussian, a novel framework incorporating a content-aware scene partition strategy and visibility-aware block optimization to achieve efficient and high-quality large-scale scene reconstruction. Specifically, our approach considers the content-complexity variation across different regions and balances computational load during scene partitioning, enabling efficient scene reconstruction. To tackle the supervision mismatch issue during independent block optimization, we introduce auxiliary points during individual block optimization to align the ground-truth supervision, which enhances the reconstruction quality. Furthermore, we propose a pseudo-view geometry constraint that effectively mitigates rendering degradation caused by airspace floaters during block merging. Extensive experiments on large-scale scenes demonstrate that our approach achieves state-of-the-art performance in both reconstruction efficiency and rendering quality, with a ...  
- **📝翻译未启用或未翻译**  

### [7] L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery  
- **⏳发布**：2025-04-07  
- **🧑‍🔬作者**：Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.05517v1)    
- **📝摘要**：Traditional 3D content representations include dense point clouds that consume large amounts of data and hence network bandwidth, while newer representations such as neural radiance fields suffer from poor frame rates due to their non-standard volumetric rendering pipeline. 3D Gaussian splats (3DGS) can be seen as a generalization of point clouds that meet the best of both worlds, with high visual quality and efficient rendering for real-time frame rates. However, delivering 3DGS scenes from a hosting server to client devices is still challenging due to high network data consumption (e.g., 1.5 GB for a single scene). The goal of this work is to create an efficient 3D content delivery framework that allows users to view high quality 3D scenes with 3DGS as the underlying data representation. The main contributions of the paper are: (1) Creating new layered 3DGS scenes for efficient delivery, (2) Scheduling algorithms to choose what splats to ...  
- **📝翻译未启用或未翻译**  

### [8] Compressing 3D Gaussian Splatting by Noise-Substituted Vector  Quantization  
- **⏳发布**：2025-04-03（更新：2025-04-08）  
- **🧑‍🔬作者**：Haishan Wang, Mohammad Hassan Vali, Arno Solin  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2504.03059v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has demonstrated remarkable effectiveness in 3D reconstruction, achieving high-quality results with real-time radiance field rendering. However, a key challenge is the substantial storage cost: reconstructing a single scene typically requires millions of Gaussian splats, each represented by 59 floating-point parameters, resulting in approximately 1 GB of memory. To address this challenge, we propose a compression method by building separate attribute codebooks and storing only discrete code indices. Specifically, we employ noise-substituted vector quantization technique to jointly train the codebooks and model features, ensuring consistency between gradient descent optimization and parameter discretization. Our method reduces the memory consumption efficiently (around $45\times$) while maintaining competitive reconstruction quality on standard 3D benchmark scenes. Experiments on different codebook sizes show the trade-off between compression ratio and image quality. Furthermore, the trained compressed model remains fully compatible with popular 3DGS viewers and enables faster rendering speed, making it well-suited for practical ...  
- **📝翻译未启用或未翻译**  


## March 2025

### [1] Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based  Prediction  
- **⏳发布**：2025-03-30  
- **🧑‍🔬作者**：Jingui Ma, Yang Hu, Luyang Tang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.23337v1)    
- **📝摘要**：Recently, 3D Gaussian Spatting (3DGS) has gained widespread attention in Novel View Synthesis (NVS) due to the remarkable real-time rendering performance. However, the substantial cost of storage and transmission of vanilla 3DGS hinders its further application (hundreds of megabytes or even gigabytes for a single scene). Motivated by the achievements of prediction in video compression, we introduce the prediction technique into the anchor-based Gaussian representation to effectively reduce the bit rate. Specifically, we propose a spatial condition-based prediction module to utilize the grid-captured scene information for prediction, with a residual compensation strategy designed to learn the missing fine-grained information. Besides, to further compress the residual, we propose an instance-aware hyper prior, developing a structure-aware and instance-aware entropy model. Extensive experiments demonstrate the effectiveness of our prediction-based compression framework and each technical component. Even compared with SOTA compression method, our framework still achieves a bit rate savings of 24.42 percent. Code ...  
- **📝翻译未启用或未翻译**  

### [2] NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact  3D Representations  
- **⏳发布**：2025-03-29（更新：2025-08-13）  
- **🧑‍🔬作者**：Zhenyu Tang, Chaoran Feng, Xinhua Cheng et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.23162v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) achieves impressive quality and rendering speed, but with millions of 3D Gaussians and significant storage and transmission costs. In this paper, we aim to develop a simple yet effective method called NeuralGS that compresses the original 3DGS into a compact representation. Our observation is that neural fields like NeRF can represent complex 3D scenes with Multi-Layer Perceptron (MLP) neural networks using only a few megabytes. Thus, NeuralGS effectively adopts the neural field representation to encode the attributes of 3D Gaussians with MLPs, only requiring a small storage size even for a large-scale scene. To achieve this, we adopt a clustering strategy and fit the Gaussians within each cluster using different tiny MLPs, based on importance scores of Gaussians as fitting weights. We experiment on multiple datasets, achieving a 91-times average model size reduction without harming the visual quality.  
- **📝翻译未启用或未翻译**  

### [3] FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor  Scene Reconstruction  
- **⏳发布**：2025-03-29  
- **🧑‍🔬作者**：Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.22986v1)    
- **📝摘要**：Recently, the integration of the efficient feed-forward scheme into 3D Gaussian Splatting (3DGS) has been actively explored. However, most existing methods focus on sparse view reconstruction of small regions and cannot produce eligible whole-scene reconstruction results in terms of either quality or efficiency. In this paper, we propose FreeSplat++, which focuses on extending the generalizable 3DGS to become an alternative approach to large-scale indoor whole-scene reconstruction, which has the potential of significantly accelerating the reconstruction speed and improving the geometric accuracy. To facilitate whole-scene reconstruction, we initially propose the Low-cost Cross-View Aggregation framework to efficiently process extremely long input sequences. Subsequently, we introduce a carefully designed pixel-wise triplet fusion method to incrementally aggregate the overlapping 3D Gaussian primitives from multiple views, adaptively reducing their redundancy. Furthermore, we propose a weighted floater removal strategy that can effectively reduce floaters, which serves as an explicit depth fusion approach that is crucial in ...  
- **📝翻译未启用或未翻译**  

### [4] Disentangled 4D Gaussian Splatting: Towards Faster and More Efficient  Dynamic Scene Rendering  
- **⏳发布**：2025-03-28（更新：2025-03-31）  
- **🧑‍🔬作者**：Hao Feng, Hao Sun, Wei Xie  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.22159v2)    
- **📝摘要**：Novel-view synthesis (NVS) for dynamic scenes from 2D images presents significant challenges due to the spatial complexity and temporal variability of such scenes. Recently, inspired by the remarkable success of NVS using 3D Gaussian Splatting (3DGS), researchers have sought to extend 3D Gaussian models to four dimensions (4D) for dynamic novel-view synthesis. However, methods based on 4D rotation and scaling introduce spatiotemporal deformation into the 4D covariance matrix, necessitating the slicing of 4D Gaussians into 3D Gaussians. This process increases redundant computations as timestamps change-an inherent characteristic of dynamic scene rendering. Additionally, performing calculations on a four-dimensional matrix is computationally intensive. In this paper, we introduce Disentangled 4D Gaussian Splatting (Disentangled4DGS), a novel representation and rendering approach that disentangles temporal and spatial deformations, thereby eliminating the reliance on 4D matrix computations. We extend the 3DGS rendering process to 4D, enabling the projection of temporal and spatial deformations into dynamic 2D ...  
- **📝翻译未启用或未翻译**  

### [5] TC-GS: Tri-plane based compression for 3D Gaussian Splatting  
- **⏳发布**：2025-03-26  
- **🧑‍🔬作者**：Taorui Wang, Zitong Yu, Yong Xu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.20221v1)    
- **📝摘要**：Recently, 3D Gaussian Splatting (3DGS) has emerged as a prominent framework for novel view synthesis, providing high fidelity and rapid rendering speed. However, the substantial data volume of 3DGS and its attributes impede its practical utility, requiring compression techniques for reducing memory cost. Nevertheless, the unorganized shape of 3DGS leads to difficulties in compression. To formulate unstructured attributes into normative distribution, we propose a well-structured tri-plane to encode Gaussian attributes, leveraging the distribution of attributes for compression. To exploit the correlations among adjacent Gaussians, K-Nearest Neighbors (KNN) is used when decoding Gaussian distribution from the Tri-plane. We also introduce Gaussian position information as a prior of the position-sensitive decoder. Additionally, we incorporate an adaptive wavelet loss, aiming to focus on the high-frequency details as iterations increase. Our approach has achieved results that are comparable to or surpass that of SOTA 3D Gaussians Splatting compression work in extensive experiments across multiple ...  
- **📝翻译未启用或未翻译**  

### [6] EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View  Synthesis  
- **⏳发布**：2025-03-26  
- **🧑‍🔬作者**：Sheng Miao, Jiaxin Huang, Dongfeng Bai et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.20168v1)    
- **📝摘要**：Novel view synthesis of urban scenes is essential for autonomous driving-related applications.Existing NeRF and 3DGS-based methods show promising results in achieving photorealistic renderings but require slow, per-scene optimization. We introduce EVolSplat, an efficient 3D Gaussian Splatting model for urban scenes that works in a feed-forward manner. Unlike existing feed-forward, pixel-aligned 3DGS methods, which often suffer from issues like multi-view inconsistencies and duplicated content, our approach predicts 3D Gaussians across multiple frames within a unified volume using a 3D convolutional network. This is achieved by initializing 3D Gaussians with noisy depth predictions, and then refining their geometric properties in 3D space and predicting color based on 2D textures. Our model also handles distant views and the sky with a flexible hemisphere background model. This enables us to perform fast, feed-forward reconstruction while achieving real-time rendering. Experimental evaluations on the KITTI-360 and Waymo datasets show that our method achieves state-of-the-art quality compared ...  
- **📝翻译未启用或未翻译**  

### [7] High-Quality Spatial Reconstruction and Orthoimage Generation Using  Efficient 2D Gaussian Splatting  
- **⏳发布**：2025-03-25（更新：2025-05-13）  
- **🧑‍🔬作者**：Qian Wang, Zhihao Zhan, Jialei He et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.19703v2)    
- **📝摘要**：Highly accurate geometric precision and dense image features characterize True Digital Orthophoto Maps (TDOMs), which are in great demand for applications such as urban planning, infrastructure management, and environmental monitoring.Traditional TDOM generation methods need sophisticated processes, such as Digital Surface Models (DSM) and occlusion detection, which are computationally expensive and prone to errors.This work presents an alternative technique rooted in 2D Gaussian Splatting (2DGS), free of explicit DSM and occlusion detection. With depth map generation, spatial information for every pixel within the TDOM is retrieved and can reconstruct the scene with high precision. Divide-and-conquer strategy achieves excellent GS training and rendering with high-resolution TDOMs at a lower resource cost, which preserves higher quality of rendering on complex terrain and thin structure without a decrease in efficiency. Experimental results demonstrate the efficiency of large-scale scene reconstruction and high-precision terrain modeling. This approach provides accurate spatial data, which assists users in better ...  
- **📝翻译未启用或未翻译**  

### [8] 4DGC: Rate-Aware 4D Gaussian Compression for Efficient Streamable  Free-Viewpoint Video  
- **⏳发布**：2025-03-24  
- **🧑‍🔬作者**：Qiang Hu, Zihan Zheng, Houqiang Zhong et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.18421v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has substantial potential for enabling photorealistic Free-Viewpoint Video (FVV) experiences. However, the vast number of Gaussians and their associated attributes poses significant challenges for storage and transmission. Existing methods typically handle dynamic 3DGS representation and compression separately, neglecting motion information and the rate-distortion (RD) trade-off during training, leading to performance degradation and increased model redundancy. To address this gap, we propose 4DGC, a novel rate-aware 4D Gaussian compression framework that significantly reduces storage size while maintaining superior RD performance for FVV. Specifically, 4DGC introduces a motion-aware dynamic Gaussian representation that utilizes a compact motion grid combined with sparse compensated Gaussians to exploit inter-frame similarities. This representation effectively handles large motions, preserving quality and reducing temporal redundancy. Furthermore, we present an end-to-end compression scheme that employs differentiable quantization and a tiny implicit entropy model to compress the motion grid and compensated Gaussians efficiently. The entire framework is ...  
- **📝翻译未启用或未翻译**  

### [9] ProtoGS: Efficient and High-Quality Rendering with 3D Gaussian  Prototypes  
- **⏳发布**：2025-03-21（更新：2025-04-08）  
- **🧑‍🔬作者**：Zhengqing Gao, Dongting Hu, Jia-Wang Bian et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.17486v3)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has made significant strides in novel view synthesis but is limited by the substantial number of Gaussian primitives required, posing challenges for deployment on lightweight devices. Recent methods address this issue by compressing the storage size of densified Gaussians, yet fail to preserve rendering quality and efficiency. To overcome these limitations, we propose ProtoGS to learn Gaussian prototypes to represent Gaussian primitives, significantly reducing the total Gaussian amount without sacrificing visual quality. Our method directly uses Gaussian prototypes to enable efficient rendering and leverage the resulting reconstruction loss to guide prototype learning. To further optimize memory efficiency during training, we incorporate structure-from-motion (SfM) points as anchor points to group Gaussian primitives. Gaussian prototypes are derived within each group by clustering of K-means, and both the anchor points and the prototypes are optimized jointly. Our experiments on real-world and synthetic datasets prove that we outperform existing methods, ...  
- **📝翻译未启用或未翻译**  

### [10] Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via  Context Model  
- **⏳发布**：2025-03-18  
- **🧑‍🔬作者**：Mufan Liu, Qi Yang, He Huang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.13948v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as an efficient and high-fidelity paradigm for novel view synthesis. To adapt 3DGS for dynamic content, deformable 3DGS incorporates temporally deformable primitives with learnable latent embeddings to capture complex motions. Despite its impressive performance, the high-dimensional embeddings and vast number of primitives lead to substantial storage requirements. In this paper, we introduce a \textbf{Light}weight \textbf{4}D\textbf{GS} framework, called Light4GS, that employs significance pruning with a deep context model to provide a lightweight storage-efficient dynamic 3DGS representation. The proposed Light4GS is based on 4DGS that is a typical representation of deformable 3DGS. Specifically, our framework is built upon two core components: (1) a spatio-temporal significance pruning strategy that eliminates over 64\% of the deformable primitives, followed by an entropy-constrained spherical harmonics compression applied to the remainder; and (2) a deep context model that integrates intra- and inter-prediction with hyperprior into a coarse-to-fine context structure to enable ...  
- **📝翻译未启用或未翻译**  

### [11] CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression  
- **⏳发布**：2025-03-17  
- **🧑‍🔬作者**：Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.12862v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has shown immense potential for novel view synthesis. However, achieving rate-distortion-optimized compression of 3DGS representations for transmission and/or storage applications remains a challenge. CAT-3DGS introduces a context-adaptive triplane hyperprior for end-to-end optimized compression, delivering state-of-the-art coding performance. Despite this, it requires prolonged training and decoding time. To address these limitations, we propose CAT-3DGS Pro, an enhanced version of CAT-3DGS that improves both compression performance and computational efficiency. First, we introduce a PCA-guided vector-matrix hyperprior, which replaces the triplane-based hyperprior to reduce redundant parameters. To achieve a more balanced rate-distortion trade-off and faster encoding, we propose an alternate optimization strategy (A-RDO). Additionally, we refine the sampling rate optimization method in CAT-3DGS, leading to significant improvements in rate-distortion performance. These enhancements result in a 46.6% BD-rate reduction and 3x speedup in training time on BungeeNeRF, while achieving 5x acceleration in decoding speed for the Amsterdam scene compared to ...  
- **📝翻译未启用或未翻译**  

### [12] CompMarkGS: Robust Watermarking for Compressed 3D Gaussian Splatting  
- **⏳发布**：2025-03-17（更新：2025-06-12）  
- **🧑‍🔬作者**：Sumin In, Youngdong Jang, Utae Jeong et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.12836v5)    
- **📝摘要**：3D Gaussian Splatting (3DGS) is increasingly adopted in various academic and commercial applications due to its real-time and high-quality rendering capabilities, emphasizing the growing need for copyright protection technologies for 3DGS. However, the large model size of 3DGS requires developing efficient compression techniques. This highlights the necessity of an integrated framework that addresses copyright protection and data compression for 3D content. Nevertheless, existing 3DGS watermarking methods significantly degrade watermark performance under 3DGS compression methods, particularly quantization-based approaches that achieve superior compression performance. To ensure reliable watermark detection under compression, we propose a compression-tolerant anchor-based 3DGS watermarking, which preserves watermark integrity and rendering quality. This is achieved by introducing anchor-based 3DGS watermarking. We embed the watermark into the anchor attributes, particularly the anchor feature, to enhance security and rendering quality. We also propose a quantization distortion layer that injects quantization noise during training, preserving the watermark after quantization-based compression. Moreover, we ...  
- **📝翻译未启用或未翻译**  

### [13] Swift4D:Adaptive divide-and-conquer Gaussian Splatting for compact and  efficient reconstruction of dynamic scene  
- **⏳发布**：2025-03-16  
- **🧑‍🔬作者**：Jiahao Wu, Rui Peng, Zhiyan Wang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.12307v1)    
- **📝摘要**：Novel view synthesis has long been a practical but challenging task, although the introduction of numerous methods to solve this problem, even combining advanced representations like 3D Gaussian Splatting, they still struggle to recover high-quality results and often consume too much storage memory and training time. In this paper we propose Swift4D, a divide-and-conquer 3D Gaussian Splatting method that can handle static and dynamic primitives separately, achieving a good trade-off between rendering quality and efficiency, motivated by the fact that most of the scene is the static primitive and does not require additional dynamic properties. Concretely, we focus on modeling dynamic transformations only for the dynamic primitives which benefits both efficiency and quality. We first employ a learnable decomposition strategy to separate the primitives, which relies on an additional parameter to classify primitives as static or dynamic. For the dynamic primitives, we employ a compact multi-resolution 4D Hash mapper to ...  
- **📝翻译未启用或未翻译**  

### [14] PCGS: Progressive Compression of 3D Gaussian Splatting  
- **⏳发布**：2025-03-11  
- **🧑‍🔬作者**：Yihang Chen, Mengyao Li, Qianyi Wu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.08511v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) achieves impressive rendering fidelity and speed for novel view synthesis. However, its substantial data size poses a significant challenge for practical applications. While many compression techniques have been proposed, they fail to efficiently utilize existing bitstreams in on-demand applications due to their lack of progressivity, leading to a waste of resource. To address this issue, we propose PCGS (Progressive Compression of 3D Gaussian Splatting), which adaptively controls both the quantity and quality of Gaussians (or anchors) to enable effective progressivity for on-demand applications. Specifically, for quantity, we introduce a progressive masking strategy that incrementally incorporates new anchors while refining existing ones to enhance fidelity. For quality, we propose a progressive quantization approach that gradually reduces quantization step sizes to achieve finer modeling of Gaussian attributes. Furthermore, to compact the incremental bitstreams, we leverage existing quantization results to refine probability prediction, improving entropy coding efficiency across progressive ...  
- **📝翻译未启用或未翻译**  

### [15] GaussianVideo: Efficient Video Representation and Compression by  Gaussian Splatting  
- **⏳发布**：2025-03-06  
- **🧑‍🔬作者**：Inseo Lee, Youngyoon Choi, Joonseok Lee  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.04333v1)    
- **📝摘要**：Implicit Neural Representation for Videos (NeRV) has introduced a novel paradigm for video representation and compression, outperforming traditional codecs. As model size grows, however, slow encoding and decoding speed and high memory consumption hinder its application in practice. To address these limitations, we propose a new video representation and compression method based on 2D Gaussian Splatting to efficiently handle video data. Our proposed deformable 2D Gaussian Splatting dynamically adapts the transformation of 2D Gaussians at each frame, significantly reducing memory cost. Equipped with a multi-plane-based spatiotemporal encoder and a lightweight decoder, it predicts changes in color, coordinates, and shape of initialized Gaussians, given the time step. By leveraging temporal gradients, our model effectively captures temporal redundancy at negligible cost, significantly enhancing video representation efficiency. Our method reduces GPU memory usage by up to 78.4%, and significantly expedites video processing, achieving 5.5x faster training and 12.5x faster decoding compared to the ...  
- **📝翻译未启用或未翻译**  

### [16] CAT-3DGS: A Context-Adaptive Triplane Approach to  Rate-Distortion-Optimized 3DGS Compression  
- **⏳发布**：2025-03-01（更新：2025-03-07）  
- **🧑‍🔬作者**：Yu-Ting Zhan, Cheng-Yuan Ho, Hebi Yang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2503.00357v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has recently emerged as a promising 3D representation. Much research has been focused on reducing its storage requirements and memory footprint. However, the needs to compress and transmit the 3DGS representation to the remote side are overlooked. This new application calls for rate-distortion-optimized 3DGS compression. How to quantize and entropy encode sparse Gaussian primitives in the 3D space remains largely unexplored. Few early attempts resort to the hyperprior framework from learned image compression. But, they fail to utilize fully the inter and intra correlation inherent in Gaussian primitives. Built on ScaffoldGS, this work, termed CAT-3DGS, introduces a context-adaptive triplane approach to their rate-distortion-optimized coding. It features multi-scale triplanes, oriented according to the principal axes of Gaussian primitives in the 3D space, to capture their inter correlation (i.e. spatial correlation) for spatial autoregressive coding in the projected 2D planes. With these triplanes serving as the hyperprior, we ...  
- **📝翻译未启用或未翻译**  


## February 2025

### [1] Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via  Sparse Time-Variant Attribute Modeling  
- **⏳发布**：2025-02-27  
- **🧑‍🔬作者**：Hanyang Kong, Xingyi Yang, Xinchao Wang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2502.20378v1)    
- **📝摘要**：Rendering dynamic scenes from monocular videos is a crucial yet challenging task. The recent deformable Gaussian Splatting has emerged as a robust solution to represent real-world dynamic scenes. However, it often leads to heavily redundant Gaussians, attempting to fit every training view at various time steps, leading to slower rendering speeds. Additionally, the attributes of Gaussians in static areas are time-invariant, making it unnecessary to model every Gaussian, which can cause jittering in static regions. In practice, the primary bottleneck in rendering speed for dynamic scenes is the number of Gaussians. In response, we introduce Efficient Dynamic Gaussian Splatting (EDGS), which represents dynamic scenes via sparse time-variant attribute modeling. Our approach formulates dynamic scenes using a sparse anchor-grid representation, with the motion flow of dense Gaussians calculated via a classical kernel representation. Furthermore, we propose an unsupervised strategy to efficiently filter out anchors corresponding to static areas. Only anchors associated ...  
- **📝翻译未启用或未翻译**  

### [2] Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and  Future Directions  
- **⏳发布**：2025-02-26  
- **🧑‍🔬作者**：Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2502.19457v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has recently emerged as a pioneering approach in explicit scene rendering and computer graphics. Unlike traditional neural radiance field (NeRF) methods, which typically rely on implicit, coordinate-based models to map spatial coordinates to pixel values, 3DGS utilizes millions of learnable 3D Gaussians. Its differentiable rendering technique and inherent capability for explicit scene representation and manipulation positions 3DGS as a potential game-changer for the next generation of 3D reconstruction and representation technologies. This enables 3DGS to deliver real-time rendering speeds while offering unparalleled editability levels. However, despite its advantages, 3DGS suffers from substantial memory and storage requirements, posing challenges for deployment on resource-constrained devices. In this survey, we provide a comprehensive overview focusing on the scalability and compression of 3DGS. We begin with a detailed background overview of 3DGS, followed by a structured taxonomy of existing compression methods. Additionally, we analyze and compare current methods from the ...  
- **📝翻译未启用或未翻译**  

### [3] Efficient 4D Gaussian Stream with Low Rank Adaptation  
- **⏳发布**：2025-02-23  
- **🧑‍🔬作者**：Zhenhuan Liu, Shuai Liu, Yidong Lu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2502.16575v1)    
- **📝摘要**：Recent methods have made significant progress in synthesizing novel views with long video sequences. This paper proposes a highly scalable method for dynamic novel view synthesis with continual learning. We leverage the 3D Gaussians to represent the scene and a low-rank adaptation-based deformation model to capture the dynamic scene changes. Our method continuously reconstructs the dynamics with chunks of video frames, reduces the streaming bandwidth by $90\%$ while maintaining high rendering quality comparable to the off-line SOTA methods.  
- **📝翻译未启用或未翻译**  

### [4] Pointmap Association and Piecewise-Plane Constraint for Consistent and  Compact 3D Gaussian Segmentation Field  
- **⏳发布**：2025-02-22  
- **🧑‍🔬作者**：Wenhao Hu, Wenhao Chai, Shengyu Hao et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2502.16303v1)    
- **📝摘要**：Achieving a consistent and compact 3D segmentation field is crucial for maintaining semantic coherence across views and accurately representing scene structures. Previous 3D scene segmentation methods rely on video segmentation models to address inconsistencies across views, but the absence of spatial information often leads to object misassociation when object temporarily disappear and reappear. Furthermore, in the process of 3D scene reconstruction, segmentation and optimization are often treated as separate tasks. As a result, optimization typically lacks awareness of semantic category information, which can result in floaters with ambiguous segmentation. To address these challenges, we introduce CCGS, a method designed to achieve both view consistent 2D segmentation and a compact 3D Gaussian segmentation field. CCGS incorporates pointmap association and a piecewise-plane constraint. First, we establish pixel correspondence between adjacent images by minimizing the Euclidean distance between their pointmaps. We then redefine object mask overlap accordingly. The Hungarian algorithm is employed to ...  
- **📝翻译未启用或未翻译**  

### [5] Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based  Static-Dynamic Separation  
- **⏳发布**：2025-02-04（更新：2025-07-01）  
- **🧑‍🔬作者**：Joohyun Kwon, Hanbyel Cho, Junmo Kim  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2502.02091v3)   · [Project](https://hanbyelcho.info/instruct-4dgs/)  
- **📝摘要**：Recent 4D dynamic scene editing methods require editing thousands of 2D images used for dynamic scene synthesis and updating the entire scene with additional training loops, resulting in several hours of processing to edit a single dynamic scene. Therefore, these methods are not scalable with respect to the temporal dimension of the dynamic scene (i.e., the number of timesteps). In this work, we propose Instruct-4DGS, an efficient dynamic scene editing method that is more scalable in terms of temporal dimension. To achieve computational efficiency, we leverage a 4D Gaussian representation that models a 4D dynamic scene by combining static 3D Gaussians with a Hexplane-based deformation field, which captures dynamic information. We then perform editing solely on the static 3D Gaussians, which is the minimal but sufficient component required for visual editing. To resolve the misalignment between the edited 3D Gaussians and the deformation field, which may arise from the editing ...  
- **📝翻译未启用或未翻译**  


## January 2025

### [1] Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting  
- **⏳发布**：2025-01-24  
- **🧑‍🔬作者**：Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.14534v1)    
- **📝摘要**：Gaussian splatting (GS) for 3D reconstruction has become quite popular due to their fast training, inference speeds and high quality reconstruction. However, GS-based reconstructions generally consist of millions of Gaussians, which makes them hard to use on computationally constrained devices such as smartphones. In this paper, we first propose a principled analysis of advances in efficient GS methods. Then, we propose Trick-GS, which is a careful combination of several strategies including (1) progressive training with resolution, noise and Gaussian scales, (2) learning to prune and mask primitives and SH bands by their significance, and (3) accelerated GS training framework. Trick-GS takes a large step towards resource-constrained GS, where faster run-time, smaller and faster-convergence of models is of paramount concern. Our results on three datasets show that Trick-GS achieves up to 2x faster training, 40x smaller disk size and 2x faster rendering speed compared to vanilla GS, while having comparable accuracy.  
- **📝翻译未启用或未翻译**  

### [2] Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made  Scenes  
- **⏳发布**：2025-01-22  
- **🧑‍🔬作者**：Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.13045v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a promising representation for photorealistic rendering of 3D scenes. However, its high storage requirements pose significant challenges for practical applications. We observe that Gaussians exhibit distinct roles and characteristics that are analogous to traditional artistic techniques -- Like how artists first sketch outlines before filling in broader areas with color, some Gaussians capture high-frequency features like edges and contours; While other Gaussians represent broader, smoother regions, that are analogous to broader brush strokes that add volume and depth to a painting. Based on this observation, we propose a novel hybrid representation that categorizes Gaussians into (i) Sketch Gaussians, which define scene boundaries, and (ii) Patch Gaussians, which cover smooth regions. Sketch Gaussians are efficiently encoded using parametric models, leveraging their geometric coherence, while Patch Gaussians undergo optimized pruning, retraining, and vector quantization to maintain volumetric consistency and storage efficiency. Our comprehensive evaluation across ...  
- **📝翻译未启用或未翻译**  

### [3] HAC++: Towards 100X Compression of 3D Gaussian Splatting  
- **⏳发布**：2025-01-21（更新：2025-02-11）  
- **🧑‍🔬作者**：Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.12255v4)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel view synthesis, boasting rapid rendering speed with high fidelity. However, the substantial Gaussians and their associated attributes necessitate effective compression techniques. Nevertheless, the sparse and unorganized nature of the point cloud of Gaussians (or anchors in our paper) presents challenges for compression. To achieve a compact size, we propose HAC++, which leverages the relationships between unorganized anchors and a structured hash grid, utilizing their mutual information for context modeling. Additionally, HAC++ captures intra-anchor contextual relationships to further enhance compression performance. To facilitate entropy coding, we utilize Gaussian distributions to precisely estimate the probability of each quantized attribute, where an adaptive quantization module is proposed to enable high-precision quantization of these attributes for improved fidelity restoration. Moreover, we incorporate an adaptive masking strategy to eliminate invalid Gaussians and anchors. Overall, HAC++ achieves a remarkable size reduction of over 100X ...  
- **📝翻译未启用或未翻译**  

### [4] GSVC: Efficient Video Representation and Compression Through 2D Gaussian  Splatting  
- **⏳发布**：2025-01-21（更新：2025-01-22）  
- **🧑‍🔬作者**：Longan Wang, Yuang Shi, Wei Tsang Ooi  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.12060v2)    
- **📝摘要**：3D Gaussian splats have emerged as a revolutionary, effective, learned representation for static 3D scenes. In this work, we explore using 2D Gaussian splats as a new primitive for representing videos. We propose GSVC, an approach to learning a set of 2D Gaussian splats that can effectively represent and compress video frames. GSVC incorporates the following techniques: (i) To exploit temporal redundancy among adjacent frames, which can speed up training and improve the compression efficiency, we predict the Gaussian splats of a frame based on its previous frame; (ii) To control the trade-offs between file size and quality, we remove Gaussian splats with low contribution to the video quality; (iii) To capture dynamics in videos, we randomly add Gaussian splats to fit content with large motion or newly-appeared objects; (iv) To handle significant changes in the scene, we detect key frames based on loss differences during the learning process. Experiment ...  
- **📝翻译未启用或未翻译**  

### [5] Object-Centric 2D Gaussian Splatting: Background Removal and  Occlusion-Aware Pruning for Compact Object Models  
- **⏳发布**：2025-01-14（更新：2025-04-03）  
- **🧑‍🔬作者**：Marcel Rogge, Didier Stricker  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.08174v2)    
- **📝摘要**：Current Gaussian Splatting approaches are effective for reconstructing entire scenes but lack the option to target specific objects, making them computationally expensive and unsuitable for object-specific applications. We propose a novel approach that leverages object masks to enable targeted reconstruction, resulting in object-centric models. Additionally, we introduce an occlusion-aware pruning strategy to minimize the number of Gaussians without compromising quality. Our method reconstructs compact object models, yielding object-centric Gaussian and mesh representations that are up to 96% smaller and up to 71% faster to train compared to the baseline while retaining competitive quality. These representations are immediately usable for downstream applications such as appearance editing and physics simulation without additional processing.  
- **📝翻译未启用或未翻译**  

### [6] Generalized and Efficient 2D Gaussian Splatting for Arbitrary-scale  Super-Resolution  
- **⏳发布**：2025-01-12（更新：2025-07-30）  
- **🧑‍🔬作者**：Du Chen, Liyi Chen, Zhengqiang Zhang, Lei Zhang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.06838v5)    
- **📝摘要**：Implicit Neural Representations (INR) have been successfully employed for Arbitrary-scale Super-Resolution (ASR). However, INR-based models need to query the multi-layer perceptron module numerous times and render a pixel in each query, resulting in insufficient representation capability and low computational efficiency. Recently, Gaussian Splatting (GS) has shown its advantages over INR in both visual quality and rendering speed in 3D tasks, which motivates us to explore whether GS can be employed for the ASR task. However, directly applying GS to ASR is exceptionally challenging because the original GS is an optimization-based method through overfitting each single scene, while in ASR we aim to learn a single model that can generalize to different images and scaling factors. We overcome these challenges by developing two novel techniques. Firstly, to generalize GS for ASR, we elaborately design an architecture to predict the corresponding image-conditioned Gaussians of the input low-resolution image in a feed-forward manner. ...  
- **📝翻译未启用或未翻译**  

### [7] GaussianVideo: Efficient Video Representation via Hierarchical Gaussian  Splatting  
- **⏳发布**：2025-01-08  
- **🧑‍🔬作者**：Andrew Bond, Jui-Hsien Wang, Long Mai, Erkut Erdem, Aykut Erdem  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.04782v1)    
- **📝摘要**：Efficient neural representations for dynamic video scenes are critical for applications ranging from video compression to interactive simulations. Yet, existing methods often face challenges related to high memory usage, lengthy training times, and temporal consistency. To address these issues, we introduce a novel neural video representation that combines 3D Gaussian splatting with continuous camera motion modeling. By leveraging Neural ODEs, our approach learns smooth camera trajectories while maintaining an explicit 3D scene representation through Gaussians. Additionally, we introduce a spatiotemporal hierarchical learning strategy, progressively refining spatial and temporal features to enhance reconstruction quality and accelerate convergence. This memory-efficient approach achieves high-quality rendering at impressive speeds. Experimental results show that our hierarchical learning, combined with robust camera motion modeling, captures complex dynamic scenes with strong temporal consistency, achieving state-of-the-art performance across diverse video datasets in both high- and low-motion scenarios.  
- **📝翻译未启用或未翻译**  

### [8] MoDec-GS: Global-to-Local Motion Decomposition and Temporal Interval  Adjustment for Compact Dynamic 3D Gaussian Splatting  
- **⏳发布**：2025-01-07（更新：2025-03-24）  
- **🧑‍🔬作者**：Sangwoon Kwak, Joonsoo Kim, Jun Young Jeong et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.03714v3)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has made significant strides in scene representation and neural rendering, with intense efforts focused on adapting it for dynamic scenes. Despite delivering remarkable rendering quality and speed, existing methods struggle with storage demands and representing complex real-world motions. To tackle these issues, we propose MoDecGS, a memory-efficient Gaussian splatting framework designed for reconstructing novel views in challenging scenarios with complex motions. We introduce GlobaltoLocal Motion Decomposition (GLMD) to effectively capture dynamic motions in a coarsetofine manner. This approach leverages Global Canonical Scaffolds (Global CS) and Local Canonical Scaffolds (Local CS), extending static Scaffold representation to dynamic video reconstruction. For Global CS, we propose Global Anchor Deformation (GAD) to efficiently represent global dynamics along complex motions, by directly deforming the implicit Scaffold attributes which are anchor position, offset, and local context features. Next, we finely adjust local motions via the Local Gaussian Deformation (LGD) of Local CS ...  
- **📝翻译未启用或未翻译**  

### [9] Compression of 3D Gaussian Splatting with Optimized Feature Planes and  Standard Video Codecs  
- **⏳发布**：2025-01-06  
- **🧑‍🔬作者**：Soonbin Lee, Fangwen Shu, Yago Sanchez, Thomas Schierl, Cornelius Hellge  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.03399v1)   · [Project](https://fraunhoferhhi.github.io/CodecGS)  
- **📝摘要**：3D Gaussian Splatting is a recognized method for 3D scene representation, known for its high rendering quality and speed. However, its substantial data requirements present challenges for practical applications. In this paper, we introduce an efficient compression technique that significantly reduces storage overhead by using compact representation. We propose a unified architecture that combines point cloud data and feature planes through a progressive tri-plane structure. Our method utilizes 2D feature planes, enabling continuous spatial representation. To further optimize these representations, we incorporate entropy modeling in the frequency domain, specifically designed for standard video codecs. We also propose channel-wise bit allocation to achieve a better trade-off between bitrate consumption and feature plane representation. Consequently, our model effectively leverages spatial correlations within the feature planes to enhance rate-distortion performance using standard, non-differentiable video codecs. Experimental results demonstrate that our method outperforms existing methods in data compactness while maintaining high rendering quality. Our ...  
- **📝翻译未启用或未翻译**  

### [10] GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields  through Efficient Dense 3D Point Tracking  
- **⏳发布**：2025-01-05  
- **🧑‍🔬作者**：Weikang Bian, Zhaoyang Huang, Xiaoyu Shi et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.02690v1)   · [Project](https://wkbian.github.io/Projects/GS-DiT/.)  
- **📝摘要**：4D video control is essential in video generation as it enables the use of sophisticated lens techniques, such as multi-camera shooting and dolly zoom, which are currently unsupported by existing methods. Training a video Diffusion Transformer (DiT) directly to control 4D content requires expensive multi-view videos. Inspired by Monocular Dynamic novel View Synthesis (MDVS) that optimizes a 4D representation and renders videos according to different 4D elements, such as camera pose and object motion editing, we bring pseudo 4D Gaussian fields to video generation. Specifically, we propose a novel framework that constructs a pseudo 4D Gaussian field with dense 3D point tracking and renders the Gaussian field for all video frames. Then we finetune a pretrained DiT to generate videos following the guidance of the rendered video, dubbed as GS-DiT. To boost the training of the GS-DiT, we also propose an efficient Dense 3D Point Tracking (D3D-PT) method for the ...  
- **📝翻译未启用或未翻译**  

### [11] Deformable Gaussian Splatting for Efficient and High-Fidelity  Reconstruction of Surgical Scenes  
- **⏳发布**：2025-01-02  
- **🧑‍🔬作者**：Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2501.01101v1)    
- **📝摘要**：Efficient and high-fidelity reconstruction of deformable surgical scenes is a critical yet challenging task. Building on recent advancements in 3D Gaussian splatting, current methods have seen significant improvements in both reconstruction quality and rendering speed. However, two major limitations remain: (1) difficulty in handling irreversible dynamic changes, such as tissue shearing, which are common in surgical scenes; and (2) the lack of hierarchical modeling for surgical scene deformation, which reduces rendering speed. To address these challenges, we introduce EH-SurGS, an efficient and high-fidelity reconstruction algorithm for deformable surgical scenes. We propose a deformation modeling approach that incorporates the life cycle of 3D Gaussians, effectively capturing both regular and irreversible deformations, thus enhancing reconstruction quality. Additionally, we present an adaptive motion hierarchy strategy that distinguishes between static and deformable regions within the surgical scene. This strategy reduces the number of 3D Gaussians passing through the deformation field, thereby improving rendering speed. ...  
- **📝翻译未启用或未翻译**  


## December 2024

### [1] GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians  
- **⏳发布**：2024-12-18  
- **🧑‍🔬作者**：Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.13983v1)    
- **📝摘要**：Rendering photorealistic head avatars from arbitrary viewpoints is crucial for various applications like virtual reality. Although previous methods based on Neural Radiance Fields (NeRF) can achieve impressive results, they lack fidelity and efficiency. Recent methods using 3D Gaussian Splatting (3DGS) have improved rendering quality and real-time performance but still require significant storage overhead. In this paper, we introduce a method called GraphAvatar that utilizes Graph Neural Networks (GNN) to generate 3D Gaussians for the head avatar. Specifically, GraphAvatar trains a geometric GNN and an appearance GNN to generate the attributes of the 3D Gaussians from the tracked mesh. Therefore, our method can store the GNN models instead of the 3D Gaussians, significantly reducing the storage overhead to just 10MB. To reduce the impact of face-tracking errors, we also present a novel graph-guided optimization module to refine face-tracking parameters during training. Finally, we introduce a 3D-aware enhancer for post-processing to enhance ...  
- **📝翻译未启用或未翻译**  

### [2] Gaussian Splatting for Efficient Satellite Image Photogrammetry  
- **⏳发布**：2024-12-17（更新：2025-03-22）  
- **🧑‍🔬作者**：Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.13047v2)    
- **📝摘要**：Recently, Gaussian splatting has emerged as a strong alternative to NeRF, demonstrating impressive 3D modeling capabilities while requiring only a fraction of the training and rendering time. In this paper, we show how the standard Gaussian splatting framework can be adapted for remote sensing, retaining its high efficiency. This enables us to achieve state-of-the-art performance in just a few minutes, compared to the day-long optimization required by the best-performing NeRF-based Earth observation methods. The proposed framework incorporates remote-sensing improvements from EO-NeRF, such as radiometric correction and shadow modeling, while introducing novel components, including sparsity, view consistency, and opacity regularizations.  
- **📝翻译未启用或未翻译**  

### [3] 4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel  Reconstruction from Sparse-View Dynamic DSA Images  
- **⏳发布**：2024-12-17（更新：2025-03-26）  
- **🧑‍🔬作者**：Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.12919v2)    
- **📝摘要**：Reconstructing 3D vessel structures from sparse-view dynamic digital subtraction angiography (DSA) images enables accurate medical assessment while reducing radiation exposure. Existing methods often produce suboptimal results or require excessive computation time. In this work, we propose 4D radiative Gaussian splatting (4DRGS) to achieve high-quality reconstruction efficiently. In detail, we represent the vessels with 4D radiative Gaussian kernels. Each kernel has time-invariant geometry parameters, including position, rotation, and scale, to model static vessel structures. The time-dependent central attenuation of each kernel is predicted from a compact neural network to capture the temporal varying response of contrast agent flow. We splat these Gaussian kernels to synthesize DSA images via X-ray rasterization and optimize the model with real captured ones. The final 3D vessel volume is voxelized from the well-trained kernels. Moreover, we introduce accumulated attenuation pruning and bounded scaling activation to improve reconstruction quality. Extensive experiments on real-world patient data demonstrate that ...  
- **📝翻译未启用或未翻译**  

### [4] RP-SLAM: Real-time Photorealistic SLAM with Efficient 3D Gaussian  Splatting  
- **⏳发布**：2024-12-13  
- **🧑‍🔬作者**：Lizhi Bai, Chunqi Tian, Jun Yang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.09868v1)    
- **📝摘要**：3D Gaussian Splatting has emerged as a promising technique for high-quality 3D rendering, leading to increasing interest in integrating 3DGS into realism SLAM systems. However, existing methods face challenges such as Gaussian primitives redundancy, forgetting problem during continuous optimization, and difficulty in initializing primitives in monocular case due to lack of depth information. In order to achieve efficient and photorealistic mapping, we propose RP-SLAM, a 3D Gaussian splatting-based vision SLAM method for monocular and RGB-D cameras. RP-SLAM decouples camera poses estimation from Gaussian primitives optimization and consists of three key components. Firstly, we propose an efficient incremental mapping approach to achieve a compact and accurate representation of the scene through adaptive sampling and Gaussian primitives filtering. Secondly, a dynamic window optimization method is proposed to mitigate the forgetting problem and improve map consistency. Finally, for the monocular case, a monocular keyframe initialization method based on sparse point cloud is proposed ...  
- **📝翻译未启用或未翻译**  

### [5] ResGS: Residual Densification of 3D Gaussian for Efficient Detail  Recovery  
- **⏳发布**：2024-12-10（更新：2025-04-04）  
- **🧑‍🔬作者**：Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.07494v2)    
- **📝摘要**：Recently, 3D Gaussian Splatting (3D-GS) has prevailed in novel view synthesis, achieving high fidelity and efficiency. However, it often struggles to capture rich details and complete geometry. Our analysis reveals that the 3D-GS densification operation lacks adaptiveness and faces a dilemma between geometry coverage and detail recovery. To address this, we introduce a novel densification operation, residual split, which adds a downscaled Gaussian as a residual. Our approach is capable of adaptively retrieving details and complementing missing geometry. To further support this method, we propose a pipeline named ResGS. Specifically, we integrate a Gaussian image pyramid for progressive supervision and implement a selection scheme that prioritizes the densification of coarse Gaussians over time. Extensive experiments demonstrate that our method achieves SOTA rendering quality. Consistent performance improvements can be achieved by applying our residual split on various 3D-GS variants, underscoring its versatility and potential for broader application in 3D-GS-based applications.  
- **📝翻译未启用或未翻译**  

### [6] Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes  
- **⏳发布**：2024-12-07  
- **🧑‍🔬作者**：Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.05700v1)    
- **📝摘要**：Recent advancements in high-fidelity dynamic scene reconstruction have leveraged dynamic 3D Gaussians and 4D Gaussian Splatting for realistic scene representation. However, to make these methods viable for real-time applications such as AR/VR, gaming, and rendering on low-power devices, substantial reductions in memory usage and improvements in rendering efficiency are required. While many state-of-the-art methods prioritize lightweight implementations, they struggle in handling scenes with complex motions or long sequences. In this work, we introduce Temporally Compressed 3D Gaussian Splatting (TC3DGS), a novel technique designed specifically to effectively compress dynamic 3D Gaussian representations. TC3DGS selectively prunes Gaussians based on their temporal relevance and employs gradient-aware mixed-precision quantization to dynamically compress Gaussian parameters. It additionally relies on a variation of the Ramer-Douglas-Peucker algorithm in a post-processing step to further reduce storage by interpolating Gaussian trajectories across frames. Our experiments across multiple datasets demonstrate that TC3DGS achieves up to 67$\times$ compression with minimal or ...  
- **📝翻译未启用或未翻译**  

### [7] Occam's LGS: An Efficient Approach for Language Gaussian Splatting  
- **⏳发布**：2024-12-02（更新：2025-03-08）  
- **🧑‍🔬作者**：Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, Danda Pani Paudel  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2412.01807v2)   · [Project](https://insait-institute.github.io/OccamLGS/)  
- **📝摘要**：TL;DR: Gaussian Splatting is a widely adopted approach for 3D scene representation, offering efficient, high-quality reconstruction and rendering. A key reason for its success is the simplicity of representing scenes with sets of Gaussians, making it interpretable and adaptable. To enhance understanding beyond visual representation, recent approaches extend Gaussian Splatting with semantic vision-language features, enabling open-set tasks. Typically, these language features are aggregated from multiple 2D views, however, existing methods rely on cumbersome techniques, resulting in high computational costs and longer training times. In this work, we show that the complicated pipelines for language 3D Gaussian Splatting are simply unnecessary. Instead, we follow a probabilistic formulation of Language Gaussian Splatting and apply Occam's razor to the task at hand, leading to a highly efficient weighted multi-view feature aggregation technique. Doing so offers us state-of-the-art results with a speed-up of two orders of magnitude without any compression, allowing for easy scene ...  
- **📝翻译未启用或未翻译**  


## November 2024

### [1] GuardSplat: Efficient and Robust Watermarking for 3D Gaussian Splatting  
- **⏳发布**：2024-11-29（更新：2025-03-17）  
- **🧑‍🔬作者**：Zixuan Chen, Guangcong Wang, Jiahao Zhu, Jianhuang Lai, Xiaohua Xie  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.19895v5)   · [Project](https://narcissusex.github.io/GuardSplat,)  
- **📝摘要**：3D Gaussian Splatting (3DGS) has recently created impressive 3D assets for various applications. However, considering security, capacity, invisibility, and training efficiency, the copyright of 3DGS assets is not well protected as existing watermarking methods are unsuited for its rendering pipeline. In this paper, we propose GuardSplat, an innovative and efficient framework for watermarking 3DGS assets. Specifically, 1) We propose a CLIP-guided pipeline for optimizing the message decoder with minimal costs. The key objective is to achieve high-accuracy extraction by leveraging CLIP's aligning capability and rich representations, demonstrating exceptional capacity and efficiency. 2) We tailor a Spherical-Harmonic-aware (SH-aware) Message Embedding module for 3DGS, seamlessly embedding messages into the SH features of each 3D Gaussian while preserving the original 3D structure. This enables watermarking 3DGS assets with minimal fidelity trade-offs and prevents malicious users from removing the watermarks from the model files, meeting the demands for invisibility and security. 3) We present ...  
- **📝翻译未启用或未翻译**  

### [2] HEMGS: A Hybrid Entropy Model for 3D Gaussian Splatting Data Compression  
- **⏳发布**：2024-11-27（更新：2025-04-22）  
- **🧑‍🔬作者**：Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.18473v2)    
- **📝摘要**：In this work, we propose a novel compression framework for 3D Gaussian Splatting (3DGS) data. Building on anchor-based 3DGS methodologies, our approach compresses all attributes within each anchor by introducing a novel Hybrid Entropy Model for 3D Gaussian Splatting (HEMGS) to achieve hybrid lossy-lossless compression. It consists of three main components: a variable-rate predictor, a hyperprior network, and an autoregressive network. First, unlike previous methods that adopt multiple models to achieve multi-rate lossy compression, thereby increasing training overhead, our variable-rate predictor enables variable-rate compression with a single model and a hyperparameter $\lambda$ by producing a learned Quantization Step feature for versatile lossy compression. Second, to improve lossless compression, the hyperprior network captures both scene-agnostic and scene-specific features to generate a prior feature, while the autoregressive network employs an adaptive context selection algorithm with flexible receptive fields to produce a contextual feature. By integrating these two features, HEMGS can accurately estimate ...  
- **📝翻译未启用或未翻译**  

### [3] 4D Scaffold Gaussian Splatting with Dynamic-Aware Anchor Growing for  Efficient and High-Fidelity Dynamic Scene Reconstruction  
- **⏳发布**：2024-11-26（更新：2025-08-05）  
- **🧑‍🔬作者**：Woong Oh Cho, In Cho, Seoha Kim et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.17044v2)    
- **📝摘要**：Modeling dynamic scenes through 4D Gaussians offers high visual fidelity and fast rendering speeds, but comes with significant storage overhead. Recent approaches mitigate this cost by aggressively reducing the number of Gaussians. However, this inevitably removes Gaussians essential for high-quality rendering, leading to severe degradation in dynamic regions. In this paper, we introduce a novel 4D anchor-based framework that tackles the storage cost in different perspective. Rather than reducing the number of Gaussians, our method retains a sufficient quantity to accurately model dynamic contents, while compressing them into compact, grid-aligned 4D anchor features. Each anchor is processed by an MLP to spawn a set of neural 4D Gaussians, which represent a local spatiotemporal region. We design these neural 4D Gaussians to capture temporal changes with minimal parameters, making them well-suited for the MLP-based spawning. Moreover, we introduce a dynamic-aware anchor growing strategy to effectively assign additional anchors to under-reconstructed dynamic ...  
- **📝翻译未启用或未翻译**  

### [4] NexusSplats: Efficient 3D Gaussian Splatting in the Wild  
- **⏳发布**：2024-11-21（更新：2025-03-09）  
- **🧑‍🔬作者**：Yuzhou Tang, Dejun Xu, Yongjie Hou, Zhenzhong Wang, Min Jiang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.14514v5)    
- **📝摘要**：Photorealistic 3D reconstruction of unstructured real-world scenes remains challenging due to complex illumination variations and transient occlusions. Existing methods based on Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) struggle with inefficient light decoupling and structure-agnostic occlusion handling. To address these limitations, we propose NexusSplats, an approach tailored for efficient and high-fidelity 3D scene reconstruction under complex lighting and occlusion conditions. In particular, NexusSplats leverages a hierarchical light decoupling strategy that performs centralized appearance learning, efficiently and effectively decoupling varying lighting conditions. Furthermore, a structure-aware occlusion handling mechanism is developed, establishing a nexus between 3D and 2D structures for fine-grained occlusion handling. Experimental results demonstrate that NexusSplats achieves state-of-the-art rendering quality and reduces the number of total parameters by 65.4\%, leading to 2.7$\times$ faster reconstruction.  
- **📝翻译未启用或未翻译**  

### [5] SCIGS: 3D Gaussians Splatting from a Snapshot Compressive Image  
- **⏳发布**：2024-11-19（更新：2024-11-25）  
- **🧑‍🔬作者**：Zixu Wang, Hao Yang, Yu Guo, Fei Wang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.12471v2)    
- **📝摘要**：Snapshot Compressive Imaging (SCI) offers a possibility for capturing information in high-speed dynamic scenes, requiring efficient reconstruction method to recover scene information. Despite promising results, current deep learning-based and NeRF-based reconstruction methods face challenges: 1) deep learning-based reconstruction methods struggle to maintain 3D structural consistency within scenes, and 2) NeRF-based reconstruction methods still face limitations in handling dynamic scenes. To address these challenges, we propose SCIGS, a variant of 3DGS, and develop a primitive-level transformation network that utilizes camera pose stamps and Gaussian primitive coordinates as embedding vectors. This approach resolves the necessity of camera pose in vanilla 3DGS and enhances multi-view 3D structural consistency in dynamic scenes by utilizing transformed primitives. Additionally, a high-frequency filter is introduced to eliminate the artifacts generated during the transformation. The proposed SCIGS is the first to reconstruct a 3D explicit scene from a single compressed image, extending its application to dynamic 3D scenes. ...  
- **📝翻译未启用或未翻译**  

### [6] Efficient Density Control for 3D Gaussian Splatting  
- **⏳发布**：2024-11-15（更新：2025-03-11）  
- **🧑‍🔬作者**：Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.10133v3)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has demonstrated outstanding performance in novel view synthesis, achieving a balance between rendering quality and real-time performance. 3DGS employs Adaptive Density Control (ADC) to increase the number of Gaussians. However, the clone and split operations within ADC are not sufficiently efficient, impacting optimization speed and detail recovery. Additionally, overfitted Gaussians that affect rendering quality may exist, and the original ADC is unable to remove them. To address these issues, we propose two key innovations: (1) Long-Axis Split, which precisely controls the position, shape, and opacity of child Gaussians to minimize the difference before and after splitting. (2) Recovery-Aware Pruning, which leverages differences in recovery speed after resetting opacity to prune overfitted Gaussians, thereby improving generalization performance. Experimental results show that our method significantly enhances rendering quality. Code is available at https://github.com/XiaoBin2001/EDC.  
- **📝翻译未启用或未翻译**  

### [7] A Hierarchical Compression Technique for 3D Gaussian Splatting  Compression  
- **⏳发布**：2024-11-11（更新：2025-03-16）  
- **🧑‍🔬作者**：He Huang, Wenjie Huang, Qi Yang, Yiling Xu, Zhu li  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.06976v2)    
- **📝摘要**：3D Gaussian Splatting (GS) demonstrates excellent rendering quality and generation speed in novel view synthesis. However, substantial data size poses challenges for storage and transmission, making 3D GS compression an essential technology. Current 3D GS compression research primarily focuses on developing more compact scene representations, such as converting explicit 3D GS data into implicit forms. In contrast, compression of the GS data itself has hardly been explored. To address this gap, we propose a Hierarchical GS Compression (HGSC) technique. Initially, we prune unimportant Gaussians based on importance scores derived from both global and local significance, effectively reducing redundancy while maintaining visual quality. An Octree structure is used to compress 3D positions. Based on the 3D GS Octree, we implement a hierarchical attribute compression strategy by employing a KD-tree to partition the 3D GS into multiple blocks. We apply farthest point sampling to select anchor primitives within each block and others ...  
- **📝翻译未启用或未翻译**  

### [8] GaussianSpa: An "Optimizing-Sparsifying" Simplification Framework for  Compact and High-Quality 3D Gaussian Splatting  
- **⏳发布**：2024-11-09（更新：2025-04-10）  
- **🧑‍🔬作者**：Yangming Zhang, Wenqi Jia, Wei Niu, Miao Yin  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2411.06019v3)   · [Project](https://noodle-lab.github.io/gaussianspa/.)  
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a mainstream for novel view synthesis, leveraging continuous aggregations of Gaussian functions to model scene geometry. However, 3DGS suffers from substantial memory requirements to store the multitude of Gaussians, hindering its practicality. To address this challenge, we introduce GaussianSpa, an optimization-based simplification framework for compact and high-quality 3DGS. Specifically, we formulate the simplification as an optimization problem associated with the 3DGS training. Correspondingly, we propose an efficient "optimizing-sparsifying" solution that alternately solves two independent sub-problems, gradually imposing strong sparsity onto the Gaussians in the training process. Our comprehensive evaluations on various datasets show the superiority of GaussianSpa over existing state-of-the-art approaches. Notably, GaussianSpa achieves an average PSNR improvement of 0.9 dB on the real-world Deep Blending dataset with 10$\times$ fewer Gaussians compared to the vanilla 3DGS. Our project page is available at https://noodle-lab.github.io/gaussianspa/.  
- **📝翻译未启用或未翻译**  


## October 2024

### [1] ELMGS: Enhancing memory and computation scaLability through coMpression  for 3D Gaussian Splatting  
- **⏳发布**：2024-10-30  
- **🧑‍🔬作者**：Muhammad Salman Ali, Sung-Ho Bae, Enzo Tartaglione  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2410.23213v1)    
- **📝摘要**：3D models have recently been popularized by the potentiality of end-to-end training offered first by Neural Radiance Fields and most recently by 3D Gaussian Splatting models. The latter has the big advantage of naturally providing fast training convergence and high editability. However, as the research around these is still in its infancy, there is still a gap in the literature regarding the model's scalability. In this work, we propose an approach enabling both memory and computation scalability of such models. More specifically, we propose an iterative pruning strategy that removes redundant information encoded in the model. We also enhance compressibility for the model by including in the optimization strategy a differentiable quantization and entropy coding estimator. Our results on popular benchmarks showcase the effectiveness of the proposed approach and open the road to the broad deployability of such a solution even on resource-constrained devices.  
- **📝翻译未启用或未翻译**  

### [2] MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes  
- **⏳发布**：2024-10-17（更新：2025-07-22）  
- **🧑‍🔬作者**：Xinjie Zhang, Zhening Liu, Yifan Zhang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2410.13613v3)    
- **📝摘要**：4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly rasterizer, enabling rapid rendering speeds. Despite its advantages, 4DGS faces significant challenges, notably the requirement of millions of 4D Gaussians, each with extensive associated attributes, leading to substantial memory and storage cost. This paper introduces a memory-efficient framework for 4DGS. We streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. This approach eliminates the need for spherical harmonics coefficients, which typically involve up to 144 parameters in classic 4DGS, thereby creating a memory-efficient 4D Gaussian representation. Furthermore, we introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit ...  
- **📝翻译未启用或未翻译**  

### [3] GS^3: Efficient Relighting with Triple Gaussian Splatting  
- **⏳发布**：2024-10-15  
- **🧑‍🔬作者**：Zoubin Bi, Yixin Zeng, Chong Zeng et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2410.11419v1)   · [Project](https://GSrelight.github.io/.)  
- **📝摘要**：We present a spatial and angular Gaussian based representation and a triple splatting process, for real-time, high-quality novel lighting-and-view synthesis from multi-view point-lit input images. To describe complex appearance, we employ a Lambertian plus a mixture of angular Gaussians as an effective reflectance function for each spatial Gaussian. To generate self-shadow, we splat all spatial Gaussians towards the light source to obtain shadow values, which are further refined by a small multi-layer perceptron. To compensate for other effects like global illumination, another network is trained to compute and add a per-spatial-Gaussian RGB tuple. The effectiveness of our representation is demonstrated on 30 samples with a wide variation in geometry (from solid to fluffy) and appearance (from translucent to anisotropic), as well as using different forms of input data, including rendered images of synthetic/reconstructed objects, photographs captured with a handheld camera and a flash, or from a professional lightstage. We achieve ...  
- **📝翻译未启用或未翻译**  

### [4] Efficient Perspective-Correct 3D Gaussian Splatting Using Hybrid  Transparency  
- **⏳发布**：2024-10-10（更新：2025-03-10）  
- **🧑‍🔬作者**：Florian Hahlbohm, Fabian Friederichs, Tim Weyrich et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2410.08129v3)    
- **📝摘要**：3D Gaussian Splats (3DGS) have proven a versatile rendering primitive, both for inverse rendering as well as real-time exploration of scenes. In these applications, coherence across camera frames and multiple views is crucial, be it for robust convergence of a scene reconstruction or for artifact-free fly-throughs. Recent work started mitigating artifacts that break multi-view coherence, including popping artifacts due to inconsistent transparency sorting and perspective-correct outlines of (2D) splats. At the same time, real-time requirements forced such implementations to accept compromises in how transparency of large assemblies of 3D Gaussians is resolved, in turn breaking coherence in other ways. In our work, we aim at achieving maximum coherence, by rendering fully perspective-correct 3D Gaussians while using a high-quality approximation of accurate blending, hybrid transparency, on a per-pixel level, in order to retain real-time frame rates. Our fast and perspectively accurate approach for evaluation of 3D Gaussians does not require matrix ...  
- **📝翻译未启用或未翻译**  

### [5] Fast Feedforward 3D Gaussian Splatting Compression  
- **⏳发布**：2024-10-10（更新：2025-03-12）  
- **🧑‍🔬作者**：Yihang Chen, Qianyi Wu, Mengyao Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2410.08017v3)    
- **📝摘要**：With 3D Gaussian Splatting (3DGS) advancing real-time and high-fidelity rendering for novel view synthesis, storage requirements pose challenges for their widespread adoption. Although various compression techniques have been proposed, previous art suffers from a common limitation: for any existing 3DGS, per-scene optimization is needed to achieve compression, making the compression sluggish and slow. To address this issue, we introduce Fast Compression of 3D Gaussian Splatting (FCGS), an optimization-free model that can compress 3DGS representations rapidly in a single feed-forward pass, which significantly reduces compression time from minutes to seconds. To enhance compression efficiency, we propose a multi-path entropy module that assigns Gaussian attributes to different entropy constraint paths for balance between size and fidelity. We also carefully design both inter- and intra-Gaussian context models to remove redundancies among the unstructured Gaussian blobs. Overall, FCGS achieves a compression ratio of over 20X while maintaining fidelity, surpassing most per-scene SOTA optimization-based methods. ...  
- **📝翻译未启用或未翻译**  


## September 2024

### [1] MGSO: Monocular Real-time Photometric SLAM with Efficient 3D Gaussian  Splatting  
- **⏳发布**：2024-09-19（更新：2025-03-24）  
- **🧑‍🔬作者**：Yan Song Hu, Nicolas Abboud, Muhammad Qasim Ali et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2409.13055v2)    
- **📝摘要**：Real-time SLAM with dense 3D mapping is computationally challenging, especially on resource-limited devices. The recent development of 3D Gaussian Splatting (3DGS) offers a promising approach for real-time dense 3D reconstruction. However, existing 3DGS-based SLAM systems struggle to balance hardware simplicity, speed, and map quality. Most systems excel in one or two of the aforementioned aspects but rarely achieve all. A key issue is the difficulty of initializing 3D Gaussians while concurrently conducting SLAM. To address these challenges, we present Monocular GSO (MGSO), a novel real-time SLAM system that integrates photometric SLAM with 3DGS. Photometric SLAM provides dense structured point clouds for 3DGS initialization, accelerating optimization and producing more efficient maps with fewer Gaussians. As a result, experiments show that our system generates reconstructions with a balance of quality, memory efficiency, and speed that outperforms the state-of-the-art. Furthermore, our system achieves all results using RGB inputs. We evaluate the Replica, TUM-RGBD, ...  
- **📝翻译未启用或未翻译**  

### [2] GLC-SLAM: Gaussian Splatting SLAM with Efficient Loop Closure  
- **⏳发布**：2024-09-17  
- **🧑‍🔬作者**：Ziheng Xu, Qingfeng Li, Chen Chen, Xuefeng Liu, Jianwei Niu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2409.10982v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has gained significant attention for its application in dense Simultaneous Localization and Mapping (SLAM), enabling real-time rendering and high-fidelity mapping. However, existing 3DGS-based SLAM methods often suffer from accumulated tracking errors and map drift, particularly in large-scale environments. To address these issues, we introduce GLC-SLAM, a Gaussian Splatting SLAM system that integrates global optimization of camera poses and scene models. Our approach employs frame-to-model tracking and triggers hierarchical loop closure using a global-to-local strategy to minimize drift accumulation. By dividing the scene into 3D Gaussian submaps, we facilitate efficient map updates following loop corrections in large scenes. Additionally, our uncertainty-minimized keyframe selection strategy prioritizes keyframes observing more valuable 3D Gaussians to enhance submap optimization. Experimental results on various datasets demonstrate that GLC-SLAM achieves superior or competitive tracking and mapping performance compared to state-of-the-art dense RGB-D SLAM systems.  
- **📝翻译未启用或未翻译**  

### [3] MesonGS: Post-training Compression of 3D Gaussians via Efficient  Attribute Transformation  
- **⏳发布**：2024-09-15  
- **🧑‍🔬作者**：Shuzhao Xie, Weixiang Zhang, Chen Tang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2409.09756v1)    
- **📝摘要**：3D Gaussian Splatting demonstrates excellent quality and speed in novel view synthesis. Nevertheless, the huge file size of the 3D Gaussians presents challenges for transmission and storage. Current works design compact models to replace the substantial volume and attributes of 3D Gaussians, along with intensive training to distill information. These endeavors demand considerable training time, presenting formidable hurdles for practical deployment. To this end, we propose MesonGS, a codec for post-training compression of 3D Gaussians. Initially, we introduce a measurement criterion that considers both view-dependent and view-independent factors to assess the impact of each Gaussian point on the rendering output, enabling the removal of insignificant points. Subsequently, we decrease the entropy of attributes through two transformations that complement subsequent entropy coding techniques to enhance the file compression rate. More specifically, we first replace rotation quaternions with Euler angles; then, we apply region adaptive hierarchical transform to key attributes to reduce ...  
- **📝翻译未启用或未翻译**  


## August 2024

### [1] GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation  with Gaussian Splatting  
- **⏳发布**：2024-08-21（更新：2025-07-14）  
- **🧑‍🔬作者**：Wanshui Gan, Fang Liu, Hongbin Xu, Ningkai Mo, Naoto Yokoya  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.11447v4)    
- **📝摘要**：We introduce GaussianOcc, a systematic method that investigates the two usages of Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views. First, traditional methods for self-supervised 3D occupancy estimation still require ground truth 6D poses from sensors during training. To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection. Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps, semantic maps), which is both time-consuming and less effective. We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting. As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster in training and 5 times faster in rendering). The relevant code ...  
- **📝翻译未启用或未翻译**  

### [2] GS-CPR: Efficient Camera Pose Refinement via 3D Gaussian Splatting  
- **⏳发布**：2024-08-20（更新：2025-03-01）  
- **🧑‍🔬作者**：Changkun Liu, Shuai Chen, Yash Bhalgat et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.11085v4)   · [Project](https://xrim-lab.github.io/GS-CPR/.)  
- **📝摘要**：We leverage 3D Gaussian Splatting (3DGS) as a scene representation and propose a novel test-time camera pose refinement (CPR) framework, GS-CPR. This framework enhances the localization accuracy of state-of-the-art absolute pose regression and scene coordinate regression methods. The 3DGS model renders high-quality synthetic images and depth maps to facilitate the establishment of 2D-3D correspondences. GS-CPR obviates the need for training feature extractors or descriptors by operating directly on RGB images, utilizing the 3D foundation model, MASt3R, for precise 2D matching. To improve the robustness of our model in challenging outdoor environments, we incorporate an exposure-adaptive module within the 3DGS framework. Consequently, GS-CPR enables efficient one-shot pose refinement given a single RGB query and a coarse initial pose estimation. Our proposed approach surpasses leading NeRF-based optimization methods in both accuracy and runtime across indoor and outdoor visual localization benchmarks, achieving new state-of-the-art accuracy on two indoor datasets. The project page is ...  
- **📝翻译未启用或未翻译**  

### [3] Implicit Gaussian Splatting with Efficient Multi-Level Tri-Plane  Representation  
- **⏳发布**：2024-08-19（更新：2024-11-09）  
- **🧑‍🔬作者**：Minye Wu, Tinne Tuytelaars  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.10041v2)    
- **📝摘要**：Recent advancements in photo-realistic novel view synthesis have been significantly driven by Gaussian Splatting (3DGS). Nevertheless, the explicit nature of 3DGS data entails considerable storage requirements, highlighting a pressing need for more efficient data representations. To address this, we present Implicit Gaussian Splatting (IGS), an innovative hybrid model that integrates explicit point clouds with implicit feature embeddings through a multi-level tri-plane architecture. This architecture features 2D feature grids at various resolutions across different levels, facilitating continuous spatial domain representation and enhancing spatial correlations among Gaussian primitives. Building upon this foundation, we introduce a level-based progressive training scheme, which incorporates explicit spatial regularization. This method capitalizes on spatial correlations to enhance both the rendering quality and the compactness of the IGS representation. Furthermore, we propose a novel compression pipeline tailored for both point clouds and 2D feature grids, considering the entropy variations across different levels. Extensive experimental evaluations demonstrate that our ...  
- **📝翻译未启用或未翻译**  

### [4] FlashGS: Efficient 3D Gaussian Splatting for Large-scale and  High-resolution Rendering  
- **⏳发布**：2024-08-15（更新：2024-08-19）  
- **🧑‍🔬作者**：Guofeng Feng, Siyan Chen, Rong Fu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.07967v2)    
- **📝摘要**：This work introduces FlashGS, an open-source CUDA Python library, designed to facilitate the efficient differentiable rasterization of 3D Gaussian Splatting through algorithmic and kernel-level optimizations. FlashGS is developed based on the observations from a comprehensive analysis of the rendering process to enhance computational efficiency and bring the technique to wide adoption. The paper includes a suite of optimization strategies, encompassing redundancy elimination, efficient pipelining, refined control and scheduling mechanisms, and memory access optimizations, all of which are meticulously integrated to amplify the performance of the rasterization process. An extensive evaluation of FlashGS' performance has been conducted across a diverse spectrum of synthetic and real-world large-scale scenes, encompassing a variety of image resolutions. The empirical findings demonstrate that FlashGS consistently achieves an average 4x acceleration over mobile consumer GPUs, coupled with reduced memory consumption. These results underscore the superior performance and resource optimization capabilities of FlashGS, positioning it as a formidable ...  
- **📝翻译未启用或未翻译**  

### [5] PRTGaussian: Efficient Relighting Using 3D Gaussians with Precomputed  Radiance Transfer  
- **⏳发布**：2024-08-10  
- **🧑‍🔬作者**：Libo Zhang, Yuxuan Han, Wenbin Lin, Jingwang Ling, Feng Xu  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.05631v1)    
- **📝摘要**：We present PRTGaussian, a realtime relightable novel-view synthesis method made possible by combining 3D Gaussians and Precomputed Radiance Transfer (PRT). By fitting relightable Gaussians to multi-view OLAT data, our method enables real-time, free-viewpoint relighting. By estimating the radiance transfer based on high-order spherical harmonics, we achieve a balance between capturing detailed relighting effects and maintaining computational efficiency. We utilize a two-stage process: in the first stage, we reconstruct a coarse geometry of the object from multi-view images. In the second stage, we initialize 3D Gaussians with the obtained point cloud, then simultaneously refine the coarse geometry and learn the light transport for each Gaussian. Extensive experiments on synthetic datasets show that our approach can achieve fast and high-quality relighting for general objects. Code and data are available at https://github.com/zhanglbthu/PRTGaussian.  
- **📝翻译未启用或未翻译**  

### [6] InstantStyleGaussian: Efficient Art Style Transfer with 3D Gaussian  Splatting  
- **⏳发布**：2024-08-08（更新：2024-08-26）  
- **🧑‍🔬作者**：Xin-Yi Yu, Jun-Xin Yu, Li-Bo Zhou, Yan Wei, Lin-Lin Ou  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.04249v2)    
- **📝摘要**：We present InstantStyleGaussian, an innovative 3D style transfer method based on the 3D Gaussian Splatting (3DGS) scene representation. By inputting a target-style image, it quickly generates new 3D GS scenes. Our method operates on pre-reconstructed GS scenes, combining diffusion models with an improved iterative dataset update strategy. It utilizes diffusion models to generate target style images, adds these new images to the training dataset, and uses this dataset to iteratively update and optimize the GS scenes, significantly accelerating the style editing process while ensuring the quality of the generated scenes. Extensive experimental results demonstrate that our method ensures high-quality stylized scenes while offering significant advantages in style transfer speed and consistency.  
- **📝翻译未启用或未翻译**  

### [7] Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields  
- **⏳发布**：2024-08-07  
- **🧑‍🔬作者**：Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2408.03822v1)   · [Project](https://maincold2.github.io/c3dgs/.)  
- **📝摘要**：3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussian-based representation and introduces an approximated volumetric rendering, achieving very fast rendering speed and promising image quality. Furthermore, subsequent studies have successfully extended 3DGS to dynamic 3D scenes, demonstrating its wide range of applications. However, a significant drawback arises as 3DGS and its following methods entail a substantial number of Gaussians to maintain the high fidelity of the rendered images, which requires a large amount of memory and storage. To address this critical issue, we place a specific emphasis on two key objectives: reducing the number of Gaussian points without sacrificing performance and compressing the Gaussian attributes, such as view-dependent color and covariance. To this end, we propose a learnable mask strategy that significantly reduces the number of Gaussians while preserving high performance. In addition, we propose a compact but effective representation of view-dependent color ...  
- **📝翻译未启用或未翻译**  


## July 2024

### [1] Ev-GS: Event-based Gaussian splatting for Efficient and Accurate  Radiance Field Rendering  
- **⏳发布**：2024-07-16  
- **🧑‍🔬作者**：Jingqian Wu, Shuo Zhu, Chutian Wang, Edmund Y. Lam  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2407.11343v1)    
- **📝摘要**：Computational neuromorphic imaging (CNI) with event cameras offers advantages such as minimal motion blur and enhanced dynamic range, compared to conventional frame-based methods. Existing event-based radiance field rendering methods are built on neural radiance field, which is computationally heavy and slow in reconstruction speed. Motivated by the two aspects, we introduce Ev-GS, the first CNI-informed scheme to infer 3D Gaussian splatting from a monocular event camera, enabling efficient novel view synthesis. Leveraging 3D Gaussians with pure event-based supervision, Ev-GS overcomes challenges such as the detection of fast-moving objects and insufficient lighting. Experimental results show that Ev-GS outperforms the method that takes frame-based signals as input by rendering realistic views with reduced blurring and improved visual quality. Moreover, it demonstrates competitive reconstruction quality and reduced computing occupancy compared to existing methods, which paves the way to a highly efficient CNI approach for signal processing.  
- **📝翻译未启用或未翻译**  


## June 2024

### [1] Trimming the Fat: Efficient Compression of 3D Gaussian Splats through  Pruning  
- **⏳发布**：2024-06-26（更新：2024-07-29）  
- **🧑‍🔬作者**：Muhammad Salman Ali, Maryam Qamar, Sung-Ho Bae, Enzo Tartaglione  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.18214v2)    
- **📝摘要**：In recent times, the utilization of 3D models has gained traction, owing to the capacity for end-to-end training initially offered by Neural Radiance Fields and more recently by 3D Gaussian Splatting (3DGS) models. The latter holds a significant advantage by inherently easing rapid convergence during training and offering extensive editability. However, despite rapid advancements, the literature still lives in its infancy regarding the scalability of these models. In this study, we take some initial steps in addressing this gap, showing an approach that enables both the memory and computational scalability of such models. Specifically, we propose "Trimming the fat", a post-hoc gradient-informed iterative pruning technique to eliminate redundant information encoded in the model. Our experimental findings on widely acknowledged benchmarks attest to the effectiveness of our approach, revealing that up to 75% of the Gaussians can be removed while maintaining or even improving upon baseline performance. Our approach achieves around ...  
- **📝翻译未启用或未翻译**  

### [2] LGS: A Light-weight 4D Gaussian Splatting for Efficient Surgical Scene  Reconstruction  
- **⏳发布**：2024-06-23  
- **🧑‍🔬作者**：Hengyu Liu, Yifan Liu, Chenxin Li, Wuyang Li, Yixuan Yuan  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.16073v1)    
- **📝摘要**：The advent of 3D Gaussian Splatting (3D-GS) techniques and their dynamic scene modeling variants, 4D-GS, offers promising prospects for real-time rendering of dynamic surgical scenarios. However, the prerequisite for modeling dynamic scenes by a large number of Gaussian units, the high-dimensional Gaussian attributes and the high-resolution deformation fields, all lead to serve storage issues that hinder real-time rendering in resource-limited surgical equipment. To surmount these limitations, we introduce a Lightweight 4D Gaussian Splatting framework (LGS) that can liberate the efficiency bottlenecks of both rendering and storage for dynamic endoscopic reconstruction. Specifically, to minimize the redundancy of Gaussian quantities, we propose Deformation-Aware Pruning by gauging the impact of each Gaussian on deformation. Concurrently, to reduce the redundancy of Gaussian attributes, we simplify the representation of textures and lighting in non-crucial areas by pruning the dimensions of Gaussian attributes. We further resolve the feature field redundancy caused by the high resolution of ...  
- **📝翻译未启用或未翻译**  

### [3] 3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods  
- **⏳发布**：2024-06-17（更新：2025-03-05）  
- **🧑‍🔬作者**：Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2407.09510v5)   · [Project](https://w-m.github.io/3dgs-compression-survey/)  
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a cutting-edge technique for real-time radiance field rendering, offering state-of-the-art performance in terms of both quality and speed. 3DGS models a scene as a collection of three-dimensional Gaussians, with additional attributes optimized to conform to the scene's geometric and visual properties. Despite its advantages in rendering speed and image fidelity, 3DGS is limited by its significant storage and memory demands. These high demands make 3DGS impractical for mobile devices or headsets, reducing its applicability in important areas of computer graphics. To address these challenges and advance the practicality of 3DGS, this survey provides a comprehensive and detailed examination of compression and compaction techniques developed to make 3DGS more efficient. We classify existing methods into two categories: compression, which focuses on reducing file size, and compaction, which aims to minimize the number of Gaussians. Both methods aim to maintain or improve quality, each by ...  
- **📝翻译未启用或未翻译**  

### [4] PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting  
- **⏳发布**：2024-06-14（更新：2025-03-24）  
- **🧑‍🔬作者**：Alex Hanson, Allen Tu, Vasu Singla et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.10219v3)    
- **📝摘要**：Recent advances in novel view synthesis have enabled real-time rendering speeds with high reconstruction accuracy. 3D Gaussian Splatting (3D-GS), a foundational point-based parametric 3D scene representation, models scenes as large sets of 3D Gaussians. However, complex scenes can consist of millions of Gaussians, resulting in high storage and memory requirements that limit the viability of 3D-GS on devices with limited resources. Current techniques for compressing these pretrained models by pruning Gaussians rely on combining heuristics to determine which Gaussians to remove. At high compression ratios, these pruned scenes suffer from heavy degradation of visual fidelity and loss of foreground details. In this paper, we propose a principled sensitivity pruning score that preserves visual fidelity and foreground details at significantly higher compression ratios than existing approaches. It is computed as a second-order approximation of the reconstruction error on the training views with respect to the spatial parameters of each Gaussian. Additionally, ...  
- **📝翻译未启用或未翻译**  

### [5] GaussianForest: Hierarchical-Hybrid 3D Gaussian Splatting for Compressed  Scene Modeling  
- **⏳发布**：2024-06-13（更新：2024-08-08）  
- **🧑‍🔬作者**：Fengyi Zhang, Yadan Luo, Tianjun Zhang, Lin Zhang, Zi Huang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.08759v2)    
- **📝摘要**：The field of novel-view synthesis has recently witnessed the emergence of 3D Gaussian Splatting, which represents scenes in a point-based manner and renders through rasterization. This methodology, in contrast to Radiance Fields that rely on ray tracing, demonstrates superior rendering quality and speed. However, the explicit and unstructured nature of 3D Gaussians poses a significant storage challenge, impeding its broader application. To address this challenge, we introduce the Gaussian-Forest modeling framework, which hierarchically represents a scene as a forest of hybrid 3D Gaussians. Each hybrid Gaussian retains its unique explicit attributes while sharing implicit ones with its sibling Gaussians, thus optimizing parameterization with significantly fewer variables. Moreover, adaptive growth and pruning strategies are designed, ensuring detailed representation in complex regions and a notable reduction in the number of required Gaussians. Extensive experiments demonstrate that Gaussian-Forest not only maintains comparable speed and quality but also achieves a compression rate surpassing 10 ...  
- **📝翻译未启用或未翻译**  

### [6] PGSR: Planar-based Gaussian Splatting for Efficient and High-Fidelity  Surface Reconstruction  
- **⏳发布**：2024-06-10（更新：2025-01-10）  
- **🧑‍🔬作者**：Danpeng Chen, Hai Li, Weicai Ye et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.06521v2)    
- **📝摘要**：Recently, 3D Gaussian Splatting (3DGS) has attracted widespread attention due to its high-quality rendering, and ultra-fast training and rendering speed. However, due to the unstructured and irregular nature of Gaussian point clouds, it is difficult to guarantee geometric reconstruction accuracy and multi-view consistency simply by relying on image reconstruction loss. Although many studies on surface reconstruction based on 3DGS have emerged recently, the quality of their meshes is generally unsatisfactory. To address this problem, we propose a fast planar-based Gaussian splatting reconstruction representation (PGSR) to achieve high-fidelity surface reconstruction while ensuring high-quality rendering. Specifically, we first introduce an unbiased depth rendering method, which directly renders the distance from the camera origin to the Gaussian plane and the corresponding normal map based on the Gaussian distribution of the point cloud, and divides the two to obtain the unbiased depth. We then introduce single-view geometric, multi-view photometric, and geometric regularization to preserve ...  
- **📝翻译未启用或未翻译**  

### [7] WE-GS: An In-the-wild Efficient 3D Gaussian Representation for  Unconstrained Photo Collections  
- **⏳发布**：2024-06-04  
- **🧑‍🔬作者**：Yuze Wang, Junyi Wang, Yue Qi  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2406.02407v1)    
- **📝摘要**：Novel View Synthesis (NVS) from unconstrained photo collections is challenging in computer graphics. Recently, 3D Gaussian Splatting (3DGS) has shown promise for photorealistic and real-time NVS of static scenes. Building on 3DGS, we propose an efficient point-based differentiable rendering framework for scene reconstruction from photo collections. Our key innovation is a residual-based spherical harmonic coefficients transfer module that adapts 3DGS to varying lighting conditions and photometric post-processing. This lightweight module can be pre-computed and ensures efficient gradient propagation from rendered images to 3D Gaussian attributes. Additionally, we observe that the appearance encoder and the transient mask predictor, the two most critical parts of NVS from unconstrained photo collections, can be mutually beneficial. We introduce a plug-and-play lightweight spatial attention module to simultaneously predict transient occluders and latent appearance representation for each image. After training and preprocessing, our method aligns with the standard 3DGS format and rendering pipeline, facilitating seamlessly integration ...  
- **📝翻译未启用或未翻译**  


## May 2024

### [1] ContextGS: Compact 3D Gaussian Splatting with Anchor Level Context Model  
- **⏳发布**：2024-05-31  
- **🧑‍🔬作者**：Yufei Wang, Zhihao Li, Lanqing Guo et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.20721v1)    
- **📝摘要**：Recently, 3D Gaussian Splatting (3DGS) has become a promising framework for novel view synthesis, offering fast rendering speeds and high fidelity. However, the large number of Gaussians and their associated attributes require effective compression techniques. Existing methods primarily compress neural Gaussians individually and independently, i.e., coding all the neural Gaussians at the same time, with little design for their interactions and spatial dependence. Inspired by the effectiveness of the context model in image compression, we propose the first autoregressive model at the anchor level for 3DGS compression in this work. We divide anchors into different levels and the anchors that are not coded yet can be predicted based on the already coded ones in all the coarser levels, leading to more accurate modeling and higher coding efficiency. To further improve the efficiency of entropy coding, e.g., to code the coarsest level with no already coded anchors, we propose to introduce ...  
- **📝翻译未启用或未翻译**  

### [2] LP-3DGS: Learning to Prune 3D Gaussian Splatting  
- **⏳发布**：2024-05-29  
- **🧑‍🔬作者**：Zhaoliang Zhang, Tianchen Song, Yongjae Lee et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.18784v1)    
- **📝摘要**：Recently, 3D Gaussian Splatting (3DGS) has become one of the mainstream methodologies for novel view synthesis (NVS) due to its high quality and fast rendering speed. However, as a point-based scene representation, 3DGS potentially generates a large number of Gaussians to fit the scene, leading to high memory usage. Improvements that have been proposed require either an empirical and preset pruning ratio or importance score threshold to prune the point cloud. Such hyperparamter requires multiple rounds of training to optimize and achieve the maximum pruning ratio, while maintaining the rendering quality for each scene. In this work, we propose learning-to-prune 3DGS (LP-3DGS), where a trainable binary mask is applied to the importance score that can find optimal pruning ratio automatically. Instead of using the traditional straight-through estimator (STE) method to approximate the binary mask gradient, we redesign the masking function to leverage the Gumbel-Sigmoid method, making it differentiable and compatible ...  
- **📝翻译未启用或未翻译**  

### [3] SafeguardGS: 3D Gaussian Primitive Pruning While Avoiding Catastrophic  Scene Destruction  
- **⏳发布**：2024-05-28（更新：2024-11-22）  
- **🧑‍🔬作者**：Yongjae Lee, Zhaoliang Zhang, Deliang Fan  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.17793v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has made significant strides in novel view synthesis. However, its suboptimal densification process results in the excessively large number of Gaussian primitives, which impacts frame-per-second and increases memory usage, making it unsuitable for low-end devices. To address this issue, many follow-up studies have proposed various pruning techniques with score functions designed to identify and remove less important primitives. Nonetheless, a comprehensive discussion of their effectiveness and implications across all techniques is missing. In this paper, we are the first to categorize 3DGS pruning techniques into two types: Scene-level pruning and Pixel-level pruning, distinguished by their scope for ranking primitives. Our subsequent experiments reveal that, while scene-level pruning leads to disastrous quality drops under extreme decimation of Gaussian primitives, pixel-level pruning not only sustains relatively high rendering quality with minuscule performance degradation but also provides an inherent boundary of pruning, i.e., a safeguard of Gaussian pruning. Building ...  
- **📝翻译未启用或未翻译**  

### [4] HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed  via Gaussian Splatting  
- **⏳发布**：2024-05-24（更新：2024-10-26）  
- **🧑‍🔬作者**：Yuanhao Cai, Zihao Xiao, Yixun Liang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.15125v4)   · [Project](https://youtu.be/wtU7Kcwe7ck)  
- **📝摘要**：High dynamic range (HDR) novel view synthesis (NVS) aims to create photorealistic images from novel viewpoints using HDR imaging techniques. The rendered HDR images capture a wider range of brightness levels containing more details of the scene than normal low dynamic range (LDR) images. Existing HDR NVS methods are mainly based on NeRF. They suffer from long training time and slow inference speed. In this paper, we propose a new framework, High Dynamic Range Gaussian Splatting (HDR-GS), which can efficiently render novel HDR views and reconstruct LDR images with a user input exposure time. Specifically, we design a Dual Dynamic Range (DDR) Gaussian point cloud model that uses spherical harmonics to fit HDR color and employs an MLP-based tone-mapper to render LDR color. The HDR and LDR colors are then fed into two Parallel Differentiable Rasterization (PDR) processes to reconstruct HDR and LDR views. To establish the data foundation for ...  
- **📝翻译未启用或未翻译**  

### [5] MotionGS : Compact Gaussian Splatting SLAM by Motion Filter  
- **⏳发布**：2024-05-18（更新：2024-05-31）  
- **🧑‍🔬作者**：Xinli Guo, Weidong Zhang, Ruonan Liu, Peng Han, Hongtian Chen  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.11129v2)    
- **📝摘要**：With their high-fidelity scene representation capability, the attention of SLAM field is deeply attracted by the Neural Radiation Field (NeRF) and 3D Gaussian Splatting (3DGS). Recently, there has been a surge in NeRF-based SLAM, while 3DGS-based SLAM is sparse. A novel 3DGS-based SLAM approach with a fusion of deep visual feature, dual keyframe selection and 3DGS is presented in this paper. Compared with the existing methods, the proposed tracking is achieved by feature extraction and motion filter on each frame. The joint optimization of poses and 3D Gaussians runs through the entire mapping process. Additionally, the coarse-to-fine pose estimation and compact Gaussian scene representation are implemented by dual keyframe selection and novel loss functions. Experimental results demonstrate that the proposed algorithm not only outperforms the existing methods in tracking and mapping, but also has less memory usage.  
- **📝翻译未启用或未翻译**  

### [6] SimEndoGS: Efficient Data-driven Scene Simulation using Robotic Surgery  Videos via Physics-embedded 3D Gaussians  
- **⏳发布**：2024-05-02（更新：2024-08-06）  
- **🧑‍🔬作者**：Zhenya Yang, Kai Chen, Yonghao Long, Qi Dou  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2405.00956v3)    
- **📝摘要**：Surgical scene simulation plays a crucial role in surgical education and simulator-based robot learning. Traditional approaches for creating these environments with surgical scene involve a labor-intensive process where designers hand-craft tissues models with textures and geometries for soft body simulations. This manual approach is not only time-consuming but also limited in the scalability and realism. In contrast, data-driven simulation offers a compelling alternative. It has the potential to automatically reconstruct 3D surgical scenes from real-world surgical video data, followed by the application of soft body physics. This area, however, is relatively uncharted. In our research, we introduce 3D Gaussian as a learnable representation for surgical scene, which is learned from stereo endoscopic video. To prevent over-fitting and ensure the geometrical correctness of these scenes, we incorporate depth supervision and anisotropy regularization into the Gaussian learning process. Furthermore, we apply the Material Point Method, which is integrated with physical properties, to ...  
- **📝翻译未启用或未翻译**  


## April 2024

### [1] CompGS: Efficient 3D Scene Representation via Compressed Gaussian  Splatting  
- **⏳发布**：2024-04-15  
- **🧑‍🔬作者**：Xiangrui Liu, Xinju Wu, Pingping Zhang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2404.09458v1)    
- **📝摘要**：Gaussian splatting, renowned for its exceptional rendering quality and efficiency, has emerged as a prominent technique in 3D scene representation. However, the substantial data volume of Gaussian splatting impedes its practical utility in real-world applications. Herein, we propose an efficient 3D scene representation, named Compressed Gaussian Splatting (CompGS), which harnesses compact Gaussian primitives for faithful 3D scene modeling with a remarkably reduced data size. To ensure the compactness of Gaussian primitives, we devise a hybrid primitive structure that captures predictive relationships between each other. Then, we exploit a small set of anchor primitives for prediction, allowing the majority of primitives to be encapsulated into highly compact residual forms. Moreover, we develop a rate-constrained optimization scheme to eliminate redundancies within such hybrid primitives, steering our CompGS towards an optimal trade-off between bitrate consumption and representation efficacy. Experimental results show that the proposed CompGS significantly outperforms existing methods, achieving superior compactness in ...  
- **📝翻译未启用或未翻译**  


## March 2024

### [1] CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D  Gaussian Field  
- **⏳发布**：2024-03-24  
- **🧑‍🔬作者**：Jiarui Hu, Xianhao Chen, Boyin Feng et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.16095v1)   · [Project](https://zju3dv.github.io/cg-slam.)  
- **📝摘要**：Recently neural radiance fields (NeRF) have been widely exploited as 3D representations for dense simultaneous localization and mapping (SLAM). Despite their notable successes in surface modeling and novel view synthesis, existing NeRF-based methods are hindered by their computationally intensive and time-consuming volume rendering pipeline. This paper presents an efficient dense RGB-D SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and geometric stability. Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping. Additionally, a novel depth uncertainty model is proposed to ensure the selection of valuable Gaussian primitives during optimization, thereby improving tracking efficiency and accuracy. Experiments on various datasets demonstrate that CG-SLAM achieves superior tracking and mapping performance with a notable tracking speed of up to 15 Hz. We will make our source code publicly available. Project ...  
- **📝翻译未启用或未翻译**  

### [2] MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images  
- **⏳发布**：2024-03-21（更新：2024-07-18）  
- **🧑‍🔬作者**：Yuedong Chen, Haofei Xu, Chuanxia Zheng et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.14627v2)    
- **📝摘要**：We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians. To accurately localize the Gaussian centers, we build a cost volume representation via plane sweeping, where the cross-view feature similarities stored in the cost volume can provide valuable geometry cues to the estimation of depth. We also learn other Gaussian primitives' parameters jointly with the Gaussian centers while only relying on photometric supervision. We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations. On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22~fps). More impressively, compared to the latest state-of-the-art method pixelSplat, MVSplat uses $10\times$ fewer parameters and infers more than $2\times$ faster while providing higher appearance and geometry quality as well as better cross-dataset generalization.  
- **📝翻译未启用或未翻译**  

### [3] HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression  
- **⏳发布**：2024-03-21（更新：2024-07-12）  
- **🧑‍🔬作者**：Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.14530v3)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel view synthesis, boasting rapid rendering speed with high fidelity. However, the substantial Gaussians and their associated attributes necessitate effective compression techniques. Nevertheless, the sparse and unorganized nature of the point cloud of Gaussians (or anchors in our paper) presents challenges for compression. To address this, we make use of the relations between the unorganized anchors and the structured hash grid, leveraging their mutual information for context modeling, and propose a Hash-grid Assisted Context (HAC) framework for highly compact 3DGS representation. Our approach introduces a binary hash grid to establish continuous spatial consistencies, allowing us to unveil the inherent spatial relations of anchors through a carefully designed context model. To facilitate entropy coding, we utilize Gaussian distributions to accurately estimate the probability of each quantized attribute, where an adaptive quantization module is proposed to enable high-precision quantization of these ...  
- **📝翻译未启用或未翻译**  

### [4] Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene  Reconstruction  
- **⏳发布**：2024-03-18  
- **🧑‍🔬作者**：Zhiyang Guo, Wengang Zhou, Li Li, Min Wang, Houqiang Li  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.11447v1)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has become an emerging tool for dynamic scene reconstruction. However, existing methods focus mainly on extending static 3DGS into a time-variant representation, while overlooking the rich motion information carried by 2D observations, thus suffering from performance degradation and model redundancy. To address the above problem, we propose a novel motion-aware enhancement framework for dynamic scene reconstruction, which mines useful motion cues from optical flow to improve different paradigms of dynamic 3DGS. Specifically, we first establish a correspondence between 3D Gaussian movements and pixel-level flow. Then a novel flow augmentation method is introduced with additional insights into uncertainty and loss collaboration. Moreover, for the prevalent deformation-based paradigm that presents a harder optimization problem, a transient-aware deformation auxiliary module is proposed. We conduct extensive experiments on both multi-view and monocular scenes to verify the merits of our work. Compared with the baselines, our method shows significant superiority in ...  
- **📝翻译未启用或未翻译**  

### [5] Compact 3D Gaussian Splatting For Dense Visual SLAM  
- **⏳发布**：2024-03-17（更新：2024-09-27）  
- **🧑‍🔬作者**：Tianchen Deng, Yaohui Chen, Leyan Zhang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.11247v2)    
- **📝摘要**：Recent work has shown that 3D Gaussian-based SLAM enables high-quality reconstruction, accurate pose estimation, and real-time rendering of scenes. However, these approaches are built on a tremendous number of redundant 3D Gaussian ellipsoids, leading to high memory and storage costs, and slow training speed. To address the limitation, we propose a compact 3D Gaussian Splatting SLAM system that reduces the number and the parameter size of Gaussian ellipsoids. A sliding window-based masking strategy is first proposed to reduce the redundant ellipsoids. Then we observe that the covariance matrix (geometry) of most 3D Gaussian ellipsoids are extremely similar, which motivates a novel geometry codebook to compress 3D Gaussian geometric attributes, i.e., the parameters. Robust and accurate pose estimation is achieved by a global bundle adjustment method with reprojection loss. Extensive experiments demonstrate that our method achieves faster training and rendering speed while maintaining the state-of-the-art (SOTA) quality of the scene representation.  
- **📝翻译未启用或未翻译**  

### [6] Sim2Real within 5 Minutes: Efficient Domain Transfer with Stylized  Gaussian Splatting for Endoscopic Images  
- **⏳发布**：2024-03-16（更新：2025-03-05）  
- **🧑‍🔬作者**：Junyang Wu, Yun Gu, Guang-Zhong Yang  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.10860v2)    
- **📝摘要**：Robot assisted endoluminal intervention is an emerging technique for both benign and malignant luminal lesions. With vision-based navigation, when combined with pre-operative imaging data as priors, it is possible to recover position and pose of the endoscope without the need of additional sensors. In practice, however, aligning pre-operative and intra-operative domains is complicated by significant texture differences. Although methods such as style transfer can be used to address this issue, they require large datasets from both source and target domains with prolonged training times. This paper proposes an efficient domain transfer method based on stylized Gaussian splatting, only requiring a few of real images (10 images) with very fast training time. Specifically, the transfer process includes two phases. In the first phase, the 3D models reconstructed from CT scans are represented as differential Gaussian point clouds. In the second phase, only color appearance related parameters are optimized to transfer the ...  
- **📝翻译未启用或未翻译**  

### [7] GaussianImage: 1000 FPS Image Representation and Compression by 2D  Gaussian Splatting  
- **⏳发布**：2024-03-13（更新：2024-07-09）  
- **🧑‍🔬作者**：Xinjie Zhang, Xingtong Ge, Tongda Xu et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.08551v5)    
- **📝摘要**：Implicit neural representations (INRs) recently achieved great success in image representation and compression, offering high visual quality and fast rendering speeds with 10-1000 FPS, assuming sufficient GPU resources are available. However, this requirement often hinders their use on low-end devices with limited memory. In response, we propose a groundbreaking paradigm of image representation and compression by 2D Gaussian Splatting, named GaussianImage. We first introduce 2D Gaussian to represent the image, where each Gaussian has 8 parameters including position, covariance and color. Subsequently, we unveil a novel rendering algorithm based on accumulated summation. Remarkably, our method with a minimum of 3$\times$ lower GPU memory usage and 5$\times$ faster fitting time not only rivals INRs (e.g., WIRE, I-NGP) in representation performance, but also delivers a faster rendering speed of 1500-2000 FPS regardless of parameter size. Furthermore, we integrate existing vector quantization technique to build an image codec. Experimental results demonstrate that our ...  
- **📝翻译未启用或未翻译**  

### [8] GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian  Splatting  
- **⏳发布**：2024-03-08（更新：2024-05-21）  
- **🧑‍🔬作者**：Francesco Palandra, Andrea Sanchietti, Daniele Baieri, Emanuele Rodolà  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.05154v2)    
- **📝摘要**：We present GSEdit, a pipeline for text-guided 3D object editing based on Gaussian Splatting models. Our method enables the editing of the style and appearance of 3D objects without altering their main details, all in a matter of minutes on consumer hardware. We tackle the problem by leveraging Gaussian splatting to represent 3D scenes, and we optimize the model while progressively varying the image supervision by means of a pretrained image-based diffusion model. The input object may be given as a 3D triangular mesh, or directly provided as Gaussians from a generative model such as DreamGaussian. GSEdit ensures consistency across different viewpoints, maintaining the integrity of the original object's information. Compared to previously proposed methods relying on NeRF-like MLP models, GSEdit stands out for its efficiency, making 3D editing tasks much faster. Our editing process is refined via the application of the SDS loss, ensuring that our edits are both ...  
- **📝翻译未启用或未翻译**  

### [9] Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis  
- **⏳发布**：2024-03-07（更新：2024-10-26）  
- **🧑‍🔬作者**：Yuanhao Cai, Yixun Liang, Jiahao Wang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.04116v3)   · [Project](https://www.youtube.com/watch?v=gDVf_Ngeghg)  
- **📝摘要**：X-ray is widely applied for transmission imaging due to its stronger penetration than natural light. When rendering novel view X-ray projections, existing methods mainly based on NeRF suffer from long training time and slow inference speed. In this paper, we propose a 3D Gaussian splatting-based framework, namely X-Gaussian, for X-ray novel view synthesis. Firstly, we redesign a radiative Gaussian point cloud model inspired by the isotropic nature of X-ray imaging. Our model excludes the influence of view direction when learning to predict the radiation intensity of 3D points. Based on this model, we develop a Differentiable Radiative Rasterization (DRR) with CUDA implementation. Secondly, we customize an Angle-pose Cuboid Uniform Initialization (ACUI) strategy that directly uses the parameters of the X-ray scanner to compute the camera information and then uniformly samples point positions within a cuboid enclosing the scanned object. Experiments show that our X-Gaussian outperforms state-of-the-art methods by 6.5 dB ...  
- **📝翻译未启用或未翻译**  

### [10] 3DGStream: On-the-Fly Training of 3D Gaussians for Efficient Streaming  of Photo-Realistic Free-Viewpoint Videos  
- **⏳发布**：2024-03-03（更新：2024-06-11）  
- **🧑‍🔬作者**：Jiakai Sun, Han Jiao, Guangyuan Li et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2403.01444v4)    
- **📝摘要**：Constructing photo-realistic Free-Viewpoint Videos (FVVs) of dynamic scenes from multi-view videos remains a challenging endeavor. Despite the remarkable advancements achieved by current neural rendering techniques, these methods generally require complete video sequences for offline training and are not capable of real-time rendering. To address these constraints, we introduce 3DGStream, a method designed for efficient FVV streaming of real-world dynamic scenes. Our method achieves fast on-the-fly per-frame reconstruction within 12 seconds and real-time rendering at 200 FPS. Specifically, we utilize 3D Gaussians (3DGs) to represent the scene. Instead of the na\"ive approach of directly optimizing 3DGs per-frame, we employ a compact Neural Transformation Cache (NTC) to model the translations and rotations of 3DGs, markedly reducing the training time and storage required for each FVV frame. Furthermore, we propose an adaptive 3DG addition strategy to handle emerging objects in dynamic scenes. Experiments demonstrate that 3DGStream achieves competitive performance in terms of rendering ...  
- **📝翻译未启用或未翻译**  


## February 2024

### [1] 4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for  Dynamic Scenes  
- **⏳发布**：2024-02-05（更新：2024-07-02）  
- **🧑‍🔬作者**：Yuanxing Duan, Fangyin Wei, Qiyu Dai et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2402.03307v3)    
- **📝摘要**：We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying scenes remain non-trivial. Prior efforts often encode dynamics by learning a canonical space plus implicit or explicit deformation fields, which struggle in challenging scenarios like sudden movements or generating high-fidelity renderings. In this paper, we introduce 4D Gaussian Splatting (4DRotorGS), a novel method that represents dynamic scenes with anisotropic 4D XYZT Gaussians, inspired by the success of 3D Gaussian Splatting in static scenes. We model dynamics at each timestamp by temporally slicing the 4D Gaussians, which naturally compose dynamic 3D Gaussians and can be seamlessly projected into images. As an explicit spatial-temporal representation, 4DRotorGS demonstrates powerful capabilities for modeling complicated dynamics and fine details--especially for scenes with abrupt motions. We further implement our temporal slicing and splatting techniques in a highly optimized ...  
- **📝翻译未启用或未翻译**  


## January 2024

### [1] Learning Segmented 3D Gaussians via Efficient Feature Unprojection for  Zero-shot Neural Scene Segmentation  
- **⏳发布**：2024-01-11（更新：2024-07-28）  
- **🧑‍🔬作者**：Bin Dou, Tianyu Zhang, Zhaohui Wang, Yongjia Ma, Zejian Yuan  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2401.05925v4)   · [Project](https://David-Dou.github.io/CoSegGaussians.)  
- **📝摘要**：Zero-shot neural scene segmentation, which reconstructs 3D neural segmentation field without manual annotations, serves as an effective way for scene understanding. However, existing models, especially the efficient 3D Gaussian-based methods, struggle to produce compact segmentation results. This issue stems primarily from their redundant learnable attributes assigned on individual Gaussians, leading to a lack of robustness against the 3D-inconsistencies in zero-shot generated raw labels. To address this problem, our work, named Compact Segmented 3D Gaussians (CoSegGaussians), proposes the Feature Unprojection and Fusion module as the segmentation field, which utilizes a shallow decoder generalizable for all Gaussians based on high-level features. Specifically, leveraging the learned Gaussian geometric parameters, semantic-aware image-based features are introduced into the scene via our unprojection technique. The lifted features, together with spatial information, are fed into the multi-scale aggregation decoder to generate segmentation identities for all Gaussians. Furthermore, we design CoSeg Loss to boost model robustness against 3D-inconsistent ...  
- **📝翻译未启用或未翻译**  


## December 2023

### [1] ASH: Animatable Gaussian Splats for Efficient and Photoreal Human  Rendering  
- **⏳发布**：2023-12-10（更新：2024-04-15）  
- **🧑‍🔬作者**：Haokai Pang, Heming Zhu, Adam Kortylewski, Christian Theobalt, Marc Habermann  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2312.05941v2)    
- **📝摘要**：Real-time rendering of photorealistic and controllable human avatars stands as a cornerstone in Computer Vision and Graphics. While recent advances in neural implicit rendering have unlocked unprecedented photorealism for digital avatars, real-time performance has mostly been demonstrated for static scenes only. To address this, we propose ASH, an animatable Gaussian splatting approach for photorealistic rendering of dynamic humans in real-time. We parameterize the clothed human as animatable 3D Gaussians, which can be efficiently splatted into image space to generate the final rendering. However, naively learning the Gaussian parameters in 3D space poses a severe challenge in terms of compute. Instead, we attach the Gaussians onto a deformable character model, and learn their parameters in 2D texture space, which allows leveraging efficient 2D convolutional architectures that easily scale with the required number of Gaussians. We benchmark ASH with competing methods on pose-controllable avatars, demonstrating that our method outperforms existing real-time methods ...  
- **📝翻译未启用或未翻译**  

### [2] EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS  
- **⏳发布**：2023-12-07（更新：2024-09-26）  
- **🧑‍🔬作者**：Sharath Girish, Kamal Gupta, Abhinav Shrivastava  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2312.04564v3)   · [Project](https://efficientgaussian.github.io)  
- **📝摘要**：Recently, 3D Gaussian splatting (3D-GS) has gained popularity in novel-view scene synthesis. It addresses the challenges of lengthy training times and slow rendering speeds associated with Neural Radiance Fields (NeRFs). Through rapid, differentiable rasterization of 3D Gaussians, 3D-GS achieves real-time rendering and accelerated training. They, however, demand substantial memory resources for both training and storage, as they require millions of Gaussians in their point cloud representation for each scene. We present a technique utilizing quantized embeddings to significantly reduce per-point memory storage requirements and a coarse-to-fine training strategy for a faster and more stable optimization of the Gaussian point clouds. Our approach develops a pruning stage which results in scene representations with fewer Gaussians, leading to faster training times and rendering speeds for real-time rendering of high resolution scenes. We reduce storage memory by more than an order of magnitude all while preserving the reconstruction quality. We validate the effectiveness ...  
- **📝翻译未启用或未翻译**  

### [3] HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian  Splatting  
- **⏳发布**：2023-12-06（更新：2023-12-07）  
- **🧑‍🔬作者**：Yuheng Jiang, Zhehao Shen, Penghao Wang et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2312.03461v2)    
- **📝摘要**：We have recently seen tremendous progress in photo-real human modeling and rendering. Yet, efficiently rendering realistic human performance and integrating it into the rasterization pipeline remains challenging. In this paper, we present HiFi4G, an explicit and compact Gaussian-based approach for high-fidelity human performance rendering from dense footage. Our core intuition is to marry the 3D Gaussian representation with non-rigid tracking, achieving a compact and compression-friendly representation. We first propose a dual-graph mechanism to obtain motion priors, with a coarse deformation graph for effective initialization and a fine-grained Gaussian graph to enforce subsequent constraints. Then, we utilize a 4D Gaussian optimization scheme with adaptive spatial-temporal regularizers to effectively balance the non-rigid prior and Gaussian updating. We also present a companion compression scheme with residual compensation for immersive experiences on various platforms. It achieves a substantial compression rate of approximately 25 times, with less than 2MB of storage per frame. Extensive experiments ...  
- **📝翻译未启用或未翻译**  


## November 2023

### [1] CompGS: Smaller and Faster Gaussian Splatting with Vector Quantization  
- **⏳发布**：2023-11-30（更新：2024-09-26）  
- **🧑‍🔬作者**：KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2311.18159v3)    
- **📝摘要**：3D Gaussian Splatting (3DGS) is a new method for modeling and rendering 3D radiance fields that achieves much faster learning and rendering time compared to SOTA NeRF methods. However, it comes with a drawback in the much larger storage demand compared to NeRF methods since it needs to store the parameters for several 3D Gaussians. We notice that many Gaussians may share similar parameters, so we introduce a simple vector quantization method based on K-means to quantize the Gaussian parameters while optimizing them. Then, we store the small codebook along with the index of the code for each Gaussian. We compress the indices further by sorting them and using a method similar to run-length encoding. Moreover, we use a simple regularizer to encourage zero opacity (invisible Gaussians) to reduce the storage and rendering time by a large factor through reducing the number of Gaussians. We do extensive experiments on standard ...  
- **📝翻译未启用或未翻译**  

### [2] LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and  200+ FPS  
- **⏳发布**：2023-11-28（更新：2024-11-12）  
- **🧑‍🔬作者**：Zhiwen Fan, Kevin Wang, Kairun Wen et al.  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2311.17245v6)    
- **📝摘要**：Recent advances in real-time neural rendering using point-based techniques have enabled broader adoption of 3D representations. However, foundational approaches like 3D Gaussian Splatting impose substantial storage overhead, as Structure-from-Motion (SfM) points can grow to millions, often requiring gigabyte-level disk space for a single unbounded scene. This growth presents scalability challenges and hinders splatting efficiency. To address this, we introduce LightGaussian, a method for transforming 3D Gaussians into a more compact format. Inspired by Network Pruning, LightGaussian identifies Gaussians with minimal global significance on scene reconstruction, and applies a pruning and recovery process to reduce redundancy while preserving visual quality. Knowledge distillation and pseudo-view augmentation then transfer spherical harmonic coefficients to a lower degree, yielding compact representations. Gaussian Vector Quantization, based on each Gaussian's global significance, further lowers bitwidth with minimal accuracy loss. LightGaussian achieves an average 15x compression rate while boosting FPS from 144 to 237 within the 3D-GS framework, ...  
- **📝翻译未启用或未翻译**  

### [3] Compact 3D Gaussian Representation for Radiance Field  
- **⏳发布**：2023-11-22（更新：2024-02-15）  
- **🧑‍🔬作者**：Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2311.13681v2)   · [Project](https://maincold2.github.io/c3dgs/.)  
- **📝摘要**：Neural Radiance Fields (NeRFs) have demonstrated remarkable potential in capturing complex 3D scenes with high fidelity. However, one persistent challenge that hinders the widespread adoption of NeRFs is the computational bottleneck due to the volumetric rendering. On the other hand, 3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussisan-based representation and adopts the rasterization pipeline to render the images rather than volumetric rendering, achieving very fast rendering speed and promising image quality. However, a significant drawback arises as 3DGS entails a substantial number of 3D Gaussians to maintain the high fidelity of the rendered images, which requires a large amount of memory and storage. To address this critical issue, we place a specific emphasis on two key objectives: reducing the number of Gaussian points without sacrificing performance and compressing the Gaussian attributes, such as view-dependent color and covariance. To this end, we propose ...  
- **📝翻译未启用或未翻译**  

### [4] SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh  Reconstruction and High-Quality Mesh Rendering  
- **⏳发布**：2023-11-21（更新：2023-12-02）  
- **🧑‍🔬作者**：Antoine Guédon, Vincent Lepetit  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2311.12775v3)   · [Project](https://anttwo.github.io/sugar/)  
- **📝摘要**：We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting. Gaussian Splatting has recently become very popular as it yields realistic rendering while being significantly faster to train than NeRFs. It is however challenging to extract a mesh from the millions of tiny 3D gaussians as these gaussians tend to be unorganized after optimization and no method has been proposed so far. Our first key contribution is a regularization term that encourages the gaussians to align well with the surface of the scene. We then introduce a method that exploits this alignment to extract a mesh from the Gaussians using Poisson reconstruction, which is fast, scalable, and preserves details, in contrast to the Marching Cubes algorithm usually applied to extract meshes from Neural SDFs. Finally, we introduce an optional refinement strategy that binds gaussians to the surface of the mesh, and jointly optimizes these ...  
- **📝翻译未启用或未翻译**  

### [5] A Compact Dynamic 3D Gaussian Representation for Real-Time Dynamic View  Synthesis  
- **⏳发布**：2023-11-21（更新：2024-07-04）  
- **🧑‍🔬作者**：Kai Katsumata, Duc Minh Vo, Hideki Nakayama  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2311.12897v2)    
- **📝摘要**：3D Gaussian Splatting (3DGS) has shown remarkable success in synthesizing novel views given multiple views of a static scene. Yet, 3DGS faces challenges when applied to dynamic scenes because 3D Gaussian parameters need to be updated per timestep, requiring a large amount of memory and at least a dozen observations per timestep. To address these limitations, we present a compact dynamic 3D Gaussian representation that models positions and rotations as functions of time with a few parameter approximations while keeping other properties of 3DGS including scale, color and opacity invariant. Our method can dramatically reduce memory usage and relax a strict multi-view assumption. In our experiments on monocular and multi-view scenarios, we show that our method not only matches state-of-the-art methods, often linked with slower rendering speeds, in terms of high rendering quality but also significantly surpasses them by achieving a rendering speed of $118$ frames per second (FPS) at ...  
- **📝翻译未启用或未翻译**  

### [6] Compressed 3D Gaussian Splatting for Accelerated Novel View Synthesis  
- **⏳发布**：2023-11-17（更新：2024-01-22）  
- **🧑‍🔬作者**：Simon Niedermayr, Josef Stumpfegger, Rüdiger Westermann  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2401.02436v2)    
- **📝摘要**：Recently, high-fidelity scene reconstruction with an optimized 3D Gaussian splat representation has been introduced for novel view synthesis from sparse image sets. Making such representations suitable for applications like network streaming and rendering on low-power devices requires significantly reduced memory consumption as well as improved rendering efficiency. We propose a compressed 3D Gaussian splat representation that utilizes sensitivity-aware vector clustering with quantization-aware training to compress directional colors and Gaussian parameters. The learned codebooks have low bitrates and achieve a compression rate of up to $31\times$ on real-world scenes with only minimal degradation of visual quality. We demonstrate that the compressed splat representation can be efficiently rendered with hardware rasterization on lightweight GPUs at up to $4\times$ higher framerates than reported via an optimized GPU compute pipeline. Extensive experiments across multiple datasets demonstrate the robustness and rendering speed of the proposed approach.  
- **📝翻译未启用或未翻译**  


## September 2023

### [1] DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content  Creation  
- **⏳发布**：2023-09-28（更新：2024-03-29）  
- **🧑‍🔬作者**：Jiaxiang Tang, Jiawei Ren, Hang Zhou, Ziwei Liu, Gang Zeng  
- **🔗链接**：[arXiv Abstract](https://arxiv.org/abs/2309.16653v2)    
- **📝摘要**：Recent advances in 3D content creation mostly leverage optimization-based 3D generation via score distillation sampling (SDS). Though promising results have been exhibited, these methods often suffer from slow per-sample optimization, limiting their practical usage. In this paper, we propose DreamGaussian, a novel 3D content generation framework that achieves both efficiency and quality simultaneously. Our key insight is to design a generative 3D Gaussian Splatting model with companioned mesh extraction and texture refinement in UV space. In contrast to the occupancy pruning used in Neural Radiance Fields, we demonstrate that the progressive densification of 3D Gaussians converges significantly faster for 3D generative tasks. To further enhance the texture quality and facilitate downstream applications, we introduce an efficient algorithm to convert 3D Gaussians into textured meshes and apply a fine-tuning stage to refine the details. Extensive experiments demonstrate the superior efficiency and competitive generation quality of our proposed approach. Notably, DreamGaussian produces ...  
- **📝翻译未启用或未翻译**  

