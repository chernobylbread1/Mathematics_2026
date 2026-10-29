### Essential Formulas

1. **Computational Cost of Linear System Solvers:**
   For an $n \times n$ system $Ax = b$:
   * **Gaussian Elimination with Back-Substitution:** Requires $\sim \frac{2}{3}n^3$ arithmetic operations for elimination on $[A \mid b]$ and $\sim n^2$ operations for back-substitution.
   * **Matrix Inversion:** Computing $A^{-1}$ via Gauss–Jordan elimination on $[A \mid I]$ requires $\sim 2n^3$ operations, plus $\sim 2n^2$ operations to compute $x = A^{-1}b$.
   * For a **single system**, Gaussian elimination is roughly $3$ times faster than calculating $A^{-1}$.

2. **Systems with Multiple Right-Hand Sides:**
   When solving $k$ systems $Ax = b_1, Ax = b_2, \dots, Ax = b_k$ sharing the same matrix $A$:
   * If $A^{-1}$ is already precomputed, each solution vector is obtained in $O(n^2)$ operations via $x_i = A^{-1}b_i$.
   * Alternatively, simultaneous Gaussian elimination on $[A \mid b_1 \mid b_2 \mid \cdots \mid b_k]$ row-reduces $A$ once in $\frac{2}{3}n^3$ operations and transforms all $k$ vectors simultaneously.

3. **Special Matrix Structures (Triangular Systems):**
   * If $A$ is **upper-triangular** ($a_{ij} = 0$ for $i > j$), no elimination steps are needed. The system is solved directly via **back-substitution** in $O(n^2)$ operations.
   * If $A$ is **lower-triangular** ($a_{ij} = 0$ for $i < j$), the system is solved directly via **forward-substitution**.

---

### Problem Statement

Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix

$$
\begin{cases}
2x-y=3, \\
4y=8; \\
\end{cases}
$$

2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

> **Why this exercise:** practices choosing a method based on the structure of the problem instead of solving another small system by two methods.

---

### Solution

**Step 1: Case 1 — Triangular Coefficient Matrix**

* **Structure of the problem:**
  The coefficient matrix is:

  $$
  A = \begin{pmatrix}
  2 & -1 \\
  0 & 4 \\
  \end{pmatrix}
  $$

  The entry below the main diagonal is already zero ($a_{21} = 0$), so $A$ is an **upper-triangular matrix**.

* **Choice of method:**
  **Direct back-substitution**.
  * **Justification:** Performing row operations (Gaussian elimination) is completely redundant because the matrix is already in row echelon form. Calculating $A^{-1}$ would require extra operations to invert a matrix whose solution is already decoupled from bottom to top.

* **Complete execution:**
  From the second equation:

  $$
  4y = 8 \implies y = \frac{8}{4} = 2
  $$

  Substitute $y = 2$ directly into the first equation:

  $$
  2x - y = 3 \implies 2x - 2 = 3
  $$

  $$
  2x = 5 \implies x = \frac{5}{2} = 2.5
  $$

  The unique solution is:

  $$
  (x, y) = \left(\frac{5}{2}, 2\right)
  $$

---

**Step 2: Case 2 — Three Systems with the Same Invertible Matrix and Known $A^{-1}$**

* **Structure of the problem:**
  We must solve:

  $$
  Ax = b_1, \qquad Ax = b_2, \qquad Ax = b_3
  $$

  where the coefficient matrix $A$ is fixed and invertible, and $A^{-1}$ has already been calculated and is known.

* **Choice of method:**
  **Matrix-vector multiplication: $x_i = A^{-1}b_i$ for each $i \in \{1, 2, 3\}$.**

* **Plan and Computational Breakdown:**
  1. For each right-hand side $b_i$, compute the solution directly:

     $$
     x_1 = A^{-1}b_1, \qquad x_2 = A^{-1}b_2, \qquad x_3 = A^{-1}b_3
     $$

  2. **Reusable Part:** The matrix $A^{-1}$ is the reusable component. Since it is already known, it requires $0$ operations to obtain and is multiplied by each $b_i$ at an efficient cost of $O(n^2)$ scalar multiplications and additions per vector.
  3. **Unnecessary Work:** Running Gaussian elimination three separate times on $[A \mid b_1]$, $[A \mid b_2]$, and $[A \mid b_3]$ from scratch would be highly inefficient, as it would repeat the row reduction of matrix $A$ three times over ($3 \times O(n^3/3)$ operations), discarding the value of having $A^{-1}$ readily available.

---

**Step 3: Case 3 — One $3 \times 3$ System with Unknown $A^{-1}$ (Single Solution Needed)**

* **Structure of the problem:**
  A single linear system $Ax = b$ with $n = 3$, where only one solution vector $x$ is requested, and $A^{-1}$ is not given.

* **Choice of method:**
  **Gaussian elimination with back-substitution on the augmented matrix $[A \mid b]$.**

* **Plan and Computational Breakdown:**
  1. Form the augmented matrix $[A \mid b]$ of size $3 \times 4$.
  2. Perform row operations to convert the matrix into upper-triangular echelon form ($[U \mid c]$).
  3. Perform back-substitution to find the unknowns sequentially ($x_3$, then $x_2$, then $x_1$).
  4. **Why Matrix Inversion is Unnecessary:**
     Finding $A^{-1}$ from scratch requires row-reducing the $3 \times 6$ augmented matrix $[A \mid I]$ (which is equivalent to solving three systems with right-hand sides $e_1, e_2, e_3$). This requires roughly $3$ times more operations than reducing the single augmented matrix $[A \mid b]$ ($2n^3$ vs $\frac{2}{3}n^3$).
     Because there is only one vector $b$ and no further systems will be solved, the computed inverse $A^{-1}$ would never be reused. Computing $A^{-1}$ merely to solve a single system constitutes wasteful computation.

---

### Final Answer

1. **Case 1 (Triangular matrix):**
   * **Chosen Method:** Direct back-substitution (elimination is unnecessary).
   * **Solution:**

     $$
     y = 2, \qquad x = \frac{5}{2} = 2.5
     $$

2. **Case 2 (Three systems, same $A$, known $A^{-1}$):**
   * **Chosen Method:** Direct multiplication $x_i = A^{-1}b_i$ for $i = 1, 2, 3$.
   * **Analysis:** $A^{-1}$ is reusable for all three systems at minimal cost ($O(n^2)$ per vector). Running Gaussian elimination three times would needlessly repeat the row reduction of $A$.

3. **Case 3 (One $3 \times 3$ system, unknown $A^{-1}$):**
   * **Chosen Method:** Gaussian elimination on $[A \mid b]$ with back-substitution.
   * **Analysis:** Inverting $A$ from scratch requires approximately three times more work than eliminating $[A \mid b]$. Because there is only a single right-hand side, $A^{-1}$ would have no future utility, making its calculation completely unnecessary.
