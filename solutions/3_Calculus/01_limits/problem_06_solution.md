### Essential Formulas

1. **Limit of a Function at Infinity:**
   For a real-valued function $f(x)$ defined on an interval $(c, \infty)$, $\lim_{x \to \infty} f(x) = L$ means that for every $\varepsilon > 0$, there exists an $M > 0$ such that for all $x > M$:

   $$
   |f(x) - L| < \varepsilon
   $$

2. **Standard Rational Limits at Infinity:**
   For any power $p > 0$:

   $$
   \lim_{x \to \infty} \frac{1}{x^p} = 0
   $$

3. **Heine's Definition of Function Limit (Sequential Characterization):**
   $\lim_{x \to \infty} f(x) = L$ if and only if for every sequence $(x_n)$ such that $x_n \to \infty$, the sequence of function values satisfies:

   $$
   \lim_{n \to \infty} f(x_n) = L
   $$

---

### Problem Statement

Compute

$$
\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2}.
$$

Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

> **Why this exercise:** deliberately transfers a technique from sequence limits to function limits.

---

### Solution

**Step 1: Identify dominant terms in the numerator and denominator**

Both the numerator $P(x) = 3x^2 - x + 1$ and the denominator $Q(x) = 5x^2 + 4x - 2$ are quadratic polynomials ($\deg = 2$). The leading terms are $3x^2$ and $5x^2$ respectively.

---

**Step 2: Factor out the dominant term $x^2$**

For all $x > 0$, factor out $x^2$ from the numerator and the denominator:

$$
\frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{x^2 \left(3 - \frac{1}{x} + \frac{1}{x^2}\right)}{x^2 \left(5 + \frac{4}{x} - \frac{2}{x^2}\right)}
$$

Cancel the non-zero factor $x^2$:

$$
= \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}}
$$

---

**Step 3: Evaluate the limit as $x \to \infty$**

Since $x$ takes all real values growing arbitrarily large:

$$
\lim_{x \to \infty} \frac{1}{x} = 0, \qquad \lim_{x \to \infty} \frac{1}{x^2} = 0
$$

$$
\lim_{x \to \infty} \frac{4}{x} = 0, \qquad \lim_{x \to \infty} \frac{2}{x^2} = 0
$$

Applying the limit laws for sums, differences, and quotients:

$$
\lim_{x \to \infty} \frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{3 - 0 + 0}{5 + 0 - 0} = \frac{3}{5}
$$

---

**Step 4: Comparison with Exercise 1 and transition from $n$ to $x$**

1. **What stays the same:**
   * **Algebraic Technique:** The algebraic strategy is identical. We factor out the dominant power ($x^2$ instead of $n^2$) and use the fact that reciprocal powers vanish at infinity ($\frac{1}{x^p} \to 0$ just like $\frac{1}{n^p} \to 0$).
   * **Leading Coefficient Rule:** The limit is determined purely by the ratio of leading coefficients ($3/5$).
2. **What changes:**
   * **Nature of the Variable:** The variable $n$ in a sequence is discrete, restricted to positive integers $n \in \{1, 2, 3, \dots\}$. The variable $x$ in a function is continuous, varying continuously through all real numbers $x \in \mathbb{R}$.
   * **Path of Approach:** A sequence approaches infinity along discrete points on the line. A function limit requires $f(x)$ to be close to $L$ for *all* real numbers $x > M$, allowing no gaps or oscillations between integer points. By Heine's theorem, the function limit implies the sequential limit for any sequence $x_n \to \infty$.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2} = \frac{3}{5}
   $$

2. **Comparison of Methods:**
   * **Methodological Identity:** Factoring out the dominant power $x^2$ algebraically reduces the expression to reciprocals that tend to zero, yielding the ratio of leading coefficients $3/5$, identical to the discrete sequence case.
   * **Conceptual Difference:** The discrete index $n \in \mathbb{N}$ is replaced by a continuous real variable $x \in \mathbb{R}$. The limit holds across the entire continuum of values rather than isolated points.
