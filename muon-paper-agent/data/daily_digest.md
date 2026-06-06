# Daily Muon Paper Digest

## Top Highlights

1. Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering
Authors: Xianliang Li, Zihan Zhang, Weiyang Liu, Han Bao
Link: http://arxiv.org/abs/2606.03899v2
Category: Spectral Norm / Low-rank Geometry
Paper type: Theory + Experiment
Relevance score: 15.5
Abstract: Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear. Existing analyses of Muon either remove momentum to study spectral updates in isolation, or retain momentum without explaining why it improves empirical performance. Our work bridges this gap by showing momentum in Muon acts as a spectral filter. Under a structured signal-plus-perturbation gradient model, we prove that momentum suppresses perturbations while preserving the dominant signal, thereby enlarging the spectral gap between them. This enlarged gap stabilizes the singular subspaces of the matrix passed to Muon's orthogonalization step, making the resulting update more reliable. We further show that applying momentum before orthogonalization achieves provably stronger alignment with the signal component of the gradient than either reversing this order or simply removing momentum. Experiments across diverse tasks, including LLM pretraining, support our theoretical analysis. More broadly, our theory offers a starting point for understanding the benefits of momentum in other matrix-based optimizers.
One-sentence summary: Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear.
Why it matters for Muon: This looks relevant because it falls under spectral norm / low-rank geometry and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, orthogonalization_match, spectral_norm_match, llm_training_stability_match
Recommended action: Must read
Potential use in my work: Experiment

2. Spectral Scaling Laws of Muon
Authors: Gagik Magakyan, Pablo Parrilo, Asuman Ozdaglar
Link: http://arxiv.org/abs/2606.04058v1
Category: Spectral Norm / Low-rank Geometry
Paper type: Unclear
Relevance score: 14.5
Abstract: Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon. To keep these updates tractable, Muon performs the orthonormalization with the Newton--Schulz (NS) iteration. Since NS is only approximate, directions with small singular values fail to be orthonormalized. In Muon, NS is applied to the momentum matrix at every step, yet little is known about how the singular value spectrum of these momentum matrices behaves during training, or how that behavior changes with model size. We present the first systematic study of this question. Tracking singular value quantiles of the momentum buffer across layers in models ranging from 77M to 2.8B parameters, we observe a consistent picture: after a short burn-in, the quantiles stabilize at a value determined by the layer type and model size. These stabilization values follow remarkably clean power laws in model size, with layer-dependent exponents. Layers up to mid-late depth scale very mildly with model size $M$ (around $M^{-0.25}$), so the standard 5-step NS configuration used at academic scale will continue to orthonormalize them at much larger scales. Some of the late layers, however, scale much more aggressively (up to $M^{-0.96}$) and will fall into the NS failure regime at frontier scale unless one uses more NS iterations or better-tuned coefficients. NS iterations are computationally expensive at scale; our laws give practitioners a principled, layer-aware recipe for choosing the minimum NS configuration that still orthonormalizes the directions that matter -- avoiding unnecessary computation without sacrificing update quality.
One-sentence summary: Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon.
Why it matters for Muon: This looks relevant because it falls under spectral norm / low-rank geometry and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, spectral_norm_match, llm_training_stability_match, second_order_match
Recommended action: Must read
Potential use in my work: Future work

3. DeMuon: A Decentralized Muon for Matrix Optimization over Graphs
Authors: Chuan He, Shuyi Ren, Jingwei Mao, Erik G. Larsson
Link: http://arxiv.org/abs/2510.01377v2
Category: Orthogonalized Updates / Newton-Schulz
Paper type: Theory + Experiment
Relevance score: 13.0
Abstract: In this paper, we propose DeMuon, a method for decentralized matrix optimization over a given communication topology. DeMuon incorporates matrix orthogonalization via Newton-Schulz iterations-a technique inherited from its centralized predecessor, Muon-and employs gradient tracking to mitigate heterogeneity among local functions. Under heavy-tailed noise conditions and additional mild assumptions, we establish the iteration complexity of DeMuon for reaching an approximate stochastic stationary point. This complexity result matches the best-known complexity bounds of centralized algorithms in terms of dependence on the target tolerance. To the best of our knowledge, DeMuon is the first direct extension of Muon to decentralized optimization over graphs with provable complexity guarantees. We conduct preliminary numerical experiments on decentralized transformer pretraining over graphs with varying degrees of connectivity. Our numerical results demonstrate a clear margin of improvement of DeMuon over other popular decentralized algorithms across different network topologies.
One-sentence summary: In this paper, we propose DeMuon, a method for decentralized matrix optimization over a given communication topology.
Why it matters for Muon: This looks relevant because it falls under orthogonalized updates / newton-schulz and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, orthogonalization_match, second_order_match
Recommended action: Must read
Potential use in my work: Experiment

