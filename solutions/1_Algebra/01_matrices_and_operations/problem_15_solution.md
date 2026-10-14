### Essential Formulas

**Associativity of Matrix Multiplication:**
For any three matrices $A$, $B$, and $C$ where the dimensions allow for multiplication, the grouping of the operations does not change the final result:

$$
(AB)C = A(BC)
$$

**Computational Cost of Matrix Multiplication:**
When multiplying an $m \times n$ matrix by an $n \times p$ matrix, the resulting $m \times p$ matrix has $m \cdot p$ entries. Each entry requires $n$ scalar multiplications. 
Therefore, the total number of individual multiplications required is: $m \cdot n \cdot p$.

---

### Problem Statement

**Exercise 15. Associativity of Multiplication and Different Calculation Paths**

Given

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix},
\quad B = \begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3
\end{pmatrix},
\quad C = \begin{pmatrix}
2 & 1 \\
0 & -1
\end{pmatrix}.
$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

> **Why this exercise:** reinforces associativity by comparing two mathematically equivalent calculation paths.

---

### Solution

**Step 1: Compute the first path $(AB)C$**

First, compute the inner product $AB$. Matrix $A$ is $2 \times 3$ and $B$ is $3 \times 2$, so the result will be a $2 \times 2$ matrix.

$$
AB = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
(1\cdot1 + 2\cdot2 + 0\cdot(-1)) & (1\cdot0 + 2\cdot1 + 0\cdot3) \\
(0\cdot1 + 1\cdot2 + 1\cdot(-1)) & (0\cdot0 + 1\cdot1 + 1\cdot3)
\end{pmatrix}
= \begin{pmatrix}
5 & 2 \\
1 & 4
\end{pmatrix}
$$

*Operations for $AB$:* $2 \times 3 \times 2 = 12$ multiplications.

Next, multiply the result by $C$:

$$
(AB)C = \begin{pmatrix}
5 & 2 \\
1 & 4
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1
\end{pmatrix}
$$

$$
(AB)C = \begin{pmatrix}
(5\cdot2 + 2\cdot0) & (5\cdot1 + 2\cdot(-1)) \\
(1\cdot2 + 4\cdot0) & (1\cdot1 + 4\cdot(-1))
\end{pmatrix}
= \begin{pmatrix}
10 & 3 \\
2 & -3
\end{pmatrix}
$$

*Operations for $(AB)C$:* $2 \times 2 \times 2 = 8$ multiplications.
**Total multiplications for Path 1:** $12 + 8 = 20$.

**Step 2: Compute the second path $A(BC)$**

First, compute the inner product $BC$. Matrix $B$ is $3 \times 2$ and $C$ is $2 \times 2$, so the result will be a $3 \times 2$ matrix.

$$
BC = \begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1
\end{pmatrix}
$$

$$
BC = \begin{pmatrix}
(1\cdot2 + 0\cdot0) & (1\cdot1 + 0\cdot(-1)) \\
(2\cdot2 + 1\cdot0) & (2\cdot1 + 1\cdot(-1)) \\
(-1\cdot2 + 3\cdot0) & (-1\cdot1 + 3\cdot(-1))
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4
\end{pmatrix}
$$

*Operations for $BC$:* $3 \times 2 \times 2 = 12$ multiplications.

Next, multiply $A$ by the result $BC$:

$$
A(BC) = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4
\end{pmatrix}
$$

$$
A(BC) = \begin{pmatrix}
(1\cdot2 + 2\cdot4 + 0\cdot(-2)) & (1\cdot1 + 2\cdot1 + 0\cdot(-4)) \\
(0\cdot2 + 1\cdot4 + 1\cdot(-2)) & (0\cdot1 + 1\cdot1 + 1\cdot(-4))
\end{pmatrix}
= \begin{pmatrix}
10 & 3 \\
2 & -3
\end{pmatrix}
$$

*Operations for $A(BC)$:* $2 \times 3 \times 2 = 12$ multiplications.
**Total multiplications for Path 2:** $12 + 12 = 24$.

**Step 3: Comparison and Explanation**

Comparing the final results, both calculation paths yield the exact same $2 \times 2$ matrix:

$$
\begin{pmatrix}
10 & 3 \\
2 & -3
\end{pmatrix}
= \begin{pmatrix}
10 & 3 \\
2 & -3
\end{pmatrix}
$$

*Explanation:* 
This example verifies that matrix multiplication is **associative**; the grouping of the matrices does not change the final output. However, it also demonstrates a critical computational property: the number of intermediate arithmetic operations varies depending on the chosen path. 

*   Path 1 $(AB)C$ required **20 scalar multiplications**.
*   Path 2 $A(BC)$ required **24 scalar multiplications**.

In practice (such as in computer science and algorithm design), associativity allows us to choose the most efficient grouping of matrix multiplications to minimize the total computational cost without altering the mathematical truth of the result.
