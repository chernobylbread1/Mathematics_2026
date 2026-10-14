# Exercise 5. Matrix Times Vector

## Given

A = [[2, -1], [1, 3]]
x = [4, 2]^T

## Solution

First, compute the matrix-vector product:

A x = [[2, -1], [1, 3]] · [4, 2]^T

Multiplying each row by the vector gives

A x = [2·4 + (-1)·2, 1·4 + 3·2]^T = [6, 10]^T

Now, express the result as a linear combination of the columns of A.

The columns of A are

a₁ = [2, 1]^T
a₂ = [-1, 3]^T

The entries of x are 4 and 2. Therefore,

A x = 4a₁ + 2a₂

Substituting the columns gives

A x = 4[2, 1]^T + 2[-1, 3]^T

Multiplying the columns by their coefficients gives

4[2, 1]^T = [8, 4]^T
2[-1, 3]^T = [-2, 6]^T

Adding the vectors gives

A x = [8, 4]^T + [-2, 6]^T = [6, 10]^T

Both methods give the same result.

## Final Answer

A x = [6, 10]^T

The linear combination of the columns is

A x = 4[2, 1]^T + 2[-1, 3]^T

Key idea: Multiplying a matrix by a vector is equivalent to taking a linear combination of the matrix columns, using the entries of the vector as coefficients.
