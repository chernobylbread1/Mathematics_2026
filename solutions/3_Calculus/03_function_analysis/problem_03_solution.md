### Essential Formulas

1. **Domain of a Rational Function:**
   For $f(x) = \frac{P(x)}{Q(x)}$:

   $$
   D_f = \{x \in \mathbb{R} : Q(x) \neq 0\}
   $$

2. **Vertical Asymptote:**
   The line $x = c$ is a vertical asymptote if:

   $$
   \lim_{x \to c^-} f(x) = \pm\infty, \qquad \lim_{x \to c^+} f(x) = \pm\infty
   $$

3. **Horizontal Asymptote:**
   The line $y = L$ is a horizontal asymptote if:

   $$
   \lim_{x \to \infty} f(x) = L, \qquad \lim_{x \to -\infty} f(x) = L
   $$

4. **Quotient Rule:**

   $$
   \left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}
   $$

---

### Problem Statement

Analyze the domain, zeros, asymptotes, and monotonicity of

$$
f(x)=\frac{x+1}{x-2}.
$$

Finally, sketch a graph consistent with all the information obtained.

> **Why this problem:** it teaches how to combine the domain, limits, and derivative in the analysis of a rational function.

---

### Solution

**Step 1: Domain of the function**

The denominator cannot be zero:

$$
x - 2 \neq 0 \implies x \neq 2
$$

Therefore:

$$
D_f = (-\infty, 2) \cup (2, \infty) = \mathbb{R} \setminus \{2\}
$$

---

**Step 2: Zeros and axis intercepts**

1. **$x$-intercept (zeros):**
   Set $f(x) = 0$:

   $$
   \frac{x + 1}{x - 2} = 0 \implies x + 1 = 0 \implies x = -1
   $$

   The only zero is $x = -1$, yielding the point $(-1, 0)$.

2. **$y$-intercept:**
   Evaluate at $x = 0$:

   $$
   f(0) = \frac{0 + 1}{0 - 2} = -\frac{1}{2}
   $$

   The $y$-intercept is $(0, -1/2)$.

---

**Step 3: Asymptotes**

1. **Vertical Asymptote at $x = 2$:**
   Compute the one-sided limits as $x \to 2$:
   * From the left ($x \to 2^-$): $x < 2 \implies x - 2 \to 0^-$:

     $$
     \lim_{x \to 2^-} \frac{x + 1}{x - 2} = \frac{3}{0^-} = -\infty
     $$

   * From the right ($x \to 2^+$): $x > 2 \implies x - 2 \to 0^+$:

     $$
     \lim_{x \to 2^+} \frac{x + 1}{x - 2} = \frac{3}{0^+} = +\infty
     $$

   The line $x = 2$ is a vertical asymptote.

2. **Horizontal Asymptote as $x \to \pm\infty$:**
   Factor out $x$:

   $$
   \lim_{x \to \pm\infty} \frac{x + 1}{x - 2} = \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x}}{1 - \frac{2}{x}} = \frac{1 + 0}{1 - 0} = 1
   $$

   The horizontal line $y = 1$ is an asymptote in both directions ($x \to +\infty$ and $x \to -\infty$).

---

**Step 4: Monotonicity and extrema**

Differentiate using the quotient rule:

$$
f'(x) = \frac{(1)(x - 2) - (x + 1)(1)}{(x - 2)^2} = \frac{x - 2 - x - 1}{(x - 2)^2} = \frac{-3}{(x - 2)^2}
$$

For every $x \in D_f$:

$$
(x - 2)^2 > 0 \implies f'(x) = \frac{-3}{(x - 2)^2} < 0
$$

* Since $f'(x) < 0$ on $(-\infty, 2)$, the function is strictly decreasing on $(-\infty, 2)$.
* Since $f'(x) < 0$ on $(2, \infty)$, the function is strictly decreasing on $(2, \infty)$.
* Because $f'(x) \neq 0$ everywhere, there are **no local extrema**.

---

**Step 5: Curvature and graph sketch**

Compute the second derivative:

$$
f''(x) = \frac{d}{dx}\left[-3(x - 2)^{-2}\right] = 6(x - 2)^{-3} = \frac{6}{(x - 2)^3}
$$

* For $x < 2$: $x - 2 < 0 \implies (x - 2)^3 < 0 \implies f''(x) < 0$ (concave downward).
* For $x > 2$: $x - 2 > 0 \implies (x - 2)^3 > 0 \implies f''(x) > 0$ (concave upward).

**Geometric Structure of the Graph:**
The graph is a rectangular hyperbola centered at $(2, 1)$:
* **Left branch ($x < 2$):** Lies entirely below the horizontal asymptote $y = 1$. Approaches $y = 1$ from below as $x \to -\infty$, crosses the $x$-axis at $(-1, 0)$, crosses the $y$-axis at $(0, -1/2)$, and plunges downward toward $-\infty$ as it approaches the vertical asymptote $x = 2$ from the left.
* **Right branch ($x > 2$):** Lies entirely above the horizontal asymptote $y = 1$. Descends from $+\infty$ along the vertical asymptote $x = 2$, decreases with concave-up curvature, and flattens out toward $y = 1$ from above as $x \to +\infty$.

---

### Final Answer

1. **Domain:**

   $$
   D_f = (-\infty, 2) \cup (2, \infty) = \mathbb{R} \setminus \{2\}
   $$

2. **Zeros and Intercepts:**
   * $x$-intercept: $(-1, 0)$
   * $y$-intercept: $(0, -1/2)$

3. **Asymptotes:**
   * Vertical Asymptote: $x = 2$
   * Horizontal Asymptote: $y = 1$

4. **Monotonicity and Extrema:**
   * Strictly decreasing on $(-\infty, 2)$ and on $(2, \infty)$
   * No local extrema ($f'(x) < 0$ everywhere on $D_f$)
