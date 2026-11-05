### Essential Formulas

1. **First Derivative and Local Extrema:**
   For a differentiable function $f(x)$, critical points satisfy $f'(x_0) = 0$.
   The nature of the extremum is determined by the sign changes of $f'(x)$ or the sign of $f''(x_0)$.

2. **Second Derivative and Curvature (Convexity/Concavity):**
   * If $f''(x) > 0$ on an interval, the graph is **concave upward** (convex).
   * If $f''(x) < 0$ on an interval, the graph is **concave downward** (concave).

3. **Inflection Points:**
   A point $(x_0, f(x_0))$ is an inflection point if the function is continuous at $x_0$ and the concavity changes strictly across $x_0$, which requires $f''(x_0) = 0$ (with sign change).

---

### Problem Statement

For

$$
f(x)=x^4-4x^2
$$

find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

> **Why this problem:** it introduces the second derivative as a tool for describing the curvature of a graph.

---

### Solution

**Step 1: Domain, symmetry, and zeros**

The function is a polynomial, so $D_f = \mathbb{R}$.
Checking symmetry:

$$
f(-x) = (-x)^4 - 4(-x)^2 = x^4 - 4x^2 = f(x)
$$

The function is even; the graph is completely symmetric about the $y$-axis.
Find the zeros:

$$
x^4 - 4x^2 = 0 \iff x^2(x^2 - 4) = 0 \iff x^2(x - 2)(x + 2) = 0
$$

The zeros are $x = 0$ (multiplicity $2$) and $x = \pm 2$.

---

**Step 2: First derivative and local extrema**

Compute $f'(x)$:

$$
f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 4x(x - \sqrt{2})(x + \sqrt{2})
$$

Set $f'(x) = 0$ to find critical points:

$$
x_1 = -\sqrt{2}, \qquad x_2 = 0, \qquad x_3 = \sqrt{2}
$$

Analyze the sign of $f'(x)$:
* On $(-\infty, -\sqrt{2})$: $f'(x) < 0$ (strictly decreasing).
* On $(-\sqrt{2}, 0)$: $f'(x) > 0$ (strictly increasing).
* On $(0, \sqrt{2})$: $f'(x) < 0$ (strictly decreasing).
* On $(\sqrt{2}, \infty)$: $f'(x) > 0$ (strictly increasing).

Evaluate the function values at the critical points:
1. **At $x = \pm\sqrt{2}$:**
   The derivative changes from negative to positive.

   $$
   f(\pm\sqrt{2}) = (\sqrt{2})^4 - 4(\sqrt{2})^2 = 4 - 4(2) = 4 - 8 = -4
   $$

   Local and global minima at $(-\sqrt{2}, -4)$ and $(\sqrt{2}, -4)$.

2. **At $x = 0$:**
   The derivative changes from positive to negative.

   $$
   f(0) = 0
   $$

   Local maximum at $(0, 0)$.

---

**Step 3: Second derivative, intervals of curvature, and inflection points**

Compute the second derivative:

$$
f''(x) = \frac{d}{dx}[4x^3 - 8x] = 12x^2 - 8 = 4(3x^2 - 2)
$$

Set $f''(x) = 0$:

$$
3x^2 - 2 = 0 \iff x^2 = \frac{2}{3} \iff x = \pm\sqrt{\frac{2}{3}} = \pm\frac{\sqrt{6}}{3} \approx \pm 0.8165
$$

Determine the sign of $f''(x)$:
* **On $\left(-\infty, -\sqrt{2/3}\right)$:** $x^2 > 2/3 \implies f''(x) > 0$. The graph is **concave upward** (convex).
* **On $\left(-\sqrt{2/3}, \sqrt{2/3}\right)$:** $x^2 < 2/3 \implies f''(x) < 0$. The graph is **concave downward** (concave).
* **On $\left(\sqrt{2/3}, \infty\right)$:** $x^2 > 2/3 \implies f''(x) > 0$. The graph is **concave upward** (convex).

Evaluate the function value at the inflection points:

$$
f\left(\pm\sqrt{\frac{2}{3}}\right) = \left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) = \frac{4}{9} - \frac{8}{3} = \frac{4 - 24}{9} = -\frac{20}{9} \approx -2.222
$$

The inflection points are:

$$
I_1 = \left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right), \qquad I_2 = \left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)
$$

---

**Step 4: Summary for the sketch of the graph**

The curve exhibits a classic symmetric "W-shape":
1. Decreases from $+\infty$ in the second quadrant, crosses the $x$-axis at $(-2, 0)$.
2. Passes through inflection point $I_1\left(-\sqrt{2/3}, -20/9\right)$, where curvature changes from upward to downward.
3. Bottoms out at the left global minimum $(-\sqrt{2}, -4)$ with horizontal tangent.
4. Rises concave-down to touch the origin $(0, 0)$ as a local maximum (tangent is horizontal).
5. Mirrors symmetrically across the $y$-axis: drops to inflection point $I_2$, reaches right global minimum $(\sqrt{2}, -4)$, crosses $x$-axis at $(2, 0)$, and ascends toward $+\infty$.

---

### Final Answer

1. **Local Extrema:**
   * **Global Minima:** at $(-\sqrt{2}, -4)$ and $(\sqrt{2}, -4)$
   * **Local Maximum:** at $(0, 0)$

2. **Curvature (Convexity and Concavity):**
   * **Concave Upward (Convex):** on $\left(-\infty, -\sqrt{2/3}\right)$ and on $\left(\sqrt{2/3}, \infty\right)$
   * **Concave Downward (Concave):** on $\left(-\sqrt{2/3}, \sqrt{2/3}\right)$

3. **Inflection Points:**

   $$
   \left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right), \qquad \left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)
   $$
