### Essential Formulas

1. **Derivative of the Natural Logarithm with Inner Function:**
   For a differentiable function $u(x) > 0$:

   $$
   \frac{d}{dx}[\ln(u(x))] = \frac{u'(x)}{u(x)}
   $$

2. **Monotonicity and the Sign of the Derivative:**
   * If $f'(x) > 0$ on an interval, $f(x)$ is strictly increasing on that interval.
   * If $f'(x) < 0$ on an interval, $f(x)$ is strictly decreasing on that interval.
   * If $f'(x_0) = 0$, $x_0$ is a stationary (critical) point.

3. **First Derivative Test for Local Extrema:**
   If $f'(x)$ changes sign from negative to positive as $x$ increases through $x_0$, then $f(x)$ attains a strict local minimum at $x_0$.

---

### Problem Statement

For

$$
f(x)=\ln(x^2+1)
$$

compute the derivative. Then determine the sign of $f'(x)$ for $x<0$, $x=0$, and $x>0$, and describe qualitatively how the function behaves around zero.

> **Why this problem:** it connects differentiation with sign analysis and the behavior of a function.

---

### Solution

**Step 1: Compute the derivative $f'(x)$**

The function is $f(x) = \ln(x^2 + 1)$.
Note that $x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$, so the function is defined and differentiable everywhere on $\mathbb{R}$.

Identify the inner function:

$$
u(x) = x^2 + 1 \implies u'(x) = 2x
$$

Applying the logarithmic chain rule:

$$
f'(x) = \frac{u'(x)}{u(x)} = \frac{2x}{x^2 + 1}
$$

---

**Step 2: Analyze the sign of the denominator**

For all real numbers $x \in \mathbb{R}$:

$$
x^2 \ge 0 \implies x^2 + 1 \ge 1 > 0
$$

Because the denominator is strictly positive for all $x$, it does not affect the sign of the quotient. The sign of $f'(x)$ is identical to the sign of the linear numerator $2x$.

---

**Step 3: Determine the sign of $f'(x)$ in the three regions**

1. **For $x < 0$:**

   $$
   x < 0 \implies 2x < 0 \implies f'(x) = \frac{2x}{x^2 + 1} < 0
   $$

   The derivative is strictly negative. The function $f(x)$ is strictly decreasing on $(-\infty, 0)$.

2. **For $x = 0$:**

   $$
   f'(0) = \frac{2(0)}{0^2 + 1} = \frac{0}{1} = 0
   $$

   The derivative equals zero. The origin is a stationary point with a horizontal tangent line.

3. **For $x > 0$:**

   $$
   x > 0 \implies 2x > 0 \implies f'(x) = \frac{2x}{x^2 + 1} > 0
   $$

   The derivative is strictly positive. The function $f(x)$ is strictly increasing on $(0, \infty)$.

---

**Step 4: Describe the qualitative behavior around zero**

* **Local and Global Minimum:**
  Since $f'(x) < 0$ for $x < 0$ and $f'(x) > 0$ for $x > 0$, the function decreases until it reaches $x = 0$ and then immediately increases. By the First Derivative Test, $f(x)$ attains a strict global minimum at $x = 0$.
* **Minimum Value:**

  $$
  f(0) = \ln(0^2 + 1) = \ln(1) = 0
  $$

* **Symmetry:**
  Because $f(-x) = \ln((-x)^2 + 1) = \ln(x^2 + 1) = f(x)$, $f$ is an even function. The graph forms a smooth, symmetric bowl-shaped curve centered at the origin $(0, 0)$, touching the $x$-axis with a horizontal tangent.

---

### Final Answer

1. **Derivative:**

   $$
   f'(x) = \frac{2x}{x^2 + 1}
   $$

2. **Sign Analysis:**
   * For $x < 0$: $f'(x) < 0$ (negative, function decreasing)
   * For $x = 0$: $f'(0) = 0$ (zero, horizontal tangent)
   * For $x > 0$: $f'(x) > 0$ (positive, function increasing)

3. **Qualitative Behavior Around Zero:**
   The function decreases on $(-\infty, 0)$, reaches a strict global minimum at $(0, 0)$ with a horizontal tangent ($m = 0$), and increases on $(0, \infty)$, forming an even, smooth U-shaped curve.
