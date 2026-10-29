### Essential Formulas

1. **Reading Solutions from Row Echelon Form:**
   Let an augmented matrix $[A \mid b]$ be in row echelon form with $m$ rows and $n$ columns for the coefficient matrix $A$.
   * **Consistency Condition:** The system is consistent if and only if there is no row of the form:

     $$
     \begin{pmatrix}
     0 & 0 & \cdots & 0 & \mid & c \\
     \end{pmatrix} \quad (c \neq 0)
     $$

   * **Number of Pivots (Rank):** Let $r = \mathrm{rank}(A) = \mathrm{rank}([A \mid b])$ be the number of non-zero rows (pivots).
   * **Pivot Variables:** Variables corresponding to columns with pivots.
   * **Free Variables:** Variables corresponding to columns without pivots.
   * **Number of Free Variables (Degrees of Freedom):**

     $$
     k = n - r
     $$

2. **Classification of the Number of Solutions:**
   * If the system is inconsistent: **$0$ solutions**.
   * If the system is consistent and $r = n$ ($k = 0$): **exactly $1$ unique solution**.
   * If the system is consistent and $r < n$ ($k > 0$): **infinitely many solutions** parameterized by $k$ free parameters.

---

### Problem Statement

For the augmented matrix

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 3 \\
0 & 1 & 2 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

> **Why this exercise:** teaches how to read information about solutions directly from row echelon form.

---

### Solution

**Step 1: Analyze the Structure of the Row Echelon Matrix**

Let the unknowns be denoted by $(x_1, x_2, x_3)$ (or $(x, y, z)$).
The given augmented matrix is:

$$
[A \mid b] = \begin{pmatrix}
1 & 2 & -1 & \mid & 3 \\
0 & 1 & 2 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* The matrix is already in **row echelon form** (staircase structure).
* The coefficient matrix $A$ has $m = 3$ rows and $n = 3$ columns.
* There are $2$ non-zero rows:
  - Row 1 has leading entry (pivot) $1$ in column 1.
  - Row 2 has leading entry (pivot) $1$ in column 2.
  - Row 3 is entirely zeros: $(0, 0, 0 \mid 0)$.

Since there is no contradictory row $(0, 0, 0 \mid c)$ with $c \neq 0$, the system is **consistent**.

---

**Step 2: Determine the Number of Free Variables**

* The number of unknowns is:

  $$
  n = 3 \quad (x_1, x_2, x_3)
  $$

* The rank of the matrix (the number of pivots) is:

  $$
  r = 2
  $$

* Columns containing pivots:
  - Column 1 has a pivot in row 1 $\implies x_1$ is a **pivot variable**.
  - Column 2 has a pivot in row 2 $\implies x_2$ is a **pivot variable**.
* Columns without a pivot:
  - Column 3 has no pivot $\implies x_3$ is a **free variable**.

* The number of variables that may be chosen freely is given by the dimension of the solution space:

  $$
  k = n - r = 3 - 2 = 1
  $$

Because the system is consistent and has $1$ free variable, it has **infinitely many solutions**.

---

**Step 3: Solve by Back-Substitution in Parametric Form**

Assign a real parameter $t \in \mathbb{R}$ to the free variable:

$$
x_3 = t
$$

* **From Row 2:**
  The equation is:

  $$
  0x_1 + 1x_2 + 2x_3 = 1 \implies x_2 + 2x_3 = 1
  $$

  Express $x_2$ in terms of $t$:

  $$
  x_2 = 1 - 2t
  $$

* **From Row 1:**
  The equation is:

  $$
  1x_1 + 2x_2 - 1x_3 = 3 \implies x_1 + 2x_2 - x_3 = 3
  $$

  Substitute $x_2 = 1 - 2t$ and $x_3 = t$:

  $$
  x_1 + 2(1 - 2t) - t = 3
  $$

  $$
  x_1 + 2 - 4t - t = 3
  $$

  $$
  x_1 + 2 - 5t = 3 \implies x_1 = 3 - 2 + 5t = 1 + 5t
  $$

---

**Step 4: Vector Representation of the Solution**

The general solution vector is:

$$
x = \begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{pmatrix}
= \begin{pmatrix}
1 + 5t \\
1 - 2t \\
t \\
\end{pmatrix}
$$

Decomposing into a particular solution vector and a homogeneous direction vector:

$$
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
1 \\
0 \\
\end{pmatrix}
+ t \begin{pmatrix}
5 \\
-2 \\
1 \\
\end{pmatrix}, \qquad t \in \mathbb{R}
$$

---

**Step 5: Quick Consistency Check**

Test the particular solution $t = 0$, giving $(x_1, x_2, x_3) = (1, 1, 0)$:
* Row 1: $1(1) + 2(1) - 1(0) = 1 + 2 = 3$ (consistent with $b_1 = 3$).
* Row 2: $0(1) + 1(1) + 2(0) = 1$ (consistent with $b_2 = 1$).
* Row 3: $0 = 0$.

Test the direction vector $(5, -2, 1)$ in the homogeneous system:
* Row 1: $1(5) + 2(-2) - 1(1) = 5 - 4 - 1 = 0$.
* Row 2: $0(5) + 1(-2) + 2(1) = -2 + 2 = 0$.

Both checks confirm the solution.

---

### Final Answer

1. **Number of Solutions:**
   There are **infinitely many solutions** because the system is consistent and has one free variable ($n - r = 3 - 2 = 1$).

2. **How Free Variables Are Determined:**
   The number of free variables is equal to the total number of unknowns ($n = 3$) minus the number of pivots ($r = 2$), giving $3 - 2 = 1$. The non-pivot column corresponds to the free variable $x_3$.

3. **Parametric Form:**

   $$
   \begin{pmatrix}
   x_1 \\
   x_2 \\
   x_3 \\
   \end{pmatrix}
   = \begin{pmatrix}
   1 \\
   1 \\
   0 \\
   \end{pmatrix}
   + t \begin{pmatrix}
   5 \\
   -2 \\
   1 \\
   \end{pmatrix}, \qquad t \in \mathbb{R}
   $$

   or in scalar form:

   $$
   x_1 = 1 + 5t, \qquad x_2 = 1 - 2t, \qquad x_3 = t \quad (t \in \mathbb{R})
   $$
