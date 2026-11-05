### Essential Formulas

1. **Definition of Euler's Number $e$:**
   The fundamental constant $e$ is defined as the limit of the sequence:

   $$
   e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2.718281828459\dots
   $$

2. **Binomial Expansion of the Sequence:**
   Using the binomial theorem:

   $$
   \left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^n \binom{n}{k} \frac{1}{n^k} = 1 + \sum_{k=1}^n \frac{1}{k!} \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\cdots\left(1 - \frac{k-1}{n}\right)
   $$

3. **Monotone Convergence Theorem:**
   Every sequence of real numbers that is bounded above and monotonically increasing converges to a finite real limit:

   $$
   a_n \le a_{n+1}, \quad a_n \le M \implies \lim_{n \to \infty} a_n = \sup \{a_n : n \in \mathbb{N}\}
   $$

---

### Problem Statement

Compute

$$
\lim_{n\to\infty}\left(1+\frac1n\right)^n.
$$

Calculate several values for increasing $n$ and compare the observed behavior with the value of the limit. Explain why a few values do not constitute a proof.

> **Why this exercise:** connects a central limit with intuition based on concrete terms of a sequence.

---

### Solution

**Step 1: Identify the limit and its mathematical value**

Let:

$$
e_n = \left(1 + \frac{1}{n}\right)^n
$$

This is the canonical indeterminate form $1^\infty$. As $n \to \infty$, the base $1 + \frac{1}{n} \to 1$, while the exponent $n \to \infty$. By definition and by rigorous analysis via the Monotone Convergence Theorem, this sequence converges to Euler's number:

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e
$$

---

**Step 2: Calculate concrete numerical values for increasing $n$**

We evaluate the sequence $e_n$ at several increasing orders of magnitude:

* For $n = 1$:

  $$
  e_1 = \left(1 + \frac{1}{1}\right)^1 = 2.00000
  $$

* For $n = 2$:

  $$
  e_2 = \left(1 + \frac{1}{2}\right)^2 = \left(\frac{3}{2}\right)^2 = 2.25000
  $$

* For $n = 5$:

  $$
  e_5 = \left(1 + \frac{1}{5}\right)^5 = (1.2)^5 = 2.48832
  $$

* For $n = 10$:

  $$
  e_{10} = \left(1 + \frac{1}{10}\right)^{10} = (1.1)^{10} \approx 2.59374
  $$

* For $n = 100$:

  $$
  e_{100} = \left(1 + \frac{1}{100}\right)^{100} = (1.01)^{100} \approx 2.70481
  $$

* For $n = 1000$:

  $$
  e_{1000} = \left(1 + \frac{1}{1000}\right)^{1000} \approx 2.71692
  $$

* For $n = 10000$:

  $$
  e_{10000} = \left(1 + \frac{1}{10000}\right)^{10000} \approx 2.71815
  $$

The exact value to six decimal places is:

$$
e \approx 2.718282
$$

---

**Step 3: Compare observed behavior with the limit**

* **Monotonicity:** The values grow steadily: $e_1 < e_2 < e_5 < e_{10} < e_{100} < e_{1000} < e_{10000}$.
* **Decelerating Growth:** The successive increments decrease rapidly: $e_2 - e_1 = 0.25$, whereas $e_{10000} - e_{1000} \approx 0.00123$.
* **Approach toward a bound:** The terms visibly stabilize near $2.718$, suggesting convergence toward a horizontal asymptote.

---

**Step 4: Why numerical values do not constitute a mathematical proof**

1. **Finiteness vs. Infinity:**
   Evaluating a finite set of terms (even up to $n = 10^{10}$) tests only an infinitesimal fraction of the infinite domain $\mathbb{N}$. A sequence might appear to stabilize initially but could later diverge, oscillate, or alter its trajectory for exceedingly large $n$.
2. **Cannot rule out false limits or slow divergence:**
   For example, the harmonic partial sums $H_n = \sum_{k=1}^n \frac{1}{k}$ grow so slowly that $H_{1000} \approx 7.485$ and $H_{10^6} \approx 14.39$, which numerically appears to flatten out, yet $\lim_{n \to \infty} H_n = +\infty$. Numerical observation alone cannot distinguish between extremely slow logarithmic divergence and true convergence.
3. **Rigorous analytical necessity:**
   A complete mathematical proof requires:
   * Proving monotonicity for all $n \in \mathbb{N}$ (e.g., using the arithmetic-geometric mean inequality or binomial expansion showing each term in the sum increases with $n$).
   * Proving boundedness: showing $e_n < 1 + \sum_{k=1}^n \frac{1}{2^{k-1}} < 3$ for all $n$.
   * Invoking the Monotone Convergence Theorem to establish that the limit exists as an intrinsic real number $e$.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{n\to\infty}\left(1+\frac1n\right)^n = e \approx 2.718281828459
   $$

2. **Table of Representative Values:**
   * $n = 1 \implies 2.00000$
   * $n = 2 \implies 2.25000$
   * $n = 10 \implies 2.59374$
   * $n = 100 \implies 2.70481$
   * $n = 1000 \implies 2.71692$
   * $n = 10000 \implies 2.71815$

3. **Methodological Distinction:**
   Empirical calculations provide valuable numerical intuition and heuristic evidence, but only a rigorous deductive proof (such as establishing that $e_n$ is monotonically increasing and bounded above by $3$) guarantees that the sequence converges for all $n \to \infty$.
