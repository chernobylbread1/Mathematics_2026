# Exercise 5. Matrix Times Vector

## Given

We are given the matrix

$$
A = \begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix}
$$

and the vector

$$
x = \begin{pmatrix}
4 \\
2
\end{pmatrix}.
$$

We need to compute $Ax$ and express the result as a linear combination of the columns of $A$.

## 1. Compute $Ax$

To multiply a matrix by a vector, multiply each row of the matrix by the vector and add the corresponding products.

$$
Ax =
\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix}
\begin{pmatrix}
4 \\
2
\end{pmatrix}
$$

Calculating each entry gives

$$
Ax =
\begin{pmatrix}
2 \cdot 4 + (-1) \cdot 2 \\
1 \cdot 4 + 3 \cdot 2
\end{pmatrix}
$$

$$
Ax =
\begin{pmatrix}
8 - 2 \\
4 + 6
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

Therefore, the result is

$$
Ax = \begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

## 2. Express $Ax$ as a Linear Combination of the Columns

The first and second columns of $A$ are

$$
a_1 = \begin{pmatrix}
2 \\
1
\end{pmatrix},
\qquad
a_2 = \begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

The entries of the vector $x$ are $4$ and $2$. These entries become the coefficients of the corresponding columns.

Therefore,

$$
Ax = 4a_1 + 2a_2.
$$

Substituting the columns of $A$ gives

$$
Ax =
4\begin{pmatrix}
2 \\
1
\end{pmatrix}
+
2\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

Multiplying each column by its coefficient,

$$
Ax =
\begin{pmatrix}
8 \\
4
\end{pmatrix}
+
\begin{pmatrix}
-2 \\
6
\end{pmatrix}.
$$

Adding the vectors gives

$$
Ax =
\begin{pmatrix}
8 + (-2) \\
4 + 6
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

This agrees with the result obtained in the first part.

## Final Answer

$$
Ax = \begin{pmatrix}
6 \\
10
\end{pmatrix}
= 4\begin{pmatrix}
2 \\
1
\end{pmatrix}
+ 2\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

**Key idea:** A matrix-vector product is a linear combination of the columns of the matrix, with the entries of the vector serving as the coefficients.
