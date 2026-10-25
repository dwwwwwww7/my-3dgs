# ICASSP 2027

> **最后更新**： 2026-10-25 03:15:39

本页面包含 2027 年 ICASSP 会议的论文列表。

## 1. TSGL: Teacher-Student Graph Learning for 3DGS Compression

- **作者**: Matin Bani Saedi, Matthew Kyan, Gene Cheung
- **发布时间**: 2026-09-29
- **arXiv链接**: [arXiv:2609.38635v1](https://arxiv.org/abs/2609.38635v1)
- **说明**: 5 pages, 2 figures. Submitted to IEEE ICASSP 2027
- **英文摘要**: 3D Gaussian Splatting (3DGS) is a popular representation for novel view synthesis. However, 3DGS contains millions of Gaussian primitives, each with rich attributes, resulting in large file sizes. We propose a novel 3DGS compression method based on Teacher-Student Graph Learning (TSGL) that operates directly on a trained model, without 3DGS retraining or access to training images. Specifically, for each block of Gaussian primitives, using decoded positions and DC spherical harmonic (SH) coefficients as predictors, we learn a signal-dependent geometry graph G encoding the pairwise similarities between neighbouring Gaussians via a teacher-student model. Given G, we perform Graph Fourier Transform (GFT) on the remaining attributes, so that signal energies are predominantly projected into the low-frequency coefficients for compact representation. On three standard benchmarks, the method reaches 27x to 33x compression with less than 0.6 dB of PSNR loss, improving on recent post-training compression methods in both size and rendering quality.

---

## 2. Robust, Estimator-Agnostic Dynamic 3DGS Compression

- **作者**: Chenjunjie Wang, Zixi Huang, Yao Wang, Jona Ballé
- **发布时间**: 2026-09-22
- **arXiv链接**: [arXiv:2609.25633v1](https://arxiv.org/abs/2609.25633v1)
- **说明**: Submitted to IEEE ICASSP 2027. This version adds an appendix; 16 pages, 15 figures
- **英文摘要**: Dynamic 3D Gaussian splats (3DGS) model time-varying scenes using a separate Gaussian set per frame. While neighboring video frames are highly correlated due to smooth motion, Gaussian representations retain this correlation to varying degrees, depending on whether the estimator tracks them across time. Some 3DGS compression methods integrate the estimation to exploit temporal redundancy; here, we focus on robust compression regardless of the estimator. We concatenate groups of frames into one Gaussian set, augment each Gaussian with a frame index, and pass it to a static (i.e., non-temporal) 3DGS codec, converting temporal redundancy into spatial redundancy. Concatenated sets are spatially partitioned to limit memory. Our technique requires neither a motion model nor knowledge of the training method. Averaged over six N3DV sequences, all six static codecs achieve gains on tracked sets (-42.0% to -71.8% BD-rate) over per-frame coding. On untracked sets, all codecs except HGSC, which appears incompatible with our technique, remain competitive with per-frame coding (-3.5% to +5.0%). We further replace D-FCGS's I-frame coding with our technique while retaining its P-frame coding, yielding an overall BD-rate of -46.2%. We propose to visualize "trackedness" using an inter-frame similarity metric. The project is available at https://wcjj1236.github.io/d3dgs-benchmark.

---

