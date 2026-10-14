### Essential Formulas

**Matrix Commutativity:**
In general, matrix multiplication is not commutative ($AB \neq BA$). However, two matrices $A$ and $B$ are said to commute if the order of multiplication does not change the result:

$$
AB = BA
$$

**Matrix Equality:**
Two matrices are equal if and only if they have the same dimensions and all their corresponding entries are identical.

---

### Problem Statement

**Exercise 11. When Do Matrices Commute?**

Given

$$
A= \begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix},\qquad B= \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}.
$$

Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

> **Why this exercise:** deepens the idea of noncommutativity by finding the conditions under which commutativity does hold.

---

### Solution

**Step 1: Compute the product $AB$**

Multiply matrix $A$ by matrix $B$:

$$
AB = \begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
(1\cdot a + 1\cdot c) & (1\cdot b + 1\cdot d) \\
(0\cdot a + 1\cdot c) & (0\cdot b + 1\cdot d)
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
a + c & b + d \\
c & d
\end{pmatrix}
$$

**Step 2: Compute the product $BA$**

Multiply matrix $B$ by matrix $A$:

$$
BA = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
$$

$$
BA = \begin{pmatrix}
(a\cdot 1 + b\cdot 0) & (a\cdot 1 + b\cdot 1) \\
(c\cdot 1 + d\cdot 0) & (c\cdot 1 + d\cdot 1)
\end{pmatrix}
$$

$$
BA = \begin{pmatrix}
a & a + b \\
c & c + d
\end{pmatrix}
$$

**Step 3: Equate $AB$ and $BA$ to find conditions**

For the matrices to commute, we must have $AB = BA$. Therefore, we equate the resulting matrices from Step 1 and Step 2:

$$
\begin{pmatrix}
a + c & b + d \\
c & d
\end{pmatrix}
= \begin{pmatrix}
a & a + b \\
c & c + d
\end{pmatrix}
$$

By equating the corresponding entries, we get a system of four equations:
1.  Top-left: $a + c = a$
2.  Top-right: $b + d = a + b$
3.  Bottom-left: $c = c$
4.  Bottom-right: $d = c + d$

Solving these equations:
*   From equation 1: $a + c = a \implies c = 0$.
*   From equation 2: $b + d = a + b \implies d = a$.
*   Equation 3 ($c = c$) is a trivial identity.
*   From equation 4, substituting $c = 0$: $d = 0 + d \implies d = d$, which is also a trivial identity.

So, the conditions are **$c = 0$** and **$a = d$**. The variables $a$ and $b$ can be any real numbers.

**Step 4: Describe the general form of matrix $B$**

Substitute the conditions $c = 0$ and $d = a$ back into the original matrix $B$:

$$
B = \begin{pmatrix}
a & b \\
0 & a
\end{pmatrix}
$$

*Conclusion:* 
For matrix $B$ to commute with matrix $A$, it must be an upper triangular matrix where the entries on the main diagonal are identical.
