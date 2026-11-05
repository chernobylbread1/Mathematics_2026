### Essential Formulas

1. **Natural Logarithm Domain Requirement:**
   The function $\ln x$ is defined strictly for positive arguments:

   $$
   D_{\ln} = (0, \infty)
   $$

2. **Derivative of the Natural Logarithm:**

   $$
   \frac{d}{dx}[\ln x] = \frac{1}{x} \qquad (x > 0)
   $$

3. **First Derivative Test for Monotonicity:**
   * If $f'(x) > 0$ on $(a, b)$, $f$ is strictly increasing on $(a, b)$.
   * If $f'(x) < 0$ on $(a, b)$, $f$ is strictly decreasing on $(a, b)$.

4. **Fundamental Logarithmic Inequality:**
   For all $x > 0$:

   $$
   \ln x \le x - 1
   $$

   with equality if and only if $x = 1$.

---

### Problem Statement

Analyze the domain, zero, and monotonicity of

$$
f(x)=\ln x-x+1.
$$

Explain why the analysis must begin with the domain.

> **Why this problem:** it reinforces the role of the domain and derivative in the analysis of a logarithmic function.

---

### Solution

**Step 1: Why the analysis must begin with the domain**

Every analytical and algebraic operation—evaluating limits, finding zeros, and computing derivatives—is valid only within the domain where the function is defined:
1. **Preventing Extraneous Mathematical Artifacts:**
   The formal derivative formula $\frac{1}{x} - 1$ could algebraically be computed at negative values such as $x = -2$. However, $f(-2)$ does not exist in real arithmetic. Without establishing the domain first, one risks making false claims about the existence of the function or its behavior in regions where it does not exist.
2. **One-Sided Boundary Behavior:**
   Knowing that the domain has an open boundary at $x = 0^+$ immediately identifies the necessity of investigating the behavior as $x \to 0^+$.

---

**Step 2: Determine the domain**

The function is $f(x) = \ln x - x + 1$.
The term $\ln x$ requires $x > 0$. The linear terms $-x + 1$ are defined on all of $\mathbb{R}$.
The intersection yields:

$$
D_f = (0, \infty)
$$

---

**Step 3: Compute the derivative and determine monotonicity**

Differentiate with respect to $x$ for all $x \in (0, \infty)$:

$$
f'(x) = \frac{d}{dx}[\ln x - x + 1] = \frac{1}{x} - 1 = \frac{1 - x}{x}
$$

Find the critical points by setting $f'(x) = 0$:

$$
\frac{1 - x}{x} = 0 \iff 1 - x = 0 \iff x = 1
$$

Since $x > 0$ on the entire domain, the denominator $x$ is always positive. The sign of $f'(x)$ is determined by $1 - x$:
* **Interval $(0, 1)$:**
  $0 < x < 1 \implies 1 - x > 0 \implies f'(x) > 0$.
  The function is strictly increasing on $(0, 1]$.
* **Interval $(1, \infty)$:**
  $x > 1 \implies 1 - x < 0 \implies f'(x) < 0$.
  The function is strictly decreasing on $[1, \infty)$.

---

**Step 4: Find the extremum and identify the zeros**

1. **Global Maximum:**
   Since $f(x)$ increases on $(0, 1]$ and decreases on $[1, \infty)$, the critical point $x = 1$ is a strict global maximum.
2. **Value at the Maximum:**

   $$
   f(1) = \ln(1) - 1 + 1 = 0 - 0 = 0
   $$

3. **Uniqueness of the Zero:**
   At its maximum, $f(1) = 0$.
   For every $x \in (0, \infty)$ with $x \neq 1$:

   $$
   f(x) < f(1) = 0
   $$

   Therefore, $f(x)$ never touches or crosses the $x$-axis anywhere else. The value $x = 1$ is the unique zero of the function.

---

**Step 5: Boundary limits**

* As $x \to 0^+$:

  $$
  \lim_{x \to 0^+} (\ln x - x + 1) = -\infty - 0 + 1 = -\infty
  $$

  The line $x = 0$ ($y$-axis) is a vertical asymptote.
* As $x \to \infty$:

  $$
  \lim_{x \to \infty} (\ln x - x + 1) = \lim_{x \to \infty} x \left(\frac{\ln x}{x} - 1 + \frac{1}{x}\right) = \infty(0 - 1 + 0) = -\infty
  $$

---

### Final Answer

1. **Domain:**

   $$
   D_f = (0, \infty)
   $$

2. **Zero:**
   The only zero is:

   $$
   x = 1
   $$

3. **Monotonicity and Extrema:**
   * Strictly increasing on $(0, 1]$
   * Strictly decreasing on $[1, \infty)$
   * Strict global maximum at $(1, 0)$

4. **Why the Domain Must Come First:**
   The logarithm $\ln x$ is defined strictly for $x > 0$. Finding derivatives or solving equations without restricting to the domain produces invalid conclusions and false critical points. The domain defines the boundary $x \to 0^+$ and frames all subsequent analysis.

