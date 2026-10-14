# Exercise 4. Matrix Multiplication and Noncommutativity

## Given Matrices

$$
A = \begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix},
\qquad
B = \begin{pmatrix}
2 & 0 \\
3 & 1
\end{pmatrix}.
$$

Both matrices have size $2 \times 2$, so both products $AB$ and $BA$ are defined.

## 1. Compute $AB$

To multiply matrices, each entry of the product is obtained by multiplying a row of the first matrix by a column of the second matrix and adding the products.

$$
AB =
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
3 & 1
\end{pmatrix}.
$$

Calculate each entry:

$$
(AB)_{11}=1\cdot2+2\cdot3=2+6=8,
$$

$$
(AB)_{12}=1\cdot0+2\cdot1=0+2=2,
$$

$$
(AB)_{21}=0\cdot2+1\cdot3=0+3=3,
$$

$$
(AB)_{22}=0\cdot0+1\cdot1=0+1=1.
$$

Therefore,

$$
AB=\begin{pmatrix}
8 & 2 \\
3 & 1
\end{pmatrix}.
$$

## 2. Compute $BA$

Now reverse the order of multiplication:

$$
BA =
\begin{pmatrix}
2 & 0 \\
3 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}.
$$

Calculate each entry:

$$
(BA)_{11}=2\cdot1+0\cdot0=2,
$$

$$
(BA)_{12}=2\cdot2+0\cdot1=4,
$$

$$
(BA)_{21}=3\cdot1+1\cdot0=3,
$$

$$
(BA)_{22}=3\cdot2+1\cdot1=6+1=7.
$$

Therefore,

$$
BA=\begin{pmatrix}
2 & 4 \\
3 & 7
\end{pmatrix}.
$$

## 3. Is $AB=BA$?

The two products are

$$
AB=\begin{pmatrix}
8 & 2 \\
3 & 1
\end{pmatrix},
\qquad
BA=\begin{pmatrix}
2 & 4 \\
3 & 7
\end{pmatrix}.
$$

They are not equal because their corresponding entries are not all equal. For example, the top-left entries are $8$ and $2$.

Thus,

$$
AB\ne BA.
$$

## 4. Noncommutativity of Matrix Multiplication

Multiplication of real numbers is commutative: for any real numbers $x$ and $y$, we have $xy=yx$.

However, matrix multiplication is not commutative in general. This means that changing the order of the factors can change the result:

$$
AB\ne BA.
$$

The matrices in this exercise provide a direct example of this property. Although both products are defined, they produce different matrices.

## Verification

Both products have size $2\times2$, which is consistent with the dimension rule for multiplying two $2\times2$ matrices.

The entries of $AB$ and $BA$ have been calculated independently using row-by-column multiplication. Since their top-left entries differ, the two matrices cannot be equal.

Therefore, the example confirms that matrix multiplication is not commutative in general.
