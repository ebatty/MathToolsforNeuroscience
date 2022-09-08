# Key concepts


## Linear transformations and matrices

*  A matrix is basically a table of numbers.
      *   We can represent matrices with numpy arrays, which we create as a list of rows: `np.array([[4, 1, 2], [3, 2, 0]])`
*   Linear transformations take in an input vector and outputs a transformed vector. Under a linear transformation, all grid line remain parallel and evenly spaced and the origin remains fixed (it must preserve vector addition and scalar multiplication).
*  Matrices represent linear transformations: each column corresponds to where the corresponding standard basis vector ends up after the transformation
*  We can think of the matrix vector multiplication $A\bar{x}=\bar{b}$ as a linear transformation where $A$ acts on $\bar{x}$ to produce $\bar{b}$.  An alternate view is to think of it as solving a system of linear equations. 
 *   `np.linalg.solve` solves matrix vector equations like the above

   *    As an example, solving $A\bar{x}=\bar{b}$ is equivalent to solving the system of linear equations:
   
   $$ \begin{align} 2x_1 + 3x_2 &= 6 \\ x_1 + 4x_2 &= 1 \end{align}$$

$$\text{if } A = \begin{bmatrix}
2 & 3 \\
1 & 4\
\end{bmatrix}, \bar{b} =\begin{bmatrix}
6 \\
1\
\end{bmatrix}$$ 



## Matrix multiplication

*   We can envision matrix multiplication as the composition of transformations. If C = AB, element $c_{ij}$  (the element of C in the ith row and jth column) equals the dot product of the ith row of A and the jth column of B.
      *  There are several ways to do matrix multiplication in Python: we can use `np.dot(A, B)`, `np.matmul(A, B)` or use a special operator @ so `A @ B`

## Determinants
*    The determinant of a matrix (det A) is a scalar value that can be viewed as describing the area changes induced by the corresponding linear transformation. It is negative if the linear transformation reverses the orientation of the space. 
      *  `np.linalg.det(A)` computes the determinant

## Inverse matrices, column space, and null space

*    We can sometimes take the inverse of a matrix so that $A^{-1}A = I$ where $I$ is the identity matrix (all zeros except for ones on the diagonal).
        *    We can use `np.linalg.inv(A)` to compute $A^{-1}$ when it exists
        * `np.eye(d)` gives us the identity matrix of dimension d
*   The column space of a matrix is the span of the columns of the matrix. This is equivalent to the range of the linear transformation where, in informal language, the range is everywhere that can be "gotten to" by the transformation. In other words, the range is the set of all vectors that the linear transformation maps to.
*  The rank of a matrix is the dimension of the column space.
     *  `np.linalg.matrix_rank(A)` computes the rank
*  The null space of a matrix is the set of all vectors that land on the origin after the resulting transformation. In other words, it is the set of all solutions of $A\bar{x} = \bar{0}$.
    *  You can use `scipy.linalg.null_space` to find a basis for the null space of a matrix.
* If the matrix A is $m$ x $n$, the null space must be a subspace of $R^n$ and the column space must be a subspace of $R^m$.
