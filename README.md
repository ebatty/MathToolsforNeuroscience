
# Mathematical Tools for Neuroscience (Neurobio 212 at Harvard)

*Developed and taught by Ella Batty, Lucy Lai, Alex Chen, and John Assad*

### Description of course

Numerical data analysis has become a nearly indispensable tool in modern neuroscience. This course aims to equip graduate students with the fundamental mathematical skills in quantitative modeling and data analysis necessary for neuroscience research (and for further computational neuroscience courses). This course is essentially organized into three sections: one on linear algebra, one on probabiliy & statistics, and one on the basics of machine learning. We will also cover some additional topics such as differential equations and dynamical systems). 

One goal in formulating this course was to alleviate the need for taking multiple undergraduate-level courses in each of the stated topics (which may be cumbersome due to back-and-forth commute, inconvenient scheduling, or just an excess of materical with no clear applicability to neuroscience research).  Our goal is to make this as fun, approachable, and applicable as possible. We would like to build mathematical intuition for these essential topics.  


### Course Prerequisites

You will not need any math experience beyond high school calculus. Python will be used in this class so some knowledge of it is necessary, although this course will also serve as an opportunity to practice those skills.  

### Description of materials
Video links below will take you to youtube, tutorial links will open Google colab notebooks.


We welcome constructive criticism given via opening a git issue.

### The materials

| Topic | Content | Content description |
|--|----------------------|---------------|
| <img width=500/> |<img width=600/>|<img width=500/>|
| **Week 1: Linear Algebra I, Vectors**| [Video 1.1: What is a vector?](https://youtu.be/YBCLN8NnrjM)                        |  Why learn linear algebra, intuition behind vectors, definition of a vector |
|  |    [Video 1.2: Vector properties & operations](https://youtu.be/7AXpa4U4j-M)                        |  Vector length, unit & zero vectors, scalar multiplication, vector addition, dot product, neuroscience example|
|  |    [Video 1.3: Vector spaces](https://youtu.be/kqaRSwyL050)                        |  Linear combinations, linear independence, spanning vectors, basis, vector spaces|
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week1/Week1Tutorial1.ipynb)                   | Geometry of the dot product, neuron optimal stimuli, correlation coefficient |
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week1/Week1Tutorial2.ipynb)                   | Vector sets |
| **Week 2: Linear Algebra II, Matrices**|  [Video 2.1: Linear transformations and matrices (3Blue1Brown Essence of Linear Algebra Chapter 3)](https://youtu.be/kYB8IZa5AuE)  | Properties of linear transformations, how matrices represent them,  |
| This week videos are all from the 3Blue1Brown Essence of Linear Algebra series |  [Video 2.2: Matrix multiplication as composition (3Blue1Brown Chapter 4)](https://youtu.be/XkY2DOUCWMU)    |  Intuition behind matrix multiplication as composition of linear transformations, properties of matrix multiplication |
| |  [Video 2.3: Three dimensional linear transformations (3Blue1Brown Chapter 5)](https://youtu.be/rHLEWRxRGiM)    |  Brief review of transformations in 3D |
| |  [Video 2.4: The determinant (3Blue1Brown Chapter 6)](https://youtu.be/Ip3X9LOh2dk)    |  Intuition behind determinants, computation of 2x2 matrix determinant |
| |  [Video 2.5:  Inverse matrices, column space, and null space (3Blue1Brown Chapter 7)](https://youtu.be/uQhTuRlWMxw)    |  Systems of linear equations, solving with inverse matrices, when do solutions exist, definition of rank,  how to think of column & null space geometrically|
| |  [Video 2.6: Nonsquare matrices as transformations between dimensions (3Blue1Brown Chapter 8)](https://youtu.be/v8VSDg_WQlA)    |  Brief review of transformations in relation to nonsquare matrices |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week2/Week2Tutorial1.ipynb)                   | Matrix multiplication by hand, thinking about transformations, encoding model matrices in the context of the invertible matrix theorem|
| |  [Tutorial 2](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week2/Week2Tutorial2.ipynb)                   | Properties of nonsquare matrices, changing bases |
| **Week 3: Linear Algebra III, Eigenstuff**|  [Video 3.1: Eigenvectors and eigenvalues (3Blue1Brown Chapter 14)](https://youtu.be/PFDu9oVAE-g)    | Definition of eigenvectors/eigenvalues, how to find eigenvalues of a matrix, brief intro to matrix diagonalization |
| |  Video 3.2: Coming soon  |  |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week3/Week3Tutorial1.ipynb)                   | Describing transformations with eigenvectors, looking at eigenstuff of a squared matrix, complex eigenvalues, understanding neural circuit discrete dynamics using eigenvalues/eigenvectors |
| **Week 4: Linear Algebra IV, Matrix Decomposition & Dimensionality Reduction**|  Video 4.1: Special Matrices Coming Soon   | |
| |  Video 4.2: Matrix decomposition & SVD   | |
| |  [Video 4.3: Dimensionality Reduction in Neuroscience (NMA W1D5 Intro lecture)](https://youtu.be/zeBFyRaoVnQ)   | Byron Yu gives overview of using dimensionality reduction on neural population responses, discusses specific research, highlights different methods and when you might use each|
| |  Video 4.4: PCA Coming Soon   | |
| |  [Tutorial 1](https://colab.research.google.com/github/ebatty/MathToolsforNeuroscience/blob/master/Week4/Week4Tutorial1.ipynb)                   | Delving into SVD, implementing PCA and exploring correlation effects, PCA on MNIST images |
| **Linear Algebra Review**|  Review Video: Coming soon   | Brief recap of key concepts of the last month |
|  |  Linking to Neuro Video: Coming soon   | Goes through a neuroscience paper that uses linear algebra heavily |
