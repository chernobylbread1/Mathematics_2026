# Exercise 1. Matrix Size and Entries

## 1. Matrix Sizes

The size of a matrix is written as \(m \times n\), where \(m\) is the number of rows and \(n\) is the number of columns.

Matrix \(A\) has 2 rows and 3 columns. Therefore,

\[
\boxed{\operatorname{size}(A)=2\times 3}
\]

Matrix \(B\) has 3 rows and 2 columns. Therefore,

\[
\boxed{\operatorname{size}(B)=3\times 2}
\]

## 2. Matrix Entries

The entry \(a_{ij}\) denotes the element in row \(i\) and column \(j\) of matrix \(A\). Similarly, \(b_{ij}\) denotes the element in row \(i\) and column \(j\) of matrix \(B\).

Given

\[
A=\begin{pmatrix}
2 & -1 & 3\\
0 & 4 & 5
\end{pmatrix},
\qquad
B=\begin{pmatrix}
1 & 0\\
-2 & 3\\
4 & 1
\end{pmatrix},
\]

we read the required entries directly from the matrices:

- \(a_{12}=-1\): row 1, column 2 of \(A\).
- \(a_{23}=5\): row 2, column 3 of \(A\).
- \(b_{21}=-2\): row 2, column 1 of \(B\).
- \(b_{32}=1\): row 3, column 2 of \(B\).

Thus,

\[
\boxed{a_{12}=-1,\quad a_{23}=5,\quad b_{21}=-2,\quad b_{32}=1}
\]

## 3. Row and Column as Vectors

The second row of \(A\) contains the elements \(0,4,5\). Written as a row vector,

\[
\boxed{\begin{pmatrix}0&4&5\end{pmatrix}}
\]

The first column of \(B\) contains the elements \(1,-2,4\). Written as a column vector,

\[
\boxed{\begin{pmatrix}1\\-2\\4\end{pmatrix}}
\]

## Verification

The matrix dimensions confirm the number of entries in each row and column:

- The second row of \(A\) contains 3 entries, consistent with the size \(2\times3\).
- The first column of \(B\) contains 3 entries, consistent with the size \(3\times2\).
- Each requested entry matches its specified row and column.

Therefore, all results are consistent with the given matrices.
