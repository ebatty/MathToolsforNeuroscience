# Key concepts

## Vectors

* Vectors are ordered lists of numbers that can also be viewed geometrically (as arrows)

## Vector operations
*   Length of a vector: $||\bar{x}|| = \sqrt{\sum_{i=1}^N x_i^2} = \sqrt{\bar{x}\cdot \bar{x}}$
*   Unit vectors have length = 1. To make a unit vector version of $\bar{x}$: $\hat{x} = \frac{\bar{x}}{||\bar{x}||}$
*   Zero vectors ($\bar{0}$) have all components equal to 0
*   Scalar multiplication of a vector: 
$
a\bar{x} = \begin{bmatrix}
    ax_1 \\ ax_2 \\ \vdots \\ ax_N
\end{bmatrix}
$

*   Vector addition:
 $\bar{x} + \bar{y} = \begin{bmatrix}
           x_{1} + y_1 \\ x_{2} + y_2\\ \vdots \\ x_{N} + y_N 
\end{bmatrix}$
*   Dot product: $\bar{x} \cdot \bar{y} = \sum_{i=1}^N x_iy_i$

## Vector spaces

* Linear combination: building one vector as the sum of scaled multiples of other vectors
* The span of a set of vectors, $Span\{\bar{v}_1, \bar{v}_2, ...\}$, is the set of all linear combinations of those vectors 
* A set of non-zero vectors is linearly dependent if one member of the set is a linear combination of the others, otherwise they are linearly independent.
* A basis for a given space is a set of linearly independent vectors that spans the space. 
* A vector space V is a collection of vectors for which 2 operations are defined, addition and multiplication by a scalar, that satisfy the below axioms for all vectors in V. If $\bar{x}, \bar{y},$ and $\bar{z}$ are any vectors in V:

    1.  $\bar{x} + \bar{y}$ is in V
    2.  $\bar{x} + \bar{y} = \bar{y} + \bar{x}$
    3.  $(\bar{x} + \bar{y}) + \bar{z} = \bar{x} + (\bar{y} + \bar{z})$
    4.  Zero vector exists in V such that $\bar{x} + \bar{0} = \bar{x}$
    5.  The inverse $-\bar{x}$ exists such that $\bar{x} + (-\bar{x}) = \bar{0}$
    6. $c\bar{x}$ is in V
    7. $c(\bar{x} + \bar{y}) = c\bar{x} + c\bar{y}$
    8. $(c+d)\bar{x} = c\bar{x} + d\bar{x}$
    9. $c(d\bar{x}) = (cd)\bar{x})$
    10. $1\bar{x} = \bar{x}$

