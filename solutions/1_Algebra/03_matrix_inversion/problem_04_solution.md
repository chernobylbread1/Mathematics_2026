### Essential Formulas

**Gauss–Jordan Inversion Method:**
To find the inverse of an $n \times n$ matrix $A$, construct the augmented matrix by appending the $n \times n$ identity matrix $I$ to the right of $A$:

$$
[A \mid I]
$$

Apply elementary row operations until the left block is transformed into the reduced row echelon form (the identity matrix $I$). The right block then becomes $A^{-1}$:

$$
[A \mid I] \longrightarrow [I \mid A^{-1}]
$$

**Why Obtaining $I$ on the Left Gives $A^{-1}$ on the Right:**
Every elementary row operation corresponds to multiplying on the left by an elementary matrix $E_k$. 

If a sequence of $k$ elementary row operations reduces $A$ to the identity matrix $I$, the net operation is equivalent to multiplying by the product matrix $E = E_k \cdots E_2 E_1$:

$$
E A = I
$$

By definition of the inverse matrix, any matrix that multiplies $A$ to yield $I$ is $A^{-1}$. Applying the exact same sequence of operations to the augmented matrix multiplies both blocks by $E = A^{-1}$:

$$
E [A \mid I] = [E A \mid E I] = [I \mid E] = [I \mid A^{-1}]
$$

Thus, whatever operations transform $A$ into $I$ simultaneously transform $I$ into $A^{-1}$.

---

### Problem Statement

**Exercise 4. Gauss–Jordan**

Find $A^{-1}$ using the Gauss–Jordan method for

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}.
$$

Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

> **Why this exercise:** introduces the Gauss–Jordan method together with its meaning, not merely as a sequence of operations.

---

### Solution

Given:

$$
A = \begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}
$$

Set up the initial augmented matrix $[A \mid I]$:

$$
[A \mid I] = \begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
$$

**Step 1: Eliminate the entry in the first column below the pivot**

The pivot in row 1 is $a_{11} = 1$. Eliminate the entry $3$ in row 2 by applying the row operation $R_2 \leftarrow R_2 - 3R_1$:

$$
R_2 = (3 - 3\cdot 1,\ 5 - 3\cdot 2\ \mid\ 0 - 3\cdot 1,\ 1 - 3\cdot 0) = (0, -1 \mid -3, 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

**Step 2: Normalize the second pivot to $+1$**

Multiply row 2 by $-1$ ($R_2 \leftarrow -R_2$):

$$
R_2 = (0,\ 1\ \mid\ 3,\ -1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

**Step 3: Eliminate the entry in the second column above the pivot (Jordan step)**

Using the pivot in row 2, eliminate the entry $2$ in row 1 by applying the row operation $R_1 \leftarrow R_1 - 2R_2$:

$$
R_1 = (1 - 2\cdot 0,\ 2 - 2\cdot 1\ \mid\ 1 - 2\cdot 3,\ 0 - 2(-1)) = (1, 0 \mid -5, 2)
$$

The augmented matrix is now fully reduced:

$$
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

The left side has reached the identity matrix $I$. Therefore, the matrix on the right is $A^{-1}$:

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

**Step 4: Explanation of the method**

Each elementary row operation applied above is represented by left-multiplication by an elementary matrix:

1. Operation $R_2 \leftarrow R_2 - 3R_1$ corresponds to:

   $$
   E_1 = \begin{pmatrix}
   1 & 0 \\
   -3 & 1 \\
   \end{pmatrix}
   $$

2. Operation $R_2 \leftarrow -R_2$ corresponds to:

   $$
   E_2 = \begin{pmatrix}
   1 & 0 \\
   0 & -1 \\
   \end{pmatrix}
   $$

3. Operation $R_1 \leftarrow R_1 - 2R_2$ corresponds to:

   $$
   E_3 = \begin{pmatrix}
   1 & -2 \\
   0 & 1 \\
   \end{pmatrix}
   $$

Their combined product is:

$$
E = E_3 E_2 E_1
$$

When applied to $[A \mid I]$:

$$
E [A \mid I] = [E A \mid E I] = [I \mid E]
$$

Since $E A = I$, the matrix $E$ must be $A^{-1}$. Because the same sequence of operations is simultaneously performed on the identity matrix $I$ in the right block, the right block accumulates the product $E I = E = A^{-1}$.

**Step 5: Verification by multiplication and formula**

* Compute $A A^{-1}$:

  $$
  A A^{-1} = \begin{pmatrix}
  1 & 2 \\
  3 & 5 \\
  \end{pmatrix}
  \begin{pmatrix}
  -5 & 2 \\
  3 & -1 \\
  \end{pmatrix}
  = \begin{pmatrix}
  1(-5) + 2(3) & 1(2) + 2(-1) \\
  3(-5) + 5(3) & 3(2) + 5(-1) \\
  \end{pmatrix}
  $$

  $$
  A A^{-1} = \begin{pmatrix}
  -5 + 6 & 2 - 2 \\
  -15 + 15 & 6 - 5 \\
  \end{pmatrix}
  = \begin{pmatrix}
  1 & 0 \\
  0 & 1 \\
  \end{pmatrix}
  = I
  $$

* Check using the $2 \times 2$ determinant formula:

  $$
  \det A = (1)(5) - (2)(3) = 5 - 6 = -1
  $$

  $$
  A^{-1} = \frac{1}{-1} \begin{pmatrix}
  5 & -2 \\
  -3 & 1 \\
  \end{pmatrix}
  = \begin{pmatrix}
  -5 & 2 \\
  3 & -1 \\
  \end{pmatrix}
  $$

Both checks confirm the result.

---

### Final Answer

Sequence of augmented matrices:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
\xrightarrow{R_2 - 3R_1}
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

$$
\xrightarrow{-R_2}
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
\xrightarrow{R_1 - 2R_2}
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

Inverse matrix:

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$
