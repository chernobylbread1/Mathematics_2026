### Essential Formulas

**Properties of Matrix Inverses:**
Let $A$ be an invertible $n \times n$ matrix with known inverse $A^{-1}$.

1. **Inverse of a Scalar Multiple:**
   For any non-zero scalar $c \neq 0$:

   $$
   (cA)^{-1} = \frac{1}{c} A^{-1}
   $$

   *Justification:* $(cA)\left(\frac{1}{c} A^{-1}\right) = \left(c \cdot \frac{1}{c}\right) (A A^{-1}) = 1 \cdot I = I$.

2. **Inverse of a Transposed Matrix:**
   Inversion and transposition commute:

   $$
   (A^T)^{-1} = (A^{-1})^T
   $$

   *Justification:* $A^T (A^{-1})^T = (A^{-1} A)^T = I^T = I$.

3. **Inverse of a Matrix Power:**
   For any positive integer $k$:

   $$
   (A^k)^{-1} = (A^{-1})^k
   $$

   In particular, for $k = 2$:

   $$
   (A^2)^{-1} = (A^{-1})^2 = A^{-1} \cdot A^{-1}
   $$

   *Justification:* $A^2 (A^{-1})^2 = (A \cdot A)(A^{-1} \cdot A^{-1}) = A (A A^{-1}) A^{-1} = A I A^{-1} = A A^{-1} = I$.

---

### Problem Statement

**Exercise 12. Finding Inverses Without Starting from Scratch**

It is known that

$$
A^{-1}=
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}.
$$

Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

> **Why this exercise:** teaches how to use inverse properties instead of carrying out unnecessary full calculations.

---

### Solution

Given:

$$
A^{-1} = \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
$$

**Step 1: Compute $(3A)^{-1}$**

Apply the scalar multiple property with $c = 3$:

$$
(3A)^{-1} = \frac{1}{3} A^{-1}
$$

Substitute the known matrix $A^{-1}$:

$$
(3A)^{-1} = \frac{1}{3} \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
$$

*Justification:*
Multiplying a linear operator $A$ by $3$ triples the scale of every output vector. Reversing this transformation requires scaling by the reciprocal factor $\frac{1}{3}$, so $(3A)^{-1} = \frac{1}{3}A^{-1}$.

**Step 2: Compute $(A^T)^{-1}$**

Apply the transpose property of inverses:

$$
(A^T)^{-1} = (A^{-1})^T
$$

Substitute $A^{-1}$ and transpose by swapping its off-diagonal entries:

$$
(A^T)^{-1} = \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}^T
= \begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
$$

*Justification:*
Transposing reflects matrix entries across the main diagonal. Because $(A^{-1}A)^T = I^T = I$, the transpose of the inverse is precisely the inverse of the transpose.

**Step 3: Compute $(A^2)^{-1}$**

Apply the power property for $k = 2$:

$$
(A^2)^{-1} = (A^{-1})^2 = A^{-1} \cdot A^{-1}
$$

Multiply $A^{-1}$ by itself:

$$
(A^2)^{-1} = \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
$$

Compute the entries:

$$
((A^2)^{-1})_{11} = 2(2) + (-1)(-3) = 4 + 3 = 7
$$

$$
((A^2)^{-1})_{12} = 2(-1) + (-1)(2) = -2 - 2 = -4
$$

$$
((A^2)^{-1})_{21} = (-3)(2) + 2(-3) = -6 - 6 = -12
$$

$$
((A^2)^{-1})_{22} = (-3)(-1) + 2(2) = 3 + 4 = 7
$$

Assemble the product:

$$
(A^2)^{-1} = \begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
$$

*Justification:*
Applying $A^2$ corresponds to applying transformation $A$ twice in succession. To reverse this two-step process, the inverse transformation $A^{-1}$ must be applied twice: $(A \cdot A)^{-1} = A^{-1} \cdot A^{-1}$.

**Step 4: Verification by explicitly reconstructing $A$**

To independently check our property-based answers, reconstruct $A = (A^{-1})^{-1}$.

Compute $\det(A^{-1})$:

$$
\det(A^{-1}) = (2)(2) - (-1)(-3) = 4 - 3 = 1
$$

Inverting $A^{-1}$ gives matrix $A$:

$$
A = \frac{1}{1} \begin{pmatrix}
2 & 1 \\
3 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
3 & 2 \\
\end{pmatrix}
$$

Now verify each computation directly:

* For $3A$:

  $$
  3A = \begin{pmatrix}
  6 & 3 \\
  9 & 6 \\
  \end{pmatrix}
  \implies \det(3A) = 36 - 27 = 9
  $$

  $$
  (3A)^{-1} = \frac{1}{9} \begin{pmatrix}
  6 & -3 \\
  -9 & 6 \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{2}{3} & -\frac{1}{3} \\
  -1 & \frac{2}{3} \\
  \end{pmatrix}
  $$

* For $A^T$:

  $$
  A^T = \begin{pmatrix}
  2 & 3 \\
  1 & 2 \\
  \end{pmatrix}
  \implies \det(A^T) = 4 - 3 = 1
  $$

  $$
  (A^T)^{-1} = \frac{1}{1} \begin{pmatrix}
  2 & -3 \\
  -1 & 2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  2 & -3 \\
  -1 & 2 \\
  \end{pmatrix}
  $$

* For $A^2$:

  $$
  A^2 = \begin{pmatrix}
  2 & 1 \\
  3 & 2 \\
  \end{pmatrix}
  \begin{pmatrix}
  2 & 1 \\
  3 & 2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  7 & 4 \\
  12 & 7 \\
  \end{pmatrix}
  \implies \det(A^2) = 49 - 48 = 1
  $$

  $$
  (A^2)^{-1} = \frac{1}{1} \begin{pmatrix}
  7 & -4 \\
  -12 & 7 \\
  \end{pmatrix}
  = \begin{pmatrix}
  7 & -4 \\
  -12 & 7 \\
  \end{pmatrix}
  $$

All direct calculations confirm the property-based derivations.

---

### Final Answer

Calculated matrices:

$$
(3A)^{-1} = \frac{1}{3} \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
$$

$$
(A^T)^{-1} = \begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
$$

$$
(A^2)^{-1} = \begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
$$

