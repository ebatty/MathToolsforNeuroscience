
# Mathematical Tools for Neuroscience (Neurobio 212 at Harvard)

*Developed and taught by Ella Batty, Lucy Lai, Alex Chen, and John Assad*

Course contact: Eleanor_Batty@hms.harvard.edu

**Scroll down to bottom for the materials**

### Description of course

Numerical data analysis has become a nearly indispensable tool in modern neuroscience. This course aims to equip graduate students with the fundamental mathematical skills in quantitative modeling and data analysis necessary for neuroscience research (and for further computational neuroscience courses). **This course is essentially organized into three sections: one on linear algebra, one on probabiliy & statistics, and one on the basics of machine learning.**
 We will also cover some additional topics such as differential equations and dynamical systems). 

One goal in formulating this course was to alleviate the need for taking multiple undergraduate-level courses in each of the stated topics (which may be cumbersome due to back-and-forth commute, inconvenient scheduling, or just an excess of materical with no clear applicability to neuroscience research).  Our goal is to make this as fun, approachable, and applicable as possible. We would like to build mathematical intuition for these essential topics.  


### Course Prerequisites

You will not need any math experience beyond high school calculus. Python will be used in this class so some knowledge of it is necessary, although this course will also serve as an opportunity to practice those skills.  

### Description of materials

There are three components to the course: video lectures, comprehension questions, and tutorials.

**Video lectures**: The course consists of short video lectures each structured around a specific topic (10-20 minutes per video). We have created most of these videos using a Khan academy inspired style. We don't want to reinvent the wheel so when great videos already exist on a specific topic, we link to those instead, but this will mostly occur in the linear algebra section. 

**Comprehension questions**: These are short questions designed to be looked at right after watching the videos to consolidate your knowledge and try out quick computations. Both questions and answers are provided below.

**Tutorials**: Each week has 1 - 2 tutorials, or problem sets. These are Google colab notebooks with exercises where you might be asked to do computations by hand, engage with interactive demos, or code. They are designed to review the video material and in some cases introduce new concepts. They are not designed for repetitive problem solving (i.e. you will not be asked to solve a matrix equation by hand 100 times...). 

