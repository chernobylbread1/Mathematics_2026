# Exercise 5. Matrix Times Vector

## Given

Let

$$
A =
\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix}
$$

and

$$
x =
\begin{pmatrix}
4 \\
2
\end{pmatrix}.
$$

We need to compute $Ax$ and express it as a linear combination of the columns of $A$.

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

Calculate each entry:

$$
Ax =
\begin{pmatrix}
2 \cdot 4 + (-1) \cdot 2 \\
1 \cdot 4 + 3 \cdot 2
\end{pmatrix}
$$

Simplifying gives

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
Ax =
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

## 2. Express $Ax$ as a Linear Combination of the Columns

The columns of $A$ are

$$
a_1 =
\begin{pmatrix}
2 \\
1
\end{pmatrix},
\qquad
a_2 =
\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

The vector $x$ contains the coefficients $4$ and $2$. Therefore, the matrix-vector product can be written as

$$
Ax = 4a_1 + 2a_2.
$$

Substituting the columns gives

$$
Ax =
4
\begin{pmatrix}
2 \\
1
\end{pmatrix}
+
2
\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

Multiplying each column by its coefficient gives

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

Add the vectors:

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

This confirms the result obtained in the first part.

## Final Answer

The matrix-vector product is

$$
Ax =
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

As a linear combination of the columns of $A$,

$$
Ax =
4
\begin{pmatrix}
2 \\
1
\end{pmatrix}
+
2
\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

**Key idea:** A matrix-vector product is a linear combination of the columns of the matrix, using the entries of the vector as coefficients.
