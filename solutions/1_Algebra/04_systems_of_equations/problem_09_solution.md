### Essential Formulas

1. **Geometric Representation of a $2 \times 2$ Linear System:**
   Each equation of the form:

   $$
   a_i x + b_i y = c_i
   $$

   defines a line $L_i$ in the Euclidean plane $\mathbb{R}^2$ with normal vector $n_i = (a_i, b_i)$.

2. **Intersection of Two Lines and Solution Uniqueness:**
   Given two lines:
   * **Unique Solution:** The lines intersect at exactly one point if and only if their slopes are distinct ($m_1 \neq m_2$), or equivalently, their normal vectors are non-collinear:

     $$
     \det \begin{pmatrix}
     a_1 & b_1 \\
     a_2 & b_2 \\
     \end{pmatrix}
     = a_1 b_2 - a_2 b_1 \neq 0
     $$

   * **No Solution:** Parallel distinct lines ($m_1 = m_2$, but different intercepts).
   * **Infinitely Many Solutions:** Identical (coincident) lines ($m_1 = m_2$, identical intercepts).

---

### Problem Statement

Find numbers $x,y$ satisfying

$$
x+y=10,\qquad 2x+5y=32.
$$

Solve the system and explain geometrically why the solution is unique.

> **Why this exercise:** reinforces the transition from two linear conditions to the intersection point of two lines.

---

### Solution

**Step 1: Set up the Linear System and Augmented Matrix**

The system is:

$$
\begin{cases}
x + y = 10, \\
2x + 5y = 32. \\
\end{cases}
$$

Write the augmented matrix $[A \mid b]$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & \mid & 10 \\
2 & 5 & \mid & 32 \\
\end{pmatrix}
$$

---

**Step 2: Solve by Elimination**

The pivot in row 1 is $a_{11} = 1$. Eliminate the entry $a_{21} = 2$ in row 2 by applying $R_2 \leftarrow R_2 - 2R_1$:

$$
R_2 = (2 - 2(1), \ 5 - 2(1) \ \mid \ 32 - 2(10)) = (0, \ 3 \ \mid \ 32 - 20) = (0, \ 3 \ \mid \ 12)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
0 & 3 & \mid & 12 \\
\end{pmatrix}
$$

---

**Step 3: Back-Substitution**

* From the second row equation:

  $$
  3y = 12 \implies y = \frac{12}{3} = 4
  $$

* Substitute $y = 4$ into the first row equation:

  $$
  x + y = 10 \implies x + 4 = 10 \implies x = 6
  $$

The numbers satisfying the system are:

$$
x = 6, \qquad y = 4
$$

---

**Step 4: Verification of the Solution**

Substitute $x = 6$ and $y = 4$ into the original equations:
* First equation:

  $$
  x + y = 6 + 4 = 10
  $$

* Second equation:

  $$
  2x + 5y = 2(6) + 5(4) = 12 + 20 = 32
  $$

Both equations are satisfied.

---

**Step 5: Geometric Explanation of Uniqueness**

1. **Equation of Line 1 ($L_1$):**
   Rewriting $x + y = 10$ in slope-intercept form ($y = mx + b$):

   $$
   y = -x + 10
   $$

   This line has:
   * Slope $m_1 = -1$
   * $y$-intercept at $(0, 10)$
   * $x$-intercept at $(10, 0)$

2. **Equation of Line 2 ($L_2$):**
   Rewriting $2x + 5y = 32$ in slope-intercept form:

   $$
   5y = -2x + 32 \implies y = -\frac{2}{5}x + \frac{32}{5} = -0.4x + 6.4
   $$

   This line has:
   * Slope $m_2 = -\frac{2}{5} = -0.4$
   * $y$-intercept at $(0, 6.4)$
   * $x$-intercept at $(16, 0)$

3. **Why the Solution Is Unique:**
   * Two straight lines in the Cartesian plane intersect at exactly one point if and only if they are not parallel.
   * Parallelism requires equal slopes ($m_1 = m_2$). Here:

     $$
     m_1 = -1 \neq -0.4 = m_2
     $$

   * Because their slopes are different, the lines are not parallel and cannot be coincident. In two-dimensional Euclidean geometry, any two distinct non-parallel straight lines must cross at exactly one single geometric point.
   * That unique point of intersection is $(x, y) = (6, 4)$.
   * From the viewpoint of linear algebra, the normal vectors to the lines are $n_1 = (1, 1)$ and $n_2 = (2, 5)$. The determinant formed by these normal vectors is:

     $$
     \det \begin{pmatrix}
     1 & 1 \\
     2 & 5 \\
     \end{pmatrix}
     = (1)(5) - (1)(2) = 5 - 2 = 3 \neq 0
     $$

     Since the determinant is non-zero, the coefficient matrix is non-singular and invertible, which confirms that the solution is unique.

---

### Final Answer

1. **Solution:**

   $$
   x = 6, \qquad y = 4
   $$

   or as a point in the coordinate plane:

   $$
   (x, y) = (6, 4)
   $$

2. **Geometric Reason for Uniqueness:**
   The equations represent two straight lines in $\mathbb{R}^2$ with distinct slopes ($m_1 = -1$ and $m_2 = -0.4$). Since their slopes are unequal, the lines are neither parallel nor identical; they must intersect at precisely one point in the plane.

