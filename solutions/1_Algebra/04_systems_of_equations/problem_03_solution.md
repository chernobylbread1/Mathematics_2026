### Essential Formulas

1. **Inconsistency in Linear Systems (Rouché–Capelli Theorem):**
   A linear system $Ax = b$ with augmented matrix $[A \mid b]$ is consistent if and only if the rank of the coefficient matrix equals the rank of the augmented matrix:

   $$
   \mathrm{rank}(A) = \mathrm{rank}([A \mid b])
   $$

   If:

   $$
   \mathrm{rank}(A) < \mathrm{rank}([A \mid b])
   $$

   then the system is **inconsistent** (it has no solution).

2. **The Contradictory Row in Row Echelon Form:**
   During Gaussian elimination, an inconsistent system reveals itself through a row of the form:

   $$
   \begin{pmatrix}
   0 & 0 & \cdots & 0 & \mid & c \\
   \end{pmatrix} \quad (c \neq 0)
   $$

   This row corresponds to the scalar equation:

   $$
   0x_1 + 0x_2 + \cdots + 0x_n = c \implies 0 = c
   $$

   which is mathematically false for any choice of unknowns.

3. **Geometric Interpretation in $\mathbb{R}^2$:**
   In two dimensions, each linear equation $a_i x + b_i y = c_i$ describes a straight line.
   * Two lines with identical normal vectors / slopes but different constants are strictly parallel and non-intersecting:

     $$
     \frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}
     $$

---

### Problem Statement

Solve or show that the system is inconsistent:

$$
\begin{cases}
x+2y=3, \\
2x+4y=7. \\
\end{cases}
$$

Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

> **Why this exercise:** teaches how to recognize that a system has no solution without guessing.

---

### Solution

**Step 1: Set up the Augmented Matrix**

Write the system as an augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 2 & \mid & 3 \\
2 & 4 & \mid & 7 \\
\end{pmatrix}
$$

Row 1 corresponds to $x + 2y = 3$, and Row 2 corresponds to $2x + 4y = 7$.

---

**Step 2: Perform Gaussian Elimination**

The pivot in the first column is $a_{11} = 1$. Eliminate the entry $a_{21} = 2$ in row 2 by applying the elementary row operation $R_2 \leftarrow R_2 - 2R_1$:

$$
R_2 = (2 - 2(1), \ 4 - 2(2) \ \mid \ 7 - 2(3)) = (0, \ 0 \ \mid \ 7 - 6) = (0, \ 0 \ \mid \ 1)
$$

The augmented matrix in row echelon form becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

---

**Step 3: Appearance and Analysis of the Contradiction**

Examining the second row of the echelon matrix:
* The coefficients for both unknowns $x$ and $y$ are zero.
* The constant term on the right-hand side is $1$.

Translating row 2 back into equation form:

$$
0\cdot x + 0\cdot y = 1 \implies 0 = 1
$$

Because $0 = 1$ is an impossible mathematical statement (a contradiction), no pair of real numbers $(x, y)$ can satisfy this equation.
Therefore, the system has no solution; it is **inconsistent**.

In terms of ranks:
* The coefficient matrix $A$ has only $1$ non-zero row:

  $$
  \mathrm{rank}(A) = 1
  $$

* The augmented matrix $[A \mid b]$ has $2$ non-zero rows:

  $$
  \mathrm{rank}([A \mid b]) = 2
  $$

Since $\mathrm{rank}(A) = 1 < 2 = \mathrm{rank}([A \mid b])$, the system is inconsistent.

---

**Step 4: Algebraic and Geometric Interpretation**

1. **Algebraic View:**
   Multiplying Equation 1 by $2$:

   $$
   2(x + 2y) = 2(3) \implies 2x + 4y = 6
   $$

   However, Equation 2 demands:

   $$
   2x + 4y = 7
   $$

   Subtracting the two equations directly gives:

   $$
   (2x + 4y) - (2x + 4y) = 7 - 6 \implies 0 = 1
   $$

   The left-hand sides of the two equations are proportional by a factor of $2$, but the right-hand sides are not ($6 \neq 7$).

2. **Geometric View (Parallel Lines):**
   Solving each equation for $y$ in slope-intercept form ($y = mx + n$):
   * Line 1 ($L_1$):

     $$
     y = -\frac{1}{2}x + \frac{3}{2}
     $$

   * Line 2 ($L_2$):

     $$
     y = -\frac{2}{4}x + \frac{7}{4} = -\frac{1}{2}x + \frac{7}{4}
     $$

   Both lines have identical slopes ($m_1 = m_2 = -1/2$), which means they are parallel.
   Their vertical intercepts are different:

   $$
   \frac{3}{2} = 1.5 \neq \frac{7}{4} = 1.75
   $$

   Because the lines are parallel and distinct, they have no points of intersection. The solution set is the empty set $\emptyset$.

---

### Final Answer

1. **Conclusion:**
   The system is **inconsistent** (it has no solution, $\emptyset$).

2. **Matrix Contradiction:**
   Row elimination yields:

   $$
   \begin{pmatrix}
   1 & 2 & \mid & 3 \\
   0 & 0 & \mid & 1 \\
   \end{pmatrix}
   $$

   where the second row represents $0 = 1$.

3. **Interpretation:**
   * **Algebraically:** The left-hand sides are identical up to a scalar factor ($2(x+2y) = 2x+4y$), but the constants are incompatible ($6 \neq 7$).
   * **Geometrically:** The two equations represent distinct parallel lines in $\mathbb{R}^2$ with identical slope $-1/2$ and different intercepts ($3/2 \neq 7/4$), which never intersect.
