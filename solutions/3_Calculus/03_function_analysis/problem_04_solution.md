### Essential Formulas

1. **Reciprocal Rule / Chain Rule for Power of a Function:**
   For $f(x) = [u(x)]^{-1}$:

   $$
   f'(x) = -[u(x)]^{-2} \cdot u'(x) = -\frac{u'(x)}{[u(x)]^2}
   $$

2. **Domain Partition and Connected Components:**
   If a rational function has singularities where the denominator vanishes, its domain is partitioned into disjoint open intervals:

   $$
   D_f = \bigcup_{k} I_k
   $$

   Monotonicity properties (increasing/decreasing) apply strictly to each connected interval $I_k$ individually, not to their disconnected union.

3. **Horizontal and Vertical Asymptotes:**
   * Line $x = c$ is a vertical asymptote if $\lim_{x \to c^\pm} f(x) = \pm\infty$.
   * Line $y = 0$ is a horizontal asymptote if $\lim_{x \to \pm\infty} f(x) = 0$.

---

### Problem Statement

Analyze

$$
f(x)=\frac1{x^2-1}.
$$

Determine the domain, asymptotes, sign, and monotonicity on the intervals of the domain. Explain why each interval must be analyzed separately.

> **Why this problem:** it practices the analysis of a function on several disjoint intervals.

---

### Solution

**Step 1: Domain and symmetry**

The denominator vanishes when:

$$
x^2 - 1 = 0 \iff (x - 1)(x + 1) = 0 \iff x = \pm 1
$$

Therefore, the domain consists of three disconnected open intervals:

$$
D_f = (-\infty, -1) \cup (-1, 1) \cup (1, \infty) = \mathbb{R} \setminus \{-1, 1\}
$$

Checking symmetry:

$$
f(-x) = \frac{1}{(-x)^2 - 1} = \frac{1}{x^2 - 1} = f(x)
$$

The function is even, meaning its graph is symmetric with respect to the $y$-axis.

---

**Step 2: Asymptotes**

1. **Vertical Asymptotes:**
   Examine one-sided limits at the boundary points $x = \pm 1$:
   * At $x = 1$:

     $$
     \lim_{x \to 1^+} \frac{1}{x^2 - 1} = \frac{1}{0^+} = +\infty, \qquad \lim_{x \to 1^-} \frac{1}{x^2 - 1} = \frac{1}{0^-} = -\infty
     $$

   * At $x = -1$ (by even symmetry):

     $$
     \lim_{x \to -1^-} \frac{1}{x^2 - 1} = \frac{1}{0^+} = +\infty, \qquad \lim_{x \to -1^+} \frac{1}{x^2 - 1} = \frac{1}{0^-} = -\infty
     $$

   Both lines $x = -1$ and $x = 1$ are vertical asymptotes.

2. **Horizontal Asymptote:**
   As $x \to \pm\infty$:

   $$
   \lim_{x \to \infty} \frac{1}{x^2 - 1} = 0, \qquad \lim_{x \to -\infty} \frac{1}{x^2 - 1} = 0
   $$

   The horizontal line $y = 0$ ($x$-axis) is a horizontal asymptote.

---

**Step 3: Sign of $f(x)$ across the domain intervals**

Because the numerator is strictly positive ($1 > 0$), the sign of $f(x)$ is determined by the quadratic denominator $x^2 - 1$:
* **On $(-\infty, -1)$:** $x^2 > 1 \implies x^2 - 1 > 0 \implies f(x) > 0$ (positive).
* **On $(-1, 1)$:** $x^2 < 1 \implies x^2 - 1 < 0 \implies f(x) < 0$ (negative).
* **On $(1, \infty)$:** $x^2 > 1 \implies x^2 - 1 > 0 \implies f(x) > 0$ (positive).

Notice $f(0) = \frac{1}{0 - 1} = -1$ ($y$-intercept). The function has no zeros since $1 \neq 0$.

---

**Step 4: Monotonicity and critical points**

Differentiate $f(x) = (x^2 - 1)^{-1}$ using the chain rule:

$$
f'(x) = -1(x^2 - 1)^{-2} \cdot (2x) = -\frac{2x}{(x^2 - 1)^2}
$$

For every $x \in D_f$, the denominator $(x^2 - 1)^2 > 0$ is strictly positive.
Thus, the sign of $f'(x)$ is governed entirely by $-2x$:
1. **Interval $(-\infty, -1)$:** $x < -1 < 0 \implies -2x > 0 \implies f'(x) > 0$.
   The function is strictly increasing on $(-\infty, -1)$.
2. **Interval $(-1, 0)$:** $-1 < x < 0 \implies -2x > 0 \implies f'(x) > 0$.
   The function is strictly increasing on $(-1, 0]$.
3. **Point $x = 0$:** $f'(0) = 0$.
   Since $f'$ changes from positive to negative on $(-1, 1)$, $f(0) = -1$ is a **local maximum**.
4. **Interval $(0, 1)$:** $0 < x < 1 \implies -2x < 0 \implies f'(x) < 0$.
   The function is strictly decreasing on $[0, 1)$.
5. **Interval $(1, \infty)$:** $x > 1 > 0 \implies -2x < 0 \implies f'(x) < 0$.
   The function is strictly decreasing on $(1, \infty)$.

---

**Step 5: Why each interval must be analyzed separately**

1. **Disconnection and Breakdown of Monotonicity Unions:**
   The domain $D_f$ is not an interval; it is a union of three disconnected components separated by infinite discontinuities at $x = -1$ and $x = 1$.
2. **False Generalizations Across Singularities:**
   Although $f'(x) > 0$ on $(-\infty, -1)$ and also $f'(x) > 0$ on $(-1, 0)$, it is mathematically incorrect to say $f$ is increasing on $(-\infty, -1) \cup (-1, 0)$. For example:

   $$
   x_1 = -2 \in (-\infty, -1) \implies f(-2) = \frac{1}{3}
   $$

   $$
   x_2 = -0.5 \in (-1, 0) \implies f(-0.5) = -\frac{4}{3}
   $$

   Here $x_1 < x_2$, yet $f(x_1) > f(x_2)$. The function drops from positive values to negative values across the asymptote. Monotonicity definitions ($x_1 < x_2 \implies f(x_1) \le f(x_2)$) hold exclusively within single connected intervals.

---

### Final Answer

1. **Domain:**

   $$
   D_f = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)
   $$

2. **Asymptotes:**
   * Vertical Asymptotes: $x = -1$ and $x = 1$
   * Horizontal Asymptote: $y = 0$

3. **Sign:**
   * Positive ($f(x) > 0$) on $(-\infty, -1)$ and on $(1, \infty)$
   * Negative ($f(x) < 0$) on $(-1, 1)$

4. **Monotonicity and Extrema:**
   * Strictly increasing on $(-\infty, -1)$ and on $(-1, 0]$
   * Strictly decreasing on $[0, 1)$ and on $(1, \infty)$
   * Local maximum at $(0, -1)$

5. **Importance of Separate Interval Analysis:**
   The domain consists of disconnected intervals separated by asymptotes. Monotonicity and the Mean Value Theorem apply only within individual connected intervals; claiming monotonicity across the union is invalidated by the discontinuous jump across the asymptotes.

