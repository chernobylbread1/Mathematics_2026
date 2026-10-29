### Essential Formulas

**Determinant and Invertibility of a Parameterized $2 \times 2$ Matrix:**
For a matrix $A(t)$ depending on a real parameter $t$:

$$
A(t) = \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

the determinant is:

$$
\det A(t) = (1)(1) - (t)(t) = 1 - t^2
$$

The matrix is **invertible** if and only if its determinant is non-zero:

$$
\det A(t) \neq 0 \iff 1 - t^2 \neq 0 \iff t \neq \pm 1
$$

**Explicit Formula for the Parameterized Inverse:**
For all values of $t$ where $\det A(t) \neq 0$:

$$
A(t)^{-1} = \frac{1}{\det A(t)} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 11. Parameter and Invertibility**

For

$$
A(t)=
\begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

> **Why this exercise:** combines a parameter, determinant, and an explicit inverse formula in one problem.

---

### Solution

Given the parameterized matrix:

$$
A(t) = \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

**Step 1: Compute the determinant of $A(t)$**

Apply the determinant formula for a $2 \times 2$ matrix:

$$
\det A(t) = (1)(1) - (t)(t) = 1 - t^2
$$

Factor the expression as a difference of squares:

$$
\det A(t) = (1 - t)(1 + t)
$$

**Step 2: Find all values of $t$ for which $A(t)$ is invertible**

A square matrix is invertible if and only if its determinant is non-zero:

$$
\det A(t) \neq 0
$$

Substitute the factored determinant:

$$
(1 - t)(1 + t) \neq 0 \implies t \neq 1 \quad \mathrm{and} \quad t \neq -1
$$

Thus, $A(t)$ is invertible for all real numbers $t$ except $t = 1$ and $t = -1$:

$$
t \in \mathbb{R} \setminus \{-1, 1\}
$$

**Step 3: State the formula for $A(t)^{-1}$**

For any $t \neq \pm 1$, apply the explicit $2 \times 2$ inverse formula:

$$
A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
$$

In entry form:

$$
A(t)^{-1} = \begin{pmatrix}
\frac{1}{1 - t^2} & -\frac{t}{1 - t^2} \\
-\frac{t}{1 - t^2} & \frac{1}{1 - t^2} \\
\end{pmatrix}
$$

**Step 4: Explain what happens at the excluded values ($t = 1$ and $t = -1$)**

At the excluded values $t = 1$ and $t = -1$, the denominator of the inverse formula becomes zero:

$$
1 - t^2 = 1 - (\pm 1)^2 = 1 - 1 = 0
$$

Because division by zero is undefined, the formula breaks down completely and yields no valid matrix.

Looking at the structure of $A(t)$ at each excluded value explains why this breakdown occurs:

* **For $t = 1$:**

  $$
  A(1) = \begin{pmatrix}
  1 & 1 \\
  1 & 1 \\
  \end{pmatrix}
  $$

  The two rows are identical ($R_1 = R_2$). The rows are linearly dependent, so $\mathrm{rank}(A(1)) = 1 < 2$. The transformation collapses the entire plane onto the line $x = y$.

* **For $t = -1$:**

  $$
  A(-1) = \begin{pmatrix}
  1 & -1 \\
  -1 & 1 \\
  \end{pmatrix}
  $$

  Row 2 is the exact negation of row 1 ($R_2 = -R_1$). Again, the rows are linearly dependent and $\mathrm{rank}(A(-1)) = 1 < 2$. The transformation collapses the plane onto the line $x = -y$.

In both cases, dimensionality is lost and the transformation is not one-to-one, geometrically explaining why an inverse cannot exist.

**Step 5: Verification by matrix multiplication**

For any $t \neq \pm 1$, multiply $A(t)$ by $A(t)^{-1}$:

$$
A(t) A(t)^{-1} = \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
\left[ \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \right]
$$

Compute the matrix product:

$$
A(t) A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix}
1(1) + t(-t) & 1(-t) + t(1) \\
t(1) + 1(-t) & t(-t) + 1(1) \\
\end{pmatrix}
$$

Simplify the entries:

$$
A(t) A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix}
1 - t^2 & -t + t \\
t - t & 1 - t^2 \\
\end{pmatrix}
= \frac{1}{1 - t^2} \begin{pmatrix}
1 - t^2 & 0 \\
0 & 1 - t^2 \\
\end{pmatrix}
$$

Divide by the scalar $1 - t^2 \neq 0$:

$$
A(t) A(t)^{-1} = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

This algebraic cancellation holds for every $t \neq \pm 1$.

---

### Final Answer

Invertibility condition:

$$
t \neq 1 \quad \mathrm{and} \quad t \neq -1 \quad (t \in \mathbb{R} \setminus \{-1, 1\})
$$

Formula for the inverse matrix:

$$
A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
$$

Behavior at excluded values:
At $t = \pm 1$, the denominator $1 - t^2$ becomes zero, causing the formula to fail due to division by zero. At these values, the rows of $A(t)$ become linearly dependent ($R_1 = R_2$ when $t = 1$ and $R_2 = -R_1$ when $t = -1$), reducing the rank to $1$ and making the matrix singular.
