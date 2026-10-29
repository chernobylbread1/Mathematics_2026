### Essential Formulas

1. **Classification of Linear Systems Depending on Parameters:**
   A system of linear equations $Ax = b$ can exhibit three mutually exclusive behaviors:
   * **Exactly one solution (Unique):** $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = n$ (full column rank; $\det A \neq 0$ for square systems).
   * **Infinitely many solutions:** $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) < n$ (consistent, but at least one free variable).
   * **No solution (Inconsistent):** $\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$ (a contradiction row appears: $0 = c$ with $c \neq 0$).

2. **Determinant Criterion for $2 \times 2$ Systems:**
   For a $2 \times 2$ system $Ax = b$:

   $$
   \det A = 0 \implies \mathrm{rank}(A) \le 1 < 2
   $$

   When $\det A = 0$, the system can **never** have a unique solution; it must either have infinitely many solutions or no solution, depending entirely on whether the right-hand constants are compatible.

---

### Problem Statement

Analyze, depending on the parameter $a$, the system

$$
\begin{cases}
x+y=2, \\
ax+ay=4. \\
\end{cases}
$$

Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

> **Why this exercise:** teaches how to analyze a parameter without assuming in advance that all theoretically possible cases must occur in a specific system.

---

### Solution

**Step 1: Set up the Augmented Matrix and Perform Elimination**

Write the augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
a & a & \mid & 4 \\
\end{pmatrix}
$$

Apply the elementary row operation $R_2 \leftarrow R_2 - a R_1$ to eliminate the entry in the first column of the second row:

$$
R_2 = (a - a\cdot 1, \ a - a\cdot 1 \ \mid \ 4 - a\cdot 2) = (0, \ 0 \ \mid \ 4 - 2a)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 4 - 2a \\
\end{pmatrix}
$$

The second row translates to the scalar equation:

$$
0x + 0y = 4 - 2a
$$

---

**Step 2: Case Analysis Based on the Value of $a$**

The nature of the solutions depends on whether $4 - 2a$ equals zero or not:

* **Case 1: $4 - 2a = 0 \iff 2a = 4 \iff a = 2$**

  When $a = 2$, the second row becomes:

  $$
  0x + 0y = 0
  $$

  The augmented matrix is:

  $$
  \begin{pmatrix}
  1 & 1 & \mid & 2 \\
  0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

  Here:

  $$
  \mathrm{rank}(A) = 1 = \mathrm{rank}([A \mid b]) < n = 2
  $$

  The system is consistent with $n - r = 2 - 1 = 1$ free variable.
  Setting $y = t \in \mathbb{R}$, we get $x = 2 - t$.
  Therefore, for $a = 2$, there are **infinitely many solutions**.

* **Case 2: $4 - 2a \neq 0 \iff a \neq 2$**

  When $a \neq 2$, the constant $c = 4 - 2a$ is non-zero. The second row yields:

  $$
  0x + 0y = 4 - 2a \neq 0 \implies 0 = 4 - 2a
  $$

  This is an impossible contradiction ($0$ equals a non-zero number).
  Here:

  $$
  \mathrm{rank}(A) = 1 < 2 = \mathrm{rank}([A \mid b])
  $$

  Therefore, for all $a \neq 2$, there is **no solution** (the system is inconsistent).
  Notice that this includes $a = 0$, where the second equation becomes $0 = 4$, which is also contradictory.

---

**Step 3: Why Exactly One Solution Cannot Occur**

Consider the coefficient matrix $A$:

$$
A = \begin{pmatrix}
1 & 1 \\
a & a \\
\end{pmatrix}
$$

Compute its determinant:

$$
\det A = (1)(a) - (1)(a) = a - a = 0
$$

The determinant $\det A$ is identically zero for **all** values of $a \in \mathbb{R}$.
For a square linear system to possess a unique solution, the coefficient matrix must be invertible, which requires $\det A \neq 0$ (or equivalently, $\mathrm{rank}(A) = 2$).
Because $\mathrm{rank}(A) = 1 < 2$ for all $a$:
* The rows (and columns) of $A$ are linearly dependent for every choice of $a$.
* The left-hand sides of the two equations are always parallel: $ax + ay = a(x + y)$.
* As a result, the system can never constrain both degrees of freedom simultaneously to a single point.
* Hence, **the case of exactly one solution never occurs**.

---

### Final Answer

1. **Occurring Cases:**
   * **Infinitely many solutions:** occurs when $a = 2$.
     The parametric solution is:

     $$
     (x, y) = (2 - t, t), \qquad t \in \mathbb{R}
     $$

   * **No solution (Inconsistent):** occurs when $a \neq 2$.

2. **The Case That Cannot Occur:**
   * **Exactly one solution** cannot occur for any real value of $a$.
   * **Reason:** The determinant $\det A = a - a = 0$ is identically zero for all $a$, meaning the coefficient matrix never has full rank ($\mathrm{rank}(A) = 1 < 2$). Thus, the two equations are either contradictory ($a \neq 2$) or redundant ($a = 2$), but never independent.

