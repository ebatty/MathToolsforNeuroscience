# Key concepts

## General dynamical systems
*  System concerned with movement of point over time in some relevant geometrical space
* The state of a dynamical system is a complete snapshot of the system at that point in time.
* The state space is the relevant geometrical space in which to model the state evolving (the set of all possible states)
* Are discrete or continuous depending on how the evolution rules are defined
*  Discrete dyanmical systems have step-like update rules: $x_{n+1} = F(x_n)$
*  Continuous dyanmical systems have differential equations governing the evolution: $\frac{dx}{dt} = F(x, t)$

## Discrete dynamical system model of neural circuit

*  We can model a neural circuit as a discrete dynamical system. If $\bar{u}_t$ is the vector of neural activity at time $t$ and $W$ is the synaptic weight matrix, then:
$$\bar{u}_{t+1} = W\bar{u}_t $$ 

## Eigenvectors & eigenvalues


*   An eigenvector is a vector that doesn't change direction in a transformation ($\bar{v}$ below).
*   The associated eigenvalue is the factor by which the eigenvector is scaled ($\lambda$ below). \\
$$A\bar{v} = \lambda\bar{v} $$

*   `np.linalg.eig` gives you the eigenvalues and eigenvectors of a matrix.
*  Eigenvalues are more specifically defined than eigenvectors: for an eigenvector $\bar{v}$, $-2\bar{v}$ and $6\bar{v}$ are also eigenvectors. In other words, there are an infinite number of eigenvectors for a given eigenvalue that lie along the same line. For this reason, we often use unit eigenvectors (although this does not account for flipping between negative/positive). 
*  Additionally, sometimes all of the vectors in a plane (or more in higher D space) can be eigenvectors for a given eigenvalue. This will not always be obvious from the outputs of `np.linalg.eig`.
*  You will not necessarily be able to form a basis for a space from the eigenvectors.
*  We solve for the eigenvalues of matrix $B$ by solving det($B$ - $\lambda I$) = 0.
* Complex eigenvalues exist and have associated complex eigenvectors - a matrix with complex eigenstuff performs some kind of rotation.
*  Nonsquare matrices do not have eigenvalues.
* An n x n matrix has n eigenvalues but they could be real or complex and they are not necessarily distinct (meaning a matrix could have two eigenvalues of 2, with different associated eigenvectors).
