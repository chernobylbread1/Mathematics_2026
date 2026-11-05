### Essential Formulas

1. **Limit of a Rational Sequence:**
   For a rational expression in $n$, the dominant behavior as $n \to \infty$ is governed by the highest power of $n$. We factor out or divide the numerator and denominator by the highest power of $n$ present in the denominator:

   $$
   \lim_{n \to \infty} \frac{1}{n^p} = 0 \qquad (p > 0)
   $$

2. **Algebraic Limit Laws:**
   If $\lim_{n \to \infty} a_n = A$ and $\lim_{n \to \infty} b_n = B$ with $B \neq 0$, then:

   $$
   \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\lim_{n \to \infty} a_n}{\lim_{n \to \infty} b_n} = \frac{A}{B}
   $$

   $$
   \lim_{n \to \infty} (a_n \pm b_n) = A \pm B
   $$

   $$
   \lim_{n \to \infty} (c \cdot a_n) = c \cdot A \qquad (c \in \mathbb{R})
   $$

---

### Problem Statement

Compute

$$
\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7}.
$$

Explain why the highest-degree terms determine the result.

> **Why this exercise:** introduces the idea of a dominant term and teaches how to simplify the behavior of expressions for large arguments.

---

### Solution

**Step 1: Identify the highest powers of $n$**

In the numerator $P(n) = 4n^2 - 3n + 1$, the highest power of $n$ is $n^2$, with leading coefficient $4$.
In the denominator $Q(n) = 2n^2 + 5n - 7$, the highest power of $n$ is also $n^2$, with leading coefficient $2$.

Both polynomials have degree $2$.

---

**Step 2: Factor out the dominant term $n^2$**

Divide both the numerator and the denominator by $n^2$ for all $n \ge 1$:

$$
\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{n^2 \left(4 - \frac{3}{n} + \frac{1}{n^2}\right)}{n^2 \left(2 + \frac{5}{n} - \frac{7}{n^2}\right)}
$$

Cancel the non-zero common factor $n^2$:

$$
= \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}}
$$

---

**Step 3: Evaluate the limits of the individual terms**

As $n \to \infty$, the terms with $n$ in the denominator tend to zero:

$$
\lim_{n \to \infty} \frac{3}{n} = 0, \qquad \lim_{n \to \infty} \frac{1}{n^2} = 0
$$

$$
\lim_{n \to \infty} \frac{5}{n} = 0, \qquad \lim_{n \to \infty} \frac{7}{n^2} = 0
$$

Applying the quotient, sum, and difference limit laws:

$$
\lim_{n \to \infty} \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}} = \frac{4 - 0 + 0}{2 + 0 - 0} = \frac{4}{2} = 2
$$

---

**Step 4: Explanation of dominant terms**

For large $n$, lower-order powers grow substantially slower than $n^2$. Specifically:

$$
\frac{-3n + 1}{4n^2} \to 0 \quad (n \to \infty) \implies 4n^2 - 3n + 1 \sim 4n^2
$$

$$
\frac{5n - 7}{2n^2} \to 0 \quad (n \to \infty) \implies 2n^2 + 5n - 7 \sim 2n^2
$$

Because all lower-order terms become negligible compared to the leading terms $n^2$, the behavior of the ratio as $n \to \infty$ is entirely determined by the ratio of the leading coefficients:

$$
\lim_{n \to \infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \lim_{n \to \infty} \frac{4n^2}{2n^2} = \frac{4}{2} = 2
$$

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7} = 2
   $$

2. **Dominance Explanation:**
   The highest-degree terms $4n^2$ and $2n^2$ grow as $n^2$, while all remaining terms grow at order at most $n^1$ or $n^0$. As $n \to \infty$, the lower-order terms divided by $n^2$ vanish to $0$, so the limit is strictly determined by the ratio of the leading coefficients $4 / 2 = 2$.
