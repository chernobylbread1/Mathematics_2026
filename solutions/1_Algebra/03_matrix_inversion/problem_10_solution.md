### Essential Formulas

**Determinant and Invertibility of a Diagonal Matrix:**
A diagonal matrix has non-zero entries only along its main diagonal:

$$
D = \begin{pmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n \\
\end{pmatrix}
$$

Because a diagonal matrix is a special case of a triangular matrix, its determinant is the product of its diagonal elements:

$$
\det D = d_1 \cdot d_2 \cdots d_n
$$

A diagonal matrix is invertible if and only if its determinant is non-zero, which requires that **every diagonal entry be non-zero**:

$$
d_i \neq 0 \quad (i = 1, 2, \dots, n)
$$

If any diagonal entry $d_k = 0$, the entire $k$-th row (and column) is zero, $\det D = 0$, and the matrix is singular (not invertible).

**Inverse of a Diagonal Matrix:**
When all diagonal entries are non-zero, the inverse is formed directly by replacing each diagonal entry with its reciprocal:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{d_1} & 0 & \cdots & 0 \\
0 & \frac{1}{d_2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{1}{d_n} \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 10. Inverse of a Diagonal Matrix**

Given

$$
D=
\begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix},\qquad E=
\begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}.
$$

Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

> **Why this exercise:** teaches how to recognize invertibility and the inverse without using a full procedure when the matrix structure gives the answer immediately.

---

### Solution

**Step 1: Evaluate matrix $E$**

Consider the matrix:

$$
E = \begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
$$

* The diagonal entry in the second row is $e_{22} = 0$.
* The entire second row consists of zeros: $R_2 = (0, 0, 0)$.
* The determinant is:

  $$
  \det E = (2)(0)(5) = 0
  $$

Because its determinant is zero (and it contains a zero row, so $\mathrm{rank}(E) = 2 < 3$), matrix $E$ is **not invertible**.

**Step 2: Evaluate matrix $D$**

Consider the matrix:

$$
D = \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
$$

* The diagonal entries are $d_{11} = 2$, $d_{22} = -3$, and $d_{33} = 5$.
* None of the diagonal entries are zero ($d_{ii} \neq 0$ for all $i$).
* The determinant is:

  $$
  \det D = (2)(-3)(5) = -30
  $$

Since $\det D = -30 \neq 0$, matrix $D$ is **invertible**.

**Step 3: Construct the inverse $D^{-1}$**

For a diagonal matrix with non-zero diagonal entries, the inverse is obtained immediately by taking the reciprocal of each diagonal entry:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & \frac{1}{-3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

**Step 4: Check the result by matrix multiplication**

Multiply $D$ by $D^{-1}$:

$$
D D^{-1} = \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

Because both matrices are diagonal, multiplying them simply multiplies the corresponding diagonal entries:

$$
D D^{-1} = \begin{pmatrix}
2\left(\frac{1}{2}\right) & 0 & 0 \\
0 & (-3)\left(-\frac{1}{3}\right) & 0 \\
0 & 0 & 5\left(\frac{1}{5}\right) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
= I
$$

Similarly:

$$
D^{-1} D = \begin{pmatrix}
\frac{1}{2}(2) & 0 & 0 \\
0 & \left(-\frac{1}{3}\right)(-3) & 0 \\
0 & 0 & \frac{1}{5}(5) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
= I
$$

The identity matrix is obtained in both orders, confirming the inverse.

---

### Final Answer

Invertibility decision:
* Matrix $E$ is **not invertible** because it has a zero on the diagonal ($e_{22} = 0$), giving $\det E = 0$.
* Matrix $D$ is **invertible** because all diagonal entries are non-zero ($2 \neq 0$, $-3 \neq 0$, $5 \neq 0$), giving $\det D = -30 \neq 0$.

Inverse matrix of $D$:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

Verification:

$$
D D^{-1} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
= I
$$
