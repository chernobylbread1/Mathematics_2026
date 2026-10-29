### Essential Formulas

1. **Classification Criteria from Echelon Form:**
   After applying minimal row operations to bring an augmented matrix $[A \mid b]$ to row echelon form:
   * **No Solution (Inconsistent):**
     There is a row of the form:

     $$
     \begin{pmatrix}
     0 & 0 & \cdots & 0 & \mid & c \\
     \end{pmatrix} \quad (c \neq 0)
     $$

     meaning $\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$.

   * **Infinitely Many Solutions:**
     The system is consistent ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = r$), but $r < n$ (there is at least one row of zeros and at least one free variable, $k = n - r > 0$).

   * **Exactly One Solution (Unique):**
     The system is consistent and every column of $A$ contains a non-zero pivot ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = n$).

2. **Geometric Interpretation in $\mathbb{R}^2$:**
   * Two intersecting lines with distinct slopes $\implies$ **one solution**.
   * Two coincident (identical) lines $\implies$ **infinitely many solutions**.
   * Two parallel non-intersecting lines $\implies$ **no solution**.

---

### Problem Statement

For each of the following systems, perform only as much elimination as necessary to recognize its type:

**System 1**

$$
\begin{cases}
x+y=2, \\
x-y=0, \\
\end{cases}
$$

**System 2**

$$
\begin{cases}
x+y=2, \\
2x+2y=4, \\
\end{cases}
$$

**System 3**

$$
\begin{cases}
x+y=2, \\
2x+2y=5. \\
\end{cases}
$$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

> **Why this exercise:** brings together the three basic cases and requires recognizing them from the structure after elimination.

---

### Solution

**Step 1: Analyze System 1**

The system is:

$$
\begin{cases}
x + y = 2 \\
x - y = 0 \\
\end{cases}
$$

Write the augmented matrix $[A_1 \mid b_1]$:

$$
[A_1 \mid b_1] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
1 & -1 & \mid & 0 \\
\end{pmatrix}
$$

Perform one elimination step ($R_2 \leftarrow R_2 - R_1$):

$$
R_2 = (1 - 1, \ -1 - 1 \ \mid \ 0 - 2) = (0, \ -2 \ \mid \ -2)
$$

The echelon matrix is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -2 & \mid & -2 \\
\end{pmatrix}
$$

* **Structural Recognition:**
  - Row 1 has pivot $1$ in column 1.
  - Row 2 has pivot $-2$ in column 2.
  - The number of pivots is $r = 2$, which equals the number of unknowns ($n = 2$).
  - There are no rows of zeros and no contradictions.
* **Justification:**
  Because $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 2 = n$, the system has full rank.
* **Classification:** **Exactly one solution** (specifically, $-2y = -2 \implies y = 1$, and $x + 1 = 2 \implies x = 1$, so $(x, y) = (1, 1)$).

---

**Step 2: Analyze System 2**

The system is:

$$
\begin{cases}
x + y = 2 \\
2x + 2y = 4 \\
\end{cases}
$$

Write the augmented matrix $[A_2 \mid b_2]$:

$$
[A_2 \mid b_2] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 4 \\
\end{pmatrix}
$$

Perform one elimination step ($R_2 \leftarrow R_2 - 2R_1$):

$$
R_2 = (2 - 2(1), \ 2 - 2(1) \ \mid \ 4 - 2(2)) = (0, \ 0 \ \mid \ 0)
$$

The echelon matrix is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* **Structural Recognition:**
  - Row 1 has pivot $1$ in column 1.
  - Row 2 is completely zero: $(0, 0 \mid 0)$, indicating that the second equation is a scalar multiple of the first ($2 \times E_1$).
  - The rank is $r = 1$, while the number of unknowns is $n = 2$.
  - Number of free variables is $k = n - r = 2 - 1 = 1$.
* **Justification:**
  The system is consistent ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 1$) but underdetermined, having $1$ free variable.
* **Classification:** **Infinitely many solutions** (parameterized by $y = t \in \mathbb{R}$, yielding $(x, y) = (2 - t, t)$).

---

**Step 3: Analyze System 3**

The system is:

$$
\begin{cases}
x + y = 2 \\
2x + 2y = 5 \\
\end{cases}
$$

Write the augmented matrix $[A_3 \mid b_3]$:

$$
[A_3 \mid b_3] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 5 \\
\end{pmatrix}
$$

Perform one elimination step ($R_2 \leftarrow R_2 - 2R_1$):

$$
R_2 = (2 - 2(1), \ 2 - 2(1) \ \mid \ 5 - 2(2)) = (0, \ 0 \ \mid \ 5 - 4) = (0, \ 0 \ \mid \ 1)
$$

The echelon matrix is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

* **Structural Recognition:**
  - Row 2 translates to the equation:

    $$
    0x + 0y = 1 \implies 0 = 1
    $$

  - This is an impossible contradiction.
  - The rank of the coefficient matrix is $\mathrm{rank}(A) = 1$, while the rank of the augmented matrix is $\mathrm{rank}([A \mid b]) = 2$.
* **Justification:**
  Because $\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$, the system contains a contradictory equation.
* **Classification:** **No solution** (inconsistent system, $\emptyset$).

---

**Step 4: Summary Comparison of the Three Types**

* **System 1:**
  - Echelon form:

    $$
    \begin{pmatrix}
    1 & 1 & \mid & 2 \\
    0 & -2 & \mid & -2 \\
    \end{pmatrix}
    $$

  - Rank: $\mathrm{rank}(A) = 2 = \mathrm{rank}([A \mid b]) = n$
  - Geometric interpretation: Two lines intersecting at the unique point $(1, 1)$
  - Classification: **Exactly one solution**

* **System 2:**
  - Echelon form:

    $$
    \begin{pmatrix}
    1 & 1 & \mid & 2 \\
    0 & 0 & \mid & 0 \\
    \end{pmatrix}
    $$

  - Rank: $\mathrm{rank}(A) = 1 = \mathrm{rank}([A \mid b]) < n$
  - Geometric interpretation: Two coincident (identical) lines
  - Classification: **Infinitely many solutions**

* **System 3:**
  - Echelon form:

    $$
    \begin{pmatrix}
    1 & 1 & \mid & 2 \\
    0 & 0 & \mid & 1 \\
    \end{pmatrix}
    $$

  - Rank: $\mathrm{rank}(A) = 1 < 2 = \mathrm{rank}([A \mid b])$
  - Geometric interpretation: Two parallel, distinct lines
  - Classification: **No solution**

---

### Final Answer

1. **System 1:**
   * **Classification:** **Exactly one solution**
   * **Justification:** After one row operation, the matrix has $2$ pivots for $2$ unknowns ($\mathrm{rank}(A) = 2 = n$), uniquely determining $(x, y) = (1, 1)$.

2. **System 2:**
   * **Classification:** **Infinitely many solutions**
   * **Justification:** Row reduction produces the zero row $(0, 0 \mid 0)$. The system is consistent with rank $r = 1 < n = 2$, leaving $1$ free variable.

3. **System 3:**
   * **Classification:** **No solution** (Inconsistent)
   * **Justification:** Row reduction produces the contradictory row $(0, 0 \mid 1)$, which corresponds to $0 = 1$.
