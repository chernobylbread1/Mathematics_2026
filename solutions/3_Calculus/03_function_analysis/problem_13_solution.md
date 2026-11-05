### Essential Formulas

1. **Quotient Rule:**

   $$
   \left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}
   $$

2. **Standard Logarithmic Limit at Infinity (Growth Comparison):**
   By l'Hôpital's rule:

   $$
   \lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{1/x}{1} = 0
   $$

3. **Logarithmic Evaluation at the Boundary:**

   $$
   \lim_{x \to 0^+} \ln x = -\infty
   $$

---

### Problem Statement

Perform a complete analysis of

$$
f(x)=\frac{\ln x}{x},\qquad x>0.
$$

Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

> **Why this problem:** it combines the domain, limits, and derivative in a less obvious example.

---

### Solution

**Step 1: Domain and zero**

The given function is $f(x) = \frac{\ln x}{x}$.
The domain is restricted by the logarithm to strictly positive numbers:

$$
D_f = (0, \infty)
$$

Find the zero:

$$
\frac{\ln x}{x} = 0 \iff \ln x = 0 \iff x = 1
$$

The unique $x$-intercept is $(1, 0)$.
* For $0 < x < 1$: $\ln x < 0 \implies f(x) < 0$.
* For $x > 1$: $\ln x > 0 \implies f(x) > 0$.

---

**Step 2: Behavior at the ends of the domain**

1. **Left Boundary ($x \to 0^+$):**
   As $x$ approaches $0$ from the right:

   $$
   \lim_{x \to 0^+} \frac{\ln x}{x} = \lim_{x \to 0^+} \left(\ln x \cdot \frac{1}{x}\right) = (-\infty) \cdot (+\infty) = -\infty
   $$

   The vertical line $x = 0$ ($y$-axis) is a vertical asymptote.

2. **Right Boundary ($x \to \infty$):**
   Direct substitution gives $\frac{\infty}{\infty}$. Apply l'Hôpital's rule:

   $$
   \lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{\frac{d}{dx}[\ln x]}{\frac{d}{dx}[x]} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = 0
   $$

   The line $y = 0$ is a horizontal asymptote as $x \to \infty$.
   Since $\ln x > 0$ for all $x > 1$, the function approaches $0$ strictly from above ($f(x) > 0$).

---

**Step 3: First derivative, monotonicity, and maximum**

Differentiate using the quotient rule:

$$
f'(x) = \frac{\left(\frac{1}{x}\right)x - (\ln x)(1)}{x^2} = \frac{1 - \ln x}{x^2}
$$

Set $f'(x) = 0$:

$$
1 - \ln x = 0 \iff \ln x = 1 \iff x = e \approx 2.71828
$$

Since $x^2 > 0$ on $(0, \infty)$, the sign of $f'(x)$ is governed by $1 - \ln x$:
* **On $(0, e)$:** $x < e \implies \ln x < 1 \implies f'(x) > 0$.
  The function is strictly increasing on $(0, e]$.
* **On $(e, \infty)$:** $x > e \implies \ln x > 1 \implies f'(x) < 0$.
  The function is strictly decreasing on $[e, \infty)$.

At $x = e$, $f'(x)$ changes from positive to negative. By the First Derivative Test, $f(x)$ attains a strict global maximum at $x = e$:

$$
f(e) = \frac{\ln e}{e} = \frac{1}{e} \approx 0.367879
$$

The global maximum point is:

$$
\left(e, \frac{1}{e}\right)
$$

---

**Step 4: Second derivative and inflection point**

Differentiate $f'(x) = \frac{1 - \ln x}{x^2}$:

$$
f''(x) = \frac{\left(-\frac{1}{x}\right)x^2 - (1 - \ln x)(2x)}{x^4} = \frac{-x - 2x + 2x \ln x}{x^4} = \frac{2\ln x - 3}{x^3}
$$

Set $f''(x) = 0$:

$$
2\ln x - 3 = 0 \iff \ln x = \frac{3}{2} \iff x = e^{3/2} = e\sqrt{e} \approx 4.4817
$$

* On $\left(0, e^{3/2}\right)$: $\ln x < \frac{3}{2} \implies f''(x) < 0$ (concave downward).
* On $\left(e^{3/2}, \infty\right)$: $\ln x > \frac{3}{2} \implies f''(x) > 0$ (concave upward).

The inflection point is:

$$
I = \left(e^{3/2}, \frac{3}{2e^{3/2}}\right) \approx (4.48, 0.33)
$$

---

**Step 5: Information necessary for a correct sketch**

To produce an accurate sketch without missing essential qualitative behaviors, the following five pieces of information are strictly necessary:
1. **Domain Boundary & Vertical Asymptote:** The graph exists only for $x > 0$ and plunges to $-\infty$ along the $y$-axis.
2. **Zero:** It crosses the horizontal axis at the unique point $(1, 0)$.
3. **Global Maximum:** It crests at $\left(e, \frac{1}{e}\right)$ with a horizontal tangent ($m = 0$).
4. **Inflection Point:** At $\left(e^{3/2}, \frac{3}{2e^{3/2}}\right)$, the curvature switches from concave down to concave up.
5. **Horizontal Asymptote:** For large $x$, the tail remains strictly positive and flattens out smoothly along $y = 0$.

---

### Final Answer

1. **Domain and Limits:**
   * $D_f = (0, \infty)$
   * $\lim_{x \to 0^+} f(x) = -\infty$ (vertical asymptote $x = 0$)
   * $\lim_{x \to \infty} f(x) = 0$ (horizontal asymptote $y = 0$)

2. **Zero:**
   * $x = 1$, point $(1, 0)$

3. **Global Maximum:**

   $$
   \left(e, \frac{1}{e}\right)
   $$

4. **Inflection Point:**

   $$
   \left(e^{3/2}, \frac{3}{2e^{3/2}}\right)
   $$

5. **Essential Information for the Sketch:**
   The combination of the vertical asymptote at $x = 0^+$, the zero at $x = 1$, the peak at $\left(e, 1/e\right)$, the inflection change at $x = e^{3/2}$, and the horizontal approach to $y = 0$ from above as $x \to \infty$.
