### Essential Formulas

1. **Fundamental Limit for $e$ (Continuous Form):**
   For any real variable $u \to 0$:

   $$
   \lim_{u \to 0} (1 + u)^{1/u} = e
   $$

   This is directly related to the discrete sequence limit from Exercise 5:

   $$
   \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e
   $$

   via the substitution $u = \frac{1}{n}$ as $n \to \infty$.

2. **Power of a Limit Law:**
   If $\lim_{x \to c} g(x) = L$ and $k \in \mathbb{R}$, then by continuity of the power function:

   $$
   \lim_{x \to c} [g(x)]^k = \left[\lim_{x \to c} g(x)\right]^k = L^k
   $$

3. **Logarithmic Evaluation of Indeterminate Powers $1^\infty$:**
   If $y = [f(x)]^{g(x)}$, then:

   $$
   \lim_{x \to c} f(x)^{g(x)} = \exp\left(\lim_{x \to c} g(x) \ln(f(x))\right)
   $$

---

### Problem Statement

Compute

$$
\lim_{x\to0}(1+3x)^{1/x}.
$$

Connect the result with the limit from Exercise 5 and show the appropriate transformation.

> **Why this exercise:** teaches how to recognize the classical pattern after a transformation.

---

### Solution

**Step 1: Identify the indeterminate form**

As $x \to 0$:

$$
1 + 3x \to 1, \qquad \frac{1}{x} \to \pm\infty
$$

The expression exhibits the indeterminate power form $1^\infty$.

---

**Step 2: Connect with the classical limit via substitution**

Recall from Exercise 5 the classical sequence limit:

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e
$$

Setting $u = \frac{1}{n}$ converts $n \to \infty$ into $u \to 0^+$. Generalizing to continuous two-sided approach:

$$
\lim_{u \to 0} (1 + u)^{1/u} = e
$$

In our given limit:

$$
\lim_{x \to 0} (1 + 3x)^{1/x}
$$

the linear increment inside the parenthesis is $3x$. We define the substitution:

$$
u = 3x \iff x = \frac{u}{3}
$$

As $x \to 0$, we have $u \to 0$.

---

**Step 3: Transform the exponent and evaluate**

Express the exponent $\frac{1}{x}$ in terms of $u$:

$$
\frac{1}{x} = \frac{1}{u / 3} = \frac{3}{u}
$$

Rewrite the original function using exponent rules:

$$
(1 + 3x)^{1/x} = (1 + u)^{3/u} = \left[(1 + u)^{1/u}\right]^3
$$

Apply the continuous power law:

$$
\lim_{x \to 0} (1 + 3x)^{1/x} = \lim_{u \to 0} \left[(1 + u)^{1/u}\right]^3 = \left[\lim_{u \to 0} (1 + u)^{1/u}\right]^3
$$

Substitute the fundamental value $e$:

$$
= e^3
$$

---

**Step 4: Alternative verification using natural logarithms**

Let $y = (1 + 3x)^{1/x}$. Take the natural logarithm:

$$
\ln y = \ln\left((1 + 3x)^{1/x}\right) = \frac{1}{x} \ln(1 + 3x) = \frac{\ln(1 + 3x)}{x}
$$

Multiply and divide by $3$:

$$
\ln y = 3 \cdot \frac{\ln(1 + 3x)}{3x}
$$

Using the standard logarithmic limit $\lim_{t \to 0} \frac{\ln(1 + t)}{t} = 1$ with $t = 3x$:

$$
\lim_{x \to 0} \ln y = 3 \cdot 1 = 3
$$

By continuity of the exponential function:

$$
\lim_{x \to 0} y = e^{\lim_{x \to 0} \ln y} = e^3
$$

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{x\to0}(1+3x)^{1/x} = e^3
   $$

2. **Connection and Transformation:**
   * Substituting $u = 3x$ transforms the exponent into $\frac{1}{x} = \frac{3}{u}$.
   * The expression rewrites as $\left[(1 + u)^{1/u}\right]^3$.
   * Since $\lim_{u \to 0} (1 + u)^{1/u} = e$ (the continuous extension of the sequence limit from Exercise 5), the overall limit evaluates directly to $e^3$.
