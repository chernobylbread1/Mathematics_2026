### Essential Formulas

1. **Critical Points and Fermat's Theorem:**
   A point $x_0$ in the interior of the domain is a critical (stationary) point of a differentiable function $f(x)$ if:

   $$
   f'(x_0) = 0
   $$

2. **First Derivative Test for Monotonicity and Local Extrema:**
   * If $f'(x) > 0$ on an interval, $f(x)$ is strictly increasing on that interval.
   * If $f'(x) < 0$ on an interval, $f(x)$ is strictly decreasing on that interval.
   * If $f'(x)$ changes from positive to negative at $x_0$, $f(x)$ has a local maximum at $x_0$.
   * If $f'(x)$ changes from negative to positive at $x_0$, $f(x)$ has a local minimum at $x_0$.

3. **Second Derivative and Inflection Point:**
   An inflection point occurs where the concavity changes, which requires $f''(x_0) = 0$ (with a sign change):

   $$
   f''(x) = \frac{d^2 f}{dx^2}
   $$

---

### Problem Statement

Analyze the monotonicity and extrema of

$$
f(x)=x^3-3x^2+2.
$$

Sketch the graph based on the results and mark the critical points.

> **Why this problem:** it teaches how to use the first derivative to describe the shape of a polynomial.

---

### Solution

**Step 1: Determine the domain and compute the first derivative**

The function is a cubic polynomial, so its domain is:

$$
D_f = \mathbb{R} = (-\infty, \infty)
$$

Compute the first derivative using the power rule:

$$
f'(x) = \frac{d}{dx}[x^3 - 3x^2 + 2] = 3x^2 - 6x
$$

Factor the derivative:

$$
f'(x) = 3x(x - 2)
$$

---

**Step 2: Find the critical points**

Set $f'(x) = 0$:

$$
3x(x - 2) = 0 \implies x_1 = 0, \quad x_2 = 2
$$

The critical points partition the real line into three intervals:
* $(-\infty, 0)$
* $(0, 2)$
* $(2, \infty)$

---

**Step 3: Analyze the sign of $f'(x)$ and determine monotonicity**

Test the sign in each interval:
1. **Interval $(-\infty, 0)$:** Choose $x = -1$:

   $$
   f'(-1) = 3(-1)(-1 - 2) = 3(-1)(-3) = 9 > 0
   $$

   Thus $f'(x) > 0$: the function is strictly increasing on $(-\infty, 0]$.

2. **Interval $(0, 2)$:** Choose $x = 1$:

   $$
   f'(1) = 3(1)(1 - 2) = 3(-1) = -3 < 0
   $$

   Thus $f'(x) < 0$: the function is strictly decreasing on $[0, 2]$.

3. **Interval $(2, \infty)$:** Choose $x = 3$:

   $$
   f'(3) = 3(3)(3 - 2) = 9(1) = 9 > 0
   $$

   Thus $f'(x) > 0$: the function is strictly increasing on $[2, \infty)$.

---

**Step 4: Classify the local extrema**

Evaluate the function values at the critical points:
1. **At $x = 0$:**
   The derivative changes sign from positive to negative ($+ \to -$).
   By the First Derivative Test, $f$ has a local maximum at $x = 0$:

   $$
   f(0) = 0^3 - 3(0)^2 + 2 = 2
   $$

   Local maximum point: $(0, 2)$.

2. **At $x = 2$:**
   The derivative changes sign from negative to positive ($- \to +$).
   By the First Derivative Test, $f$ has a local minimum at $x = 2$:

   $$
   f(2) = 2^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2
   $$

   Local minimum point: $(2, -2)$.

---

**Step 5: Second derivative and inflection point**

Compute the second derivative:

$$
f''(x) = \frac{d}{dx}[3x^2 - 6x] = 6x - 6 = 6(x - 1)
$$

Set $f''(x) = 0 \implies x = 1$.
* For $x < 1$: $f''(x) < 0$ (concave downward).
* For $x > 1$: $f''(x) > 0$ (concave upward).
The point $(1, f(1)) = (1, 0)$ is the inflection point, which also happens to be a zero of the function.

---

**Step 6: Description of the graph sketch**

* The graph enters from the bottom left, since $\lim_{x \to -\infty} f(x) = -\infty$.
* It rises through its negative zero ($x = 1 - \sqrt{3} \approx -0.732$) to a local maximum at $(0, 2)$, with a horizontal tangent line.
* It descends through the inflection point and zero at $(1, 0)$ with slope $f'(1) = -3$.
* It reaches a local minimum at $(2, -2)$, with a horizontal tangent line.
* It rises through its third zero ($x = 1 + \sqrt{3} \approx 2.732$) and diverges toward $+\infty$ as $x \to \infty$.

---

### Final Answer

1. **Monotonicity:**
   * Strictly increasing on $(-\infty, 0]$ and on $[2, \infty)$
   * Strictly decreasing on $[0, 2]$

2. **Extrema:**
   * **Local Maximum:** at $(0, 2)$
   * **Local Minimum:** at $(2, -2)$

3. **Key Geometric Features:**
   * Critical points: $(0, 2)$ (local max) and $(2, -2)$ (local min)
   * Inflection point: $(1, 0)$
   * Polynomial limits: $\lim_{x \to -\infty} f(x) = -\infty$ and $\lim_{x \to \infty} f(x) = +\infty$