## Full Top 10

1. Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering
Authors: Xianliang Li, Zihan Zhang, Weiyang Liu, Han Bao
Link: http://arxiv.org/abs/2606.03899v2
Category: Spectral Norm / Low-rank Geometry
Paper type: Theory + Experiment
Relevance score: 15.5
Abstract: Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear. Existing analyses of Muon either remove momentum to study spectral updates in isolation, or retain momentum without explaining why it improves empirical performance. Our work bridges this gap by showing momentum in Muon acts as a spectral filter. Under a structured signal-plus-perturbation gradient model, we prove that momentum suppresses perturbations while preserving the dominant signal, thereby enlarging the spectral gap between them. This enlarged gap stabilizes the singular subspaces of the matrix passed to Muon's orthogonalization step, making the resulting update more reliable. We further show that applying momentum before orthogonalization achieves provably stronger alignment with the signal component of the gradient than either reversing this order or simply removing momentum. Experiments across diverse tasks, including LLM pretraining, support our theoretical analysis. More broadly, our theory offers a starting point for understanding the benefits of momentum in other matrix-based optimizers.
One-sentence summary: Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear.
Why it matters for Muon: This looks relevant because it falls under spectral norm / low-rank geometry and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, orthogonalization_match, spectral_norm_match, llm_training_stability_match
Recommended action: Must read
Potential use in my work: Experiment

2. Spectral Scaling Laws of Muon
Authors: Gagik Magakyan, Pablo Parrilo, Asuman Ozdaglar
Link: http://arxiv.org/abs/2606.04058v1
Category: Spectral Norm / Low-rank Geometry
Paper type: Unclear
Relevance score: 14.5
Abstract: Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon. To keep these updates tractable, Muon performs the orthonormalization with the Newton--Schulz (NS) iteration. Since NS is only approximate, directions with small singular values fail to be orthonormalized. In Muon, NS is applied to the momentum matrix at every step, yet little is known about how the singular value spectrum of these momentum matrices behaves during training, or how that behavior changes with model size. We present the first systematic study of this question. Tracking singular value quantiles of the momentum buffer across layers in models ranging from 77M to 2.8B parameters, we observe a consistent picture: after a short burn-in, the quantiles stabilize at a value determined by the layer type and model size. These stabilization values follow remarkably clean power laws in model size, with layer-dependent exponents. Layers up to mid-late depth scale very mildly with model size $M$ (around $M^{-0.25}$), so the standard 5-step NS configuration used at academic scale will continue to orthonormalize them at much larger scales. Some of the late layers, however, scale much more aggressively (up to $M^{-0.96}$) and will fall into the NS failure regime at frontier scale unless one uses more NS iterations or better-tuned coefficients. NS iterations are computationally expensive at scale; our laws give practitioners a principled, layer-aware recipe for choosing the minimum NS configuration that still orthonormalizes the directions that matter -- avoiding unnecessary computation without sacrificing update quality.
One-sentence summary: Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon.
Why it matters for Muon: This looks relevant because it falls under spectral norm / low-rank geometry and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, spectral_norm_match, llm_training_stability_match, second_order_match
Recommended action: Must read
Potential use in my work: Future work

3. DeMuon: A Decentralized Muon for Matrix Optimization over Graphs
Authors: Chuan He, Shuyi Ren, Jingwei Mao, Erik G. Larsson
Link: http://arxiv.org/abs/2510.01377v2
Category: Orthogonalized Updates / Newton-Schulz
Paper type: Theory + Experiment
Relevance score: 13.0
Abstract: In this paper, we propose DeMuon, a method for decentralized matrix optimization over a given communication topology. DeMuon incorporates matrix orthogonalization via Newton-Schulz iterations-a technique inherited from its centralized predecessor, Muon-and employs gradient tracking to mitigate heterogeneity among local functions. Under heavy-tailed noise conditions and additional mild assumptions, we establish the iteration complexity of DeMuon for reaching an approximate stochastic stationary point. This complexity result matches the best-known complexity bounds of centralized algorithms in terms of dependence on the target tolerance. To the best of our knowledge, DeMuon is the first direct extension of Muon to decentralized optimization over graphs with provable complexity guarantees. We conduct preliminary numerical experiments on decentralized transformer pretraining over graphs with varying degrees of connectivity. Our numerical results demonstrate a clear margin of improvement of DeMuon over other popular decentralized algorithms across different network topologies.
One-sentence summary: In this paper, we propose DeMuon, a method for decentralized matrix optimization over a given communication topology.
Why it matters for Muon: This looks relevant because it falls under orthogonalized updates / newton-schulz and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, orthogonalization_match, second_order_match
Recommended action: Must read
Potential use in my work: Experiment

