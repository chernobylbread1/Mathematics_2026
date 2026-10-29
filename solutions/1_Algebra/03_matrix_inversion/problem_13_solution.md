### Essential Formulas

**Inverse of a Composite Transformation (Product Rule):**
For two invertible linear transformations represented by matrices $H$ and $S$:

$$
(HS)^{-1} = S^{-1} H^{-1}
$$

**The "Undoing from the End" Principle:**
When transformations are composed in the order $T = HS$:

$$
Tx = H(Sx)
$$

Transformation $S$ acts first, and transformation $H$ acts second. To return to the initial state $x$:
1. The last operation applied ($H$) must be undone first by applying $H^{-1}$.
2. The earlier operation ($S$) is undone next by applying $S^{-1}$.

Algebraically, adjacent matrix-inverse pairs cancel associatively:

$$
(S^{-1} H^{-1})(HS) = S^{-1} (H^{-1} H) S = S^{-1} I S = S^{-1} S = I
$$

If the operations were reversed in the wrong order ($H^{-1} S^{-1}$):

$$
(H^{-1} S^{-1})(HS) \neq I
$$

---

### Problem Statement

**Exercise 13. Undoing a Composite Transformation**

The matrices

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},\qquad H=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

> **Why this exercise:** reinforces the inverse of a product in a less direct configuration.

---

### Solution

Given:

$$
S = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
H = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

**Step 1: Way 1 — First compute $T$, then invert $T$**

Compute the composite matrix $T = HS$:

$$
T = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1(2) + 1(0) & 1(0) + 1(1) \\
0(2) + 1(0) & 0(0) + 1(1) \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

Compute the determinant of $T$:

$$
\det T = (2)(1) - (1)(0) = 2
$$

Because $\det T = 2 \neq 0$, $T$ is invertible. Apply the $2 \times 2$ inverse formula:

$$
T^{-1} = \frac{1}{2} \begin{pmatrix}
1 & -1 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

**Step 2: Way 2 — Use $(HS)^{-1} = S^{-1}H^{-1}$**

Compute the individual inverses $S^{-1}$ and $H^{-1}$:

* For $S$:

  $$
  \det S = (2)(1) - (0)(0) = 2 \implies S^{-1} = \frac{1}{2} \begin{pmatrix}
  1 & 0 \\
  0 & 2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  \frac{1}{2} & 0 \\
  0 & 1 \\
  \end{pmatrix}
  $$

* For $H$:

  $$
  \det H = (1)(1) - (1)(0) = 1 \implies H^{-1} = \frac{1}{1} \begin{pmatrix}
  1 & -1 \\
  0 & 1 \\
  \end{pmatrix}
  = \begin{pmatrix}
  1 & -1 \\
  0 & 1 \\
  \end{pmatrix}
  $$

Multiply $S^{-1}$ on the left of $H^{-1}$:

$$
S^{-1} H^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\
0 + 1(0) & 0 + 1(1) \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

*Comparison:*
Both methods produce the identical inverse matrix:

$$
T^{-1} = (HS)^{-1} = S^{-1} H^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

**Step 3: Compute $H^{-1}S^{-1}$ and show that the incorrect order fails**

Now compute the product in the unreversed order:

$$
H^{-1} S^{-1} = \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1\left(\frac{1}{2}\right) + (-1)(0) & 1(0) + (-1)(1) \\
0\left(\frac{1}{2}\right) + 1(0) & 0(0) + 1(1) \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
$$

Comparing $H^{-1}S^{-1}$ with the true inverse $T^{-1}$:

$$
H^{-1} S^{-1} = \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\neq \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
= T^{-1}
$$

The entry in row 1, column 2 is $-1$ instead of $-\frac{1}{2}$. Thus, multiplying in the incorrect order produces an entirely different, incorrect matrix.

**Step 4: Explanation of the rule: "when undoing a composition of operations, we undo them from the end"**

Geometrically:
1. In $T = HS$, an initial point $(x, y)^T$ is transformed by $S$ first (scaling $x$ to $2x$), yielding $(2x, y)^T$.
2. Next, the shear $H$ is applied to this scaled point, adding $y$ to the existing $x$-coordinate to give $(2x + y, y)^T$.

To reverse this sequence:
* The shear was the **last** operation applied. We must undo it first by subtracting $y$ from the first coordinate using $H^{-1}$. This recovers $(2x, y)^T$.
* Once the shear has been removed, the scaling $S$ can be undone by applying $S^{-1}$ (dividing the first coordinate by $2$), recovering $(x, y)^T$.

If one applied $S^{-1}$ first (the incorrect order $H^{-1}S^{-1}$), the horizontal halving would act on the already-sheared coordinate $(2x + y)$, halving the shear term as well as $x$, which corrupts the subsequent undoing by $H^{-1}$.

Hence, undoing any chain of actions must strictly proceed in reverse order—from the end back to the beginning.

**Step 5: Verification by multiplication**

Multiply $T$ by $(HS)^{-1} = S^{-1}H^{-1}$:

$$
T T^{-1} = \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
2\left(\frac{1}{2}\right) + 1(0) & 2\left(-\frac{1}{2}\right) + 1(1) \\
0\left(\frac{1}{2}\right) + 1(0) & 0\left(-\frac{1}{2}\right) + 1(1) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

Multiply $T$ by the incorrect order $H^{-1}S^{-1}$:

$$
T (H^{-1}S^{-1}) = \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
2\left(\frac{1}{2}\right) + 1(0) & 2(-1) + 1(1) \\
0\left(\frac{1}{2}\right) + 1(0) & 0(-1) + 1(1) \\
\end{pmatrix}
= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\neq I
$$

This rigorously confirms that only $S^{-1}H^{-1}$ inverts $T$.

---

### Final Answer

Calculated inverse matrix:

$$
T^{-1} = (HS)^{-1} = S^{-1} H^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

Incorrect order matrix:

$$
H^{-1} S^{-1} = \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\neq T^{-1}
$$

Rule explanation:
Undoing a sequence of operations must proceed from the end because the last operation applied is outermost; it must be undone first before earlier inner operations become accessible: $(HS)^{-1} = S^{-1}H^{-1}$.
