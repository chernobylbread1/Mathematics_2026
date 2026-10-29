### Essential Formulas

**Diagonal Scaling Matrix and Its Inverse:**
A diagonal matrix in $\mathbb{R}^2$ represents a non-uniform scaling transformation along the coordinate axes:

$$
S = \begin{pmatrix}
k_1 & 0 \\
0 & k_2 \\
\end{pmatrix}
$$

When applied to a vector $v = (x, y)^T$:

$$
Sv = \begin{pmatrix}
k_1 x \\
k_2 y \\
\end{pmatrix}
$$

The transformation scales the $x$-coordinate by a factor of $k_1$ and the $y$-coordinate by a factor of $k_2$.

If $k_1 \neq 0$ and $k_2 \neq 0$, the inverse transformation is represented by inverting each non-zero diagonal scale factor:

$$
S^{-1} = \begin{pmatrix}
\frac{1}{k_1} & 0 \\
0 & \frac{1}{k_2} \\
\end{pmatrix}
$$

**Undoing a Geometric Transformation:**
Applying a transformation followed by its inverse restores any input vector $v$ to itself:

$$
S^{-1}(Sv) = (S^{-1}S)v = Iv = v
$$

---

### Problem Statement

**Exercise 8. Inverse of a Transformation**

The matrix

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & \frac12 \\
\end{pmatrix}
$$

describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

> **Why this exercise:** gives the inverse the interpretation of undoing a transformation.

---

### Solution

Given the scaling matrix:

$$
S = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 1: Find the inverse matrix $S^{-1}$**

Compute the determinant of $S$:

$$
\det S = (2)\left(\frac{1}{2}\right) - (0)(0) = 1
$$

Since $\det S = 1 \neq 0$, $S$ is invertible. Using the $2 \times 2$ inverse formula:

$$
S^{-1} = \frac{1}{1} \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

**Step 2: Geometric explanation of the inverse transformation**

* **Action of $S$:**
  Matrix $S$ acts on an arbitrary point $(x, y)^T$ as:

  $$
  S \begin{pmatrix}
  x \\
  y \\
  \end{pmatrix}
  = \begin{pmatrix}
  2x \\
  \frac{1}{2}y \\
  \end{pmatrix}
  $$

  It stretches the plane horizontally by a factor of $2$ along the $x$-axis and compresses the plane vertically by a factor of $\frac{1}{2}$ along the $y$-axis.

* **Action of $S^{-1}$:**
  Matrix $S^{-1}$ acts on a point $(u, v)^T$ as:

  $$
  S^{-1} \begin{pmatrix}
  u \\
  v \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{1}{2}u \\
  2v \\
  \end{pmatrix}
  $$

  It reverses each individual deformation: it compresses the plane horizontally by a factor of $\frac{1}{2}$ (undoing the horizontal stretch) and expands the plane vertically by a factor of $2$ (undoing the vertical compression).

*Geometrically:*
The inverse transformation $S^{-1}$ completely undoes the geometric deformation imposed by $S$, bringing every stretched or compressed coordinate back to its initial position in the plane.

**Step 3: Check the action of $S$ and $S^{-1}$ on a simple vector**

Choose the vector:

$$
v = \begin{pmatrix}
4 \\
6 \\
\end{pmatrix}
$$

1. Apply the transformation $S$ to $v$:

   $$
   v' = Sv = \begin{pmatrix}
   2 & 0 \\
   0 & \frac{1}{2} \\
   \end{pmatrix}
   \begin{pmatrix}
   4 \\
   6 \\
   \end{pmatrix}
   = \begin{pmatrix}
   2(4) \\
   \frac{1}{2}(6) \\
   \end{pmatrix}
   = \begin{pmatrix}
   8 \\
   3 \\
   \end{pmatrix}
   $$

   The horizontal coordinate doubled ($4 \to 8$) and the vertical coordinate halved ($6 \to 3$).

2. Apply the inverse transformation $S^{-1}$ to the intermediate vector $v'$:

   $$
   S^{-1}v' = \begin{pmatrix}
   \frac{1}{2} & 0 \\
   0 & 2 \\
   \end{pmatrix}
   \begin{pmatrix}
   8 \\
   3 \\
   \end{pmatrix}
   = \begin{pmatrix}
   \frac{1}{2}(8) \\
   2(3) \\
   \end{pmatrix}
   = \begin{pmatrix}
   4 \\
   6 \\
   \end{pmatrix}
   = v
   $$

The vector $(8, 3)^T$ is mapped back to the original vector $(4, 6)^T$, confirming that $S^{-1}(Sv) = v$.

**Step 4: Verification by direct matrix multiplication**

Multiply $S$ by $S^{-1}$:

$$
S S^{-1} = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
2\left(\frac{1}{2}\right) & 0 \\
0 & \left(\frac{1}{2}\right)(2) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

$$
S^{-1} S = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
= \begin{pmatrix}
\left(\frac{1}{2}\right)(2) & 0 \\
0 & 2\left(\frac{1}{2}\right) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

The identity matrix is produced in both orders.

---

### Final Answer

Inverse matrix:

$$
S^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

Geometric explanation:
While $S$ stretches by $2$ along the $x$-axis and compresses by $\frac{1}{2}$ along the $y$-axis, the inverse $S^{-1}$ reverses these actions by compressing by $\frac{1}{2}$ along the $x$-axis and stretching by $2$ along the $y$-axis.

Action on test vector $v = (4, 6)^T$:

$$
Sv = \begin{pmatrix}
8 \\
3 \\
\end{pmatrix},
\qquad
S^{-1}(Sv) = \begin{pmatrix}
4 \\
6 \\
\end{pmatrix}
= v
$$
