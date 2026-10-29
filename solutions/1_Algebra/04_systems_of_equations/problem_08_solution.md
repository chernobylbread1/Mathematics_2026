### Essential Formulas

1. **Role of the Coefficient Matrix in Row Operations:**
   In Gaussian elimination on $[A \mid b]$, the sequence of elementary row operations:
   * row swaps to place pivots,
   * row additions/subtractions to clear entries below pivots,
   is governed **entirely** by the entries of the coefficient matrix $A$. The right-hand side vector $b$ merely undergoes the resulting linear transformations passively.

2. **Simultaneous Row Reduction for Multiple Right-Hand Sides:**
   When solving multiple systems $Ax = b_1, Ax = b_2, \dots, Ax = b_k$ with the same coefficient matrix $A$, they can be solved simultaneously by forming a combined augmented matrix:

   $$
   [A \mid b_1 \mid b_2 \mid \cdots \mid b_k]
   $$

   Applying Gaussian elimination reduces $A$ to row echelon form only once, processing all right-hand sides in parallel.

---

### Problem Statement

Solve by elimination the two systems

$$
\begin{cases}
2x+y=5, \\
x-y=1, \\
\end{cases}
$$

$$
\begin{cases}
2x+y=1, \\
x-y=4. \\
\end{cases}
$$

Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

> **Why this exercise:** shows the role of the coefficient matrix independently of the right-hand side.

---

### Solution

**Step 1: Solve System 1 by Elimination**

The first system is:

$$
\begin{cases}
2x + y = 5 \\
x - y = 1 \\
\end{cases}
$$

* Set up the augmented matrix:

  $$
  [A \mid b_1] = \begin{pmatrix}
  2 & 1 & \mid & 5 \\
  1 & -1 & \mid & 1 \\
  \end{pmatrix}
  $$

* **Row Operation 1 (Swap rows for pivot $1$):** $R_1 \leftrightarrow R_2$:

  $$
  \begin{pmatrix}
  1 & -1 & \mid & 1 \\
  2 & 1 & \mid & 5 \\
  \end{pmatrix}
  $$

* **Row Operation 2 (Eliminate below pivot):** $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2(1), \ 1 - 2(-1) \ \mid \ 5 - 2(1)) = (0, \ 3 \ \mid \ 3)
  $$

  The echelon matrix is:

  $$
  \begin{pmatrix}
  1 & -1 & \mid & 1 \\
  0 & 3 & \mid & 3 \\
  \end{pmatrix}
  $$

* **Back-substitution:**
  - From row 2:

    $$
    3y = 3 \implies y = 1
    $$

  - From row 1:

    $$
    x - y = 1 \implies x - 1 = 1 \implies x = 2
    $$

  Solution for System 1: $(x, y) = (2, 1)$.

---

**Step 2: Solve System 2 by Elimination**

The second system is:

$$
\begin{cases}
2x + y = 1 \\
x - y = 4 \\
\end{cases}
$$

* Set up the augmented matrix:

  $$
  [A \mid b_2] = \begin{pmatrix}
  2 & 1 & \mid & 1 \\
  1 & -1 & \mid & 4 \\
  \end{pmatrix}
  $$

* **Row Operation 1 (Swap rows for pivot $1$):** $R_1 \leftrightarrow R_2$:

  $$
  \begin{pmatrix}
  1 & -1 & \mid & 4 \\
  2 & 1 & \mid & 1 \\
  \end{pmatrix}
  $$

* **Row Operation 2 (Eliminate below pivot):** $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2(1), \ 1 - 2(-1) \ \mid \ 1 - 2(4)) = (0, \ 3 \ \mid \ -7)
  $$

  The echelon matrix is:

  $$
  \begin{pmatrix}
  1 & -1 & \mid & 4 \\
  0 & 3 & \mid & -7 \\
  \end{pmatrix}
  $$

