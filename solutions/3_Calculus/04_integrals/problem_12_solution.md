### Essential Formulas

1. **Integral of an Odd Function over a Symmetric Interval:**
   If $f(-x) = -f(x)$ for all $x \in [-a, a]$, then:

   $$
   \int_{-a}^{a} f(x) \, dx = 0
   $$

2. **Integral of an Even Function over a Symmetric Interval:**
   If $g(-x) = g(x)$ for all $x \in [-a, a]$, then:

   $$
   \int_{-a}^{a} g(x) \, dx = 2 \int_{0}^{a} g(x) \, dx
   $$

3. **Piecewise Splitting for Absolute Value:**

   $$
   |x| =
   \begin{cases}
   -x, & x < 0, \\
   x, & x \ge 0
   \end{cases}
   $$

---

### Problem Statement

Compare

$$
\int_{-2}^{2}x\,dx
$$

and

$$
\int_{-2}^{2}|x|\,dx.
$$

Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

> **Why this problem:** it teaches how to use symmetry and geometry before applying a computational procedure.

---

### Solution

**Step 1: Predict results from symmetry and geometric sketches**

1. **First Function: $f(x) = x$**
   * **Symmetry:** $f(-x) = -x = -f(x)$. The function is **odd**; its graph is symmetric with respect to the origin $(0, 0)$.
   * **Geometric Sketch:** On $[-2, 2]$, the line $y = x$ forms two congruent triangles:
     * Triangle 1 on $[-2, 0]$ lies below the $x$-axis, with base $2$ and height $2$. Signed contribution: $-2$.
     * Triangle 2 on $[0, 2]$ lies above the $x$-axis, with base $2$ and height $2$. Signed contribution: $+2$.
   * **Prediction:** The negative signed area on the left cancels the positive signed area on the right:

     $$
     \int_{-2}^{2} x \, dx = 0
     $$

2. **Second Function: $g(x) = |x|$**
   * **Symmetry:** $g(-x) = |-x| = |x| = g(x)$. The function is **even**; its graph is symmetric with respect to the $y$-axis.
   * **Geometric Sketch:** The absolute value reflects the left branch upward into the upper half-plane, forming a symmetric V-shape.
     * Both triangles lie above the $x$-axis, each possessing geometric area $\frac{1}{2} \cdot 2 \cdot 2 = 2$.
   * **Prediction:** Both halves contribute positively and reinforce each other:

     $$
     \int_{-2}^{2} |x| \, dx = 2 + 2 = 4
     $$

---

**Step 2: Carry out the exact calculation for $\int_{-2}^2 x \, dx$**

Find the antiderivative $F(x) = \frac{x^2}{2}$:

$$
\int_{-2}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{-2}^{2}
$$

Apply the Fundamental Theorem of Calculus:

$$
= \frac{2^2}{2} - \frac{(-2)^2}{2} = \frac{4}{2} - \frac{4}{2} = 2 - 2 = 0
$$

The exact evaluation confirms the prediction of $0$.

---

**Step 3: Carry out the exact calculation for $\int_{-2}^2 |x| \, dx$**

Split the integral at $x = 0$ according to the piecewise definition of $|x|$:

$$
\int_{-2}^{2} |x| \, dx = \int_{-2}^{0} (-x) \, dx + \int_{0}^{2} x \, dx
$$

Evaluate each integral:
1. Left integral on $[-2, 0]$:

   $$
   \int_{-2}^{0} (-x) \, dx = \left[ -\frac{x^2}{2} \right]_{-2}^{0} = 0 - \left(-\frac{(-2)^2}{2}\right) = 0 - (-2) = 2
   $$

2. Right integral on $[0, 2]$:

   $$
   \int_{0}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{0}^{2} = \frac{2^2}{2} - 0 = 2 - 0 = 2
   $$

Summing the two contributions:

$$
\int_{-2}^{2} |x| \, dx = 2 + 2 = 4
$$

The exact evaluation confirms the prediction of $4$.

---

**Step 4: Explain the difference between the two integrals**

1. **Signed Area vs. Total Area:**
   * In $\int_{-2}^2 x \, dx$, the definite integral computes **net signed accumulation**. Because $x$ changes sign across the symmetric midpoint $x = 0$, the negative area on $[-2, 0]$ directly negates the positive area on $[0, 2]$:

     $$
     (-2) + (+2) = 0
     $$

   * In $\int_{-2}^2 |x| \, dx$, the absolute value operator removes all signs, measuring **total geometric area**. The negative output is folded upward, transforming subtraction into addition:

     $$
     |-2| + |+2| = 2 + 2 = 4
     $$

2. **Parity Role:**
   Odd symmetry over a symmetric interval always integrates to zero due to mutual cancellation. Even symmetry doubles the integral of one half.

---

### Final Answer

1. **Predictions from Symmetry:**
   * $\int_{-2}^{2} x \, dx = 0$ (odd function over symmetric interval $[-2, 2]$)
   * $\int_{-2}^{2} |x| \, dx = 4$ (even function, sum of two positive areas of $2$)

2. **Exact Computed Values:**

   $$
   \int_{-2}^{2} x \, dx = 0
   $$

   $$
   \int_{-2}^{2} |x| \, dx = 4
   $$

3. **Explanation of Difference:**
   The integral of $x$ measures signed area, where opposite signs cancel ($2 - 2 = 0$). The integral of $|x|$ measures total geometric area, eliminating cancellation and summing both positive triangles ($2 + 2 = 4$).
