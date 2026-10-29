### Essential Formulas

1. **Overdetermined Linear Systems ($m > n$):**
   A system with more equations ($m$) than unknowns ($n$) is called **overdetermined**.
   * Such a system is consistent if and only if the extra equations are linearly dependent on the independent equations, so that:

     $$
     \mathrm{rank}(A) = \mathrm{rank}([A \mid b]) \le n
     $$

   * If the right-hand side vector $b$ does not lie precisely in the column space of $A$, the system becomes **inconsistent** ($\mathrm{rank}([A \mid b]) > \mathrm{rank}(A)$).

2. **Geometric Interpretation in $\mathbb{R}^2$ (Three Lines):**
   In the coordinate plane, each linear equation defines a line.
   * A system of three lines has a unique solution if and only if all three lines are **concurrent** (they all pass through the exact same point of intersection).
   * Even an infinitesimally small shift in one line's constant displaces it away from the intersection point, turning the concurrency into a non-degenerate triangle where no single point satisfies all three equations.

---

### Problem Statement

Compare the systems

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3 \\
\end{cases}
$$

and

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3.1. \\
\end{cases}
$$

Check the consistency of each system and explain why a small change in one number can change the type of the system.

> **Why this exercise:** shows the difference between a consistent and an inconsistent system without introducing new theory.

---

### Solution

**Step 1: Analyze and Solve System 1**

The first system is:

$$
\begin{cases}
x + y = 2 \\
2x - y = 1 \\
3x = 3 \\
\end{cases}
$$

Set up the augmented matrix $[A \mid b_1]$:

$$
[A \mid b_1] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & -1 & \mid & 1 \\
3 & 0 & \mid & 3 \\
\end{pmatrix}
$$

Apply Gaussian elimination:
* $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2(1), \ -1 - 2(1) \ \mid \ 1 - 2(2)) = (0, \ -3 \ \mid \ -3)
  $$

* $R_3 \leftarrow R_3 - 3R_1$:

  $$
  R_3 = (3 - 3(1), \ 0 - 3(1) \ \mid \ 3 - 3(2)) = (0, \ -3 \ \mid \ -3)
  $$

The matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & -3 & \mid & -3 \\
\end{pmatrix}
$$

* $R_3 \leftarrow R_3 - R_2$:

  $$
  R_3 = (0 - 0, \ -3 - (-3) \ \mid \ -3 - (-3)) = (0, \ 0 \ \mid \ 0)
  $$

The echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* **Consistency check:**
  Row 3 is $(0, 0 \mid 0)$, so there is no contradiction.
  The rank is $\mathrm{rank}(A) = \mathrm{rank}([A \mid b_1]) = 2 = n$.
  The system is **consistent** and has **exactly one unique solution**:
  - From row 2: $-3y = -3 \implies y = 1$.
  - From row 1: $x + 1 = 2 \implies x = 1$.
  Unique solution: $(x, y) = (1, 1)$.

Notice that equation 3 is simply the sum of equations 1 and 2:

$$
(x + y) + (2x - y) = 2 + 1 \iff 3x = 3
$$

---

**Step 2: Analyze and Solve System 2**

The second system is:

$$
\begin{cases}
x + y = 2 \\
2x - y = 1 \\
3x = 3.1 \\
\end{cases}
$$

Set up the augmented matrix $[A \mid b_2]$:

$$
[A \mid b_2] = \begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & -1 & \mid & 1 \\
3 & 0 & \mid & 3.1 \\
\end{pmatrix}
$$

Apply the same elimination steps:
* $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (0, \ -3 \ \mid \ -3)
  $$

* $R_3 \leftarrow R_3 - 3R_1$:

  $$
  R_3 = (3 - 3(1), \ 0 - 3(1) \ \mid \ 3.1 - 3(2)) = (0, \ -3 \ \mid \ 3.1 - 6) = (0, \ -3 \ \mid \ -2.9)
  $$

The matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & -3 & \mid & -2.9 \\
\end{pmatrix}
$$

* $R_3 \leftarrow R_3 - R_2$:

  $$
  R_3 = (0 - 0, \ -3 - (-3) \ \mid \ -2.9 - (-3)) = (0, \ 0 \ \mid \ 0.1)
  $$

The echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & 0 & \mid & 0.1 \\
\end{pmatrix}
$$

* **Consistency check:**
  Row 3 translates to:

  $$
  0x + 0y = 0.1 \implies 0 = 0.1
  $$

  This is a contradiction. Here:

  $$
  \mathrm{rank}(A) = 2 < 3 = \mathrm{rank}([A \mid b_2])
  $$

  Therefore, System 2 is **inconsistent** (it has **no solution**).

---

**Step 3: Why a Small Change in One Number Changes the System Type**

1. **Algebraic Perspective:**
   The first two equations determine the values of the two unknowns completely and uniquely:

   $$
   (x, y) = (1, 1)
   $$

   Once $x$ and $y$ are fixed by the first two equations, the left-hand side of the third equation is locked:

   $$
   3x = 3(1) = 3
   $$

   There is only **one single number** that the right-hand side of equation 3 can be for the system to remain consistent, namely $3$.
   Any deviation whatsoever, no matter how small (such as $3.1$, $3.001$, or $2.999$), creates a mismatch between the locked value of $3x$ and the requested target, instantly causing a contradiction ($3 \neq 3.1$).

2. **Geometric Perspective (Concurrency of Three Lines):**
   * In System 1, the three lines $L_1: x+y=2$, $L_2: 2x-y=1$, and $L_3: x=1$ all pass through the exact same point $(1, 1)$. They are **concurrent lines**.
   * In System 2, the third line is shifted to $x = \frac{3.1}{3} \approx 1.0333$. This vertical line no longer passes through $(1, 1)$.
   * Instead, the three lines intersect in pairs at three distinct points, forming a small triangle. Because there is no point common to all three lines simultaneously, the intersection of the three sets is empty.
   * Concurrency in a 2D plane is an unstable geometric property: a random or perturbed third line almost never passes through the intersection of two pre-existing lines.

---

### Final Answer

1. **Consistency of System 1:**
   **Consistent** with exactly one unique solution:

   $$
   (x, y) = (1, 1)
   $$

2. **Consistency of System 2:**
   **Inconsistent** (no solution, $\emptyset$) due to the contradictory echelon row $(0, 0 \mid 0.1)$.

3. **Explanation:**
   The first two equations uniquely fix the point $(x, y) = (1, 1)$. This requires $3x$ to evaluate to $3$. In System 1, the right-hand side is $3$, so the third equation is satisfied (concurrent lines). In System 2, changing $3$ to $3.1$ creates a geometric mismatch ($3 \neq 3.1$), shifting the third line away from the intersection point and making the system inconsistent.

