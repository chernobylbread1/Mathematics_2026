### Essential Formulas

1. **Definition of an Oblique (Slant) Asymptote:**
   A straight line $y = a x + b$ is an oblique asymptote of $y = f(x)$ as $x \to \infty$ (or $x \to -\infty$) if the vertical distance between the curve and the line approaches zero:

   $$
   \lim_{x \to \pm\infty} [f(x) - (a x + b)] = 0
   $$

2. **Decomposition via Polynomial Division:**
   For a rational function $f(x) = \frac{P(x)}{Q(x)}$ where $\deg P = \deg Q + 1$:

   $$
   \frac{P(x)}{Q(x)} = (a x + b) + \frac{R(x)}{Q(x)}
   $$

   where $\deg R < \deg Q$.

3. **Vertical Asymptote Criterion:**
   The vertical line $x = c$ is an asymptote if:

   $$
   \lim_{x \to c^\pm} f(x) = \pm\infty
   $$

---

### Problem Statement

Analyze the asymptotes of

$$
f(x)=\frac{x^2+1}{x-1}.
$$

Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

> **Why this problem:** it teaches how to recognize an oblique asymptote and interpret the decomposition of a function.

---

### Solution

**Step 1: Domain and vertical asymptote**

The denominator of $f(x) = \frac{x^2+1}{x-1}$ vanishes when $x - 1 = 0 \iff x = 1$.
The domain is:

$$
D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)
$$

Compute the one-sided limits at the singularity $x = 1$:
* From the right ($x \to 1^+$):

  $$
  \lim_{x \to 1^+} \frac{x^2 + 1}{x - 1} = \frac{1^2 + 1}{0^+} = \frac{2}{0^+} = +\infty
  $$

* From the left ($x \to 1^-$):

  $$
  \lim_{x \to 1^-} \frac{x^2 + 1}{x - 1} = \frac{1^2 + 1}{0^-} = \frac{2}{0^-} = -\infty
  $$

Therefore, the vertical line $x = 1$ is a vertical asymptote.

---

**Step 2: Perform polynomial division**

The degree of the numerator is $2$ and the degree of the denominator is $1$. Because the numerator degree exceeds the denominator degree by exactly $1$, an oblique asymptote exists.
Divide the polynomial $x^2 + 1$ by $x - 1$:

$$
x^2 + 1 = (x^2 - x) + (x - 1) + 2 = x(x - 1) + 1(x - 1) + 2 = (x + 1)(x - 1) + 2
$$

Dividing both sides by $x - 1$ yields:

$$
\frac{x^2 + 1}{x - 1} = x + 1 + \frac{2}{x - 1}
$$

* Linear quotient: $q(x) = x + 1$
* Remainder: $R = 2$

---

**Step 3: Determine the oblique asymptote**

Consider the difference between the function and the linear polynomial $y = x + 1$:

$$
f(x) - (x + 1) = \frac{2}{x - 1}
$$

Evaluate the limit of this difference as $x \to \pm\infty$:

$$
\lim_{x \to \infty} [f(x) - (x + 1)] = \lim_{x \to \infty} \frac{2}{x - 1} = 0
$$

$$
\lim_{x \to -\infty} [f(x) - (x + 1)] = \lim_{x \to -\infty} \frac{2}{x - 1} = 0
$$

By definition, the straight line:

$$
y = x + 1
$$

is the oblique asymptote of the function as both $x \to +\infty$ and $x \to -\infty$.

---

**Step 4: Explain why the remainder term vanishes for large $|x|$**

1. **Fixed Numerator vs. Unbounded Denominator:**
   In the remainder term:

   $$
   \frac{R}{Q(x)} = \frac{2}{x - 1}
   $$

   the numerator is a fixed non-zero constant ($2$). As $|x|$ becomes arbitrarily large, the denominator $|x - 1|$ grows without bound.
2. **Algebraic Decay to Zero:**
   Dividing a finite constant by an arbitrarily large number yields a value that shrinks to zero:

   $$
   \lim_{|x| \to \infty} \left|\frac{2}{x - 1}\right| = 0
   $$

3. **Geometric Proximity to the Asymptote:**
   The remainder term $\frac{2}{x - 1}$ represents the exact vertical distance between the curve $y = f(x)$ and the line $y = x + 1$.
   * When $x > 1$: $\frac{2}{x - 1} > 0$, so $f(x) > x + 1$. The curve approaches the asymptote from above.
   * When $x < 1$: $\frac{2}{x - 1} < 0$, so $f(x) < x + 1$. The curve approaches the asymptote from below.
   As $|x| \to \infty$, this gap becomes infinitesimal, making the graph indistinguishable from the straight line $y = x + 1$.

---

### Final Answer

1. **Vertical Asymptote:**

   $$
   x = 1
   $$

2. **Polynomial Decomposition:**

   $$
   f(x) = x + 1 + \frac{2}{x - 1}
   $$

3. **Oblique Asymptote:**

   $$
   y = x + 1
   $$

4. **Why the Remainder Vanishes:**
   The remainder term $\frac{2}{x-1}$ has a fixed constant numerator $2$ and a denominator that grows without bound as $|x| \to \infty$. Its magnitude tends to $0$, meaning the vertical gap between the curve and the line $y = x + 1$ vanishes asymptotically.
