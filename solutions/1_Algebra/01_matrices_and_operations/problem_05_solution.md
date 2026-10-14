
# Exercise 5. Matrix Times Vector

## Given

$$
A=
\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix},
\qquad
x=
\begin{pmatrix}
4 \\
2
\end{pmatrix}.
$$

## Solution

First, compute the matrix-vector product:

$$
Ax=
\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix}
\begin{pmatrix}
4 \\
2
\end{pmatrix}.
$$

Multiplying each row by the vector gives

$$
Ax=
\begin{pmatrix}
2\cdot4+(-1)\cdot2 \\
1\cdot4+3\cdot2
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

Now, express the result as a linear combination of the columns of A.

The columns of A are

$$
a_1=
\begin{pmatrix}
2 \\
1
\end{pmatrix},
\qquad
a_2=
\begin{pmatrix}
-1 \\
3
\end{pmatrix}.
$$

The entries of x are 4 and 2. Therefore,

$$
Ax=4a_1+2a_2.
$$

Substituting the columns gives

$$
Ax=
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

Multiplying the columns by their coefficients gives

$$
4\begin{pmatrix}
2 \\
1
\end{pmatrix}
=
\begin{pmatrix}
8 \\
4
\end{pmatrix},
\qquad
2\begin{pmatrix}
-1 \\
3
\end{pmatrix}
=
\begin{pmatrix}
-2 \\
6
\end{pmatrix}.
$$

Adding the vectors gives

$$
Ax=
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
Ax=
\begin{pmatrix}
6 \\
10
\end{pmatrix}.
$$

The linear combination of the columns is

$$
Ax=
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

**Key idea:** Multiplying a matrix by a vector is equivalent to taking a linear combination of the matrix columns, using the entries of the vector as coefficients.

