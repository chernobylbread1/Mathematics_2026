### Essential Formulas

1. **Parametric Systems and Validity of Row Operations:**
   In Gaussian elimination involving a parameter $t$:
   * Row scaling $R_i \leftarrow \frac{1}{\alpha(t)} R_i$ or division during back-substitution requires $\alpha(t) \neq 0$.
   * Any parameter value that causes a pivot to vanish ($\alpha(t) = 0$) must be isolated and analyzed separately as a special case.

2. **Classification of Solutions for Square Systems:**
   For an $n \times n$ system $A(t)x = b$:
   * If all $n$ pivots in row echelon form are non-zero ($\det A(t) \neq 0$), the system has **exactly one solution**.
   * If a pivot position becomes zero:
     - If the corresponding right-hand entry is non-zero, the row reads $0 = c \ (c \neq 0)$, meaning **no solution** (inconsistent).
     - If both sides of the row are zero and no contradictions occur elsewhere, the system has **infinitely many solutions**.

---

### Problem Statement

Analyze the number of solutions depending on $t$:

$$
\begin{cases}
x+y+z=1, \\
x+ty+z=2, \\
x+y+tz=3. \\
\end{cases}
$$

Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

> **Why this exercise:** develops parametric analysis while still relying only on elimination.

---

### Solution

**Step 1: Set up the Augmented Matrix**

Write the system as an augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
1 & t & 1 & \mid & 2 \\
1 & 1 & t & \mid & 3 \\
\end{pmatrix}
$$

The top-left entry $a_{11} = 1$ is a fixed non-zero pivot independent of $t$.

---

**Step 2: Perform Elimination to Upper-Triangular Form**

Eliminate the first entry in rows 2 and 3 by subtracting row 1:

* **Row 2:** Apply $R_2 \leftarrow R_2 - R_1$:

  $$
  R_2 = (1 - 1, \ t - 1, \ 1 - 1 \ \mid \ 2 - 1) = (0, \ t - 1, \ 0 \ \mid \ 1)
  $$

* **Row 3:** Apply $R_3 \leftarrow R_3 - R_1$:

  $$
  R_3 = (1 - 1, \ 1 - 1, \ t - 1 \ \mid \ 3 - 1) = (0, \ 0, \ t - 1 \ \mid \ 2)
  $$

The augmented matrix is now in upper-triangular echelon form:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & t - 1 & 0 & \mid & 1 \\
0 & 0 & t - 1 & \mid & 2 \\
\end{pmatrix}
$$

Translating rows 2 and 3 back into equations:

* Row 2: $(t - 1)y = 1$
* Row 3: $(t - 1)z = 2$

---

**Step 3: Identify the Critical Parameter Value**

In the standard elimination/back-substitution procedure, the next steps would be:

$$
y = \frac{1}{t - 1}, \qquad z = \frac{2}{t - 1}
$$

Division by $t - 1$ is mathematically valid **only if** $t - 1 \neq 0$, which means $t \neq 1$.
Therefore, the standard calculation step **ceases to be valid when $t = 1$**.

We must analyze the two cases separately:
1. $t = 1$ (the singular value)
2. $t \neq 1$ (the general case)

---

**Step 4: Case 1 — When $t = 1$**

Substitute $t = 1$ directly into the echelon matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & 0 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 2 \\
\end{pmatrix}
$$

Examining row 2:

$$
0\cdot x + 0\cdot y + 0\cdot z = 1 \implies 0 = 1
$$

Examining row 3:

$$
0\cdot x + 0\cdot y + 0\cdot z = 2 \implies 0 = 2
$$

Both rows yield impossible contradictions ($0 = 1$ and $0 = 2$).
In terms of ranks:

$$
\mathrm{rank}(A) = 1, \qquad \mathrm{rank}([A \mid b]) = 3
$$

Since $\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$, the system is inconsistent.
Therefore, for $t = 1$, the system has **no solution**.

---

**Step 5: Case 2 — When $t \neq 1$**

When $t \neq 1$, the quantity $t - 1 \neq 0$.
The matrix has $3$ non-zero pivots on the main diagonal:
* Pivot 1: $1 \neq 0$
* Pivot 2: $t - 1 \neq 0$
* Pivot 3: $t - 1 \neq 0$

Thus:

$$
\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 3 = n
$$

The system has full rank, which guarantees **exactly one unique solution**.
We solve for the unknowns by back-substitution:

* From row 3:

  $$
  z = \frac{2}{t - 1}
  $$

* From row 2:

  $$
  y = \frac{1}{t - 1}
  $$

* From row 1:

  $$
  x + y + z = 1 \implies x = 1 - y - z
  $$

  Substitute $y$ and $z$:

  $$
  x = 1 - \frac{1}{t - 1} - \frac{2}{t - 1} = 1 - \frac{3}{t - 1} = \frac{(t - 1) - 3}{t - 1} = \frac{t - 4}{t - 1}
  $$

Thus, for each $t \neq 1$, the unique solution is:

$$
(x, y, z) = \left(\frac{t - 4}{t - 1}, \ \frac{1}{t - 1}, \ \frac{2}{t - 1}\right)
$$

---

**Step 6: Summary of Possible Behaviors**

* Does the case of **infinitely many solutions** ever occur?
  No. Infinitely many solutions would require $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) < 3$. At $t = 1$, the coefficient rows become zero, but the constants remain non-zero ($1$ and $2$), leading immediately to a contradiction rather than a redundant row. For all other values ($t \neq 1$), the rank is $3$. Hence, infinitely many solutions cannot occur for any real value of $t$.

---

### Final Answer

1. **Classification Depending on $t$:**
   * **For $t \neq 1$:** The system has **exactly one unique solution**:

     $$
     x = \frac{t - 4}{t - 1}, \qquad y = \frac{1}{t - 1}, \qquad z = \frac{2}{t - 1}
     $$

   * **For $t = 1$:** The system has **no solution** (inconsistent).

2. **Critical Value Analysis:**
   The standard elimination step of solving $y = \frac{1}{t-1}$ and $z = \frac{2}{t-1}$ breaks down at $t = 1$ due to division by zero. Substituting $t = 1$ yields the contradiction $0 = 1$, confirming there are no solutions.

