# Exercise 5. Matrix Times Vector

## Given

\[
A=\begin{pmatrix}
2 & -1\\
1 & 3
\end{pmatrix},
\qquad
x=\begin{pmatrix}
4\\
2
\end{pmatrix}.
\]

We need to compute \(Ax\) and express the result as a linear combination of the columns of \(A\).

## 1. Compute \(Ax\)

Each entry of \(Ax\) is obtained by taking the dot product of a row of \(A\) with the vector \(x\):

\[
Ax=
\begin{pmatrix}
2 & -1\\
1 & 3
\end{pmatrix}
\begin{pmatrix}
4\\
2
\end{pmatrix}.
\]

Calculating each entry gives

\[
Ax=
\begin{pmatrix}
2\cdot 4+(-1)\cdot 2\\
1\cdot 4+3\cdot 2
\end{pmatrix}
=
\begin{pmatrix}
8-2\\
4+6
\end{pmatrix}
=
\begin{pmatrix}
6\\
10
\end{pmatrix}.
\]

Therefore,

\[
\boxed{Ax=\begin{pmatrix}6\\10\end{pmatrix}}.
\]

## 2. Express \(Ax\) as a Linear Combination of the Columns

Let the columns of \(A\) be

\[
a_1=\begin{pmatrix}2\\1\end{pmatrix},
\qquad
a_2=\begin{pmatrix}-1\\3\end{pmatrix}.
\]

The entries of the vector \(x\) are the coefficients of these columns. Since

\[
x=\begin{pmatrix}4\\2\end{pmatrix},
\]

the matrix-vector product can be written as

\[
Ax=4a_1+2a_2.
\]

Substituting the columns gives

\[
Ax=
4\begin{pmatrix}2\\1\end{pmatrix}
+
2\begin{pmatrix}-1\\3\end{pmatrix}.
\]

Multiplying each column by its coefficient,

\[
Ax=
\begin{pmatrix}8\\4\end{pmatrix}
+
\begin{pmatrix}-2\\6\end{pmatrix}
=
\begin{pmatrix}6\\10\end{pmatrix}.
\]

This agrees with the result obtained in the first part.

## Final Answer

\[
\boxed{Ax=\begin{pmatrix}6\\10\end{pmatrix}
=4\begin{pmatrix}2\\1\end{pmatrix}
+2\begin{pmatrix}-1\\3\end{pmatrix}}
\]

**Key idea:** Multiplying a matrix by a vector forms a linear combination of the matrix columns, using the entries of the vector as coefficients.
