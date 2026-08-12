# [Distingushed Colloquium : Jeff Dean, Feb 10, 2026](https://www.youtube.com/watch?v=UTTeXZrpMR0&t=2490s)

## Some observations
* In recent years, ML has completely changed our expectations of what is possible with computers.
* Increasing scale (compute, data, model size) delivers better results
* Algorithmic and model architecure improvements have provided massive improvements as well
* The kinds of computations we want to run and the hardware on which we run them is changing dramatically

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
*   = 18,000,000,000,000,000,000 ops/day assume 1B ops/sec/core: ~20M core days / day
#### 2014
* Models that Map One Sequence to Another are Powerful
* [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215)
*   Using a neural encoder over an input sequence to generate state, use that to initialize state of a neural decoder. Scale up LSTMs and this works.

