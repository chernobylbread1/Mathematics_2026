### Essential Formulas

1. **Root of a Dominant Exponential Term:**
   For positive real numbers $a > b > 0$:

   $$
   \sqrt[n]{a^n + b^n} = \sqrt[n]{a^n \left(1 + \left(\frac{b}{a}\right)^n\right)} = a \left(1 + \left(\frac{b}{a}\right)^n\right)^{1/n}
   $$

2. **Squeeze Theorem for Roots:**
   For $0 < b < a$ and all $n \ge 1$:

   $$
   a = \sqrt[n]{a^n} < \sqrt[n]{a^n + b^n} \le \sqrt[n]{a^n + a^n} = a \sqrt[n]{2}
   $$

3. **Limit of the $n$-th Root of a Positive Constant:**
   For any constant $c > 0$:

   $$
   \lim_{n \to \infty} c^{1/n} = 1
   $$

---

### Problem Statement

Compute

$$
\lim_{n\to\infty}\sqrt[n]{5^n+2^n}.
$$

Explain which term dominates and why the transformation looks different from the case of a quotient of polynomials.

> **Why this exercise:** extends the idea of dominance to exponential expressions.

---

### Solution

**Step 1: Identify the dominant base**

The terms under the radical are exponential powers with different bases: $5^n$ and $2^n$.
Since $5 > 2 > 0$, the ratio satisfies:

$$
\frac{2^n}{5^n} = \left(\frac{2}{5}\right)^n
$$

As $n \to \infty$, since $\frac{2}{5} < 1$, this ratio decays exponentially to zero:

$$
\lim_{n \to \infty} \left(\frac{2}{5}\right)^n = 0
$$

Thus, $5^n$ is the dominant term, completely overwhelming $2^n$ for large $n$.

---

**Step 2: Method 1 — Factoring the dominant term**

Factor out the dominant term $5^n$ from inside the $n$-th root:

$$
\sqrt[n]{5^n + 2^n} = \sqrt[n]{5^n \left(1 + \frac{2^n}{5^n}\right)} = \sqrt[n]{5^n} \cdot \sqrt[n]{1 + \left(\frac{2}{5}\right)^n}
$$

Since $5 > 0$, $\sqrt[n]{5^n} = 5$:

$$
= 5 \cdot \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n}
$$

As $n \to \infty$:

$$
1 \le 1 + \left(\frac{2}{5}\right)^n \le 1 + 1 = 2
$$

Taking the $n$-th root of both sides:

$$
1 \le \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n} \le 2^{1/n}
$$

Since $\lim_{n \to \infty} 2^{1/n} = 1$, by the Squeeze Theorem:

$$
\lim_{n \to \infty} \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n} = 1
$$

Therefore:

$$
\lim_{n \to \infty} \sqrt[n]{5^n + 2^n} = 5 \cdot 1 = 5
$$

---

**Step 3: Method 2 — Direct Squeeze Theorem**

For every positive integer $n$:

$$
5^n < 5^n + 2^n < 5^n + 5^n = 2 \cdot 5^n
$$

Taking the $n$-th root of all three terms:

$$
\sqrt[n]{5^n} < \sqrt[n]{5^n + 2^n} < \sqrt[n]{2 \cdot 5^n}
$$

$$
5 < \sqrt[n]{5^n + 2^n} < 5 \cdot \sqrt[n]{2}
$$

Evaluate the limits of the lower and upper bounds:

$$
\lim_{n \to \infty} 5 = 5
$$

$$
\lim_{n \to \infty} (5 \cdot \sqrt[n]{2}) = 5 \cdot 1 = 5
$$

By the Squeeze Theorem, the sequence must converge to the common bound:

$$
\lim_{n \to \infty} \sqrt[n]{5^n + 2^n} = 5
$$

---

**Step 4: Why the transformation differs from polynomial quotients**

1. **Radical vs. Fractional Structure:**
   In polynomial quotients $\frac{P(n)}{Q(n)}$, we divide numerator and denominator by $n^k$. In an $n$-th root expression, there is no denominator; we must factor the dominant base $5^n$ out from *under* the radical radical sign:

   $$
   \sqrt[n]{a^n} = a
   $$

2. **Exponential vs. Polynomial Dominance:**
   Polynomial terms grow as power functions $n^p$. In contrast, exponential terms grow as $a^n$. Because $\lim_{n \to \infty} \frac{b^n}{a^n} = 0$ whenever $b < a$, only the single largest base survives. The outer $n$-th root then acts as the inverse of the dominant power, extracting the base $5$.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{n\to\infty}\sqrt[n]{5^n+2^n} = 5
   $$

2. **Dominant Term and Transformation:**
   * The term $5^n$ dominates because $\lim_{n \to \infty} (2/5)^n = 0$.
   * Instead of dividing two polynomials by a common power of $n$, we factor $5^n$ out from under the radical as $\sqrt[n]{5^n} = 5$. The remaining factor $(1 + (2/5)^n)^{1/n}$ approaches $1^{0} = 1$ by the Squeeze Theorem.
