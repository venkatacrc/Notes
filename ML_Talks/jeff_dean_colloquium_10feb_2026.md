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
* RLMF: use machine-feedback from another model (often called a reward model). Prompt: Please say whether you prefer response A or B for question Q
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
* Goal: Train the world's best multimodal models and use them all across Google
* Gemini 1.0 Dec 2023
* Gemini 1.5 Feb 2024 (demonstrated 10M token context window, Flash model)
* Gemini 2.0 Dec 2024 (2.0 Flash as good as 1.5 Pro, multimodal live steaming, ...)
* Gemini 2.0 Thinking: Jan 2025 (2.0 Flash Experimental Thinking)
* Gemini 2.5 Mar 2025 (2.5 Pro released), Apr 2025 (2.5 Flash), Aug 2025 (2.5 Pro Deep Think)
* Gemini 3.0 (3 Pro released)
* [Introducing Gemini: our largest and most capable AI model](https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/)
* [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/pdf/2312.11805)
* [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/pdf/2403.05530) - Increased context length - models can now handle up to 10M tokens, with external APIs now offering up to 2 M tokens for text and/or video. Clearer context - The information within the context window is clearer, reducing hallucinations & enabling in-context learning.
* Gemini - Multimodal from the start - input sequence: Text + Audio + Image + Video => Transformer => Image Decoder,Text Decoder  -> Images, Text
* Gemini - Combining many advances: TPUs, Model-parallel and data-parallel training, Cross-datacenter training, Fast and automated detection of SDC errors, Pathways, JAX, Distributed representations of words, Tranformers, Sparse Mixture of Experts, Distillation, Chain of Thought decoding, Speculative Decoding, SFT, RLHF, RLMF, RLxF, + ..
* [Introducing Gemini 2.0: our new AI model for the agentic era](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) 2.0 Flash model more capable than 1.5 Pro-scale model
* [Gemini 2.5: Our most intelligent AI model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/) #1 on Arena with the largest score jump ever (+40)!
* Tackling More Advanced Mathematics: International Mathematical Olympiad(IMO) Gold-medal Level Performance July 2025 - An advanced version of Gemini Deep Think solved 5/6 IMO problems perfectly, earning 35/42 total points, and achieving gold-medal level performance. [Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) Key Aspects: Problems solved by a single model with deep thinking and reasoning capabilities, input provided as informal mathematics, all problems solved within 4.5 hour time limit [here](https://storage.googleapis.com/deepmind-media/gemini/IMO_2025.pdf)
* [A new era of intelligence with Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

#### Organizing a Large-Scale Scientific Effort Like Gemini
* Core areas - Data, Infra, Serving, Evals, Codebase, Longer-term Research
* Capabilities - Safety, Vision, Audio, Code, Agents, Internalization
* Model Development Areas - Pre-training, Post-training, On-device Models

#### Forward Looking
* **Human & AI Agent Collaboration**
* Currently, most users are one person interactively working with one model or agent at a time
* in the future, much more work will happen with a human coordinating activities of dozens or hundreds of AI agents that have been given high level instructions on what to accomplish
* Many interesting research Qs: 1. How can we give effective reward singnals for less verifiable domains? 2. What is the right HCI paradigm for "managing a team of 50 virtual interns or research assistants"? 3. How can agents themselves cooperatively accomplish complex tasks? 4. What will this enable?
* **Illusion of Attentinf to All Information**
* Millions of tokens in context window is incredibly useful. Enables In-context learning, Complex reasoning and extraction/summarization over ~1000 pages of text, multiple hours of video, and/or tens of hours of audio
* What if e wanted to push this to give the illusion of attending to trillions or tensof trillions of tokens of information? - Hybrid systems with learned retrieval algorithms over very large corpora, lightweight models that can assess relevance, and then attend to most important few hundred documents across large corpora
* Many uses: Personalized Gemini, Web search, Multimodal search/retrieval, Coding agents over very large databases
* **Inference Efficiency is Critical**
* Demand for highly capable models is very high and growing fast
* Making inference efficient is vital: Specialized hardware designed purely for inference will be important, Model and algorithmic improvements for efficient inference, Low latency for highly capable models is a huge plus: will enable new use cases
* In the future, AI applied to automating chip design will help design efficient inference hardware with much shorter timelines and much less human effort => more specialized hardware that is more efficient
* Leaderboard and common baselines enable data-driven decision making about how to improve
* Multiple rounds of experimentation, Many experimentations at small scale, Advance smaller number of successful experiments to next scale, Every so often(few weeks) incorporate successful experiments demonstrated at largest experimental scale into new candidate baseline, Repeat


  

