### Essential Formulas

1. **Degrees of Freedom and Free Variables:**
   For a consistent system $Ax = b$ with $n$ unknowns and $\mathrm{rank}(A) = r$:
   * $r$ is the number of pivot (leading) variables.
   * The number of **free variables** (degrees of freedom) is:

     $$
     k = n - r
     $$

   * If $k > 0$, the system has **infinitely many solutions**.

2. **Parametric Form of the General Solution:**
   Each free variable is assigned an independent real parameter ($t, s \in \mathbb{R}$). Back-substitution then expresses the pivot variables in terms of these parameters.
   The complete solution can be expressed as:

   $$
   x = x_p + t_1 v_1 + t_2 v_2 + \cdots + t_k v_k
   $$

   where $x_p$ is a particular solution and $\{v_1, \dots, v_k\}$ are basis vectors of the null space $\mathrm{ker}(A)$.

3. **Row Echelon Form Structure:**
   A row of all zeros $(0, 0, \dots, 0 \mid 0)$ indicates a redundant equation that is a linear combination of other equations and does not restrict the solution set.

---

### Problem Statement

Solve

$$
\begin{cases}
x+y+z=2, \\
2x+2y+2z=4, \\
x-y+z=0. \\
\end{cases}
$$

Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

> **Why this exercise:** shows the case of multiple solutions and teaches a simple parametric description.

---

### Solution

**Step 1: Set up the Augmented Matrix**

Write the system as an augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
2 & 2 & 2 & \mid & 4 \\
1 & -1 & 1 & \mid & 0 \\
\end{pmatrix}
$$

---

**Step 2: Perform Gaussian Elimination**

* **Eliminate entry in row 2:** Apply $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2\cdot 1, \ 2 - 2\cdot 1, \ 2 - 2\cdot 1 \ \mid \ 4 - 2\cdot 2) = (0, \ 0, \ 0 \ \mid \ 0)
  $$

* **Eliminate entry in row 3:** Apply $R_3 \leftarrow R_3 - R_1$:

  $$
  R_3 = (1 - 1\cdot 1, \ -1 - 1\cdot 1, \ 1 - 1\cdot 1 \ \mid \ 0 - 1\cdot 2) = (0, \ -2, \ 0 \ \mid \ -2)
  $$

The matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & 0 & 0 & \mid & 0 \\
0 & -2 & 0 & \mid & -2 \\
\end{pmatrix}
$$

* **Swap rows to bring non-zero row above zero row ($R_2 \leftrightarrow R_3$):**

  $$
  \begin{pmatrix}
  1 & 1 & 1 & \mid & 2 \\
  0 & -2 & 0 & \mid & -2 \\
  0 & 0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

* **Normalize row 2 ($R_2 \leftarrow -\frac{1}{2}R_2$):**

  $$
  \begin{pmatrix}
  1 & 1 & 1 & \mid & 2 \\
  0 & 1 & 0 & \mid & 1 \\
  0 & 0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

The matrix is now in reduced/echelon form.

---

**Step 3: Identify Pivot and Free Variables**

* Pivot in Column 1 (Row 1): unknown $x$ is a **leading (pivot) variable**.
* Pivot in Column 2 (Row 2): unknown $y$ is a **leading (pivot) variable**.
* Column 3 contains no pivot: unknown $z$ is a **free variable**.

Because there are $n = 3$ unknowns and $\mathrm{rank}(A) = 2$ pivots, the number of free variables is $3 - 2 = 1$. The system has **infinitely many solutions**.

Assign a free parameter $t \in \mathbb{R}$ to $z$:

$$
z = t
$$

---

**Step 4: Express Solution in Parametric Form**

* From row 2:

  $$
  y + 0\cdot z = 1 \implies y = 1
  $$

* From row 1:

  $$
  x + y + z = 2
  $$

  Substitute $y = 1$ and $z = t$:

  $$
  x + 1 + t = 2 \implies x = 1 - t
  $$

Thus, the general solution in parametric scalar form is:

$$
\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t, \\
\end{cases}
\qquad t \in \mathbb{R}
$$

In vector form:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
1 - t \\
1 \\
t \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
1 \\
0 \\
\end{pmatrix}
+ t \begin{pmatrix}
-1 \\
0 \\
1 \\
\end{pmatrix}, \qquad t \in \mathbb{R}
$$

Geometrically, this solution set represents a line in three-dimensional space $\mathbb{R}^3$ passing through $(1, 1, 0)$ with direction vector $(-1, 0, 1)$.

---

**Step 5: Verification for a Chosen Parameter Value**

Choose the specific parameter value $t = 2$:

* The corresponding coordinates are:

  $$
  x = 1 - 2 = -1, \qquad y = 1, \qquad z = 2
  $$

  Point: $(-1, 1, 2)$.

* Substitute this point into the three original equations:
  1. Equation 1:

     $$
     x + y + z = -1 + 1 + 2 = 2
     $$

     Matches right-hand side $2$.

  2. Equation 2:

     $$
     2x + 2y + 2z = 2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4
     $$

     Matches right-hand side $4$.

  3. Equation 3:

     $$
     x - y + z = -1 - 1 + 2 = 0
     $$

     Matches right-hand side $0$.

All three equations are satisfied, verifying the parametric solution.

---

### Final Answer

1. **Free Variable:**
   The variable $z$ is free (it has no pivot in its column).

2. **Parametric Solution:**

   $$
   \begin{pmatrix}
   x \\
   y \\
   z \\
   \end{pmatrix}
   = \begin{pmatrix}
   1 \\
   1 \\
   0 \\
   \end{pmatrix}
   + t \begin{pmatrix}
   -1 \\
   0 \\
   1 \\
   \end{pmatrix}, \qquad t \in \mathbb{R}
   $$

   or equivalently:

   $$
   x = 1 - t, \qquad y = 1, \qquad z = t \quad (t \in \mathbb{R})
   $$

3. **Check for $t = 2$:**
   For $t = 2$, $(x, y, z) = (-1, 1, 2)$. Substituting into the original equations yields $2 = 2$, $4 = 4$, and $0 = 0$.
