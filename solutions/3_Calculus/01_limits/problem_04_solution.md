### Essential Formulas

1. **Geometric Sequence Convergence:**
   For a geometric sequence $a_n = q^n$ where $q \in \mathbb{R}$:
   * If $|q| < 1$: the sequence converges to $0$:

     $$
     \lim_{n \to \infty} q^n = 0
     $$

   * If $q = 1$: the sequence is identically constant, $a_n = 1$, converging to $1$:

     $$
     \lim_{n \to \infty} 1^n = 1
     $$

   * If $q > 1$: the sequence grows exponentially without bound, diverging to $+\infty$:

     $$
     \lim_{n \to \infty} q^n = +\infty
     $$

   * If $q \le -1$: the sequence oscillates indefinitely without approaching any single limit; it diverges.

2. **Squeeze Theorem (Sandwich Theorem):**
   If $a_n \le b_n \le c_n$ for all $n \ge n_0$, and:

   $$
   \lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L
   $$

   then the sequence $b_n$ converges and:

   $$
   \lim_{n \to \infty} b_n = L
   $$

3. **Absolute Value Criterion for Null Sequences:**

   $$
   \lim_{n \to \infty} |a_n| = 0 \iff \lim_{n \to \infty} a_n = 0
   $$

---

### Problem Statement

Analyze

$$
\left(\frac23\right)^n,\qquad \left(\frac32\right)^n,\qquad (-1)^n,\qquad \frac{(-1)^n}{n}.
$$

For each sequence, describe the type of behavior and justify your answer.

> **Why this exercise:** organizes the basic types of sequence behavior and shows that oscillation does not always rule out convergence.

---

### Solution

**Step 1: Analyze $a_n = \left(\frac{2}{3}\right)^n$**

* **Type of Behavior:** Monotonically decreasing, bounded, and convergent to $0$.
* **Justification:**
  This is a geometric sequence $q^n$ with base $q = \frac{2}{3}$.
  Since $0 < q < 1$:

  $$
  0 < \left(\frac{2}{3}\right)^{n+1} = \frac{2}{3} \left(\frac{2}{3}\right)^n < \left(\frac{2}{3}\right)^n
  $$

  The terms are strictly positive and strictly decreasing. Since $|q| = \frac{2}{3} < 1$:

  $$
  \lim_{n \to \infty} \left(\frac{2}{3}\right)^n = 0
  $$

---

**Step 2: Analyze $b_n = \left(\frac{3}{2}\right)^n$**

* **Type of Behavior:** Monotonically increasing, unbounded, diverging to $+\infty$.
* **Justification:**
  This is a geometric sequence with base $q = \frac{3}{2} = 1.5 > 1$.
  By Bernoulli's inequality, writing $q = 1 + \frac{1}{2}$:

  $$
  \left(1 + \frac{1}{2}\right)^n \ge 1 + \frac{n}{2}
  $$

  As $n \to \infty$, $1 + \frac{n}{2} \to +\infty$. Therefore, by comparison:

  $$
  \lim_{n \to \infty} \left(\frac{3}{2}\right)^n = +\infty
  $$

---

**Step 3: Analyze $c_n = (-1)^n$**

* **Type of Behavior:** Bounded, oscillating, and divergent (no limit exists).
* **Justification:**
  The sequence alternates strictly between $-1$ and $+1$:

  $$
  c_n =
  \begin{cases}
  1, & n = 2k, \\
  -1, & n = 2k+1
  \end{cases}
  $$

  Consider two subsequences:
  * For even indices $n = 2k$: $c_{2k} = (-1)^{2k} = 1 \implies \lim_{k \to \infty} c_{2k} = 1$.
  * For odd indices $n = 2k+1$: $c_{2k+1} = (-1)^{2k+1} = -1 \implies \lim_{k \to \infty} c_{2k+1} = -1$.

  Since the sequence possesses two distinct subsequential limits ($1 \neq -1$), the overall limit $\lim_{n \to \infty} (-1)^n$ does not exist. The sequence oscillates perpetually within the bounded interval $[-1, 1]$.

---

**Step 4: Analyze $d_n = \frac{(-1)^n}{n}$**

* **Type of Behavior:** Damped oscillating, bounded, and convergent to $0$.
* **Justification:**
  The sequence changes signs with every step: $-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, -\frac{1}{5}, \dots$
  To determine convergence, consider its absolute value:

  $$
  |d_n| = \left| \frac{(-1)^n}{n} \right| = \frac{|(-1)^n|}{n} = \frac{1}{n}
  $$

  Since $\lim_{n \to \infty} \frac{1}{n} = 0$, we have:

  $$
  -\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}
  $$

  Both bounding sequences satisfy:

  $$
  \lim_{n \to \infty} \left(-\frac{1}{n}\right) = 0, \qquad \lim_{n \to \infty} \frac{1}{n} = 0
  $$

  By the Squeeze Theorem:

  $$
  \lim_{n \to \infty} \frac{(-1)^n}{n} = 0
  $$

  Thus, despite persistent sign oscillation, the decaying amplitude drives the sequence to converge to $0$.

---

### Final Answer

1. **Sequence $\left(\frac{2}{3}\right)^n$:**
   Monotonic null sequence; converges to $0$ because the common ratio satisfies $|q| < 1$.

2. **Sequence $\left(\frac{3}{2}\right)^n$:**
   Monotonically growing sequence; diverges to $+\infty$ because the common ratio satisfies $q > 1$.

3. **Sequence $(-1)^n$:**
   Bounded oscillating sequence; diverges because it alternates between two distinct accumulation points, $+1$ and $-1$.

4. **Sequence $\frac{(-1)^n}{n}$:**
   Damped alternating sequence; converges to $0$ by the Squeeze Theorem because the amplitude $\frac{1}{n}$ vanishes as $n \to \infty$.
