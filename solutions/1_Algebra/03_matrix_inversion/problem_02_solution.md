### Essential Formulas

**Explicit Formula for the Inverse of a $2 \times 2$ Matrix:**
Let $A$ be a $2 \times 2$ matrix:

$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

The determinant of $A$ is:

$$
\det A = ad - bc
$$

If $\det A \neq 0$, the matrix is invertible, and its inverse is obtained by swapping the main diagonal entries, negating the off-diagonal entries, and dividing each element by $\det A$:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \frac{1}{ad - bc} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

If $\det A = 0$, the matrix is singular and no inverse exists.

**Verification Condition:**
To confirm that a candidate matrix $A^{-1}$ is indeed the inverse, multiplying $A$ by $A^{-1}$ must yield the identity matrix:

$$
A A^{-1} = I
$$

---

### Problem Statement

**Exercise 2. Formula for a 2×2 Matrix**

Find the inverse of

$$
A=
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
$$

using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

> **Why this exercise:** teaches the simplest explicit formula for an inverse and requires verification using the definition.

---

### Solution

Given:

$$
A = \begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
$$

Here, the entries are $a = 3$, $b = 2$, $c = 5$, and $d = 4$.

**Step 1: Compute the determinant of $A$**

Evaluate the determinant:

$$
\det A = ad - bc = (3)(4) - (2)(5) = 12 - 10 = 2
$$

Because $\det A = 2 \neq 0$, the matrix $A$ is invertible.

**Step 2: Apply the explicit $2 \times 2$ inverse formula**

Form the adjugate matrix by interchanging the diagonal entries ($3 \leftrightarrow 4$) and reversing the signs of the off-diagonal entries ($2 \to -2$, $5 \to -5$):

$$
\mathrm{adj}(A) = \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
$$

Divide by the determinant $\det A = 2$:

$$
A^{-1} = \frac{1}{2} \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
$$

Distribute the scalar factor $\frac{1}{2}$:

$$
A^{-1} = \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
$$

**Step 3: Check the result by computing $A A^{-1}$**

Multiply $A$ by the computed inverse $A^{-1}$:

$$
A A^{-1} = \begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
\left[ \frac{1}{2} \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix} \right]
$$

Pull out the scalar factor $\frac{1}{2}$ and perform matrix multiplication:

$$
A A^{-1} = \frac{1}{2} \begin{pmatrix}
3\cdot 4 + 2\cdot(-5) & 3\cdot(-2) + 2\cdot 3 \\
5\cdot 4 + 4\cdot(-5) & 5\cdot(-2) + 4\cdot 3 \\
\end{pmatrix}
$$

Simplify each entry:

$$
A A^{-1} = \frac{1}{2} \begin{pmatrix}
12 - 10 & -6 + 6 \\
20 - 20 & -10 + 12 \\
\end{pmatrix}
= \frac{1}{2} \begin{pmatrix}
2 & 0 \\
0 & 2 \\
\end{pmatrix}
$$

Divide by $2$:

$$
A A^{-1} = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

The product yields the identity matrix $I$, confirming that the computed inverse is correct.

**Step 4: Additional check ($A^{-1}A = I$)**

Multiply in the reverse order:

$$
A^{-1}A = \frac{1}{2} \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
= \frac{1}{2} \begin{pmatrix}
4(3) + (-2)(5) & 4(2) + (-2)(4) \\
-5(3) + 3(5) & -5(2) + 3(4) \\
\end{pmatrix}
$$

$$
A^{-1}A = \frac{1}{2} \begin{pmatrix}
12 - 10 & 8 - 8 \\
-15 + 15 & -10 + 12 \\
\end{pmatrix}
= \frac{1}{2} \begin{pmatrix}
2 & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

This completes the two-sided verification.

---

### Final Answer

Determinant:

$$
\det A = 2
$$

Inverse matrix:

$$
A^{-1} = \frac{1}{2} \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
$$

Product verification:

$$
A A^{-1} = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

