### Essential Formulas

**Matrix Multiplication via Columns:**
If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, the product $AB$ is an $m \times p$ matrix. 
Instead of calculating entry-by-entry, matrix multiplication can be viewed column-by-column. If we denote the columns of $B$ as vectors $b_1, b_2, \dots, b_p$, then the matrix $B$ can be written as a block matrix:

$$
B = \begin{pmatrix}
b_1 & b_2 & \cdots & b_p
\end{pmatrix}
$$

The product $AB$ is then formed by multiplying matrix $A$ with each individual column of $B$:

$$
AB = A \begin{pmatrix}
b_1 & b_2 & \cdots & b_p
\end{pmatrix}
= \begin{pmatrix}
A b_1 & A b_2 & \cdots & A b_p
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 10. Columns of a Matrix Product**

Given

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix},
\qquad 
B = \begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1
\end{pmatrix}.
$$

Denote the columns of $B$ by $b_1, b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

> **Why this exercise:** extends the interpretation of matrix-vector multiplication to a full product of two matrices instead of simply repeating another $Ax$ exercise.

---

### Solution

**Step 1: Compute $A b_1$ and $A b_2$**

First, we identify the columns of matrix $B$ as independent column vectors:

$$
b_1 = \begin{pmatrix}
1 \\
-1 \\
3
\end{pmatrix},
\qquad
b_2 = \begin{pmatrix}
2 \\
0 \\
1
\end{pmatrix}
$$

Now, multiply matrix $A$ by the column vector $b_1$:

$$
A b_1 = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
1 \\
-1 \\
3
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1) + (2\cdot-1) + (0\cdot3) \\
(0\cdot1) + (1\cdot-1) + (1\cdot3)
\end{pmatrix}
= \begin{pmatrix}
1 - 2 + 0 \\
0 - 1 + 3
\end{pmatrix}
= \begin{pmatrix}
-1 \\
2
\end{pmatrix}
$$

Next, multiply matrix $A$ by the column vector $b_2$:

$$
A b_2 = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
2 \\
0 \\
1
\end{pmatrix}
= \begin{pmatrix}
(1\cdot2) + (2\cdot0) + (0\cdot1) \\
(0\cdot2) + (1\cdot0) + (1\cdot1)
\end{pmatrix}
= \begin{pmatrix}
2 + 0 + 0 \\
0 + 0 + 1
\end{pmatrix}
= \begin{pmatrix}
2 \\
1
\end{pmatrix}
$$

**Step 2: Compute the matrix $AB$**

Multiply the full $2 \times 3$ matrix $A$ by the full $3 \times 2$ matrix $B$:

$$
AB = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1
\end{pmatrix}
$$

Calculate each entry (Row of $A$ $\times$ Column of $B$):

$$
AB = \begin{pmatrix}
(1\cdot1 + 2\cdot(-1) + 0\cdot3) & (1\cdot2 + 2\cdot0 + 0\cdot1) \\
(0\cdot1 + 1\cdot(-1) + 1\cdot3) & (0\cdot2 + 1\cdot0 + 1\cdot1)
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
-1 & 2 \\
2 & 1
\end{pmatrix}
$$

**Step 3: Comparison and Explanation**

Let's look at the columns of the resulting matrix $AB$:

The first column of $AB$ is:

$$
\begin{pmatrix}
-1 \\
2
\end{pmatrix}
$$

which matches exactly with our result for $A b_1$.

The second column of $AB$ is:

$$
\begin{pmatrix}
2 \\
1
\end{pmatrix}
$$

which matches exactly with our result for $A b_2$.

*Explanation:* 
By the definition of matrix multiplication, the entry in the $i$-th row and $j$-th column of $AB$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$. Therefore, calculating the entire $j$-th column of $AB$ simultaneously is mathematically identical to isolating the $j$-th column vector of $B$ and multiplying the entire matrix $A$ by it. 

This confirms that a full matrix product $AB$ can be viewed as a collection of individual matrix-vector products aligned side-by-side:

$$
AB = A \begin{pmatrix}
b_1 & b_2
\end{pmatrix}
= \begin{pmatrix}
A b_1 & A b_2
\end{pmatrix}
$$
