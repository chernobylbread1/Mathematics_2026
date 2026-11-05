### Essential Formulas

1. **Logarithmic Integration Rule:**
   For any non-zero differentiable function $g(x)$:

   $$
   \int \frac{g'(x)}{g(x)} \, dx = \ln |g(x)| + C
   $$

2. **Derivative of the Natural Logarithm:**

   $$
   \frac{d}{dx}[\ln |u|] = \frac{1}{u} \qquad (u \neq 0)
   $$

3. **Breakdown of the Power Rule at $n = -1$:**
   The standard power rule $\int u^n \, du = \frac{u^{n+1}}{n+1}$ is undefined for $n = -1$ because the denominator $n + 1 = 0$. The unique antiderivative of $u^{-1} = \frac{1}{u}$ is:

   $$
   \int \frac{1}{u} \, du = \ln |u| + C
   $$

---

### Problem Statement

Compute

$$
\int\frac{2x}{x^2+5}\,dx.
$$

Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

> **Why this problem:** it teaches how to recognize the structure “derivative of the denominator over the denominator.”

---

### Solution

**Step 1: Identify the denominator as a substitution candidate**

Consider the rational integrand:

$$
f(x) = \frac{2x}{x^2 + 5}
$$

Let the candidate for substitution be the entire denominator:

$$
u = x^2 + 5
$$

Note that for all real numbers $x \in \mathbb{R}$, $x^2 \ge 0 \implies x^2 + 5 \ge 5 > 0$. Thus, the denominator never vanishes, and the integrand is continuous on all of $\mathbb{R}$.

---

**Step 2: Compare the numerator with the derivative of the denominator**

Compute the differential of $u$:

$$
\frac{du}{dx} = \frac{d}{dx}[x^2 + 5] = 2x \implies du = 2x \, dx
$$

Comparing this with the given fraction:
* Denominator: $u = x^2 + 5$
* Numerator together with $dx$: $2x \, dx = du$

The numerator is the exact derivative of the denominator.

---

**Step 3: Perform the substitution and evaluate the integral**

Substitute $u = x^2 + 5$ and $du = 2x \, dx$:

$$
\int \frac{2x}{x^2 + 5} \, dx = \int \frac{1}{u} \, du
$$

Apply the standard reciprocal integral rule:

$$
\int \frac{1}{u} \, du = \ln |u| + C
$$

Substitute back $u = x^2 + 5$:

$$
= \ln |x^2 + 5| + C
$$

Because $x^2 + 5 > 0$ for all real $x$, the absolute value bars may be dropped:

$$
= \ln(x^2 + 5) + C
$$

---

**Step 4: Explain the source of the logarithm in the result**

1. **Reversal of the Logarithmic Chain Rule:**
   When differentiating the composite logarithm $y = \ln(g(x))$, the chain rule gives:

   $$
   \frac{d}{dx}[\ln(g(x))] = \frac{1}{g(x)} \cdot g'(x) = \frac{g'(x)}{g(x)}
   $$

   Whenever an integrand exhibits the canonical form $\frac{g'(x)}{g(x)}$ (the derivative of the denominator in the numerator), its antiderivative is naturally the natural logarithm of the denominator.
2. **Singular Case of the Power Family:**
   In the hierarchy of power functions $\int u^n \, du$, every exponent $n \neq -1$ produces another power function $\frac{u^{n+1}}{n+1}$. The isolated singularity $n = -1$ cannot produce a power function; its accumulation is uniquely described by the natural logarithm.

---

### Final Answer

1. **Substitution Components:**
   * Candidate: $u = x^2 + 5$
   * Differential: $du = 2x \, dx$
   * The numerator is the exact derivative of the denominator.

2. **Indefinite Integral:**

   $$
   \int\frac{2x}{x^2+5}\,dx = \ln(x^2 + 5) + C
   $$

3. **Source of the Logarithm:**
   The integrand matches the form $\frac{g'(x)}{g(x)}$. Because the derivative of $\ln(u)$ is $\frac{1}{u}$, reversing the chain rule for $\frac{g'(x)}{g(x)}$ produces $\ln|g(x)|$.
