# Daily Muon Paper Digest

## Top Highlights

1. Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering
Authors: Xianliang Li, Zihan Zhang, Weiyang Liu, Han Bao
Link: http://arxiv.org/abs/2606.03899v2
Category: Muon Core
Paper type: Theory + Experiment
Relevance score: 19.5
Abstract: Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear. Existing analyses of Muon either remove momentum to study spectral updates in isolation, or retain momentum without explaining why it improves empirical performance. Our work bridges this gap by showing momentum in Muon acts as a spectral filter. Under a structured signal-plus-perturbation gradient model, we prove that momentum suppresses perturbations while preserving the dominant signal, thereby enlarging the spectral gap between them. This enlarged gap stabilizes the singular subspaces of the matrix passed to Muon's orthogonalization step, making the resulting update more reliable. We further show that applying momentum before orthogonalization achieves provably stronger alignment with the signal component of the gradient than either reversing this order or simply removing momentum. Experiments across diverse tasks, including LLM pretraining, support our theoretical analysis. More broadly, our theory offers a starting point for understanding the benefits of momentum in other matrix-based optimizers.

2. Spectral Scaling Laws of Muon
Authors: Gagik Magakyan, Pablo Parrilo, Asuman Ozdaglar
Link: http://arxiv.org/abs/2606.04058v1
Category: Muon Core
Paper type: Unclear
Relevance score: 18.5
Abstract: Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon. To keep these updates tractable, Muon performs the orthonormalization with the Newton--Schulz (NS) iteration. Since NS is only approximate, directions with small singular values fail to be orthonormalized. In Muon, NS is applied to the momentum matrix at every step, yet little is known about how the singular value spectrum of these momentum matrices behaves during training, or how that behavior changes with model size. We present the first systematic study of this question. Tracking singular value quantiles of the momentum buffer across layers in models ranging from 77M to 2.8B parameters, we observe a consistent picture: after a short burn-in, the quantiles stabilize at a value determined by the layer type and model size. These stabilization values follow remarkably clean power laws in model size, with layer-dependent exponents. Layers up to mid-late depth scale very mildly with model size $M$ (around $M^{-0.25}$), so the standard 5-step NS configuration used at academic scale will continue to orthonormalize them at much larger scales. Some of the late layers, however, scale much more aggressively (up to $M^{-0.96}$) and will fall into the NS failure regime at frontier scale unless one uses more NS iterations or better-tuned coefficients. NS iterations are computationally expensive at scale; our laws give practitioners a principled, layer-aware recipe for choosing the minimum NS configuration that still orthonormalizes the directions that matter -- avoiding unnecessary computation without sacrificing update quality.

3. DeMuon: A Decentralized Muon for Matrix Optimization over Graphs
Authors: Chuan He, Shuyi Ren, Jingwei Mao, Erik G. Larsson
Link: http://arxiv.org/abs/2510.01377v2
Category: Muon Core
Paper type: Theory + Experiment
Relevance score: 17.0
Abstract: In this paper, we propose DeMuon, a method for decentralized matrix optimization over a given communication topology. DeMuon incorporates matrix orthogonalization via Newton-Schulz iterations-a technique inherited from its centralized predecessor, Muon-and employs gradient tracking to mitigate heterogeneity among local functions. Under heavy-tailed noise conditions and additional mild assumptions, we establish the iteration complexity of DeMuon for reaching an approximate stochastic stationary point. This complexity result matches the best-known complexity bounds of centralized algorithms in terms of dependence on the target tolerance. To the best of our knowledge, DeMuon is the first direct extension of Muon to decentralized optimization over graphs with provable complexity guarantees. We conduct preliminary numerical experiments on decentralized transformer pretraining over graphs with varying degrees of connectivity. Our numerical results demonstrate a clear margin of improvement of DeMuon over other popular decentralized algorithms across different network topologies.

4. Why Muon Outperforms Adam: A Curvature Perspective
Authors: Shuche Wang, Fengzhuo Zhang, Jiaxiang Li, Dirk Bergemann, Zhuoran Yang
Link: http://arxiv.org/abs/2606.04662v1
Category: Muon Core
Paper type: Theory + Experiment
Relevance score: 14.0
Abstract: Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear. Our work takes a first step toward demystifying Muon's superiority over Adam from a curvature perspective. First, we apply a second-order Taylor approximation to the training landscape and show that Muon achieves a larger one-step loss decrease than Adam at matched validation loss. The two optimizers have comparable first-order gains, but Muon consistently incurs a smaller second-order curvature penalty. Second, we decompose this curvature penalty into the squared update norm and Normalized Directional Sharpness (NDS). We find that Muon and Adam have comparable update norms, so Muon's smaller curvature penalty is driven by lower NDS, not update scale. Third, we study how training data and model structure shape Muon's NDS advantage. Using Zipf-Probabilistic Context-Free Grammar (PCFG) data with controlled imbalance, we show that data imbalance amplifies Muon's NDS advantage over Adam. A within-/cross-layer decomposition further shows that, in the middle and late stages of training, Muon's lower NDS is mainly sustained by smaller within-layer curvature. Beyond empirical evidence, we analyze stylized quadratic problems with heterogeneous curvature and gradient alignment toward high-curvature modes. We prove that Muon attains a smaller average NDS than GD by balancing update energy across curvature groups; when curvature heterogeneity is sufficiently strong, this also yields lower local quadratic loss after the same number of steps.

5. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training
Authors: Senmiao Wang, Tiantian Fang, Haoran Zhang, Yushun Zhang, Kunxiang Zhao, Alex Schwing
Link: http://arxiv.org/abs/2606.06470v1
Category: Muon Core
Paper type: Theory
Relevance score: 10.0
Abstract: We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-training, for both the AdamW and Muon optimizers. Theoretically, we justify this spectrum-control principle by proving that uniformly bounding each layer's singular values ensures geometric convergence of gradient descent to global minima, for certain deep linear networks. Our code is available at https://github.com/Empath-aln/PC-layer.

## Additional Papers

6. HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning | Muon-Adjacent Experiments | Experiment | Score: 7.0 | http://arxiv.org/abs/2606.06100v1
7. Multi-ResNets for Subspace Preconditioning in Constrained Optimization | Muon-Adjacent Experiments | Experiment | Score: 6.5 | http://arxiv.org/abs/2606.06300v1
8. Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss | Not Relevant | Unclear | Score: 10.0 | http://arxiv.org/abs/2606.06418v1
9. ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents | Not Relevant | Experiment | Score: 7.0 | http://arxiv.org/abs/2606.06284v1
10. Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability | Not Relevant | Experiment | Score: 6.5 | http://arxiv.org/abs/2606.06333v1