4. Why Muon Outperforms Adam: A Curvature Perspective
Authors: Shuche Wang, Fengzhuo Zhang, Jiaxiang Li, Dirk Bergemann, Zhuoran Yang
Link: http://arxiv.org/abs/2606.04662v1
Category: Matrix Preconditioning / Shampoo / Second-order
Paper type: Theory + Experiment
Relevance score: 10.0
Abstract: Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear. Our work takes a first step toward demystifying Muon's superiority over Adam from a curvature perspective. First, we apply a second-order Taylor approximation to the training landscape and show that Muon achieves a larger one-step loss decrease than Adam at matched validation loss. The two optimizers have comparable first-order gains, but Muon consistently incurs a smaller second-order curvature penalty. Second, we decompose this curvature penalty into the squared update norm and Normalized Directional Sharpness (NDS). We find that Muon and Adam have comparable update norms, so Muon's smaller curvature penalty is driven by lower NDS, not update scale. Third, we study how training data and model structure shape Muon's NDS advantage. Using Zipf-Probabilistic Context-Free Grammar (PCFG) data with controlled imbalance, we show that data imbalance amplifies Muon's NDS advantage over Adam. A within-/cross-layer decomposition further shows that, in the middle and late stages of training, Muon's lower NDS is mainly sustained by smaller within-layer curvature. Beyond empirical evidence, we analyze stylized quadratic problems with heterogeneous curvature and gradient alignment toward high-curvature modes. We prove that Muon attains a smaller average NDS than GD by balancing update energy across curvature groups; when curvature heterogeneity is sufficiently strong, this also yields lower local quadratic loss after the same number of steps.
One-sentence summary: Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear.
Why it matters for Muon: This looks relevant because it falls under matrix preconditioning / shampoo / second-order and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: direct_muon_match, optimizer_match, second_order_match
Recommended action: Must read
Potential use in my work: Future work

5. HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning
Authors: Moshiur Farazi, Sameera Ramasinghe, Mahbub Ahmed Turza, Shafin Rahman
Link: http://arxiv.org/abs/2606.06100v1
Category: LLM Training Stability / Attention / QK-clip
Paper type: Experiment
Relevance score: 7.0
Abstract: Vision-Language Models (VLMs) struggle with compositional reasoning that requires understanding inter-object relationships. A natural remedy is to inject explicit scene graph triplets $\langle s, p, o \rangle$ from an off-the-shelf scene graph generator (SGG), but we show this backfires: discrete text labels collide with the continuous visual modality, degrading GQA accuracy from 60.38\% to 58.86\%. We propose \textbf{HyperVis}, which bypasses the SGG semantic bottleneck entirely. From $N$ class-agnostic region proposals, we compute a dense $O(N^2)$ visual relation tensor via spatially-biased cross-attention, project it onto a Lorentz hyperboloid, and enforce hierarchy through spatial physics, namely IoA-driven entailment cones and exterior-angle repulsion. We discover that HyperVis contributes in two complementary ways: (1) as a \emph{training-time regularizer}, the hyperbolic relational losses shape LoRA representations that improve generative VQA (GQA 61.03\% vs.\ 57.21\% for LoRA fine-tuning without relational losses, recovering and surpassing the baseline); and (2) as an \emph{inference-time relational encoder}, hyperbolic prefix tokens boost discriminative compositional scoring (SugarCrepe 79.94\%, $+$6.25pp over baseline). The learned curvature stabilises at $κ{=}4.0$, an order of magnitude above prior hyperbolic VLMs where $κ$ typically collapses toward zero, indicating that continuous visual features genuinely require the exponential volume of strongly curved space. A controlled Euclidean ablation confirms this decomposition: the relational pipeline regularises LoRA comparably in flat space (GQA 60.81\%), but the compositionality gain is specifically hyperbolic (SugarCrepe $+$4.58pp over Euclidean), with entailment loss ${\sim}6{\times}$ higher in Euclidean training. Codes are available at TBA.
One-sentence summary: Vision-Language Models (VLMs) struggle with compositional reasoning that requires understanding inter-object relationships.
Why it matters for Muon: This looks relevant because it falls under llm training stability / attention / qk-clip and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: optimizer_match, llm_training_stability_match, second_order_match
Recommended action: Skim
Potential use in my work: Future work

