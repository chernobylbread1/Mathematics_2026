### Essential Formulas

1. **Symmetry of Functions:**
   * **Even Function:** $f(-x) = f(x)$ (symmetric with respect to the $y$-axis).
   * **Odd Function:** $f(-x) = -f(x)$ (symmetric with respect to the origin).

2. **Quotient Rule for Differentiation:**

   $$
   \left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}
   $$

3. **Conditions for Extrema and Curvature:**
   * Critical points: $f'(x_0) = 0$.
   * Inflection points: $f''(x_0) = 0$ with a sign change across $x_0$.
   * Concave upward (convex) if $f''(x) > 0$; concave downward (concave) if $f''(x) < 0$.

---

### Problem Statement

Perform a complete analysis of

$$
f(x)=\frac{x}{x^2+1}.
$$

Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

> **Why this problem:** it combines all the basic elements of function analysis into one organized process.

---

### Solution

**Step 1: Domain, symmetry, and zeros**

1. **Domain:**
   Because $x^2 + 1 \ge 1 > 0$ for all real numbers $x$, the denominator never vanishes:

   $$
   D_f = \mathbb{R} = (-\infty, \infty)
   $$

   The function is continuous and infinitely differentiable on the entire real line.

2. **Symmetry:**
   Evaluate $f(-x)$:

   $$
   f(-x) = \frac{-x}{(-x)^2 + 1} = -\frac{x}{x^2 + 1} = -f(x)
   $$

   The function is **odd**, which means its graph possesses rotational point symmetry of $180^\circ$ about the origin $(0, 0)$.

3. **Zeros and Intercepts:**

   $$
   f(x) = 0 \iff x = 0
   $$

   The origin $(0, 0)$ is the unique $x$-intercept and $y$-intercept.

---

**Step 2: Limits at infinity and asymptotes**

Compute the limits as $x \to \pm\infty$:

$$
\lim_{x \to \infty} \frac{x}{x^2 + 1} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{0}{1 + 0} = 0
$$

$$
\lim_{x \to -\infty} \frac{x}{x^2 + 1} = 0
$$

* The horizontal line $y = 0$ ($x$-axis) is the horizontal asymptote in both directions.
* There are no vertical asymptotes because the denominator has no real roots.

---

**Step 3: First derivative, monotonicity, and local extrema**

Differentiate using the quotient rule:

$$
f'(x) = \frac{(1)(x^2 + 1) - x(2x)}{(x^2 + 1)^2} = \frac{x^2 + 1 - 2x^2}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2}
$$

Factor the numerator:

$$
f'(x) = \frac{(1 - x)(1 + x)}{(x^2 + 1)^2}
$$

Set $f'(x) = 0$ to find critical points:

$$
1 - x^2 = 0 \implies x_1 = -1, \quad x_2 = 1
$$

The denominator $(x^2 + 1)^2 > 0$ is strictly positive. The sign of $f'(x)$ is governed by $1 - x^2$:
* On $(-\infty, -1)$: $x^2 > 1 \implies f'(x) < 0$ (strictly decreasing).
* On $(-1, 1)$: $x^2 < 1 \implies f'(x) > 0$ (strictly increasing).
* On $(1, \infty)$: $x^2 > 1 \implies f'(x) < 0$ (strictly decreasing).

Evaluate the function values at the critical points:
1. **At $x = -1$:**
   Derivative changes from negative to positive ($- \to +$).

   $$
   f(-1) = \frac{-1}{(-1)^2 + 1} = -\frac{1}{2}
   $$

   Local and global minimum at $\left(-1, -\frac{1}{2}\right)$.

2. **At $x = 1$:**
   Derivative changes from positive to negative ($+ \to -$).

   $$
   f(1) = \frac{1}{1^2 + 1} = \frac{1}{2}
   $$

   Local and global maximum at $\left(1, \frac{1}{2}\right)$.

---

**Step 4: Second derivative, convexity, and inflection points**

Differentiate $f'(x) = \frac{1 - x^2}{(x^2 + 1)^2}$:

$$
f''(x) = \frac{(-2x)(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1)(2x)}{(x^2 + 1)^4}
$$

Cancel the common factor $(x^2 + 1)$:

$$
f''(x) = \frac{-2x(x^2 + 1) - 4x(1 - x^2)}{(x^2 + 1)^3} = \frac{-2x^3 - 2x - 4x + 4x^3}{(x^2 + 1)^3} = \frac{2x^3 - 6x}{(x^2 + 1)^3}
$$

Factor the numerator:

$$
f''(x) = \frac{2x(x^2 - 3)}{(x^2 + 1)^3} = \frac{2x(x - \sqrt{3})(x + \sqrt{3})}{(x^2 + 1)^3}
$$

Set $f''(x) = 0$:

$$
x_1 = -\sqrt{3}, \qquad x_2 = 0, \qquad x_3 = \sqrt{3}
$$

Analyze the sign of $f''(x)$:
* On $(-\infty, -\sqrt{3})$: $f''(x) < 0$ (concave downward).
* On $(-\sqrt{3}, 0)$: $f''(x) > 0$ (concave upward).
* On $(0, \sqrt{3})$: $f''(x) < 0$ (concave downward).
* On $(\sqrt{3}, \infty)$: $f''(x) > 0$ (concave upward).

Compute the inflection points:
* At $x = -\sqrt{3}$: $f(-\sqrt{3}) = \frac{-\sqrt{3}}{3 + 1} = -\frac{\sqrt{3}}{4} \approx -0.4330$
* At $x = 0$: $f(0) = 0$
* At $x = \sqrt{3}$: $f(\sqrt{3}) = \frac{\sqrt{3}}{4} \approx 0.4330$

The inflection points are:

$$
I_1 = \left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right), \qquad I_2 = (0, 0), \qquad I_3 = \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)
$$

---

**Step 5: Visual reconstruction of the graph sketch**

1. Starts asymptotically from below the negative $x$-axis as $x \to -\infty$.
2. Curving downward until inflection point $I_1\left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right)$, where it bends upward.
3. Bottoms out at the global minimum $\left(-1, -\frac{1}{2}\right)$ with a horizontal tangent ($m = 0$).
4. Ascends through the origin $(0, 0)$ with maximum slope $f'(0) = 1$, switching to concave downward.
5. Reaches the global maximum $\left(1, \frac{1}{2}\right)$ with a horizontal tangent ($m = 0$).
6. Descends through inflection point $I_3\left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$, bending upward to form an asymptotic tail approaching $y = 0$ from above.

---

### Final Answer

1. **Domain:** $D_f = \mathbb{R}$
2. **Symmetry:** Odd function ($f(-x) = -f(x)$, point symmetry about origin)
3. **Zeros:** $(0, 0)$
4. **Asymptotes:** Horizontal asymptote $y = 0$ (no vertical asymptotes)
5. **Extrema:**
   * Global Minimum: $\left(-1, -\frac{1}{2}\right)$
   * Global Maximum: $\left(1, \frac{1}{2}\right)$
6. **Inflection Points:**

   $$
   \left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right), \qquad (0, 0), \qquad \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)
   $$

