### Essential Formulas

1. **Interval Additivity of Definite Integrals:**
   For any integrable function $f(x)$ on $[a, c]$ and partition point $b \in (a, c)$:

   $$
   \int_a^c f(x) \, dx = \int_a^b f(x) \, dx + \int_b^c f(x) \, dx
   $$

2. **Geometric Formulas for Elementary Shapes:**
   * Area of a triangle: $A = \frac{1}{2} b h$
   * Area of a rectangle: $A = b h$

3. **Fundamental Theorem of Calculus:**

   $$
   \int_a^b f(x) \, dx = F(b) - F(a)
   $$

---

### Problem Statement

Let

$$
f(x)=
\begin{cases}
x+1,&-1\le x<1, \\
2,&1\le x\le3.
\end{cases}
$$

Sketch the graph, decide where to split the integral, compute

$$
\int_{-1}^{3}f(x)\,dx
$$

and verify the result geometrically.

> **Why this problem:** it requires understanding the definition of the function before carrying out the calculation.

---

### Solution

**Step 1: Analyze and sketch the graph of $f(x)$**

The function is defined piecewise on $[-1, 3]$:
1. **First branch on $[-1, 1)$:**
   The function is linear: $f(x) = x + 1$.
   * At the left endpoint: $f(-1) = -1 + 1 = 0$, giving the intercept $(-1, 0)$.
   * As $x \to 1^-$: $\lim_{x \to 1^-} (x + 1) = 2$.
   This segment is a straight line sloping upward from $(-1, 0)$ to $(1, 2)$.

2. **Second branch on $[1, 3]$:**
   The function is constant: $f(x) = 2$.
   * At $x = 1$: $f(1) = 2$.
   * At $x = 3$: $f(3) = 2$.
   This segment is a horizontal line segment from $(1, 2)$ to $(3, 2)$.

**Continuity at the Transition Point:**
Notice that $\lim_{x \to 1^-} f(x) = 2 = f(1)$. The two branches join continuously at the point $(1, 2)$. The graph consists of a ramp rising from $(-1, 0)$ to $(1, 2)$, followed by a flat plateau at height $2$ continuing to $(3, 2)$.

---

**Step 2: Decide where to split the integral**

Because the analytical formula defining $f(x)$ changes rule at $x = 1$, the integral must be split at the transition point $x = 1$:

$$
\int_{-1}^{3} f(x) \, dx = \int_{-1}^{1} f(x) \, dx + \int_{1}^{3} f(x) \, dx
$$

Substitute the respective branch formulas into each integral:

$$
\int_{-1}^{3} f(x) \, dx = \int_{-1}^{1} (x + 1) \, dx + \int_{1}^{3} 2 \, dx
$$

---

**Step 3: Compute each integral algebraically**

1. **Evaluate the first integral $I_1$ on $[-1, 1]$:**

   $$
   I_1 = \int_{-1}^{1} (x + 1) \, dx = \left[ \frac{x^2}{2} + x \right]_{-1}^{1}
   $$

   Substitute the limits:

   $$
   I_1 = \left(\frac{1^2}{2} + 1\right) - \left(\frac{(-1)^2}{2} + (-1)\right) = \left(\frac{1}{2} + 1\right) - \left(\frac{1}{2} - 1\right)
   $$

   $$
   I_1 = \frac{3}{2} - \left(-\frac{1}{2}\right) = \frac{3}{2} + \frac{1}{2} = 2
   $$

2. **Evaluate the second integral $I_2$ on $[1, 3]$:**

   $$
   I_2 = \int_{1}^{3} 2 \, dx = \left[ 2x \right]_{1}^{3} = 2(3) - 2(1) = 6 - 2 = 4
   $$

3. **Sum the two components:**

   $$
   \int_{-1}^{3} f(x) \, dx = I_1 + I_2 = 2 + 4 = 6
   $$

---

**Step 4: Verify the result geometrically**

Because $f(x) \ge 0$ on all of $[-1, 3]$, the definite integral represents the exact geometric area enclosed under the graph:
1. **Geometric Shape of Region 1 (under the line from $x = -1$ to $x = 1$):**
   This region is a right-angled triangle lying on the $x$-axis:
   * Base: $b_1 = 1 - (-1) = 2$
   * Height: $h_1 = f(1) = 2$

   Compute its area using the triangle formula:

   $$
   A_1 = \frac{1}{2} \cdot b_1 \cdot h_1 = \frac{1}{2} \cdot 2 \cdot 2 = 2
   $$

   This matches $I_1 = 2$.

2. **Geometric Shape of Region 2 (under the line from $x = 1$ to $x = 3$):**
   This region is a rectangle lying on the $x$-axis:
   * Base: $b_2 = 3 - 1 = 2$
   * Height: $h_2 = 2$

   Compute its area using the rectangle formula:

   $$
   A_2 = b_2 \cdot h_2 = 2 \cdot 2 = 4
   $$

   This matches $I_2 = 4$.

3. **Total Geometric Area:**

   $$
   A_{\mathrm{total}} = A_1 + A_2 = 2 + 4 = 6
   $$

The geometric area matches the analytical calculation.

---

### Final Answer

1. **Split Point:**
   The integral splits at $x = 1$:

   $$
   \int_{-1}^{3} f(x) \, dx = \int_{-1}^{1} (x + 1) \, dx + \int_{1}^{3} 2 \, dx
   $$

2. **Evaluation of the Definite Integral:**

   $$
   \int_{-1}^{3} f(x) \, dx = 2 + 4 = 6
   $$

3. **Geometric Verification:**
   The region under the graph decomposes into a right triangle of base $2$ and height $2$ (area $2$) plus a rectangle of width $2$ and height $2$ (area $4$). The sum of their geometric areas is $2 + 4 = 6$.
