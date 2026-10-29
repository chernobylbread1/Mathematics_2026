### Essential Formulas

1. **Linear Dependence and Redundancy of Equations:**
   An equation $E_k$ in a linear system is **redundant** if it can be expressed as a linear combination of the other equations:

   $$
   E_k = c_1 E_1 + c_2 E_2 + \cdots + c_{k-1} E_{k-1}
   $$

   When an equation is redundant, removing it leaves the solution set completely unchanged.

2. **Detection via Row Reduction:**
   When performing Gaussian elimination on $[A \mid b]$, any redundant equation transforms into a row of all zeros:

   $$
   \begin{pmatrix}
   0 & 0 & \cdots & 0 & \mid & 0 \\
   \end{pmatrix}
   $$

   If the system is consistent and the number of non-zero rows $r = \mathrm{rank}(A)$ is strictly less than the number of unknowns $n$, the system possesses $k = n - r$ degrees of freedom (infinitely many solutions).

---

### Problem Statement

Consider the system

$$
x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.
$$

Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

> **Why this exercise:** teaches how to recognize redundant equations within a system.

---

### Solution

**Step 1: Set up the Linear System and Augmented Matrix**

Label the equations as follows:
* Equation 1 ($E_1$): $x_1 + x_2 = 10$
* Equation 2 ($E_2$): $x_2 + x_3 = 8$
* Equation 3 ($E_3$): $x_1 - x_3 = 2$

Writing in matrix form with unknowns $(x_1, x_2, x_3)^T$:

$$
[A \mid b] = \begin{pmatrix}
1 & 1 & 0 & \mid & 10 \\
0 & 1 & 1 & \mid & 8 \\
1 & 0 & -1 & \mid & 2 \\
\end{pmatrix}
$$

---

**Step 2: Perform Gaussian Elimination**

* **Eliminate $x_1$ from row 3:** Apply $R_3 \leftarrow R_3 - R_1$:

  $$
  R_3 = (1 - 1, \ 0 - 1, \ -1 - 0 \ \mid \ 2 - 10) = (0, \ -1, \ -1 \ \mid \ -8)
  $$

  The augmented matrix becomes:

  $$
  \begin{pmatrix}
  1 & 1 & 0 & \mid & 10 \\
  0 & 1 & 1 & \mid & 8 \\
  0 & -1 & -1 & \mid & -8 \\
  \end{pmatrix}
  $$

* **Eliminate $x_2$ from row 3:** Apply $R_3 \leftarrow R_3 + R_2$:

  $$
  R_3 = (0 + 0, \ -1 + 1, \ -1 + 1 \ \mid \ -8 + 8) = (0, \ 0, \ 0 \ \mid \ 0)
  $$

  The matrix is now in row echelon form:

  $$
  \begin{pmatrix}
  1 & 1 & 0 & \mid & 10 \\
  0 & 1 & 1 & \mid & 8 \\
  0 & 0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

The third row has vanished completely into $(0, 0, 0 \mid 0)$.

---

**Step 3: Solve the System in Parametric Form**

* **Pivots:**
  - Row 1 pivot is in column 1 $\implies x_1$ is a pivot variable.
  - Row 2 pivot is in column 2 $\implies x_2$ is a pivot variable.
* **Free variable:**
  - Column 3 has no pivot $\implies x_3$ is a free variable.

Set $x_3 = t \in \mathbb{R}$:
* From row 2:

  $$
  x_2 + x_3 = 8 \implies x_2 = 8 - t
  $$

* From row 1:

  $$
  x_1 + x_2 = 10 \implies x_1 + (8 - t) = 10 \implies x_1 = 2 + t
  $$

Thus, the general solution is:

$$
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{pmatrix}
= \begin{pmatrix}
2 + t \\
8 - t \\
t \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
8 \\
0 \\
\end{pmatrix}
+ t \begin{pmatrix}
1 \\
-1 \\
1 \\
\end{pmatrix}, \qquad t \in \mathbb{R}
$$

The system has **infinitely many solutions**.

---

**Step 4: Check Independence and Show the Redundancy Explicitly**

The appearance of the zero row $(0, 0, 0 \mid 0)$ shows that the three equations are **not independently necessary**.
Specifically, Equation 3 follows directly from Equation 1 and Equation 2.

We demonstrate this by direct algebraic subtraction:

$$
E_1 - E_2: \quad (x_1 + x_2) - (x_2 + x_3) = 10 - 8
$$

Simplifying the left-hand side:

$$
x_1 + x_2 - x_2 - x_3 = x_1 - x_3
$$

Simplifying the right-hand side:

$$
10 - 8 = 2
$$

Therefore:

$$
E_1 - E_2 \iff x_1 - x_3 = 2 \equiv E_3
$$

Because $E_3$ is an exact linear combination of $E_1$ and $E_2$ ($E_3 = E_1 - E_2$), any point $(x_1, x_2, x_3)$ satisfying $E_1$ and $E_2$ automatically satisfies $E_3$.
Hence, the third equation adds no new information or geometric restriction, making it redundant.

---

### Final Answer

1. **Solution of the System:**

   $$
   \begin{pmatrix}
   x_1 \\
   x_2 \\
   x_3 \\
   \end{pmatrix}
   = \begin{pmatrix}
   2 \\
   8 \\
   0 \\
   \end{pmatrix}
   + t \begin{pmatrix}
   1 \\
   -1 \\
   1 \\
   \end{pmatrix}, \qquad t \in \mathbb{R}
   $$

   or in scalar form: $x_1 = 2 + t, \ x_2 = 8 - t, \ x_3 = t$.

2. **Necessity of All Equations:**
   **No**, not all three equations are independently necessary. Equation 3 is redundant.

3. **Derivation of Redundancy:**
   Subtracting Equation 2 from Equation 1:

   $$
   (x_1 + x_2) - (x_2 + x_3) = 10 - 8 \implies x_1 - x_3 = 2
   $$

   which is identically Equation 3 ($E_3 = E_1 - E_2$).

