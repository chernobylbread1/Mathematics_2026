### Essential Formulas

1. **Definition of Matrix Inverse:**
   An $n \times n$ matrix $A$ is invertible if there exists an $n \times n$ matrix $B$ such that:

   $$
   AB = I, \qquad BA = I
   $$

   When such a matrix exists, it is unique and denoted by $A^{-1}$.

2. **Involutory Matrix:**
   A square matrix $A$ is said to be involutory if it is its own inverse:

   $$
   A^2 = I \iff A^{-1} = A
   $$

3. **Determinant of an Involutory Matrix:**
   Applying the determinant product rule to $A^2 = I$:

   $$
   \det(A^2) = (\det A)^2 = \det I = 1 \implies \det A = \pm 1
   $$

   Because $\det A \neq 0$, an involutory matrix is always invertible.

4. **General $2 \times 2$ Involutory Matrices:**
   For a matrix:

   $$
   A = \begin{pmatrix}
   a & b \\
   c & d \\
   \end{pmatrix}
   $$

   The condition $A^2 = I$ implies $d = -a$ and $a^2 + bc = 1$ (unless $A = \pm I$).
   A standard geometric involution is a reflection matrix across the line $y = x$ or across the coordinate axes.

---

### Problem Statement

Assume that a square matrix $A$ satisfies

$$
A^2 = I.
$$

Show that

$$
A^{-1} = A.
$$

Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

> **Why this exercise:** requires using the definition of the inverse in a short argument and constructing an example independently, without introducing a new topic.

---

### Solution

**Step 1: Algebraic Proof that $A^{-1} = A$**

We present two equivalent ways to justify this result:

* **Way 1: Directly using the definition of the inverse matrix**

  By definition, a matrix $B$ is the inverse of $A$ if and only if:

  $$
  AB = I, \qquad BA = I
  $$

  We are given that $A^2 = I$, which means:

  $$
  A \cdot A = I
  $$

  Setting $B = A$, this equation simultaneously establishes both:

  $$
  A \cdot B = A \cdot A = I
  $$

  and

  $$
  B \cdot A = A \cdot A = I
  $$

  Because the inverse of an invertible matrix is unique, the unique matrix satisfying these relations must be $A^{-1}$. Therefore:

  $$
  A^{-1} = A
  $$

* **Way 2: Using the invertibility of $A$ and cancellation**

  Taking the determinant of both sides of $A^2 = I$:

  $$
  \det(A^2) = (\det A)^2 = \det I = 1 \implies \det A = \pm 1
  $$

  Since $\det A \neq 0$, the inverse $A^{-1}$ exists. Multiplying both sides of $A^2 = I$ on the left by $A^{-1}$:

  $$
  A^{-1}(A^2) = A^{-1}I
  $$

  Using the associativity of matrix multiplication:

  $$
  (A^{-1}A)A = A^{-1}
  $$

  $$
  IA = A^{-1} \implies A = A^{-1}
  $$

---

**Step 2: Constructing a $2 \times 2$ Example (Different from $I$ and $-I$)**

We seek a $2 \times 2$ matrix $A \neq I$ and $A \neq -I$ such that $A^2 = I$.

Consider the reflection matrix across the line $y = x$:

$$
A = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

Comparing $A$ with $I$ and $-I$:

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}, \qquad -I = \begin{pmatrix}
-1 & 0 \\
0 & -1 \\
\end{pmatrix}
$$

Clearly, $A \neq I$ and $A \neq -I$.

*(Other equally valid reflection matrices include $\mathrm{diag}(1, -1)$ and $\mathrm{diag}(-1, 1)$.)*

---

**Step 3: Verification by Matrix Multiplication**

Now we verify that $A^2 = I$ by direct multiplication:

$$
A^2 = A \cdot A = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

Computing each entry using row-by-column multiplication:

* Top-left entry:

  $$
  (0)(0) + (1)(1) = 0 + 1 = 1
  $$

* Top-right entry:

  $$
  (0)(1) + (1)(0) = 0 + 0 = 0
  $$

* Bottom-left entry:

  $$
  (1)(0) + (0)(1) = 0 + 0 = 0
  $$

* Bottom-right entry:

  $$
  (1)(1) + (0)(0) = 1 + 0 = 1
  $$

Combining these entries:

$$
A^2 = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

We can also independently check $A^{-1}$ using the $2 \times 2$ determinant and adjugate formula:

$$
\det A = (0)(0) - (1)(1) = 0 - 1 = -1
$$

$$
A^{-1} = \frac{1}{-1} \begin{pmatrix}
0 & -1 \\
-1 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
= A
$$

The result confirms that $A^{-1} = A$.

---

**Step 4: Geometric Interpretation**

A linear operator that is its own inverse satisfies $T^2 = \mathrm{id}$.
In geometric terms:
* The matrix $A$ swaps the standard basis vectors:

  $$
  A \begin{pmatrix}
  1 \\
  0 \\
  \end{pmatrix}
  = \begin{pmatrix}
  0 \\
  1 \\
  \end{pmatrix}, \qquad A \begin{pmatrix}
  0 \\
  1 \\
  \end{pmatrix}
  = \begin{pmatrix}
  1 \\
  0 \\
  \end{pmatrix}
  $$

* Applying this reflection a second time swaps the basis vectors back to their original positions:

  $$
  A \left( A \begin{pmatrix}
  x \\
  y \\
  \end{pmatrix} \right) = A \begin{pmatrix}
  y \\
  x \\
  \end{pmatrix}
  = \begin{pmatrix}
  x \\
  y \\
  \end{pmatrix}
  $$

* Because performing the transformation twice returns any vector to its original state, the operation undoes itself, so $A^{-1} = A$.

---

### Final Answer

1. **Proof:**
   Since $A \cdot A = I$, the matrix $A$ acts on itself to produce the identity matrix $I$. By the definition and uniqueness of the matrix inverse, $A^{-1} = A$.

2. **Example Matrix:**

   $$
   A = \begin{pmatrix}
   0 & 1 \\
   1 & 0 \\
   \end{pmatrix}
   $$

   (which is neither $I$ nor $-I$).

3. **Verification:**

   $$
   A^2 = \begin{pmatrix}
   0 & 1 \\
   1 & 0 \\
   \end{pmatrix}
   \begin{pmatrix}
   0 & 1 \\
   1 & 0 \\
   \end{pmatrix}
   = \begin{pmatrix}
   1 & 0 \\
   0 & 1 \\
   \end{pmatrix}
   = I \implies A^{-1} = A
   $$
