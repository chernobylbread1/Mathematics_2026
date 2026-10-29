### Essential Formulas

1. **Homogeneous Linear Systems:**
   A linear system is called **homogeneous** if all right-hand side constants are zero:

   $$
   Ax = 0
   $$

2. **Universal Existence of the Trivial Solution:**
   Every homogeneous linear system is **always consistent**, because setting all unknowns to zero:

   $$
   x_1 = 0, \ x_2 = 0, \ \dots, \ x_n = 0 \iff x = 0
   $$

   satisfies every equation identically:

   $$
   A \cdot 0 = 0
   $$

   This solution $x = (0, 0, \dots, 0)$ is called the **trivial solution**. Consequently, a homogeneous system can never have "no solution".

3. **Condition for Non-Trivial Solutions:**
   Let $A$ be an $m \times n$ matrix with $\mathrm{rank}(A) = r$.
   * If $r = n$: the trivial solution $x = 0$ is the **unique solution**.
   * If $r < n$: the system has **infinitely many non-trivial solutions**, parameterized by $k = n - r$ free variables (forming the null space or kernel $\mathrm{ker}(A)$).

---

### Problem Statement

Solve

$$
\begin{cases}
x+2y-z=0, \\
2x+4y-2z=0, \\
x-y+2z=0. \\
\end{cases}
$$

Give all solutions in parametric form and explain why $(0,0,0)$ always satisfies a homogeneous system.

> **Why this exercise:** shows the special case of a system with a zero right-hand side without introducing additional theory.

---

### Solution

**Step 1: Set up the Augmented Matrix**

Write the homogeneous system as an augmented matrix $[A \mid 0]$:

$$
[A \mid 0] = \begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
2 & 4 & -2 & \mid & 0 \\
1 & -1 & 2 & \mid & 0 \\
\end{pmatrix}
$$

The first pivot is $a_{11} = 1$ in row 1.

---

**Step 2: Perform Gaussian Elimination**

* **Eliminate row 2 entry:** Apply $R_2 \leftarrow R_2 - 2R_1$:

  $$
  R_2 = (2 - 2(1), \ 4 - 2(2), \ -2 - 2(-1) \ \mid \ 0 - 2(0)) = (0, \ 0, \ 0 \ \mid \ 0)
  $$

* **Eliminate row 3 entry:** Apply $R_3 \leftarrow R_3 - R_1$:

  $$
  R_3 = (1 - 1, \ -1 - 2, \ 2 - (-1) \ \mid \ 0 - 0) = (0, \ -3, \ 3 \ \mid \ 0)
  $$

The matrix becomes:

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
0 & -3 & 3 & \mid & 0 \\
\end{pmatrix}
$$

* **Swap rows to bring non-zero row up ($R_2 \leftrightarrow R_3$):**

  $$
  \begin{pmatrix}
  1 & 2 & -1 & \mid & 0 \\
  0 & -3 & 3 & \mid & 0 \\
  0 & 0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

* **Normalize row 2 ($R_2 \leftarrow -\frac{1}{3}R_2$):**

  $$
  \begin{pmatrix}
  1 & 2 & -1 & \mid & 0 \\
  0 & 1 & -1 & \mid & 0 \\
  0 & 0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

The augmented matrix is now in row echelon form.

---

**Step 3: Identify Pivots and Free Variables**

* Column 1 has a pivot in row 1 $\implies x$ is a **pivot variable**.
* Column 2 has a pivot in row 2 $\implies y$ is a **pivot variable**.
* Column 3 has no pivot $\implies z$ is a **free variable**.

The number of unknowns is $n = 3$, and the rank is $r = 2$.
The number of free variables is:

$$
k = n - r = 3 - 2 = 1
$$

Since $k = 1 > 0$, there are **infinitely many solutions** (including non-trivial ones).

Assign a real parameter $t \in \mathbb{R}$ to the free variable:

$$
z = t
$$

---

**Step 4: Solve by Back-Substitution**

* From row 2:

  $$
  y - z = 0 \implies y = z = t
  $$

* From row 1:

  $$
  x + 2y - z = 0
  $$

  Substitute $y = t$ and $z = t$:

  $$
  x + 2(t) - t = 0 \implies x + t = 0 \implies x = -t
  $$

---

**Step 5: Write the Parametric Solution**

The general solution in scalar parametric form is:

$$
\begin{cases}
x = -t, \\
y = t, \\
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
-t \\
t \\
t \\
\end{pmatrix}
= t \begin{pmatrix}
-1 \\
1 \\
1 \\
\end{pmatrix}, \qquad t \in \mathbb{R}
$$

Geometrically, this is a straight line in $\mathbb{R}^3$ passing through the origin $(0, 0, 0)$ along the direction vector $(-1, 1, 1)$.

---

**Step 6: Why $(0, 0, 0)$ Always Satisfies a Homogeneous System**

Consider any homogeneous linear equation in $n$ variables:

$$
a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = 0
$$

When $(x_1, x_2, \dots, x_n) = (0, 0, \dots, 0)$, every term on the left-hand side is multiplied by zero:

$$
a_1(0) + a_2(0) + \cdots + a_n(0) = 0 + 0 + \cdots + 0 = 0
$$

Since $0 = 0$ is always true, the zero vector $(0, 0, \dots, 0)$ automatically satisfies every linear equation whose constant term is zero.
In matrix terms:

$$
A \cdot \mathbf{0} = \mathbf{0}
$$

holds for any matrix $A$, because the zero vector is an annihilator under linear transformation.
Setting $t = 0$ in our parametric solution yields:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= 0 \begin{pmatrix}
-1 \\
1 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
0 \\
0 \\
0 \\
\end{pmatrix}
$$

which confirms that the trivial solution $(0, 0, 0)$ is indeed contained within the solution set.

---

### Final Answer

1. **Parametric Solution:**

   $$
   \begin{pmatrix}
   x \\
   y \\
   z \\
   \end{pmatrix}
   = t \begin{pmatrix}
   -1 \\
   1 \\
   1 \\
   \end{pmatrix}, \qquad t \in \mathbb{R}
   $$

   or in scalar form:

   $$
   x = -t, \qquad y = t, \qquad z = t \quad (t \in \mathbb{R})
   $$

2. **Why $(0,0,0)$ Always Satisfies Any Homogeneous System:**
   In every equation of a homogeneous system, each variable is multiplied by its coefficient and summed to produce zero ($a_{i1}x_1 + \dots + a_{in}x_n = 0$). Substituting $x_1 = \dots = x_n = 0$ results in a sum of zeros which identically equals zero ($A \mathbf{0} = \mathbf{0}$). Therefore, $(0,0,0)$ is always a solution (the trivial solution).
