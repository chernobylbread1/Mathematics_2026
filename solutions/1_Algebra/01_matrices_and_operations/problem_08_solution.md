### Essential Formulas

**Elementary Row Operations:**
There are three basic types of elementary row operations that can be performed on a matrix:
1. **Row Addition:** Adding a multiple of one row to another row (e.g., $R_i \leftarrow R_i + k R_j$).
2. **Row Switching:** Interchanging two rows (e.g., $R_i \leftrightarrow R_j$).
3. **Row Multiplication:** Multiplying a row by a non-zero scalar (e.g., $R_i \leftarrow k R_i$).

**Reversibility (Inverse Operations):**
Every elementary row operation is reversible by another elementary row operation of the same type:
* The reverse of $R_i \leftarrow R_i + k R_j$ is $R_i \leftarrow R_i - k R_j$.
* The reverse of $R_i \leftrightarrow R_j$ is simply applying the same swap again: $R_i \leftrightarrow R_j$.
* The reverse of $R_i \leftarrow k R_i$ is $R_i \leftarrow \frac{1}{k} R_i$.

---

### Problem Statement

**Exercise 8. Row Operations and Their Reversibility**

For

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3
\end{pmatrix}
$$

perform, in order:
1. $R_2 \leftarrow R_2 - 2R_1$
2. $R_3 \leftarrow R_3 + R_1$
3. interchange $R_2$ and $R_3$

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

> **Why this exercise:** prepares for elimination by showing that row operations are controlled and reversible transformations of a matrix.

---

### Solution

**Initial Matrix:**

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3
\end{pmatrix}
$$

**Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$**
Multiply Row 1 by 2 to get $(2, 4, -2)$. Subtract this from Row 2 $(2, 4, 1)$:
Row 2 becomes: $(2 - 2, 4 - 4, 1 - (-2)) = (0, 0, 3)$. 
The new matrix is:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3
\end{pmatrix}
$$

**Step 2: Perform $R_3 \leftarrow R_3 + R_1$**
Add Row 1 $(1, 2, -1)$ to Row 3 $(-1, 1, 3)$:
Row 3 becomes: $(-1 + 1, 1 + 2, 3 - 1) = (0, 3, 2)$. 
The new matrix is:

$$
A_2 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2
\end{pmatrix}
$$

**Step 3: Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)**
Swap the second and third rows of the matrix from Step 2. 
The new matrix is:

$$
A_3 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3
\end{pmatrix}
$$

**Reversing the Operations:**
To reverse the transformations and return a matrix to its previous state, we apply the inverse mathematical operation:

1. The operation $R_2 \leftarrow R_2 - 2R_1$ is reversed by **adding** 2 times Row 1 back to Row 2:
**Reverse Operation 1:** $R_2 \leftarrow R_2 + 2R_1$

2. The operation $R_3 \leftarrow R_3 + R_1$ is reversed by **subtracting** Row 1 from Row 3:
**Reverse Operation 2:** $R_3 \leftarrow R_3 - R_1$

3. The operation of interchanging $R_2$ and $R_3$ is reversed by simply **swapping them back**:
**Reverse Operation 3:** Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)
