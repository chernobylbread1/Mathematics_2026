### Essential Formulas

1. **Integration by Substitution (Reversing the Chain Rule):**
   If $u = g(x)$ is a differentiable function whose range is an interval $I$, and $f$ is continuous on $I$, then:

   $$
   \int f(g(x)) g'(x) \, dx = \int f(u) \, du
   $$

2. **Power Rule for the Substituted Variable:**
   For any power $n \neq -1$:

   $$
   \int u^n \, du = \frac{u^{n+1}}{n+1} + C
   $$

3. **Chain Rule for Differentiation:**

   $$
   \frac{d}{dx}[F(g(x))] = F'(g(x)) \cdot g'(x)
   $$

---

### Problem Statement

Compute

$$
\int 2x(x^2+1)^4\,dx.
$$

Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

> **Why this problem:** it teaches how to recognize substitution as reversing the chain rule.

---

### Solution

**Step 1: Identify the candidate for the substitution variable $u$**

Examine the structure of the integrand:

$$
2x(x^2 + 1)^4
$$

* The factor $(x^2 + 1)^4$ has the inner polynomial $g(x) = x^2 + 1$ raised to the fourth power.
* The outer factor is $2x$.

We choose the inner function as our candidate:

$$
u = x^2 + 1
$$

---

**Step 2: Show that the derivative of $u$ appears in the integral**

Compute the differential of $u$:

$$
\frac{du}{dx} = \frac{d}{dx}[x^2 + 1] = 2x \implies du = 2x \, dx
$$

Comparing this with the integral:

$$
\int (x^2 + 1)^4 \cdot (2x \, dx)
$$

The factor $2x \, dx$ is present in the integral, matching the differential $du$.
This confirms that the integrand is of the exact chain-rule form $f(g(x)) g'(x) \, dx$.

---

**Step 3: Perform the substitution and evaluate the integral**

Substitute $u = x^2 + 1$ and $du = 2x \, dx$ into the integral:

$$
\int 2x(x^2 + 1)^4 \, dx = \int u^4 \, du
$$

Apply the basic power rule for $u$:

$$
\int u^4 \, du = \frac{u^{4+1}}{4+1} + C = \frac{u^5}{5} + C
$$

Substitute back $u = x^2 + 1$ to return to the original variable $x$:

$$
= \frac{(x^2 + 1)^5}{5} + C
$$

---

**Step 4: Verify the result by differentiation**

Differentiate the obtained antiderivative using the chain rule:

$$
\frac{d}{dx}\left[\frac{(x^2 + 1)^5}{5} + C\right] = \frac{1}{5} \cdot \frac{d}{dx}\left[(x^2 + 1)^5\right] + 0
$$

By the chain rule with inner function $x^2 + 1$:

$$
= \frac{1}{5} \cdot 5(x^2 + 1)^{5-1} \cdot \frac{d}{dx}[x^2 + 1]
$$

$$
= (x^2 + 1)^4 \cdot (2x) = 2x(x^2 + 1)^4
$$

The derivative matches the integrand.

---

### Final Answer

1. **Substitution Candidate:**

   $$
   u = x^2 + 1 \implies du = 2x \, dx
   $$

   The derivative $g'(x) = 2x$ supplies the factor in the differential $2x \, dx = du$.

2. **Indefinite Integral:**

   $$
   \int 2x(x^2+1)^4\,dx = \frac{(x^2 + 1)^5}{5} + C
   $$

3. **Verification:**

   $$
   \frac{d}{dx}\left[\frac{(x^2 + 1)^5}{5} + C\right] = \frac{5(x^2 + 1)^4 \cdot 2x}{5} = 2x(x^2 + 1)^4
   $$
