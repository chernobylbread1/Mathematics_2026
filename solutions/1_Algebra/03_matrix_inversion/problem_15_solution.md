### Essential Formulas

1. **Matrix Inversion Method for Linear Systems:**
   If $A$ is an $n \times n$ invertible matrix and $b$ is a vector in $\mathbb{R}^n$, the linear system:

   $$
   Ax = b
   $$

   has the unique solution:

   $$
   x = A^{-1}b
   $$

2. **Inverse of a $2 \times 2$ Matrix:**
   For a $2 \times 2$ matrix:

   $$
   A = \begin{pmatrix}
   a & b \\
   c & d \\
   \end{pmatrix}
   $$

   with $\det A = ad - bc \neq 0$:

   $$
   A^{-1} = \frac{1}{\det A} \begin{pmatrix}
   d & -b \\
   -c & a \\
   \end{pmatrix}
   $$

3. **Gaussian Elimination on Augmented Matrix:**
   To solve $Ax = b$, the system is written as the augmented matrix $[A \mid b]$:

   $$
   [A \mid b] = \begin{pmatrix}
   a_{11} & a_{12} & \mid & b_1 \\
   a_{21} & a_{22} & \mid & b_2 \\
   \end{pmatrix}
   $$

   Elementary row operations (row swaps, scalar multiplications, and row additions) are applied to transform $[A \mid b]$ into upper-triangular echelon form:

   $$
   \begin{pmatrix}
   u_{11} & u_{12} & \mid & c_1 \\
   0 & u_{22} & \mid & c_2 \\
   \end{pmatrix}
   $$

   from which the solution is computed by back-substitution.

---

### Problem Statement

For

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},\qquad b=
\begin{pmatrix}
7 \\
8 \\
\end{pmatrix}
$$

solve $Ax=b$ in two ways:

1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

> **Why this exercise:** compares two known methods and prepares the student to choose a solution method consciously.

---

### Solution

**Step 1: Method 1 — Solving via $x = A^{-1}b$**

* **Compute the determinant of $A$:**

  $$
  \det A = (2)(3) - (1)(1) = 6 - 1 = 5
  $$

  Because $\det A = 5 \neq 0$, the inverse $A^{-1}$ exists.

* **Compute $A^{-1}$:**
  Using the $2 \times 2$ formula:

  $$
  A^{-1} = \frac{1}{5} \begin{pmatrix}
  3 & -1 \\
  -1 & 2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{3}{5} & -\frac{1}{5} \\
  -\frac{1}{5} & \frac{2}{5} \\
  \end{pmatrix}
  $$

* **Multiply $A^{-1}$ by $b$:**

  $$
  x = A^{-1}b = \frac{1}{5} \begin{pmatrix}
  3 & -1 \\
  -1 & 2 \\
  \end{pmatrix}
  \begin{pmatrix}
  7 \\
  8 \\
  \end{pmatrix}
  $$

  Computing the vector components:
  * First component:

    $$
    (3)(7) + (-1)(8) = 21 - 8 = 13
    $$

  * Second component:

    $$
    (-1)(7) + (2)(8) = -7 + 16 = 9
    $$

  Multiplying by the scalar factor $\frac{1}{5}$:

  $$
  x = \frac{1}{5} \begin{pmatrix}
  13 \\
  9 \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{13}{5} \\
  \frac{9}{5} \\
  \end{pmatrix}
  $$

  Hence, $x_1 = \frac{13}{5} = 2.6$ and $x_2 = \frac{9}{5} = 1.8$.

---

**Step 2: Method 2 — Solving via Gaussian Elimination**

* **Set up the augmented matrix $[A \mid b]$:**

  $$
  [A \mid b] = \begin{pmatrix}
  2 & 1 & \mid & 7 \\
  1 & 3 & \mid & 8 \\
  \end{pmatrix}
  $$

* **Step 2.1: Swap rows to obtain a pivot of $1$ in column 1 ($R_1 \leftrightarrow R_2$):**

  $$
  \begin{pmatrix}
  1 & 3 & \mid & 8 \\
  2 & 1 & \mid & 7 \\
  \end{pmatrix}
  $$

* **Step 2.2: Eliminate the entry below the pivot ($R_2 \leftarrow R_2 - 2R_1$):**

  Calculate row 2 entries:
  * First column: $2 - 2(1) = 0$
  * Second column: $1 - 2(3) = 1 - 6 = -5$
  * Right-hand side: $7 - 2(8) = 7 - 16 = -9$

  The matrix is now in upper-triangular echelon form:

  $$
  \begin{pmatrix}
  1 & 3 & \mid & 8 \\
  0 & -5 & \mid & -9 \\
  \end{pmatrix}
  $$

