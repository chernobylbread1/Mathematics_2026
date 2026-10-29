### Essential Formulas

**Definition of the Inverse Matrix:**
Let $A$ be an $n \times n$ square matrix. A square matrix $B$ of the same size is called the **inverse** of $A$ (denoted $A^{-1}$) if and only if multiplying $A$ and $B$ in either order yields the $n \times n$ identity matrix $I$:

$$
AB = I \quad \mathrm{and} \quad BA = I
$$

For $2 \times 2$ matrices, the identity matrix is:

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

If such a matrix $B$ exists, it is unique, and we write $B = A^{-1}$ and $A = B^{-1}$.

---

### Problem Statement

**Exercise 1. Definition of the Inverse**

For

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

> **Why this exercise:** starts from the definition of the inverse through multiplication before any formulas or computational methods are introduced.

---

### Solution

**Step 1: Compute the matrix product $AB$**

Multiply row-by-column:

$$
AB = \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

Calculate each entry:

$$
(AB)_{11} = 2\cdot 1 + 1\cdot(-1) = 2 - 1 = 1
$$

$$
(AB)_{12} = 2\cdot(-1) + 1\cdot 2 = -2 + 2 = 0
$$

$$
(AB)_{21} = 1\cdot 1 + 1\cdot(-1) = 1 - 1 = 0
$$

$$
(AB)_{22} = 1\cdot(-1) + 1\cdot 2 = -1 + 2 = 1
$$

Assemble the product:

$$
AB = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

**Step 2: Compute the matrix product $BA$**

Now multiply in reverse order:

$$
BA = \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
$$

Calculate each entry:

$$
(BA)_{11} = 1\cdot 2 + (-1)\cdot 1 = 2 - 1 = 1
$$

$$
(BA)_{12} = 1\cdot 1 + (-1)\cdot 1 = 1 - 1 = 0
$$

$$
(BA)_{21} = (-1)\cdot 2 + 2\cdot 1 = -2 + 2 = 0
$$

$$
(BA)_{22} = (-1)\cdot 1 + 2\cdot 1 = -1 + 2 = 1
$$

Assemble the product:

$$
BA = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

**Step 3: Relate the result to the definition of the inverse**

The definition of an inverse requires that a matrix acts as a two-sided multiplicative inverse, satisfying both $AB = I$ and $BA = I$:

1. Multiplying $A$ on the right by $B$ gives the identity matrix ($AB = I$).
2. Multiplying $A$ on the left by $B$ also gives the identity matrix ($BA = I$).

Because both conditions are satisfied without invoking any external formula, $B$ is indeed the inverse of $A$:

$$
B = A^{-1}
$$

**Step 4: Verification**

To confirm consistency with the standard $2 \times 2$ determinant:

$$
\det A = (2)(1) - (1)(1) = 2 - 1 = 1 \neq 0
$$

Since $\det A = 1 \neq 0$, $A$ is guaranteed to be invertible. The explicit inverse formula yields:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \frac{1}{1} \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
= B
$$

This independently verifies that $B = A^{-1}$.

---

### Final Answer

Calculated products:

$$
AB = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

$$
BA = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

Conclusion:
Because $AB = I$ and $BA = I$, the matrix $B$ satisfies the definition of the inverse, and therefore $B = A^{-1}$.
