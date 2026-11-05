### Essential Formulas

1. **Comparison of Polynomial Degrees:**
   Let $P(n) = a_p n^p + \dots + a_0$ and $Q(n) = b_q n^q + \dots + b_0$ with $a_p \neq 0$ and $b_q \neq 0$. The limit of the rational sequence:

   $$
   \lim_{n \to \infty} \frac{P(n)}{Q(n)}
   $$

   depends entirely on the relationship between degrees $p = \deg P$ and $q = \deg Q$:
   * If $\deg P < \deg Q$ ($p < q$): the denominator grows strictly faster than the numerator, and the limit is $0$:

     $$
     \lim_{n \to \infty} \frac{P(n)}{Q(n)} = 0
     $$

   * If $\deg P = \deg Q$ ($p = q$): the numerator and denominator grow at the same polynomial rate, and the limit is the ratio of their leading coefficients:

     $$
     \lim_{n \to \infty} \frac{P(n)}{Q(n)} = \frac{a_p}{b_q}
     $$

   * If $\deg P > \deg Q$ ($p > q$): the numerator grows strictly faster than the denominator, so the sequence diverges to $\pm \infty$:

     $$
     \lim_{n \to \infty} \left| \frac{P(n)}{Q(n)} \right| = \infty
     $$

2. **Standard Null Sequence:**
   For any power $k > 0$:

   $$
   \lim_{n \to \infty} \frac{1}{n^k} = 0
   $$

---

### Problem Statement

Compute

$$
\lim_{n\to\infty}\frac{3n+1}{n^2+4},\qquad \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}.
$$

Compare the two cases and formulate a general observation about the degrees of the polynomials in the numerator and denominator.

> **Why this exercise:** teaches how to compare growth rates and recognize qualitatively different cases.

---

### Solution

**Step 1: Compute the first limit**

Consider:

$$
a_n = \frac{3n + 1}{n^2 + 4}
$$

The degree of the numerator is $1$, and the degree of the denominator is $2$.
Divide both numerator and denominator by the highest power in the denominator, which is $n^2$:

$$
a_n = \frac{\frac{3n + 1}{n^2}}{\frac{n^2 + 4}{n^2}} = \frac{\frac{3}{n} + \frac{1}{n^2}}{1 + \frac{4}{n^2}}
$$

Taking the limit as $n \to \infty$:

$$
\lim_{n \to \infty} \left(\frac{3}{n} + \frac{1}{n^2}\right) = 0 + 0 = 0
$$

$$
\lim_{n \to \infty} \left(1 + \frac{4}{n^2}\right) = 1 + 0 = 1
$$

By the quotient limit law:

$$
\lim_{n \to \infty} \frac{3n + 1}{n^2 + 4} = \frac{0}{1} = 0
$$

---

**Step 2: Compute the second limit**

Consider:

$$
b_n = \frac{2n^3 - n}{5n^2 + 1}
$$

The degree of the numerator is $3$, and the degree of the denominator is $2$.
Divide both numerator and denominator by the highest power in the denominator, which is $n^2$:

$$
b_n = \frac{\frac{2n^3 - n}{n^2}}{\frac{5n^2 + 1}{n^2}} = \frac{2n - \frac{1}{n}}{5 + \frac{1}{n^2}}
$$

As $n \to \infty$:

$$
\lim_{n \to \infty} \left(5 + \frac{1}{n^2}\right) = 5
$$

While the numerator behaves as:

$$
\lim_{n \to \infty} \left(2n - \frac{1}{n}\right) = \infty - 0 = \infty
$$

Since the denominator approaches a positive constant $5$ and the numerator grows without bound toward $+\infty$:

$$
\lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1} = +\infty
$$

The sequence diverges to $+\infty$.

---

**Step 3: Comparison and General Observation**

1. **Case $\deg P < \deg Q$ (First limit):**
   The degree of $3n+1$ is $1$, whereas the degree of $n^2+4$ is $2$. The denominator outgrows the numerator by a factor of $n$. Consequently, the ratio shrinks to zero.

2. **Case $\deg P > \deg Q$ (Second limit):**
   The degree of $2n^3-n$ is $3$, whereas the degree of $5n^2+1$ is $2$. The numerator outgrows the denominator by a factor of $n$. Consequently, the ratio grows without bound.

3. **General Observation:**
   For any rational sequence $\frac{P(n)}{Q(n)}$ with degrees $p$ and $q$ and leading coefficients $a_p$ and $b_q$:
   * When $p < q$, $\lim_{n \to \infty} \frac{P(n)}{Q(n)} = 0$.
   * When $p = q$, $\lim_{n \to \infty} \frac{P(n)}{Q(n)} = \frac{a_p}{b_q}$.
   * When $p > q$, $\lim_{n \to \infty} \frac{P(n)}{Q(n)} = \mathrm{sgn}(a_p / b_q) \cdot \infty$.

---

### Final Answer

1. **First Limit:**

   $$
   \lim_{n\to\infty}\frac{3n+1}{n^2+4} = 0
   $$

2. **Second Limit:**

   $$
   \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1} = +\infty
   $$

3. **General Principle:**
   The asymptotic limit of a rational sequence is governed strictly by the degrees of its polynomials:
   * $\deg(\mathrm{numerator}) < \deg(\mathrm{denominator}) \implies$ limit is $0$.
   * $\deg(\mathrm{numerator}) = \deg(\mathrm{denominator}) \implies$ limit is the ratio of leading coefficients.
   * $\deg(\mathrm{numerator}) > \deg(\mathrm{denominator}) \implies$ expression diverges to $\pm\infty$.
