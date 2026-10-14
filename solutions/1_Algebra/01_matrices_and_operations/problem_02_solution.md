# Exercise 2. Addition and Scalar Multiplication

## Given Matrices

$$
A = \begin{pmatrix}
1 & 2 \\
-1 & 3
\end{pmatrix},
\qquad
B = \begin{pmatrix}
4 & -2 \\
0 & 5
\end{pmatrix}.
$$

Both matrices have size $2 \times 2$.

## 1. Matrix Addition: $A+B$

Matrix addition is performed by adding corresponding entries.

$$
A+B =
\begin{pmatrix}
1+4 & 2+(-2) \\
-1+0 & 3+5
\end{pmatrix}
$$

Therefore,

$$
A+B =
\begin{pmatrix}
5 & 0 \\
-1 & 8
\end{pmatrix}.
$$

## 2. Matrix Subtraction: $A-B$

Matrix subtraction is performed by subtracting corresponding entries.

$$
A-B =
\begin{pmatrix}
1-4 & 2-(-2) \\
-1-0 & 3-5
\end{pmatrix}
$$

Therefore,

$$
A-B =
\begin{pmatrix}
-3 & 4 \\
-1 & -2
\end{pmatrix}.
$$

## 3. Scalar Multiplication: $3A-2B$

First, multiply every entry of $A$ by $3$:

$$
3A =
\begin{pmatrix}
3 & 6 \\
-3 & 9
\end{pmatrix}.
$$

Next, multiply every entry of $B$ by $2$:

$$
2B =
\begin{pmatrix}
8 & -4 \\
0 & 10
\end{pmatrix}.
$$

Now subtract the corresponding entries:

$$
3A-2B =
\begin{pmatrix}
3-8 & 6-(-4) \\
-3-0 & 9-10
\end{pmatrix}.
$$

Therefore,

$$
3A-2B =
\begin{pmatrix}
-5 & 10 \\
-3 & -1
\end{pmatrix}.
$$

## Why Must Matrices Have the Same Size for Addition?

Matrix addition requires adding corresponding entries. Each entry in one matrix must have a corresponding entry in the same position in the other matrix.

Therefore, the matrices must have the same number of rows and the same number of columns. If their sizes differ, some entries cannot be paired, so their sum is not defined.

## Verification

All three results have size $2 \times 2$, as expected.

We can also verify the scalar multiplication result using

$$
3A-2B =
\begin{pmatrix}
3(1)-2(4) & 3(2)-2(-2) \\
3(-1)-2(0) & 3(3)-2(5)
\end{pmatrix}
$$

$$
=
\begin{pmatrix}
-5 & 10 \\
-3 & -1
\end{pmatrix}.
$$

This confirms the calculated result.
