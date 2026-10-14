# Exercise 5. Matrix Times Vector

## Given

$$
A = \begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix},
\qquad
x = \begin{pmatrix}
4 \\
2
\end{pmatrix}.
$$

## Solution

### 1. Compute $Ax$

Multiply each row of $A$ by the vector $x$:

$$
Ax =
\begin{pmatrix}
2 \cdot 4 + (-1) \cdot 2 \\
1 \cdot 4 + 3 \cdot 2
\end{pmatrix}
=
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

### 2. Express $Ax$ as a Linear Combination of the Columns

The columns of $A$ are

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

The entries of $x$ are $4$ and $2$, so they are the coefficients of the corresponding columns. Therefore,

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
\end{pmatrix}
=
\begin{pmatrix}
8 \\
4
\end{pmatrix}
+
\begin{pmatrix}
-2 \\
6
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

Both methods give the same result.

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

**Key idea:** A matrix-vector product is a linear combination of the columns of the matrix, with the entries of the vector as coefficients.