6. Dead Directions: Geometric Singular Learning
Authors: Tejas Pradeep Shirodkar
Link: http://arxiv.org/abs/2606.05957v1
Category: LLM Training Stability / Attention / QK-clip
Paper type: Theory
Relevance score: 6.5
Abstract: Singular learning theory and information geometry have studied the same parameter spaces in mostly separate vocabularies: the former computes Bayesian invariants in resolved coordinates, the latter works in original coordinates under a non-degeneracy assumption that overparameterised models routinely violate. We bridge them through one primitive, the dead direction: a unit vector along which the Fisher metric degenerates, equivalently a tangent to the analytic singular set with a definite KL order, set by how fast the KL divergence vanishes. The two readings name the same vector; our central move shows its KL order is recoverable as the decay rate of the directional Fisher curvature approaching the singularity, in original parameter coordinates and without a Hironaka resolution. A selection rule on smooth fibres translates this rate into Watanabe's single-direction contribution to the real log canonical threshold, and we extend the recovery to multi-component crossings, multiplicity $m$, the singular fluctuation $ν$ (universal in the KL order for 1D directions), prior-RLCT shifts, and tempered posteriors. We then lift this rate to a deep network: a multi-layer K-FAC factorisation writes each Fisher block as a product of activation- and gradient-side rates with a duality between them, instantiated at modern-network primitives (residual streams, layer normalisation, attention). A quotient theorem carries the rate to the gauge quotient $Θ/G$ under gradient flow on a $G$-invariant metric; SGD qualifies, standard Adam does not, and we construct a $G$-equivariant Adam-family preconditioner (DDCAdam) that does. The bridge yields a parameter-coordinate handle on singular geometry, closed-form per-architecture predictions, and a trajectory-rate readout of Watanabe's triple $(λ, m, ν)$ from one checkpoint's forward and backward passes, without posterior sampling.
One-sentence summary: Singular learning theory and information geometry have studied the same parameter spaces in mostly separate vocabularies: the former computes Bayesian invariants in resolved coordinates, the latter works in original coordinates under a non-degeneracy assumption that overparameterised models routinely violate.
Why it matters for Muon: This looks relevant because it falls under llm training stability / attention / qk-clip and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: llm_training_stability_match, second_order_match, low_rank_geometry_match
Recommended action: Skim
Potential use in my work: Proof idea

7. TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion
Authors: Peizhuo Li, Hongyi Li, Mingfeng Fan, Fangzhou Xu, Shuhao Liao, Yuxuan Ma
Link: http://arxiv.org/abs/2606.05880v1
Category: LLM Training Stability / Attention / QK-clip
Paper type: Experiment
Relevance score: 6.5
Abstract: Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce TAGA, a Terrain-aware Active Gaze learning framework for Attention-based humanoid control. By fusing vision, proprioception, and motion commands, our framework guides the model to learn anticipatory cues and actively attend to specific areas of the height scan, selectively using these informative regions for the downstream network. This adaptively increases the information density of observations under tight onboard computational constraints, thus enabling fine-grained perceptive locomotion over larger-scale terrains. We find that such gaze behaviors can naturally emerge through reinforcement learning alone, without requiring additional supervision or explicit guidance, significantly improve training efficiency. As a result, the trained policy demonstrates robust and generalizable locomotion in simulation and on hardware, including reliable terrain-aware foothold selection, elevated-platform traversal, competitive sparse-foothold traversal, and the largest reported real-world gap traversal distance of 1.2m among perceptive humanoid locomotion systems, while maintaining stability under severe perceptual disturbances and environmental interference.
One-sentence summary: Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding.
Why it matters for Muon: This looks relevant because it falls under llm training stability / attention / qk-clip and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: optimizer_match, llm_training_stability_match, low_rank_geometry_match
Recommended action: Skim
Potential use in my work: Future work