* **Back-substitution:**
  - From row 2:

    $$
    3y = -7 \implies y = -\frac{7}{3}
    $$

  - From row 1:

    $$
    x - y = 4 \implies x - \left(-\frac{7}{3}\right) = 4 \implies x + \frac{7}{3} = \frac{12}{3} \implies x = \frac{5}{3}
    $$

  Solution for System 2: $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

---

**Step 3: Verification of Both Solutions**

* **System 1 with $(x, y) = (2, 1)$:**
  - $2(2) + 1 = 4 + 1 = 5$ (matches $b_1$)
  - $2 - 1 = 1$ (matches $b_1$)

* **System 2 with $(x, y) = (5/3, -7/3)$:**
  - $2(5/3) + (-7/3) = 10/3 - 7/3 = 3/3 = 1$ (matches $b_2$)
  - $5/3 - (-7/3) = 5/3 + 7/3 = 12/3 = 4$ (matches $b_2$)

Both solutions are verified.

---

**Step 4: Comparison of Elimination Steps**

1. **Identical Parts of the Calculation:**
   * In both systems, the exact same sequence of row operations was chosen and executed:
     - Operation 1: $R_1 \leftrightarrow R_2$
     - Operation 2: $R_2 \leftarrow R_2 - 2R_1$
   * The transformation of the coefficient matrix entries was completely identical:

     $$
     \begin{pmatrix}
     2 & 1 \\
     1 & -1 \\
     \end{pmatrix}
     \xrightarrow{R_1 \leftrightarrow R_2}
     \begin{pmatrix}
     1 & -1 \\
     2 & 1 \\
     \end{pmatrix}
     \xrightarrow{R_2 \leftarrow R_2 - 2R_1}
     \begin{pmatrix}
     1 & -1 \\
     0 & 3 \\
     \end{pmatrix}
     $$

2. **Why This Part Is Identical:**
   * The choices of which row to swap and what scalar multiplier to subtract depend **only on the entries of the coefficient matrix $A$**, because the goal is to produce a leading pivot of $1$ and zeros below it.
   * The right-hand side vector does not influence the choice of row operations; it is simply transformed by the same operations that are applied to $A$.

3. **Simultaneous Augmented Matrix Perspective:**
   Because the row operations on $A$ are identical, both systems can be solved in a single calculation using a multi-augmented matrix:

   $$
   [A \mid b_1 \mid b_2] = \begin{pmatrix}
   2 & 1 & \mid & 5 & \mid & 1 \\
   1 & -1 & \mid & 1 & \mid & 4 \\
   \end{pmatrix}
   $$

   Applying the same row operations reduces both systems simultaneously:

   $$
   \xrightarrow{R_1 \leftrightarrow R_2}
   \begin{pmatrix}
   1 & -1 & \mid & 1 & \mid & 4 \\
   2 & 1 & \mid & 5 & \mid & 1 \\
   \end{pmatrix}
   \xrightarrow{R_2 \leftarrow R_2 - 2R_1}
   \begin{pmatrix}
   1 & -1 & \mid & 1 & \mid & 4 \\
   0 & 3 & \mid & 3 & \mid & -7 \\
   \end{pmatrix}
   $$

   This demonstrates that the work required to reduce the coefficient matrix $A$ can be done once and shared across multiple right-hand sides.

---

### Final Answer

1. **Solution of System 1:**

   $$
   (x, y) = (2, 1)
   $$

2. **Solution of System 2:**

   $$
   (x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)
   $$

3. **Comparison:**
   * **The identical part:** The sequence of row operations ($R_1 \leftrightarrow R_2$, followed by $R_2 \leftarrow R_2 - 2R_1$) and the resulting row echelon coefficient matrix:

     $$
     \begin{pmatrix}
     1 & -1 \\
     0 & 3 \\
     \end{pmatrix}
     $$

     are identical in both cases.
   * **Why:** Elementary row operations are selected solely to eliminate coefficients in $A$. The right-hand side vectors $b_1$ and $b_2$ do not dictate the row operations, but merely receive them.
