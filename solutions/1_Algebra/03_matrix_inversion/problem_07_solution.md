### Essential Formulas

**Inverse of a Matrix Product (Reversal Rule):**
For any two invertible matrices $A$ and $B$ of the same size, the product $AB$ is invertible and its inverse is given by the product of the individual inverses in **reversed order**:

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

**Algebraic Justification:**
Multiplying $AB$ on the left by $B^{-1}A^{-1}$ allows the adjacent inverse pairs to collapse associatively into the identity matrix:

$$
(B^{-1} A^{-1})(A B) = B^{-1} (A^{-1} A) B = B^{-1} I B = B^{-1} B = I
$$

Similarly on the right:

$$
(A B)(B^{-1} A^{-1}) = A (B B^{-1}) A^{-1} = A I A^{-1} = A A^{-1} = I
$$

If the order were not reversed ($A^{-1}B^{-1}$), the factors $A^{-1}$ and $A$ would be separated by $B^{-1}$, preventing cancellation because matrix multiplication is non-commutative.

---

### Problem Statement

**Exercise 7. Inverse of a Product**

For

$$
A=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix}
$$

compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

> **Why this exercise:** reinforces the inverse-of-a-product property and requires its interpretation.

---

### Solution

Given:

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix}
$$

**Step 1: Compute $(AB)^{-1}$ by direct multiplication and inversion**

Compute the matrix product $AB$:

$$
AB = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
1(2) + 1(0) & 1(0) + 1(3) \\
0(2) + 1(0) & 0(0) + 1(3) \\
\end{pmatrix}
= \begin{pmatrix}
2 & 3 \\
0 & 3 \\
\end{pmatrix}
$$

Compute the determinant of $AB$:

$$
\det(AB) = (2)(3) - (3)(0) = 6
$$

Since $\det(AB) = 6 \neq 0$, find $(AB)^{-1}$ using the $2 \times 2$ inverse formula:

$$
(AB)^{-1} = \frac{1}{6} \begin{pmatrix}
3 & -3 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

**Step 2: Compute individual inverses $A^{-1}$ and $B^{-1}$, then $B^{-1}A^{-1}$**

* For matrix $A$:

  $$
  \det A = (1)(1) - (1)(0) = 1
  $$

  $$
  A^{-1} = \frac{1}{1} \begin{pmatrix}
  1 & -1 \\
  0 & 1 \\
  \end{pmatrix}
  = \begin{pmatrix}
  1 & -1 \\
  0 & 1 \\
  \end{pmatrix}
  $$

* For matrix $B$:

  $$
  \det B = (2)(3) - (0)(0) = 6
  $$

  $$
  B^{-1} = \frac{1}{6} \begin{pmatrix}
  3 & 0 \\
  0 & 2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{1}{2} & 0 \\
  0 & \frac{1}{3} \\
  \end{pmatrix}
  $$

Now multiply $B^{-1}$ on the left of $A^{-1}$:

$$
B^{-1} A^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\
0 + \frac{1}{3}(0) & 0 + \frac{1}{3}(1) \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

**Step 3: Compare results and explain the reversed order**

Comparing the results:

$$
(AB)^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
= B^{-1} A^{-1}
$$

Both calculations yield identical matrices.

*Meaning of the reversed order:*
When transformations are composed, the sequence of operations acts from right to left:
1. In $ABx = A(Bx)$, vector $x$ is transformed first by $B$, and the intermediate result $Bx$ is transformed second by $A$.
2. To undo this composition, the last operation applied must be reversed first. Therefore, we must first apply $A^{-1}$ to undo $A$, and subsequently apply $B^{-1}$ to undo $B$.
3. This is commonly known as the **shoes and socks principle**: when putting on socks and then shoes ($AB$), undoing the process requires taking off the shoes first and then the socks ($B^{-1}A^{-1}$).

**Step 4: Verification using the unreversed order**

To demonstrate that the reversed order is strictly necessary, compute $A^{-1}B^{-1}$:

$$
A^{-1} B^{-1} = \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{3} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

Notice that:

$$
A^{-1} B^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{3} \\
0 & \frac{1}{3} \\
\end{pmatrix}
\neq \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
= (AB)^{-1}
$$

The unreversed product fails because $(AB)(A^{-1}B^{-1}) \neq I$. This confirms that reversing the order to $B^{-1}A^{-1}$ is mathematically essential.

---

### Final Answer

Calculated matrices:

$$
(AB)^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

$$
B^{-1} A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

Conclusion:

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

The order is reversed because the last transformation applied in $A(Bx)$ must be undone first: $B^{-1}(A^{-1}(ABx)) = x$.
