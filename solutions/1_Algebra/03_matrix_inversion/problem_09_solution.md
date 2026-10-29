### Essential Formulas

**Solving Linear Matrix Equations ($AX = B$):**
In matrix algebra, multiplication is non-commutative in general ($MN \neq NM$). Therefore, the side on which an operation is applied matters fundamentally:

To isolate the unknown matrix $X$ in the equation:

$$
AX = B
$$

where $A$ is invertible ($\det A \neq 0$):
* Multiply both sides **on the left** by $A^{-1}$:

  $$
  A^{-1}(AX) = A^{-1}B
  $$

* Use associativity to group adjacent inverse matrices:

  $$
  (A^{-1}A)X = A^{-1}B \implies IX = A^{-1}B \implies X = A^{-1}B
  $$

*Caution:* Multiplying on the right by $A^{-1}$ yields $(AX)A^{-1} = B A^{-1}$, which cannot simplify to $X$ because $AXA^{-1} \neq X$ in general.

**Inverse of a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix with determinant $\det A = ad - bc \neq 0$:

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

**Exercise 9. Matrix Equation**

Given

$$
A=
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}.
$$

Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

> **Why this exercise:** teaches that order matters in matrix equations and must guide the solution.

---

### Solution

Given:

$$
A = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}
$$

**Step 1: Decide on which side to multiply by $A^{-1}$**

In the equation $AX = B$, matrix $A$ stands to the left of the unknown matrix $X$. 

To eliminate $A$, we must multiply $A$ on the left by $A^{-1}$ so that the product $A^{-1}A$ produces the identity matrix $I$:

$$
A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies X = A^{-1}B
$$

*Decision:*
We must multiply **on the left** by $A^{-1}$. Multiplying on the right would yield $(AX)A^{-1} = B A^{-1}$, which does not isolate $X$ due to the non-commutativity of matrix multiplication.

**Step 2: Compute $A^{-1}$**

Evaluate the determinant of $A$:

$$
\det A = (1)(1) - (2)(0) = 1
$$

Since $\det A = 1 \neq 0$, the inverse exists. Using the $2 \times 2$ formula:

$$
A^{-1} = \frac{1}{1} \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
$$

**Step 3: Calculate $X = A^{-1}B$**

Multiply $A^{-1}$ on the left of $B$:

$$
X = \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}
$$

Compute the entries row-by-column:

$$
X_{11} = 1(3) + (-2)(2) = 3 - 4 = -1
$$

$$
X_{12} = 1(1) + (-2)(4) = 1 - 8 = -7
$$

$$
X_{21} = 0(3) + 1(2) = 0 + 2 = 2
$$

$$
X_{22} = 0(1) + 1(4) = 0 + 4 = 4
$$

Assemble matrix $X$:

$$
X = \begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
$$

**Step 4: Check the result by computing $AX$**

Multiply the original matrix $A$ by the calculated solution matrix $X$:

$$
AX = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
$$

Compute each entry:

$$
(AX)_{11} = 1(-1) + 2(2) = -1 + 4 = 3
$$

$$
(AX)_{12} = 1(-7) + 2(4) = -7 + 8 = 1
$$

$$
(AX)_{21} = 0(-1) + 1(2) = 0 + 2 = 2
$$

$$
(AX)_{22} = 0(-7) + 1(4) = 0 + 4 = 4
$$

Assemble the product:

$$
AX = \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}
= B
$$

Because $AX = B$, the solution matrix $X$ is confirmed.

---

### Final Answer

Side decision:
Multiply **on the left** by $A^{-1}$ because $A$ is positioned on the left of $X$: $X = A^{-1}B$.

Inverse matrix:

$$
A^{-1} = \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
$$

Solution matrix:

$$
X = \begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
$$

Verification:

$$
AX = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
= \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}
= B
$$
