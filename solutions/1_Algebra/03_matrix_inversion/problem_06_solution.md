### Essential Formulas

**Solving Linear Systems via the Inverse Matrix:**
Consider a system of linear equations in matrix form:

$$
Ax = b
$$

where $A$ is an $n \times n$ coefficient matrix, $x$ is the vector of unknowns, and $b$ is the right-hand side vector. If $A$ is invertible ($\det A \neq 0$), multiply both sides on the left by $A^{-1}$:

$$
A^{-1}(Ax) = A^{-1}b \implies (A^{-1}A)x = A^{-1}b \implies Ix = A^{-1}b
$$

Thus, the unique solution is given directly by:

$$
x = A^{-1}b
$$

**Explicit Inverse of a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix with entries $a, b, c, d$ and determinant $\det A = ad - bc \neq 0$:

$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

the inverse is:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 6. Solving a System Using the Inverse**

Solve

$$
Ax=b,
$$

where

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},\qquad b=
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix},
$$

using $x=A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

> **Why this exercise:** shows the connection between inverse matrices and solving a linear system.

---

### Solution

Given:

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b = \begin{pmatrix}
5 \\
7 \\
\end{pmatrix}
$$

**Step 1: Find the inverse matrix $A^{-1}$**

Compute the determinant of $A$:

$$
\det A = (2)(3) - (1)(1) = 6 - 1 = 5
$$

Since $\det A = 5 \neq 0$, the inverse $A^{-1}$ exists.

Construct $A^{-1}$ using the $2 \times 2$ formula:

$$
A^{-1} = \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

**Step 2: Solve the system using $x = A^{-1}b$**

Multiply $A^{-1}$ by the vector $b$:

$$
x = A^{-1}b = \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix}
$$

Compute the matrix-vector product:

$$
x = \frac{1}{5} \begin{pmatrix}
3(5) + (-1)(7) \\
(-1)(5) + 2(7) \\
\end{pmatrix}
= \frac{1}{5} \begin{pmatrix}
15 - 7 \\
-5 + 14 \\
\end{pmatrix}
= \frac{1}{5} \begin{pmatrix}
8 \\
9 \\
\end{pmatrix}
$$

In component form:

$$
x = \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

**Step 3: Check by substituting $x$ back into $Ax$**

Multiply the original coefficient matrix $A$ by the solution vector $x$:

$$
Ax = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

Compute each row product:

$$
Ax = \begin{pmatrix}
2\left(\frac{8}{5}\right) + 1\left(\frac{9}{5}\right) \\
1\left(\frac{8}{5}\right) + 3\left(\frac{9}{5}\right) \\
\end{pmatrix}
= \begin{pmatrix}
\frac{16 + 9}{5} \\
\frac{8 + 27}{5} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{25}{5} \\
\frac{35}{5} \\
\end{pmatrix}
= \begin{pmatrix}
5 \\
7 \\
\end{pmatrix}
$$

Because the result matches the vector $b$:

$$
Ax = b
$$

the solution is verified.

**Step 4: Algebraic verification of each equation**

Write the system as scalar equations:

1. First equation ($2x_1 + x_2 = 5$):

   $$
   2\left(\frac{8}{5}\right) + \frac{9}{5} = \frac{16}{5} + \frac{9}{5} = \frac{25}{5} = 5
   $$

2. Second equation ($x_1 + 3x_2 = 7$):

   $$
   \frac{8}{5} + 3\left(\frac{9}{5}\right) = \frac{8}{5} + \frac{27}{5} = \frac{35}{5} = 7
   $$

Both equations are simultaneously satisfied.

---

### Final Answer

Inverse matrix:

$$
A^{-1} = \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

Solution vector:

$$
x = \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
= \frac{1}{5} \begin{pmatrix}
8 \\
9 \\
\end{pmatrix}
$$

Verification:

$$
Ax = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
= \begin{pmatrix}
5 \\
7 \\
\end{pmatrix}
= b
$$
