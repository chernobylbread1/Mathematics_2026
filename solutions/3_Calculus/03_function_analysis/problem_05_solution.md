### Essential Formulas

1. **Product Rule for Exponential Products:**
   For $f(x) = x e^{-x}$:

   $$
   f'(x) = \frac{d}{dx}[x] \cdot e^{-x} + x \cdot \frac{d}{dx}[e^{-x}] = e^{-x} - x e^{-x} = (1 - x)e^{-x}
   $$

2. **Dominance of Exponential Growth over Polynomial Growth:**
   For any power $p > 0$:

   $$
   \lim_{x \to \infty} \frac{x^p}{e^x} = 0
   $$

3. **Second Derivative and Inflection Point:**
   The concavity changes at $x_0$ where $f''(x_0) = 0$:

   $$
   f''(x) = (x - 2)e^{-x}
   $$

---

### Problem Statement

Analyze the monotonicity and extrema of

$$
f(x)=xe^{-x}.
$$

Also examine the behavior as $x\to\infty$ and explain how the limit affects the shape of the graph on the right-hand side.

> **Why this problem:** it combines the derivative with a limit in the description of the global behavior of a function.

---

### Solution

**Step 1: Domain and first derivative**

The domain of the function is the entire real line:

$$
D_f = \mathbb{R} = (-\infty, \infty)
$$

Compute the first derivative by applying the product rule and chain rule:

$$
f'(x) = (1)e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}
$$

---

**Step 2: Find critical points and analyze monotonicity**

Because the exponential factor is strictly positive for all real numbers:

$$
e^{-x} > 0 \quad \forall x \in \mathbb{R}
$$

the sign of $f'(x)$ is identical to the sign of the linear term $1 - x$.
Set $f'(x) = 0$:

$$
(1 - x)e^{-x} = 0 \iff 1 - x = 0 \iff x = 1
$$

The critical point is $x = 1$.
* **Interval $(-\infty, 1)$:**
  For $x < 1$, $1 - x > 0 \implies f'(x) > 0$.
  The function is strictly increasing on $(-\infty, 1]$.
* **Interval $(1, \infty)$:**
  For $x > 1$, $1 - x < 0 \implies f'(x) < 0$.
  The function is strictly decreasing on $[1, \infty)$.

---

**Step 3: Classify the extremum**

At $x = 1$, the first derivative changes sign from positive to negative ($+ \to -$).
By the First Derivative Test, $f(x)$ attains a strict global maximum at $x = 1$:

$$
f(1) = 1 \cdot e^{-1} = \frac{1}{e} \approx 0.367879
$$

The maximum point is:

$$
\left(1, \frac{1}{e}\right)
$$

---

**Step 4: Examine the limits at infinity**

1. **Behavior as $x \to \infty$:**
   Rewrite the product as a fraction:

   $$
   \lim_{x \to \infty} xe^{-x} = \lim_{x \to \infty} \frac{x}{e^x}
   $$

   This is an indeterminate form of type $\frac{\infty}{\infty}$. Applying l'Hôpital's rule:

   $$
   \lim_{x \to \infty} \frac{\frac{d}{dx}[x]}{\frac{d}{dx}[e^x]} = \lim_{x \to \infty} \frac{1}{e^x} = 0
   $$

   Therefore, the line $y = 0$ is a horizontal asymptote as $x \to \infty$.
   Since $x > 0$ and $e^{-x} > 0$ for all $x > 0$, the function values remain strictly positive:

   $$
   f(x) > 0 \quad \forall x > 0
   $$

   The curve approaches the horizontal asymptote $y = 0$ from above.

2. **Behavior as $x \to -\infty$:**

   $$
   \lim_{x \to -\infty} xe^{-x} = (-\infty) \cdot e^{+\infty} = -\infty
   $$

---

**Step 5: How the limit affects the shape on the right-hand side**

1. **Constraint of the Asymptote:**
   After peaking at the global maximum $(1, 1/e)$, the function decreases for all $x > 1$. However, because $\lim_{x \to \infty} f(x) = 0$ and $f(x) > 0$ for all $x > 0$, the graph can never cross the $x$-axis or drop below zero.
2. **Transition in Curvature (Inflection Point):**
   To transition from descending steeply after the peak to flattening out along the $x$-axis, the graph must change its curvature.
   Compute the second derivative:

   $$
   f''(x) = \frac{d}{dx}[(1 - x)e^{-x}] = -1 \cdot e^{-x} + (1 - x)(-e^{-x}) = (x - 2)e^{-x}
   $$

   At $x = 2$, $f''(2) = 0$, giving an inflection point at:

   $$
   \left(2, \frac{2}{e^2}\right) \approx (2, 0.2707)
   $$

   * On $(1, 2)$: the curve is concave downward ($f'' < 0$), curving toward the ground.
   * On $(2, \infty)$: the curve turns concave upward ($f'' > 0$), creating a smooth, asymptotic tail that glides horizontally above the $x$-axis without ever touching it.

---

### Final Answer

1. **Monotonicity:**
   * Strictly increasing on $(-\infty, 1]$
   * Strictly decreasing on $[1, \infty)$

2. **Extremum:**
   * Strict global maximum at $\left(1, \frac{1}{e}\right)$

3. **Limit at Infinity:**

   $$
   \lim_{x \to \infty} xe^{-x} = 0
   $$

4. **Shape Effect on the Right:**
   The horizontal asymptote $y = 0$ forces the decreasing curve to remain strictly positive, passing through an inflection point at $\left(2, \frac{2}{e^2}\right)$ where the concavity changes from downward to upward, creating a smooth horizontal tail.
