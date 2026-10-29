### Essential Formulas

1. **Augmented Matrix Representation:**
   For a linear system $Ax = b$, the augmented matrix $[A \mid b]$ combines the coefficient matrix and the right-hand side vector:

   $$
   [A \mid b] = \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} & \mid & b_1 \\
   a_{21} & a_{22} & \cdots & a_{2n} & \mid & b_2 \\
   \vdots & \vdots & \ddots & \vdots & \mid & \vdots \\
   a_{m1} & a_{m2} & \cdots & a_{mn} & \mid & b_m \\
   \end{pmatrix}
   $$

2. **Elementary Row Operations:**
   The set of solutions to $Ax = b$ remains unchanged under the following operations:
   * **Row Swap:** $R_i \leftrightarrow R_j$
   * **Row Scaling:** $R_i \leftarrow k R_i$ with $k \neq 0$
   * **Row Addition:** $R_i \leftarrow R_i + c R_j$

3. **Gaussian Elimination and Back-Substitution:**
   The algorithm transforms $[A \mid b]$ into row echelon form (upper-triangular structure with leading ones or pivots):

   $$
   \begin{pmatrix}
   p_{11} & * & * & \mid & c_1 \\
   0 & p_{22} & * & \mid & c_2 \\
   0 & 0 & p_{33} & \mid & c_3 \\
   \end{pmatrix}
   $$

   Once in row echelon form, the unknowns are determined sequentially from the bottom row upwards (back-substitution).

---

### Problem Statement

Solve using Gaussian elimination:

$$
\begin{cases}
x+y+z=6, \\
2x-y+z=3, \\
x+2y-z=2. \\
\end{cases}
$$

After solving, substitute the result into all equations and check consistency.

> **Why this exercise:** introduces the basic method for solving a system and builds the habit of checking the result.

---

### Solution

**Step 1: Write the Augmented Matrix**

Set up the augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
2 & -1 & 1 & \mid & 3 \\
1 & 2 & -1 & \mid & 2 \\
\end{pmatrix}
$$

The first pivot is $a_{11} = 1$ in row 1.

---

**Step 2: Eliminate Entries in Column 1 Below the First Pivot**

* **Eliminate entry in row 2:** Apply $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2\cdot 1, \ -1 - 2\cdot 1, \ 1 - 2\cdot 1 \ \mid \ 3 - 2\cdot 6) = (0, \ -3, \ -1 \ \mid \ -9)
  $$

* **Eliminate entry in row 3:** Apply $R_3 \leftarrow R_3 - R_1$:

  $$
  R_3 = (1 - 1\cdot 1, \ 2 - 1\cdot 1, \ -1 - 1\cdot 1 \ \mid \ 2 - 1\cdot 6) = (0, \ 1, \ -2 \ \mid \ -4)
  $$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
0 & 1 & -2 & \mid & -4 \\
\end{pmatrix}
$$

---

**Step 3: Swap Rows for a Simpler Pivot in Column 2**

Swap row 2 and row 3 ($R_2 \leftrightarrow R_3$) to place the convenient pivot $1$ into the second row:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & -3 & -1 & \mid & -9 \\
\end{pmatrix}
$$

---

**Step 4: Eliminate Entries in Column 2 Below the Second Pivot**

Eliminate the $-3$ in row 3 by adding $3$ times row 2 ($R_3 \leftarrow R_3 + 3R_2$):

$$
R_3 = (0 + 3\cdot 0, \ -3 + 3\cdot 1, \ -1 + 3\cdot(-2) \ \mid \ -9 + 3\cdot(-4)) = (0, \ 0, \ -7 \ \mid \ -21)
$$

The augmented matrix is now in row echelon form:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & 0 & -7 & \mid & -21 \\
\end{pmatrix}
$$

---

**Step 5: Solve by Back-Substitution**

* **From row 3:**

  $$
  -7z = -21 \implies z = \frac{-21}{-7} = 3
  $$

* **From row 2:**

  $$
  y - 2z = -4
  $$

  Substitute $z = 3$:

  $$
  y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2
  $$

* **From row 1:**

  $$
  x + y + z = 6
  $$

  Substitute $y = 2$ and $z = 3$:

  $$
  x + 2 + 3 = 6 \implies x + 5 = 6 \implies x = 1
  $$

Thus, the unique solution is:

$$
(x, y, z) = (1, 2, 3)
$$

or as a column vector:

$$
x = \begin{pmatrix}
1 \\
2 \\
3 \\
\end{pmatrix}
$$

---

**Step 6: Verification in All Three Equations**

Substitute $x = 1$, $y = 2$, $z = 3$ into each original equation:

1. **Equation 1:**

   $$
   x + y + z = 1 + 2 + 3 = 6 = b_1
   $$

2. **Equation 2:**

   $$
   2x - y + z = 2(1) - 2 + 3 = 2 - 2 + 3 = 3 = b_2
   $$

3. **Equation 3:**

   $$
   x + 2y - z = 1 + 2(2) - 3 = 1 + 4 - 3 = 2 = b_3
   $$

All three equations are satisfied simultaneously, confirming that the solution is correct.

---

### Final Answer

1. **Solution of the System:**

   $$
   x = 1, \qquad y = 2, \qquad z = 3
   $$

   or in vector form:

   $$
   \begin{pmatrix}
   x \\
   y \\
   z \\
   \end{pmatrix}
   = \begin{pmatrix}
   1 \\
   2 \\
   3 \\
   \end{pmatrix}
   $$

2. **Consistency Check:**
   Substituting $(1, 2, 3)$ into all three original equations produces $6 = 6$, $3 = 3$, and $2 = 2$. The system has exactly one unique solution.
