### Essential Formulas

1. **Matrix Form of a Linear System:**
   A system of $m$ linear equations in $n$ unknowns can be represented concisely as a single matrix equation:

   $$
   Ax = b
   $$

   where:
   * $A$ is the $m \times n$ **coefficient matrix**, whose entry $a_{ij}$ is the coefficient of unknown $x_j$ in the $i$-th equation.
   * $x$ is the $n \times 1$ **vector of unknowns**:

     $$
     x = \begin{pmatrix}
     x_1 \\
     x_2 \\
     \vdots \\
     x_n \\
     \end{pmatrix}
     $$

   * $b$ is the $m \times 1$ **right-hand side vector** of constants:

     $$
     b = \begin{pmatrix}
     b_1 \\
     b_2 \\
     \vdots \\
     b_m \\
     \end{pmatrix}
     $$

2. **Row-by-Column Multiplication (Equation Correspondence):**
   The $i$-th equation of the system is produced by the matrix multiplication of the $i$-th row of $A$ by the vector $x$:

   $$
   \sum_{j=1}^n a_{ij} x_j = b_i
   $$

   Each row of $A$ contains the coefficients corresponding to exactly one equation in the system.

---

### Problem Statement

Write the system

$$
\begin{cases}
2x-y+z=4, \\
x+3y-2z=1, \\
3x+y+z=7. \\
\end{cases}
$$

in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

> **Why this exercise:** teaches how to move between a system of equations and matrix notation.

---

### Solution

**Step 1: Identify the Unknowns and Coefficients**

The system consists of three linear equations with three unknowns $(x, y, z)$:

* Equation 1: $2x - 1y + 1z = 4$
* Equation 2: $1x + 3y - 2z = 1$
* Equation 3: $3x + 1y + 1z = 7$

Ordering the unknowns consistently as:

$$
x = \begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
$$

we extract the numerical coefficients from each equation:
* For Equation 1: coefficients are $2, -1, 1$.
* For Equation 2: coefficients are $1, 3, -2$.
* For Equation 3: coefficients are $3, 1, 1$.

The right-hand side constants are $4, 1, 7$.

---

**Step 2: Construct the Matrix Form $Ax = b$**

* **Coefficient Matrix $A$ ($3 \times 3$):**

  $$
  A = \begin{pmatrix}
  2 & -1 & 1 \\
  1 & 3 & -2 \\
  3 & 1 & 1 \\
  \end{pmatrix}
  $$

* **Vector of Unknowns $x$ ($3 \times 1$):**

  $$
  x = \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  $$

* **Right-Hand Side Vector $b$ ($3 \times 1$):**

  $$
  b = \begin{pmatrix}
  4 \\
  1 \\
  7 \\
  \end{pmatrix}
  $$

The complete matrix equation is:

$$
\begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
4 \\
1 \\
7 \\
\end{pmatrix}
$$

---

**Step 3: Verification of Row-by-Equation Correspondence**

Carrying out the matrix multiplication row by row:

* **Row 1:**

  $$
  \begin{pmatrix}
  2 & -1 & 1 \\
  \end{pmatrix}
  \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  = 2\cdot x + (-1)\cdot y + 1\cdot z = 2x - y + z
  $$

  Setting this equal to the first component of $b$ gives $2x - y + z = 4$ (Equation 1).

* **Row 2:**

  $$
  \begin{pmatrix}
  1 & 3 & -2 \\
  \end{pmatrix}
  \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  = 1\cdot x + 3\cdot y + (-2)\cdot z = x + 3y - 2z
  $$

  Setting this equal to the second component of $b$ gives $x + 3y - 2z = 1$ (Equation 2).

* **Row 3:**

  $$
  \begin{pmatrix}
  3 & 1 & 1 \\
  \end{pmatrix}
  \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  = 3\cdot x + 1\cdot y + 1\cdot z = 3x + y + z
  $$

  Setting this equal to the third component of $b$ gives $3x + y + z = 7$ (Equation 3).

Each row vector in matrix $A$ acts as a linear functional that computes the left-hand side of its respective equation, while the corresponding entry of vector $b$ specifies the target value.

---

### Final Answer

1. **Matrix Form $Ax = b$:**

   $$
   \begin{pmatrix}
   2 & -1 & 1 \\
   1 & 3 & -2 \\
   3 & 1 & 1 \\
   \end{pmatrix}
   \begin{pmatrix}
   x \\
   y \\
   z \\
   \end{pmatrix}
   = \begin{pmatrix}
   4 \\
   1 \\
   7 \\
   \end{pmatrix}
   $$

2. **Identified Components:**
   * **Coefficient Matrix:**

     $$
     A = \begin{pmatrix}
     2 & -1 & 1 \\
     1 & 3 & -2 \\
     3 & 1 & 1 \\
     \end{pmatrix}
     $$

   * **Vector of Unknowns:**

     $$
     x = \begin{pmatrix}
     x \\
     y \\
     z \\
     \end{pmatrix}
     $$

   * **Right-Hand Side Vector:**

     $$
     b = \begin{pmatrix}
     4 \\
     1 \\
     7 \\
     \end{pmatrix}
     $$

3. **Row Correspondence:**
   Row $i$ of matrix $A$ contains the coefficients of $x$, $y$, and $z$ from the $i$-th equation, so the inner product of row $i$ with $x$ yields the left-hand side of equation $i$, which equals component $b_i$.

