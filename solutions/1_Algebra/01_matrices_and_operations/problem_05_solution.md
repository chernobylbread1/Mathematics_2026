### Essential Formulas
**Matrix-Vector Multiplication:**
For a $2 \times 2$ matrix $A$ and a $2 \times 1$ column vector $x$:

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
$$

The product $Ax$ is calculated as:

$$
Ax = \begin{pmatrix} a \cdot x_1 + b \cdot x_2 \\ c \cdot x_1 + d \cdot x_2 \end{pmatrix}
$$

**Linear Combination of Columns:**
The product $Ax$ can also be expressed as a linear combination of the column vectors of matrix $A$, scaled by the components of vector $x$:

$$
Ax = x_1 \begin{pmatrix} a \\ c \end{pmatrix} + x_2 \begin{pmatrix} b \\ d \end{pmatrix}
$$

---

### Problem Statement
**Exercise 5. Matrix Times Vector**
Let

$$
A= \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix},\qquad x= \begin{pmatrix} 4 \\ 2 \end{pmatrix}
$$

Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

> **Why this exercise:** shows that multiplying a matrix by a vector can be understood as a linear combination of the matrix columns.

---

### Solution
**Step 1: Compute $Ax$**
To compute the product $Ax$, we multiply the rows of matrix $A$ by the column vector $x$:

$$
Ax = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix}
$$

$$
Ax = \begin{pmatrix} (2 \cdot 4) + (-1 \cdot 2) \\ (1 \cdot 4) + (3 \cdot 2) \end{pmatrix}
$$

$$
Ax = \begin{pmatrix} 8 - 2 \\ 4 + 6 \end{pmatrix}
$$

$$
Ax = \begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

**Step 2: Express $Ax$ as a linear combination of the columns of $A$**
The columns of matrix $A$ are:

$$
c_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \quad c_2 = \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$

The coefficients are the respective elements of vector $x$: $x_1 = 4$ and $x_2 = 2$.
Expressing $Ax$ as a linear combination:

$$
Ax = 4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$

**Verification:**

$$
4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 8 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

This matches our initial calculation.