### Other resources
Helpful for before this course: Basic Introduction to Maths and Python for Neuroscience by John Butler [https://github.com/john-s-butler-dit/Basic-Introduction-to-Python]

Similar course: Mathematical Tools for Neural and Cognitive Science by Eero Simoncelli & Mike Landy [https://www.cns.nyu.edu/~eero/math-tools/]

A good follow-up to learn computational neuroscience: Neuromatch Academy [https://github.com/NeuromatchAcademy/course-content]


### The materials

Video links below will take you to Youtube, tutorial links will open Google colab notebooks.

**We welcome constructive criticism given via opening a git issue. Note that the Week 1 videos created by me are a little rough right now due a steep learning curve (and a delay in acquiring appropriate audio equipment) but I promise they get better so bear with it.**

| Topic | Content | Content description |
|--|----------------------|---------------|
| <img width=500/> |<img width=600/>|<img width=500/>|
| **Week 1: Linear Algebra I, Vectors**| [Video 1.1: What is a vector?](https://youtu.be/YBCLN8NnrjM) <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week1/video11_notes.pdf)                       |  Why learn linear algebra, intuition behind vectors, definition of a vector |
|  |    [Video 1.2: Vector properties & operations](https://youtu.be/7AXpa4U4j-M)   <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week1/video12_notes.pdf)                        |  Vector length, unit & zero vectors, scalar multiplication, vector addition, dot product, neuroscience example|
|  |    [Video 1.3: Vector spaces](https://youtu.be/kqaRSwyL050) <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week1/video13_notes.pdf)                              |  Linear combinations, linear independence, spanning vectors, basis, vector spaces|
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week1/Week1Tutorial1.ipynb)                   | Geometry of the dot product, neuron optimal stimuli, correlation coefficient |
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week1/Week1Tutorial2.ipynb)                   | Vector sets |
| **Week 2: Linear Algebra II, Matrices**|  [Video 2.1: Linear transformations and matrices (3Blue1Brown Essence of Linear Algebra Chapter 3)](https://youtu.be/kYB8IZa5AuE)  | Properties of linear transformations, how matrices represent them,  |
| This week videos are all from the 3Blue1Brown Essence of Linear Algebra series |  [Video 2.2: Matrix multiplication as composition (3Blue1Brown Chapter 4)](https://youtu.be/XkY2DOUCWMU)    |  Intuition behind matrix multiplication as composition of linear transformations, properties of matrix multiplication |
| |  [Video 2.3: Three dimensional linear transformations (3Blue1Brown Chapter 5)](https://youtu.be/rHLEWRxRGiM)    |  Brief review of transformations in 3D |
| |  [Video 2.4: The determinant (3Blue1Brown Chapter 6)](https://youtu.be/Ip3X9LOh2dk)    |  Intuition behind determinants, computation of 2x2 matrix determinant |
| |  [Video 2.5:  Inverse matrices, column space, and null space (3Blue1Brown Chapter 7)](https://youtu.be/uQhTuRlWMxw)    |  Systems of linear equations, solving with inverse matrices, when do solutions exist, definition of rank,  how to think of column & null space geometrically|
| |  [Video 2.6: Nonsquare matrices as transformations between dimensions (3Blue1Brown Chapter 8)](https://youtu.be/v8VSDg_WQlA)    |  Brief review of transformations in relation to nonsquare matrices |
| | [Comprehension Questions](https://forms.gle/sR45h2Ja82aSq737A) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week2/Week2Tutorial1.ipynb)                   | Matrix multiplication by hand, thinking about transformations, encoding model matrices in the context of the invertible matrix theorem|
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week2/Week2Tutorial2.ipynb)                   | Properties of nonsquare matrices, changing bases |
| **Week 3: Linear Algebra III, Eigenstuff**|  [Video 3.1: Eigenvectors and eigenvalues (3Blue1Brown Chapter 14)](https://youtu.be/PFDu9oVAE-g)    | Definition of eigenvectors/eigenvalues, how to find eigenvalues of a matrix, brief intro to matrix diagonalization |
| |  [Video 3.2: Eigenstuff in neural circuits](https://youtu.be/j3tg9RSOh0o) <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week3/video32_notes.pdf)          | Outline of using eigenvalues/vectors to understand dynamics of a small neural circuit |
| | [Comprehension Questions](https://forms.gle/yTqdbzLVB9UVt4J88) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week3/Week3Tutorial1.ipynb)                   | Describing transformations with eigenvectors, looking at eigenstuff of a squared matrix, complex eigenvalues, understanding neural circuit discrete dynamics using eigenvalues/eigenvectors |
| **Week 4: Linear Algebra IV, Matrix Decomposition & Dimensionality Reduction**|  [Video 4.1: Special Matrices](https://youtu.be/kXXvUTnXW9w)  <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week4/video41_notes.pdf)   |  Covers diagonal, orthogonal, and symmetric matrices |
| |  [Video 4.2: Matrix decomposition & SVD](https://youtu.be/KHafaOoAS8w)  <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week4/video42_notes.pdf)   | Covers what matrix decomposition is/what we can use it for/and types, especially eigendecomposition and SVD |
| |  [Video 4.3: Dimensionality Reduction in Neuroscience (NMA W1D5 Intro lecture)](https://youtu.be/zeBFyRaoVnQ)   | Byron Yu gives overview of using dimensionality reduction on neural population responses, discusses specific research, highlights different methods and when you might use each|
| |  [Video 4.4: PCA](https://youtu.be/K7V_Z81H_Vw)  | What is PCA, how do we compute it, how does it relate to SVD |
| | [Comprehension Questions](https://forms.gle/gKb77GpEU4ATpSpi8) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week4/Week4Tutorial1.ipynb)                   | Delving into SVD, implementing PCA and exploring correlation effects, PCA on MNIST images |
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week4/Week4Tutorial2.ipynb)                   | Delving into SVD as low rank receptive field approximation |
| <br><br>| | |
| **Week 5: Dynamical Systems & Differential Equations**|  [Video 5.1: Intro to Dynamical Systems](https://youtu.be/lxB_XdzhieU)  <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week5/video51_notes.pdf)   |  What is a dynamical system and what are the types |
| |  [Video 5.2: Solving Differential Equations](https://youtu.be/rSMn_aU_XgA)  <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week5/video52_notes.pdf)   | Covers analytical, numerical, and graphical solutions for differential equations |
| |  [Video 5.3: Systems of Differential Equations](https://youtu.be/lV8SoeAxLgM)   <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week5/video53_notes.pdf)  | Continuous dynamical systems, phase portraits, eigenvalue dependence |
| | [Comprehension Questions](https://forms.gle/omStmTpqo31zWyXB7) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week5/Week5Tutorial1.ipynb)                   | Dynamical system exploration concerning rate of ion channels opening |
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week5/Week5Tutorial2.ipynb)                   | Exploration of FitzHugh-Nagumo Model|
| <br><br>| | |
| **Week 6: Probability & Statistics I, Intro to Probability**| Read Chapters 1, 2, 3, and 5 of https://seeing-theory.brown.edu/ (they're brief)| Covers basic probability, probability distributions, and Bayesian inference|
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week6/Week6Tutorial1.ipynb)                   | Explore Poisson distribution, compute marginal distributions|
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week6/Week6Tutorial2.ipynb)                   | Compute probabilities for 2 armed bandit task, code simulations|
| **Week 7: Probability & Statistics II, Intro to Statistics**|  [Video 7.1: Descriptive Statistics](https://youtu.be/pkJjG-pbqHA) <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week7/video71_notes.pdf)      |  Descriptive vs inferential statistics, measures of central tendency, dispersion, and shape |
| |  [Video 7.2: Overview of Statistical Inference](https://youtu.be/VZDJfR99yAo)   <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week7/video72_notes.pdf)      | Covers probability vs statistics, estimation vs hypothesis testing |
| |  [Video 7.3: Point Estimators Examples & Goodness](https://youtu.be/3MyV1oxahC0)    | Point estimators, bias, variance, consistency, population mean & variance estimators |
| |  [Video 7.4: Maximum Likelihood Estimation](https://youtu.be/k3P-3mLGyHo)    | Likelihood defintion, maximum likelihood estimator of firing rate, numerical methods|
| |  [Video 7.5: Bayesian Inference](https://youtu.be/FeikJ4qeAp0)  <br><br> [Notes](https://github.com/ebatty/MathToolsforNeuroscience/blob/master/Week7/video75_notes.pdf)   | Frequentist vs Bayesian probability, priors, Bayes estimators & risk|
| | [Comprehension Questions](https://forms.gle/PSSG7uFcnc5hyxqg8) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week7/Week7Tutorial1.ipynb)                   | Clarify correlation, Bayesian decoding, MLE derivation|
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week7/Week7Tutorial2.ipynb)                   | Normal distribution point estimators|
| **Week 8: Probability & Statistics III, Statistical Encoding Models**|  [Video 8.1: What are encoding & decoding?](https://youtu.be/xG4fe_v2NfU)    | Broad intro to encoding/decoding |
| |  [Video 8.2: Statistical Encoding Models](https://youtu.be/DJG0cYA8h5M)   | Spike triggered averages, linear-nonlinear-Poisson models, gradient descent |
| | [Comprehension Questions](https://forms.gle/mcijrJG3iX9kitgi8) | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week8/Week8Tutorial1.ipynb)                   | Compute STA of retinal data, implement gradient descent by hand to compute LNP parameters |
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week8/Week8Tutorial2.ipynb)                   | Play with LNP filters and see resulting dynamics|
