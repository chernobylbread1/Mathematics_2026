### Essential Formulas

1. **Definition of Absolute Value:**
   For any real expression $u$:

   $$
   |u| =
   \begin{cases}
   u, & u \ge 0, \\
   -u, & u < 0
   \end{cases}
   $$

2. **Differentiability via One-Sided Derivatives:**
   A continuous function $f(x)$ is differentiable at $c$ if and only if:

   $$
   f'_-(c) = f'_+(c)
   $$

3. **Geometric Nature of a Corner Point (Kink):**
   If $f'_-(c) \neq f'_+(c)$, the curve makes an abrupt angular turn at $(c, f(c))$, forming a sharp corner where no unique tangent line exists.

---

### Problem Statement

Analyze

$$
f(x)=|x^2-4|.
$$

First sketch $x^2-4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

> **Why this problem:** it shows the limits of mechanical application of calculus and the importance of the geometry of the graph.

---

### Solution

**Step 1: Sketch and analyze the base parabola $g(x) = x^2 - 4$**

Consider the quadratic polynomial:

$$
g(x) = x^2 - 4
$$

1. **Roots:**

   $$
   x^2 - 4 = 0 \iff x = \pm 2
   $$

   The base curve crosses the $x$-axis at $(-2, 0)$ and $(2, 0)$.

2. **Vertex and Sign:**
   * Vertex is at $(0, -4)$, which is the global minimum.
   * For $|x| > 2$: $g(x) > 0$ (positive, above the $x$-axis).
   * For $|x| < 2$: $g(x) < 0$ (negative, below the $x$-axis).

The graph of $g(x)$ is a standard symmetric parabola opening upward with its vertex submerged $4$ units below the $x$-axis.

---

**Step 2: Explain the effect of the absolute value**

Applying the absolute value $f(x) = |g(x)| = |x^2 - 4|$ forces all outputs to be non-negative:
* Where $x^2 - 4 \ge 0$ (for $x \le -2$ and $x \ge 2$), the function remains unchanged:

  $$
  f(x) = x^2 - 4
  $$

* Where $x^2 - 4 < 0$ (for $-2 < x < 2$), the function value is negated:

  $$
  f(x) = -(x^2 - 4) = 4 - x^2
  $$

**Geometric Effect:**
The negative bowl of the parabola between $x = -2$ and $x = 2$ is reflected vertically across the $x$-axis into the upper half-plane. The lowest point $(0, -4)$ flips into a local maximum peak at $(0, 4)$. The outer wings on $(-\infty, -2]$ and $[2, \infty)$ remain identical to the original parabola.

---

**Step 3: Identify the points of non-differentiability**

The transition points occur precisely at the roots of $x^2 - 4 = 0$:

$$
x = -2, \qquad x = 2
$$

We test differentiability at $x = 2$:
1. **Right-hand derivative ($x \to 2^+$):**
   For $x > 2$, $f(x) = x^2 - 4$:

   $$
   f'_+(2) = \lim_{h \to 0^+} \frac{f(2 + h) - f(2)}{h} = \lim_{x \to 2^+} \frac{d}{dx}[x^2 - 4] = \left. 2x \right|_{x=2} = 4
   $$

2. **Left-hand derivative ($x \to 2^-$):**
   For $x < 2$, $f(x) = 4 - x^2$:

   $$
   f'_-(2) = \lim_{h \to 0^-} \frac{f(2 + h) - f(2)}{h} = \lim_{x \to 2^-} \frac{d}{dx}[4 - x^2] = \left. (-2x) \right|_{x=2} = -4
   $$

Because $f'_-(2) = -4 \neq 4 = f'_+(2)$, the two-sided derivative $f'(2)$ does not exist.

Similarly, at $x = -2$:
1. **Left-hand derivative ($x \to -2^-$):**

   $$
   f'_-(-2) = \left. 2x \right|_{x=-2} = -4
   $$

2. **Right-hand derivative ($x \to -2^+$):**

   $$
   f'_+(-2) = \left. (-2x) \right|_{x=-2} = -2(-2) = 4
   $$

Because $f'_-(-2) = -4 \neq 4 = f'_+(-2)$, the derivative $f'(-2)$ does not exist.

---

**Step 4: Geometric justification**

1. **Abrupt Slope Jump:**
   As a point moves along the curve from left to right through $x = 2$, the incoming tangent vector along the downward arch has slope $-4$, while the outgoing tangent vector along the outer branch has slope $+4$.
2. **Sharp V-Shaped Corner:**
   The instantaneous jump in slope of $\Delta m = 4 - (-4) = 8$ prevents the existence of a unique tangent line. The graph forms a sharp corner (kink) at $(2, 0)$ and at $(-2, 0)$, where secant lines from the left and right fail to converge to a common line.

---

### Final Answer

1. **Piecewise Formulation:**

   $$
   f(x) =
   \begin{cases}
   x^2 - 4, & |x| \ge 2, \\
   4 - x^2, & |x| < 2
   \end{cases}
   $$

2. **Effect of Absolute Value:**
   The segment of the parabola on $(-2, 2)$ lying below the $x$-axis is reflected upward across the $x$-axis, transforming the vertex $(0, -4)$ into a smooth local maximum at $(0, 4)$.

3. **Points Where Derivative Does Not Exist:**

   $$
   x = -2, \qquad x = 2
   $$

4. **Geometric Justification:**
   At $x = \pm 2$, the reflection produces sharp corner points. The one-sided slopes are $+4$ and $-4$, disagreeing with each other, meaning no unique tangent line exists at these roots.
