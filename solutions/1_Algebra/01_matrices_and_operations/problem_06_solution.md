### Essential Formulas

**Matrix Transpose:**
The transpose of a matrix $A$, denoted as $A^T$, is found by swapping its rows and columns. If $A$ is an $m \times n$ matrix, then $A^T$ will be an $n \times m$ matrix. The element at the $i$-th row and $j$-th column of $A$ becomes the element at the $j$-th row and $i$-th column of $A^T$.

**Matrix Multiplication and Dimensions:**
To multiply two matrices $A$ and $B$, the number of columns in $A$ must equal the number of rows in $B$. 
If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, their product $AB$ will be an $m \times p$ matrix.

**Property of Transpose for Matrix Products:**
The transpose of a product of two matrices is the product of their transposes in the reverse order:

$$
(AB)^T = B^T A^T
$$

---

### Problem Statement

**Exercise 6. Transpose**

For

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix},
\qquad
B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}
$$

compute $A^T$, $B^T$, and $AB$. Then verify in this example that

$$
(AB)^T = B^T A^T.
$$

> **Why this exercise:** teaches transposition and an important property that reverses the order of factors.

---

### Solution

**Step 1: Compute $A^T$ and $B^T$**

Matrix $A$ is a $2 \times 3$ matrix. Swapping its rows and columns gives the $3 \times 2$ transpose matrix $A^T$:

$$
A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
$$

Matrix $B$ is a $3 \times 2$ matrix. Swapping its rows and columns gives the $2 \times 3$ transpose matrix $B^T$:

$$
B^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix}
$$

**Step 2: Compute $AB$**

Multiply the $2 \times 3$ matrix $A$ by the $3 \times 2$ matrix $B$. The result will be a $2 \times 2$ matrix.

$$
AB = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}
$$

Calculate each entry (Row of $A$ $\times$ Column of $B$):
*   **Row 1, Col 1:** $(1 \cdot 1) + (2 \cdot 2) + (3 \cdot -1) = 1 + 4 - 3 = 2$
*   **Row 1, Col 2:** $(1 \cdot 0) + (2 \cdot 1) + (3 \cdot 3) = 0 + 2 + 9 = 11$
*   **Row 2, Col 1:** $(4 \cdot 1) + (5 \cdot 2) + (6 \cdot -1) = 4 + 10 - 6 = 8$
*   **Row 2, Col 2:** $(4 \cdot 0) + (5 \cdot 1) + (6 \cdot 3) = 0 + 5 + 18 = 23$

$$
AB = \begin{pmatrix} 2 & 11 \\ 8 & 23 \end{pmatrix}
$$

**Step 3: Verify that $(AB)^T = B^T A^T$**

First, find the transpose of the product $(AB)$:

$$
(AB)^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
$$

Next, compute the product of the transposes, $B^T A^T$. 
Multiply the $2 \times 3$ matrix $B^T$ by the $3 \times 2$ matrix $A^T$:

$$
B^T A^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
$$

Calculate each entry:
*   **Row 1, Col 1:** $(1 \cdot 1) + (2 \cdot 2) + (-1 \cdot 3) = 1 + 4 - 3 = 2$
*   **Row 1, Col 2:** $(1 \cdot 4) + (2 \cdot 5) + (-1 \cdot 6) = 4 + 10 - 6 = 8$
*   **Row 2, Col 1:** $(0 \cdot 1) + (1 \cdot 2) + (3 \cdot 3) = 0 + 2 + 9 = 11$
*   **Row 2, Col 2:** $(0 \cdot 4) + (1 \cdot 5) + (3 \cdot 6) = 0 + 5 + 18 = 23$

$$
B^T A^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
$$

Comparing the two results:

$$
\begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix} = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
$$

The property $(AB)^T = B^T A^T$ is successfully verified for these matrices.
