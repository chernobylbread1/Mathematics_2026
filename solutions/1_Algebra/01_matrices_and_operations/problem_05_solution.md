# Exercise 5. Matrix Times Vector

## Given

A = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}

x = \begin{pmatrix} 4 \\ 2 \end{pmatrix}

## Solution

First, compute the matrix-vector product:

A x = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix}

Multiplying each row by the vector gives

A x = \begin{pmatrix} 2\cdot4 + (-1)\cdot2 \\ 1\cdot4 + 3\cdot2 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}

Now, express the result as a linear combination of the columns of A.

The columns of A are

A = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}

so

 a₁ = \begin{pmatrix} 2 \\ 1 \end{pmatrix},   a₂ = \begin{pmatrix} -1 \\ 3 \end{pmatrix}

The entries of x are 4 and 2. Therefore,

A x = 4a₁ + 2a₂

Substituting the columns gives

A x = 4\begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2\begin{pmatrix} -1 \\ 3 \end{pmatrix}

Multiplying the columns by their coefficients gives

4\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 8 \\ 4 \end{pmatrix},
2\begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} -2 \\ 6 \end{pmatrix}

Adding the vectors gives

A x = \begin{pmatrix} 8 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}

Both methods give the same result.

## Final Answer

A x = \begin{pmatrix} 6 \\ 10 \end{pmatrix}

The linear combination of the columns is

A x = 4\begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2\begin{pmatrix} -1 \\ 3 \end{pmatrix}

**Key idea:** Multiplying a matrix by a vector is equivalent to taking a linear combination of the matrix columns, using the entries of the vector as coefficients.
