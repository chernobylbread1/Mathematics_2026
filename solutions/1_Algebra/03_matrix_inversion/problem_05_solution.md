### Essential Formulas

**Gauss–Jordan Inversion for an $n \times n$ Matrix:**
Form the augmented matrix by placing the identity matrix $I_n$ alongside matrix $A$:

$$
[A \mid I_n]
$$

Through elementary row operations:
1. Create leading $1$s (pivots) in each successive column.
2. Eliminate all non-zero entries both below and above each pivot (forward and backward elimination).

When the left block becomes $I_n$, the right block is the unique inverse matrix $A^{-1}$:

$$
[A \mid I_n] \longrightarrow [I_n \mid A^{-1}]
$$

**Verification by Multiplication:**
A calculated matrix $A^{-1}$ is correct if and only if:

$$
A A^{-1} = I_n \quad \mathrm{and} \quad A^{-1} A = I_n
$$

---

### Problem Statement

**Exercise 5. A 3×3 Matrix**

Use Gauss–Jordan elimination to find the inverse of

$$
A=
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}.
$$

Check the result by multiplication.

> **Why this exercise:** provides necessary practice with the full method in a situation where the $2\times2$ formula no longer applies.

---

### Solution

Given:

$$
A = \begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}
$$

Set up the initial augmented matrix $[A \mid I]$:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
1 & 0 & 1 & \mid & 0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 1: Eliminate entries in column 1 below the pivot $a_{11} = 1$**

Row 2 already has a $0$ in the first column. Eliminate the leading entry of row 3 by applying $R_3 \leftarrow R_3 - R_1$:

$$
R_3 = (1 - 1,\ 0 - 1,\ 1 - 0\ \mid\ 0 - 1,\ 0 - 0,\ 1 - 0) = (0, -1, 1 \mid -1, 0, 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & -1 & 1 & \mid & -1 & 0 & 1 \\
\end{pmatrix}
$$

**Step 2: Eliminate entries in column 2 above and below the pivot $a_{22} = 1$**

* Eliminate below the pivot ($R_3 \leftarrow R_3 + R_2$):

  $$
  R_3 = (0 + 0,\ -1 + 1,\ 1 + 1\ \mid\ -1 + 0,\ 0 + 1,\ 1 + 0) = (0, 0, 2 \mid -1, 1, 1)
  $$

* Eliminate above the pivot ($R_1 \leftarrow R_1 - R_2$):

  $$
  R_1 = (1 - 0,\ 1 - 1,\ 0 - 1\ \mid\ 1 - 0,\ 0 - 1,\ 0 - 0) = (1, 0, -1 \mid 1, -1, 0)
  $$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 0 & -1 & \mid & 1 & -1 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 2 & \mid & -1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 3: Normalize the third pivot to $+1$**

Scale row 3 by $\frac{1}{2}$ ($R_3 \leftarrow \frac{1}{2} R_3$):

$$
R_3 = \left( 0,\ 0,\ 1\ \mid\ -\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2} \right)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 0 & -1 & \mid & 1 & -1 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 4: Eliminate entries in column 3 above the pivot $a_{33} = 1$**

* Eliminate in row 1 ($R_1 \leftarrow R_1 + R_3$):

  $$
  R_1 = \left( 1,\ 0,\ 0\ \mid\ 1 - \frac{1}{2},\ -1 + \frac{1}{2},\ 0 + \frac{1}{2} \right) = \left( 1, 0, 0 \mid \frac{1}{2}, -\frac{1}{2}, \frac{1}{2} \right)
  $$

* Eliminate in row 2 ($R_2 \leftarrow R_2 - R_3$):

  $$
  R_2 = \left( 0,\ 1,\ 0\ \mid\ 0 - \left(-\frac{1}{2}\right),\ 1 - \frac{1}{2},\ 0 - \frac{1}{2} \right) = \left( 0, 1, 0 \mid \frac{1}{2}, \frac{1}{2}, -\frac{1}{2} \right)
  $$

The augmented matrix is now in reduced row echelon form $[I \mid A^{-1}]$:

$$
\begin{pmatrix}
1 & 0 & 0 & \mid & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

Factoring out the scalar $\frac{1}{2}$:

$$
A^{-1} = \frac{1}{2} \begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 5: Check the result by matrix multiplication**

Multiply $A$ by $A^{-1}$:

$$
A A^{-1} = \begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}
\left[ \frac{1}{2} \begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix} \right]
$$

Factor out $\frac{1}{2}$ and compute the entries:

$$
A A^{-1} = \frac{1}{2} \begin{pmatrix}
1(1) + 1(1) + 0(-1) & 1(-1) + 1(1) + 0(1) & 1(1) + 1(-1) + 0(1) \\
0(1) + 1(1) + 1(-1) & 0(-1) + 1(1) + 1(1) & 0(1) + 1(-1) + 1(1) \\
1(1) + 0(1) + 1(-1) & 1(-1) + 0(1) + 1(1) & 1(1) + 0(-1) + 1(1) \\
\end{pmatrix}
$$

Simplify each sum:

$$
A A^{-1} = \frac{1}{2} \begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
= I
$$

The multiplication yields the $3 \times 3$ identity matrix $I$, confirming that the inverse matrix is correct.

---

### Final Answer

Calculated inverse matrix:

$$
A^{-1} = \frac{1}{2} \begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

Verification:

$$
A A^{-1} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
= I
$$
