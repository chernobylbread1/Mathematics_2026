### Essential Formulas

1. **Polynomial Curve Fitting via Linear Systems:**
   A polynomial of degree $n$:

   $$
   p(x) = c_n x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0
   $$

   passing through $m$ distinct points $(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)$ satisfies the system of linear equations:

   $$
   p(x_i) = y_i, \qquad i = 1, 2, \dots, m
   $$

   The unknown quantities are the polynomial coefficients $(c_0, c_1, \dots, c_n)$, while powers of the given abscissae $x_i^k$ act as constant numerical coefficients.

2. **Vandermonde Matrix Structure:**
   For a quadratic polynomial $p(x) = ax^2 + bx + c$, the interpolation conditions at three points produce the linear system:

   $$
   \begin{pmatrix}
   x_1^2 & x_1 & 1 \\
   x_2^2 & x_2 & 1 \\
   x_3^2 & x_3 & 1 \\
   \end{pmatrix}
   \begin{pmatrix}
   a \\
   b \\
   c \\
   \end{pmatrix}
   = \begin{pmatrix}
   y_1 \\
   y_2 \\
   y_3 \\
   \end{pmatrix}
   $$

   When the nodes $x_1, x_2, x_3$ are all distinct, the coefficient matrix is non-singular and the polynomial is uniquely determined.

---

### Problem Statement

Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

> **Why this exercise:** shows that finding unknown coefficients can be reduced to solving a linear system.

---

### Solution

**Step 1: Set up the Linear System from the Given Points**

The quadratic polynomial is:

$$
p(x) = ax^2 + bx + c
$$

We are given that the graph of $p(x)$ passes through three points:

1. **Point $(0, 1)$:**

   $$
   p(0) = a(0)^2 + b(0) + c = 1 \implies c = 1
   $$

2. **Point $(1, 3)$:**

   $$
   p(1) = a(1)^2 + b(1) + c = 3 \implies a + b + c = 3
   $$

3. **Point $(2, 9)$:**

   $$
   p(2) = a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9
   $$

This yields a linear system of three equations in the three unknowns $(a, b, c)$:

$$
\begin{cases}
c = 1, \\
a + b + c = 3, \\
4a + 2b + c = 9. \\
\end{cases}
$$

In standard matrix form $Ax = y$ with unknowns ordered as $(a, b, c)^T$:

$$
\begin{pmatrix}
0 & 0 & 1 \\
1 & 1 & 1 \\
4 & 2 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
3 \\
9 \\
\end{pmatrix}
$$

---

**Step 2: Solve the Linear System**

* **Direct Substitution of $c = 1$:**
  From the first equation, we immediately have:

  $$
  c = 1
  $$

* Substitute $c = 1$ into the remaining two equations:
  - From Equation 2:

    $$
    a + b + 1 = 3 \implies a + b = 2
    $$

  - From Equation 3:

    $$
    4a + 2b + 1 = 9 \implies 4a + 2b = 8
    $$

    Dividing this equation by $2$:

    $$
    2a + b = 4
    $$

* **Solve the resulting $2 \times 2$ system for $a$ and $b$:**
  Subtract the equation $a + b = 2$ from $2a + b = 4$:

  $$
  (2a + b) - (a + b) = 4 - 2 \implies a = 2
  $$

  Substitute $a = 2$ back into $a + b = 2$:

  $$
  2 + b = 2 \implies b = 0
  $$

Thus, the unique coefficients are:

$$
a = 2, \qquad b = 0, \qquad c = 1
$$

The resulting polynomial is:

$$
p(x) = 2x^2 + 1
$$

---

**Step 3: Systematic Check via Augmented Matrix**

To confirm via Gaussian elimination, reorder equations so the leading coefficient is non-zero ($R_1 \leftrightarrow R_2$):

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 3 \\
4 & 2 & 1 & \mid & 9 \\
0 & 0 & 1 & \mid & 1 \\
\end{pmatrix}
$$

Apply $R_2 \leftarrow R_2 - 4R_1$:

$$
R_2 = (4 - 4(1), \ 2 - 4(1), \ 1 - 4(1) \ \mid \ 9 - 4(3)) = (0, \ -2, \ -3 \ \mid \ -3)
$$

The matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 3 \\
0 & -2 & -3 & \mid & -3 \\
0 & 0 & 1 & \mid & 1 \\
\end{pmatrix}
$$

By back-substitution:
* Row 3: $c = 1$
* Row 2: $-2b - 3(1) = -3 \implies -2b = 0 \implies b = 0$
* Row 1: $a + 0 + 1 = 3 \implies a = 2$

Both methods yield $a = 2, b = 0, c = 1$.

---

**Step 4: Check by Substituting All Three Given Points**

Verify that $p(x) = 2x^2 + 1$ reproduces the exact target values:

1. **At $x = 0$:**

   $$
   p(0) = 2(0)^2 + 1 = 0 + 1 = 1
   $$

   Point $(0, 1)$ lies on the curve.

2. **At $x = 1$:**

   $$
   p(1) = 2(1)^2 + 1 = 2(1) + 1 = 3
   $$

   Point $(1, 3)$ lies on the curve.

3. **At $x = 2$:**

   $$
   p(2) = 2(2)^2 + 1 = 2(4) + 1 = 8 + 1 = 9
   $$

   Point $(2, 9)$ lies on the curve.

All three points are verified.

---

### Final Answer

1. **Coefficients:**

   $$
   a = 2, \qquad b = 0, \qquad c = 1
   $$

2. **Polynomial:**

   $$
   p(x) = 2x^2 + 1
   $$

3. **Check:**
   * $p(0) = 1$ (matches $(0,1)$)
   * $p(1) = 3$ (matches $(1,3)$)
   * $p(2) = 9$ (matches $(2,9)$)
