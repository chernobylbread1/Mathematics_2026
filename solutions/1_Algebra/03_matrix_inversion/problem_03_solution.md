### Essential Formulas

**Invertibility Criterion via Determinants:**
A square matrix $A$ possesses an inverse $A^{-1}$ if and only if its determinant is non-zero:

$$
\det A \neq 0
$$

If $\det A = 0$, the matrix is singular and no inverse exists because the inverse formula:

$$
A^{-1} = \frac{1}{\det A} \mathrm{adj}(A)
$$

requires division by zero, which is mathematically undefined.

**Invertibility and Linear Independence of Rows:**
An $n \times n$ matrix $A$ is invertible if and only if its rows form a linearly independent set of vectors spanning $\mathbb{R}^n$:

$$
\mathrm{rank}(A) = n
$$

If a linear relationship exists between the rows ($\sum c_i R_i = 0$ with not all $c_i = 0$):
1. The rows are **linearly dependent**.
2. The row rank is strictly less than $n$ ($\mathrm{rank}(A) < n$).
3. The linear transformation collapses $n$-dimensional space into a lower-dimensional subspace, preventing the existence of an inverse mapping.

---

### Problem Statement

**Exercise 3. When Does the Inverse Not Exist?**

For

$$
A=
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
$$

explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

> **Why this exercise:** connects two signs of noninvertibility instead of treating them as unrelated facts.

---

### Solution

Given:

$$
A = \begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
$$

**Step 1: Way 1 — Using the determinant**

Compute the determinant of $A$ using the $2 \times 2$ formula:

$$
\det A = (2)(2) - (4)(1) = 4 - 4 = 0
$$

*Reasoning:*
The formula for the inverse of a $2 \times 2$ matrix requires multiplying the adjugate matrix by the reciprocal of the determinant:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
2 & -4 \\
-1 & 2 \\
\end{pmatrix}
= \frac{1}{0} \begin{pmatrix}
2 & -4 \\
-1 & 2 \\
\end{pmatrix}
$$

Division by zero is undefined. Therefore, no matrix with finite real entries can satisfy $A A^{-1} = I$, and $A^{-1}$ does not exist.

**Step 2: Way 2 — Using dependence between the rows**

Write down the two row vectors of matrix $A$:

$$
R_1 = (2, 4), \qquad R_2 = (1, 2)
$$

Compare the two rows:

$$
R_1 = (2, 4) = 2 \cdot (1, 2) = 2 R_2
$$

Equivalently:

$$
R_1 - 2 R_2 = (0, 0)
$$

*Reasoning:*
Because row 1 is a non-zero scalar multiple of row 2, the rows are **linearly dependent**:

1. The span of the rows is a $1$-dimensional line in $\mathbb{R}^2$ rather than the entire $2$-dimensional plane:

   $$
   \mathrm{rank}(A) = 1 < 2
   $$

2. Geometrically, the linear map $x \mapsto Ax$ collapses all of $\mathbb{R}^2$ onto the line spanned by the vector $(2, 1)^T$:

   $$
   A \begin{pmatrix}
   x_1 \\
   x_2 \\
   \end{pmatrix}
   = \begin{pmatrix}
   2x_1 + 4x_2 \\
   x_1 + 2x_2 \\
   \end{pmatrix}
   = (x_1 + 2x_2) \begin{pmatrix}
   2 \\
   1 \\
   \end{pmatrix}
   $$

3. This map is not injective (not one-to-one): any non-zero vector on the line $x_1 + 2x_2 = 0$ (for instance, $x = (-2, 1)^T$) is mapped to the zero vector:

   $$
   A \begin{pmatrix}
   -2 \\
   1 \\
   \end{pmatrix}
   = \begin{pmatrix}
   2(-2) + 4(1) \\
   1(-2) + 2(1) \\
   \end{pmatrix}
   = \begin{pmatrix}
   0 \\
   0 \\
   \end{pmatrix}
   $$

Because a collapsed transformation cannot be uniquely undone, no inverse map or matrix can exist.

**Step 3: Synthesis — Connection between the two explanations**

The determinant measures the signed area of the parallelogram spanned by the row vectors $R_1$ and $R_2$. Because $R_1 = 2R_2$, the vectors are parallel and point in the same direction, bounding a degenerate parallelogram with zero area. 

Thus, a zero determinant and linear dependence of the rows are two expressions of the same underlying geometric and algebraic reality: dimension loss.

**Step 4: Verification by contradiction**

Suppose an inverse matrix exists:

$$
B = \begin{pmatrix}
x & y \\
z & w \\
\end{pmatrix}
$$

such that $AB = I$. Multiplying gives:

$$
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
x & y \\
z & w \\
\end{pmatrix}
= \begin{pmatrix}
2x + 4z & 2y + 4w \\
x + 2z & y + 2w \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

Looking at the first column requires:

$$
2x + 4z = 1 \quad \mathrm{and} \quad x + 2z = 0
$$

Multiplying the second equation by $2$ gives $2x + 4z = 0$, leading to the direct contradiction:

$$
1 = 0
$$

Hence, no such matrix $B$ can exist.

---

### Final Answer

Why $A^{-1}$ does not exist:

1. **Determinant view:**

   $$
   \det A = (2)(2) - (4)(1) = 0
   $$

   Because $\det A = 0$, evaluating $A^{-1} = \frac{1}{\det A}\mathrm{adj}(A)$ requires division by zero, so the inverse is undefined.

2. **Row dependence view:**

   $$
   R_1 = 2 R_2 \iff R_1 - 2 R_2 = (0, 0)
   $$

   The rows are linearly dependent, so $\mathrm{rank}(A) = 1 < 2$. The transformation collapses 2D space onto a 1D line and is not one-to-one, making inversion impossible.
