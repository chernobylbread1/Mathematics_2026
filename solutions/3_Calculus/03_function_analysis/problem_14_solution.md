### Essential Formulas

1. **Reconstruction of Monotonicity from Derivative Factors:**
   For a factored derivative $f'(x) = (x - r_1)(x - r_2)$ with $r_1 < r_2$:
   * $f'(x) > 0$ on $(-\infty, r_1)$ and on $(r_2, \infty)$
   * $f'(x) < 0$ on $(r_1, r_2)$

2. **First Derivative Test for Extrema:**
   * Sign change from $+ \to - \implies$ local maximum.
   * Sign change from $- \to + \implies$ local minimum.

3. **Family of Antiderivatives:**
   If $g'(x) = f'(x)$, then $g(x) = f(x) + C$, which represents a rigid vertical shift of the graph by $C$.

---

### Problem Statement

It is known that

$$
f'(x)=(x-1)(x+2).
$$

Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for

$$
g(x)=\frac{x^3}{3}+\frac{x^2}{2}-2x
$$

verify that $g'(x)=(x-1)(x+2)$, and compare the specific graph with the earlier qualitative sketch.

> **Why this problem:** it teaches how to read the behavior of a function directly from its derivative.

---

### Solution

**Step 1: Determine monotonicity and locations of extrema from $f'(x)$**

The derivative is given in factored form:

$$
f'(x) = (x - 1)(x + 2)
$$

Set $f'(x) = 0$ to find the critical points:

$$
x_1 = -2, \qquad x_2 = 1
$$

Analyze the sign of $f'(x)$ across the three intervals of the real line:
1. **Interval $(-\infty, -2)$:**
   Choose test point $x = -3$:

   $$
   f'(-3) = (-3 - 1)(-3 + 2) = (-4)(-1) = 4 > 0
   $$

   The function is strictly increasing on $(-\infty, -2]$.

2. **Interval $(-2, 1)$:**
   Choose test point $x = 0$:

   $$
   f'(0) = (0 - 1)(0 + 2) = (-1)(2) = -2 < 0
   $$

   The function is strictly decreasing on $[-2, 1]$.

3. **Interval $(1, \infty)$:**
   Choose test point $x = 2$:

   $$
   f'(2) = (2 - 1)(2 + 2) = (1)(4) = 4 > 0
   $$

   The function is strictly increasing on $[1, \infty)$.

**Classification of Extrema:**
* At $x = -2$: the derivative changes from positive to negative ($+ \to -$).
  There is a **local maximum** at $x = -2$.
* At $x = 1$: the derivative changes from negative to positive ($- \to +$).
  There is a **local minimum** at $x = 1$.

---

**Step 2: Describe the qualitative shape of $f(x)$**

* The graph is a typical cubic polynomial with positive leading coefficient.
* It rises from $-\infty$ as $x \to -\infty$, ascends to a local crest at $x = -2$, descends through an inflection point at $x = -\frac{1}{2}$, reaches a local trough at $x = 1$, and then rises indefinitely toward $+\infty$ as $x \to \infty$.
* Because the derivative specifies the function only up to an additive constant $C$, the exact vertical position ($y$-intercept) is arbitrary, but the horizontal locations of the crest ($x = -2$) and trough ($x = 1$) are rigid.

---

**Step 3: Verify the derivative of $g(x)$**

The specific function is:

$$
g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x
$$

Differentiate $g(x)$ term by term using the power rule:

$$
g'(x) = \frac{d}{dx}\left[\frac{x^3}{3}\right] + \frac{d}{dx}\left[\frac{x^2}{2}\right] - \frac{d}{dx}[2x]
$$

$$
g'(x) = x^2 + x - 2
$$

Factor the quadratic polynomial:

$$
x^2 + x - 2 = (x - 1)(x + 2)
$$

The derivative matches:

$$
g'(x) = (x - 1)(x + 2) = f'(x)
$$

The verification is complete.

---

**Step 4: Compute exact coordinates for $g(x)$ and compare with qualitative sketch**

Evaluate $g(x)$ at the critical points and axis intercepts:
1. **Local Maximum at $x = -2$:**

   $$
   g(-2) = \frac{(-2)^3}{3} + \frac{(-2)^2}{2} - 2(-2) = -\frac{8}{3} + \frac{4}{2} + 4 = -\frac{8}{3} + 6 = \frac{10}{3} \approx 3.333
   $$

   The local maximum is $\left(-2, \frac{10}{3}\right)$.

2. **Local Minimum at $x = 1$:**

   $$
   g(1) = \frac{1^3}{3} + \frac{1^2}{2} - 2(1) = \frac{1}{3} + \frac{1}{2} - 2 = \frac{5}{6} - \frac{12}{6} = -\frac{7}{6} \approx -1.167
   $$

   The local minimum is $\left(1, -\frac{7}{6}\right)$.

3. **Origin Intercept:**

   $$
   g(0) = 0
   $$

   The specific curve passes through $(0, 0)$.

4. **Inflection Point:**

   $$
   g''(x) = 2x + 1 = 0 \implies x = -\frac{1}{2}
   $$

   $$
   g\left(-\frac{1}{2}\right) = \frac{-1/8}{3} + \frac{1/4}{2} - 2\left(-\frac{1}{2}\right) = -\frac{1}{24} + \frac{1}{8} + 1 = \frac{13}{12} \approx 1.083
   $$

**Comparison:**
The specific graph of $g(x)$ confirms every qualitative feature predicted from $f'(x)$: an upward-trending cubic curve peaking at $x = -2$ and bottoming at $x = 1$. The specific formula fixes the vertical constant ($C = 0$), anchoring the peak at $y = 10/3$ and the trough at $y = -7/6$, while pinning the curve through the origin.

---

### Final Answer

1. **Monotonicity from $f'(x)$:**
   * Strictly increasing on $(-\infty, -2]$ and on $[1, \infty)$
   * Strictly decreasing on $[-2, 1]$

2. **Locations of Extrema:**
   * Local Maximum at $x = -2$
   * Local Minimum at $x = 1$

3. **Verification for $g(x)$:**

   $$
   g'(x) = x^2 + x - 2 = (x - 1)(x + 2)
   $$

4. **Specific Extrema Values for $g(x)$:**
   * Local Maximum: $\left(-2, \frac{10}{3}\right)$
   * Local Minimum: $\left(1, -\frac{7}{6}\right)$

