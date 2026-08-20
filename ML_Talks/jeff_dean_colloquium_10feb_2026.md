# [Distingushed Colloquium : Jeff Dean, Feb 10, 2026](https://www.youtube.com/watch?v=UTTeXZrpMR0&t=2490s)

## Some observations
* In recent years, ML has completely changed our expectations of what is possible with computers.
* Increasing scale (compute, data, model size) delivers better results
* Algorithmic and model architecure improvements have provided massive improvements as well
* The kinds of computations we want to run and the hardware on which we run them is changing dramatically

## Silent data corruption (SDC)
*[Cores that don't count](https://storage.googleapis.com/gweb-research2023-media/pubtools/6169.pdf)
* At large scale, all chips/machines/network cards/cables etc. don't always work as designed
* Non-deterministically produce incorrect results, silently (sometimes related to dynamic conditions like temperature)
* Challenging problem when running largely independent computation
* Multiplicatively worse at scale with synchronous stochastic gradient descent
* Can quickly spread results across thousands of components across ML supercomputer
* Metrics anamoly: anamoly due to SDC. Anamoly with no SDC
* Pathways Cotroller transparently handles SDC


### Neural Nets and Gradient Descent Key Building Blocks for AI
* Key building block: backpropagation of errors (using chain rule) gives effective algorithm for updating the weights of a neural network to minimize errors on training data
* Backpropagation of errors gives an algorithm for how to update the weights of the whole neural network based on errors observed at the outputs of the model

#### 1990
* CSci 5299 UnderGrad Honors Senior Thesis: Parallel Implementation of Neural Network TrainingL Two Back-Propagation Approaches Jeff Dean ID #1321294
* May be we just needed to use 32 computers instead of 1 to train really impressive neural networks!

### Fifteen Years of Machine Learning Advances or How Did Today's Models Come To Be?

#### 2012
* [Large Scale Distributed Deep Networks](https://papers.nips.cc/paper_files/paper/2012/file/6aca97005c68f1206823815f66102863-Paper.pdf)
*   Combining model parallelism and data parallelism for neural network training across thousands of computers enables training of much larger (50-100X) neural networks than previously possible
* Scale Matters [Building High-level Features Using Large Scale Unsupervised Learning](https://ai.stanford.edu/~ang/papers/icml12-HighLevelFeaturesUsingUnsupervisedLearning.pdf)
*   When trained completely unsupervised on 10M randomYouTube frames, one of the neurons at the higher layers of the model learned to detect cats
*   Visualization of the optimalstimulus for this neuron
*   Training a very large neural network (60X bigger than previous largest neural network) using 16,000 CPU cores gave major advances in quality (combining ideas from my undergrad thesis!)
*   (~70% relative improvement in ImageNet 22K state-of-the-art)
#### 2013
* [Word2Vec: Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/pdf/1310.4546)
*   Nearby words in high dimensional space are related. cat, puma, tiger, are all nearby
*   Directions are meaningful. king - queen ~= man- woman
* The Back-of-the-Envelope Origin of TPUs
*   Acoustic Modeling for Speech Recognition
*   Current best model: 8 layers x 2560 units per layer
*   ~100M multiply/adds per 10ms of speech inference
*   Scenario: 3 mins of speech per user per day?
*   1 billion users x 3 mins/day x 100M ops/10ms
*   = 1,800,000,000,000,000,000,000 ops/day assume 1B ops/sec/core: ~20M core days / day
*   with traditional hardware need to ~double the compute footprint
#### 2014
* Models that Map One Sequence to Another are Powerful
* [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215)
*   Using a neural encoder over an input sequence to generate state, use that to initialize state of a neural decoder. Scale up LSTMs and this works.
* Distillation: Use Powerful "Teacher" Models to Make Smaller, Cheaper "Student" Models
* [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) Distillation: Use large hgh quality model as "teacher" when training smaller "student" model
* Gives much richer signal for training: try to get student to match "soft probability distribution" of large model
* 

#### 2015
* [TPUv1 for Neural Network Inference](https://arxiv.org/pdf/1704.04760), 92 Teraops is 15x-30x faster and 30x-80x more energy efficient
* reduced precision ok ~1.2 * ~0.6 = ~0.7, handful of specific operations
* Specialization is much more efficient: Compared to contemporary CPUs & GPUs

#### 2016
* Specialized TPU Supercomputers for Neural Network Training
* Connect thounds of chips together (TPU pods) with custom high-speed networks to enable faster neural network training
* [TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings](https://arxiv.org/pdf/2304.01433)
* [Continual Hardware Performance Scaling](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)
* ~3600X peak performance per pod vs. TPU v2
* ~30X energy efficiency improvement vs. TPU v2
* Open Source tools enable the whole community - TensorFlow, PyTorch, JAX

#### 2017
* [Transformer Model Architecture: Attention Is All You Need](https://arxiv.org/pdf/1706.03762)
* Don't try to force state into single recurrent distributed representation. Instead, save all past representations and attend to them.
* Higher accuracy w/10x-100x less compute and 10x smaller models! - [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361)
* Sparse Models (e.g. Mixture of Experts) Outperform Dense Models
* [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/pdf/1701.06538)
* Give model much larger capacity w/lots of experts but only activate a few chosen experts per token: (A) ~8x reduction in training compute cost for ~same accuracy, or (B) major accuracy improvements for same training compute cost
* Continued Research on Sparse Models - Gemini 1.5 Pro, Gemini 2.0 / Gemini 2.5 use MoE architectures, building on a long line of Google research efforts on sparse models
* [2020 GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding](https://arxiv.org/abs/2006.16668)
* [2021 Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974)
* [2021 Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)
* [2022 Unified Scaling Laws for Routed Language Models](https://arxiv.org/abs/2202.01169)
* [2022 Designing Effective Sparse Expert Models](https://ieeexplore.ieee.org/document/9835248)
* [2023 From Sparse to Soft Mixtures of Experts](https://arxiv.org/abs/2308.00951)
* [2024 Mixtures of Experts Unlock Parameter Scaling for Deep RL](https://arxiv.org/pdf/2402.08609)
* [2024 Mixture-of-Depths: Dynamically allocating compute in transformer-based language models](https://arxiv.org/abs/2404.02258)
* [2024 DiPaCo: Distributed Path Composition](https://arxiv.org/abs/2403.10616)

#### 2018
* Language Modeling At Scale With Self-Supervised Data
* There's lots of text in the world! Self-supervised learning on text can provide very large amounts of training data with the "right" answer known ("wrong guess" is used to provide gradient descent loss training signal.
* Self-supervised learning on text with large models is one of the major reasons chat/language models have gotten so good
* Fill-in-the-Blank (e.g. look in both directions, BERT)
* [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805)
* Different kinds of training objectives: Autoregressive (look at prefix, predict next word)
* [Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165)
* [Pathways: Asynchronous Distributed Dataflow for ML](https://arxiv.org/pdf/2203.12533) - Scalable software can simplify running large-scale computations - with JAX + Pathways,entire training process driven by a single Python process on one host

#### 2022:
* Thinking longer at inference time is very useful 
* [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) - Prompting model to "show its work" improves accuracy on reasoning tasks dramatically

#### 2021-Present
* Reinforcement Learning for Post-Training - improve the capabilities of the model in many domains
* Given pre-trained model, use RL for several purposes:
* Encourage behaviors that are desired in the model's responses - style, length of responses. Safety properties (don't engage in some kinds of topics)
* Enhance capabilities by showing the model hwo to tackle more complex problems
* Key question: where does the reward signal come from?
* Reward signal can come from many sources
* RLHF: Use human-feedback to generate positive and negative rewards
* RLMF: use machine-feedback from another model (often called a reward model). Prompt: "Please say whether you prefer response <A> or <B> for question <Q>"
* RL in verifiable domains like math or coding
* Generate proofs or mathematical solutions which can be checked with a theorem prover or another auomated system: give positive reward when it reasons correctly
* Generate code to tackle various coding or software engineering problems, and then execute code in sandbox enviroment, give positive reward when code compiles and passes tests of correctness, negative reward otherwise
* These dramatically improve the capabilities of the model many domains (especially in verifiable domains like math or coding)
* Open research question: how can we improve effectiveness of RL in non-verifiable domains?

#### 2023: Speculative Decoding for Faster, More efficient Inference
* Enables faster decoding from autoregressive models: 2X-3X in typical scenarios.
* Change only the decoding algorithm: no architecture changes, no re-training.
* No tradeiff: guaranteed identical output distribution
* [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/pdf/2211.17192)
* Observation 1: Decoding from large Transformers is memory bound: Hardware can do: XXX FPOPs per byte read and Tranformers need X FPOPs per byte read
* Observation 2: Some tokens are easier to predict than others, example: Can you tell me what is sqrt of 7? Sure, the sqrt of 7(easier) is 2.646 (harder)
* Idea (inspired by speculative execution): a fast drafter model quickly generates next several tokens and the target model checks them in parallel

#### Innovations at Many Levels
* Inference algorithms: Chain-of-Thought, Speculative Decoding, Inference-time compute scaling
* Training algorithms: Unsupervised and self-supervised learning, asynchronous training, Distillation, SFT + RLxF
* Model architecture: Word2Vec, Seq2Seq, Transformers, MoEs, Visual Transformers
* Software abstractions: DistBelief, TensforFlow, PyTorch, JAX, Pathways
* Hardware: TPUv1 -> TPUv2 -> TPUv3 -> TPUv4 -> TPUv5p -> Trillium -> Ironwood

#### Gemini: Building the World's Most Advanced Models
* Project started in Deb 2023
* Goal: Train the world's 

  

