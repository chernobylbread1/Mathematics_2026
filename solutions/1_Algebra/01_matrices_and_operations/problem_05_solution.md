
# Exercise 5. Matrix Times Vector

### Essential Formulas

**Matrix-Vector Multiplication:**

For a matrix \(A\) and a column vector \(x\), the product \(Ax\) is calculated by multiplying each row of \(A\) by the vector \(x\).

**Linear Combination of Columns:**

The product \(Ax\) can also be expressed as a linear combination of the columns of matrix \(A\), using the entries of vector \(x\) as coefficients.

For a matrix with columns \(c_1\) and \(c_2\),

$$
Ax = x_1c_1 + x_2c_2
$$

---

### Problem Statement

Let

$$
A= \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix},
\qquad
x= \begin{pmatrix} 4 \\ 2 \end{pmatrix}
$$

Compute \(Ax\). Then express \(Ax\) as a linear combination of the columns of \(A\), with coefficients coming from the vector \(x\).

> **Why this exercise:** shows that multiplying a matrix by a vector can be understood as a linear combination of the matrix columns.

---

### Solution

**Step 1: Compute \(Ax\)**

To compute the product \(Ax\), we multiply the rows of matrix \(A\) by the column vector \(x\):

$$
Ax = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}
\begin{pmatrix} 4 \\ 2 \end{pmatrix}
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

**Step 2: Express \(Ax\) as a linear combination of the columns of \(A\)**

The columns of matrix \(A\) are:

$$
c_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix},
\qquad
c_2 = \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$

The coefficients are the respective elements of vector \(x\): \(x_1 = 4\) and \(x_2 = 2\).

Expressing \(Ax\) as a linear combination:

$$
Ax = 4 \begin{pmatrix} 2 \\ 1 \end{pmatrix}
+ 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$

**Verification:**

$$
4 \begin{pmatrix} 2 \\ 1 \end{pmatrix}
+ 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix}
=
\begin{pmatrix} 8 \\ 4 \end{pmatrix}
+ \begin{pmatrix} -2 \\ 6 \end{pmatrix}
=
\begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

This matches our initial calculation.

---

### Final Answer

$$
Ax = \begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

The linear combination of the columns is

$$
Ax = 4c_1 + 2c_2
$$