* **Step 2.3: Back-substitution:**
  From the second row equation:

  $$
  -5x_2 = -9 \implies x_2 = \frac{-9}{-5} = \frac{9}{5}
  $$

  Substitute $x_2 = \frac{9}{5}$ into the first row equation ($x_1 + 3x_2 = 8$):

  $$
  x_1 + 3\left(\frac{9}{5}\right) = 8
  $$

  $$
  x_1 + \frac{27}{5} = \frac{40}{5}
  $$

  $$
  x_1 = \frac{40}{5} - \frac{27}{5} = \frac{13}{5}
  $$

  Therefore, the solution vector is:

  $$
  x = \begin{pmatrix}
  \frac{13}{5} \\
  \frac{9}{5} \\
  \end{pmatrix}
  $$

---

**Step 3: Verification of the Solution**

Substitute the computed solution vector:

$$
x = \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

into the original equation $Ax = b$:

$$
Ax = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
= \begin{pmatrix}
2 \cdot \frac{13}{5} + 1 \cdot \frac{9}{5} \\
1 \cdot \frac{13}{5} + 3 \cdot \frac{9}{5} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{26 + 9}{5} \\
\frac{13 + 27}{5} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{35}{5} \\
\frac{40}{5} \\
\end{pmatrix}
= \begin{pmatrix}
7 \\
8 \\
\end{pmatrix}
= b
$$

Both methods yield the exact same solution vector, confirming correctness.

---

**Step 4: Comparison of Methods and Essential Steps**

1. **Step-by-step breakdown:**

   * **Method 1 ($A^{-1}b$):**
     * Step 1: Compute $\det A$ ($1$ determinant computation).
     * Step 2: Form $A^{-1}$ using the $2 \times 2$ inverse formula ($4$ entry swaps/signs and scalar multiplication).
     * Step 3: Perform matrix-vector multiplication $A^{-1}b$ ($4$ scalar multiplications and $2$ additions).
     * *Total work:* Requires computing all $4$ entries of the inverse matrix before using the specific values of $b$.

   * **Method 2 (Gaussian elimination):**
     * Step 1: Swap rows $R_1 \leftrightarrow R_2$ to obtain a unit pivot.
     * Step 2: One row operation ($R_2 \leftarrow R_2 - 2R_1$) to reach upper-triangular echelon form.
     * Step 3: Back-substitution for $x_2$ and then $x_1$ ($2$ substitutions).
     * *Total work:* Transforms only the $2 \times 2$ matrix and the single vector $b$ simultaneously.

2. **Which method is simpler in this example?**
   * In this specific $2 \times 2$ problem:
     * **Gaussian elimination** is slightly simpler because it requires only one row subtraction and straightforward back-substitution without explicitly constructing all entries of an auxiliary matrix.
     * However, because $2 \times 2$ matrix inversion has a direct formula, **both methods have similar simplicity** at this scale.
   * **General takeaway:**
     * For solving a **single system** $Ax = b$ of larger size ($n \ge 3$), **Gaussian elimination** is significantly simpler and faster ($\sim \frac{1}{3}n^3$ operations vs $\sim \frac{4}{3}n^3$ operations for full matrix inversion followed by multiplication).
     * The **matrix inverse method** becomes superior when solving $Ax = b$ for **multiple different right-hand vectors** $b_1, b_2, \dots, b_k$, because $A^{-1}$ only needs to be calculated once.

---

### Final Answer

1. **Solution Vector (Both Methods):**

   $$
   x = \begin{pmatrix}
   \frac{13}{5} \\
   \frac{9}{5} \\
   \end{pmatrix}
   = \begin{pmatrix}
   2.6 \\
   1.8 \\
   \end{pmatrix}
   $$

2. **Comparison of Steps:**
   * Method 1 requires computing $\det A$, constructing the full inverse $A^{-1}$, and performing matrix-vector multiplication $A^{-1}b$.
   * Method 2 requires one row operation ($R_2 \leftarrow R_2 - 2R_1$) on the augmented matrix followed by back-substitution.

3. **Simpler Method:**
   * For this single system, **Gaussian elimination** is simpler because it avoids computing the full inverse matrix and directly solves for the unknowns.