8. Rethinking Bregman Divergences in Kronecker-Factored Optimizers
Authors: Bing Liu, Wenjie Zhou, Chengcheng Zhao
Link: http://arxiv.org/abs/2606.00542v2
Category: Matrix Preconditioning / Shampoo / Second-order
Paper type: Experiment
Relevance score: 6.5
Abstract: Shampoo-style optimizers approximate gradient covariance matrices using Kronecker-factored structures. Recent work~\cite{lin2026understanding} showed that such approximations can be viewed as projections under Bregman matrix divergences, leading to different Kronecker-factored preconditioners. However, it remains unclear what role the choice of divergence plays when the covariance is not exactly Kronecker-factored. We study this question through the spectrum of the covariance matrix. We show that Frobenius, von Neumann, and LogDet divergences distribute the unavoidable Kronecker approximation error differently across the covariance spectrum. We further show that their Kronecker factors are governed by divergence-weighted residuals rather than the raw approximation error, explaining how these spectral preferences are realized in the resulting preconditioners. Empirically, we observe that the top covariance eigenspace is substantially better aligned with the Hessian matrix, while the tail spectrum is much noisier and unreliable. Motivated by these findings, we propose a subspace-aware Kronecker optimizer that applies eigenvalue-based preconditioning in the top subspace and uses an adaptive isotropic acceleration constant in the bottom subspace.
One-sentence summary: Shampoo-style optimizers approximate gradient covariance matrices using Kronecker-factored structures.
Why it matters for Muon: This looks relevant because it falls under matrix preconditioning / shampoo / second-order and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: optimizer_match, spectral_norm_match, second_order_match
Recommended action: Skim
Potential use in my work: Future work

9. Introduction to optimization methods for training SciML models
Authors: Alena Kopaničáková, Elisa Riccietti
Link: http://arxiv.org/abs/2601.10222v2
Category: Matrix Preconditioning / Shampoo / Second-order
Paper type: Unclear
Relevance score: 6.5
Abstract: Optimization is central to both modern machine learning (ML) and scientific machine learning (SciML), yet the structure of the underlying optimization problems differs substantially across these domains. Classical ML typically relies on stochastic, sample-separable objectives that favor first-order and adaptive gradient methods. In contrast, SciML often involves physics-informed or operator-constrained formulations in which differential operators induce global coupling, stiffness, and strong anisotropy in the loss landscape. As a result, optimization behavior in SciML is governed by the spectral properties of the underlying physical models rather than by data statistics, frequently limiting the effectiveness of standard stochastic methods and motivating deterministic or curvature-aware approaches. This document provides a unified introduction to optimization methods in ML and SciML, emphasizing how problem structure shapes algorithmic choices. We review first- and second-order optimization techniques in both deterministic and stochastic settings, discuss their adaptation to physics-constrained and data-driven SciML models, and illustrate practical strategies through tutorial examples, while highlighting open research directions at the interface of scientific computing and scientific machine learning.
One-sentence summary: Optimization is central to both modern machine learning (ML) and scientific machine learning (SciML), yet the structure of the underlying optimization problems differs substantially across these domains.
Why it matters for Muon: This looks relevant because it falls under matrix preconditioning / shampoo / second-order and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: optimizer_match, spectral_norm_match, second_order_match
Recommended action: Skim
Potential use in my work: Future work

10. EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs
Authors: Sungwon Kim, Juho Song, Seungmin Shin, Guimok Cho, Sangkook Kim, Chanyoung Park
Link: http://arxiv.org/abs/2606.03260v1
Category: Spectral Norm / Low-rank Geometry
Paper type: Unclear
Relevance score: 6.0
Abstract: Deep learning surrogates for 3D Partial Differential Equations (PDEs) often fail to generalize across geometric transformations because they depend heavily on specific coordinate systems. While equivariant networks offer a solution, they typically rely on local operations in the spatial domain, making the global receptive field, which is essential for PDE dynamics, computationally expensive. Conversely, Fourier Neural Operators (FNOs) efficiently capture global interactions, yet establishing 3D equivariance within them remains impractical due to the prohibitive cost of spectral group convolutions. To bridge this gap, we introduce EqGINO, a geometrically robust framework that enforces isotropy in the spectral domain. By design, EqGINO guarantees exact equivariance to the discrete symmetries inherent to the discretized computational domain. Beyond this discrete guarantee, our structural prior enables effective generalization to arbitrary continuous orientations even with a limited number of SE(3)-transformed training samples. Consequently, our method robustly models coordinate-invariant physical laws on complex irregular 3D geometries. Our code is available at https://github.com/sung-won-kim/EqGINO
One-sentence summary: Deep learning surrogates for 3D Partial Differential Equations (PDEs) often fail to generalize across geometric transformations because they depend heavily on specific coordinate systems.
Why it matters for Muon: This looks relevant because it falls under spectral norm / low-rank geometry and matched several Muon-adjacent ranking signals.
Technical notes: Matched signals: optimizer_match, spectral_norm_match, low_rank_geometry_match
Recommended action: Skim
Potential use in my work: Future work
