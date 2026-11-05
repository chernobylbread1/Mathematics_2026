### Essential Formulas

1. **Fractional and Negative Exponent Definitions:**
   * $\sqrt{x} = x^{1/2}$
   * $\frac{1}{x^n} = x^{-n}$
   * $\sqrt[3]{x} = x^{1/3}$

2. **General Power Rule for Integration:**
   For any constant exponent $\alpha \neq -1$:

   $$
   \int x^\alpha \, dx = \frac{x^{\alpha+1}}{\alpha+1} + C
   $$

3. **Domain of Integrand:**
   An antiderivative exists on any connected subinterval of the domain of the integrand where the function is continuous.

---

### Problem Statement

Compute

$$
\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx.
$$

First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

> **Why this problem:** it reinforces the power rule and reminds the student to keep track of the domain.

---

### Solution

**Step 1: Rewrite terms using power notation**

Convert all radicals and fractions into standard power form:
* $2\sqrt{x} = 2x^{1/2}$
* $\frac{3}{x^2} = 3x^{-2}$
* $x^{1/3}$ is already in power form.

Thus, the integrand is:

$$
f(x) = 2x^{1/2} + 3x^{-2} - x^{1/3}
$$

---

**Step 2: Determine the domain of the integrand**

Analyze the restrictions on each term of $f(x)$:
1. $\sqrt{x} = x^{1/2}$ requires $x \ge 0$ in real arithmetic.
2. $\frac{3}{x^2} = 3x^{-2}$ requires a non-zero denominator: $x^2 \neq 0 \implies x \neq 0$.
3. $x^{1/3}$ is defined for all real $x$.

Intersecting these conditions ($x \ge 0$ and $x \neq 0$):

$$
D_f = (0, \infty)
$$

The integration is performed on the domain $(0, \infty)$.

---

**Step 3: Compute the antiderivative**

Integrate term by term applying the power rule $\int x^\alpha \, dx = \frac{x^{\alpha+1}}{\alpha+1}$:
1. First term:

   $$
   \int 2x^{1/2} \, dx = 2 \cdot \frac{x^{1/2 + 1}}{\frac{1}{2} + 1} = 2 \cdot \frac{x^{3/2}}{\frac{3}{2}} = 2 \cdot \frac{2}{3} x^{3/2} = \frac{4}{3} x^{3/2}
   $$

2. Second term:

   $$
   \int 3x^{-2} \, dx = 3 \cdot \frac{x^{-2 + 1}}{-2 + 1} = 3 \cdot \frac{x^{-1}}{-1} = -3x^{-1} = -\frac{3}{x}
   $$

3. Third term:

   $$
   \int \left(-x^{1/3}\right) \, dx = -\frac{x^{1/3 + 1}}{\frac{1}{3} + 1} = -\frac{x^{4/3}}{\frac{4}{3}} = -\frac{3}{4} x^{4/3}
   $$

Summing the terms and including the integration constant $C$:

$$
F(x) = \frac{4}{3} x^{3/2} - \frac{3}{x} - \frac{3}{4} x^{4/3} + C
$$

In radical notation:

$$
F(x) = \frac{4}{3} x\sqrt{x} - \frac{3}{x} - \frac{3}{4} x\sqrt[3]{x} + C
$$

---

**Step 4: Verify the result by differentiation**

Differentiate $F(x) = \frac{4}{3} x^{3/2} - 3x^{-1} - \frac{3}{4} x^{4/3} + C$:

$$
F'(x) = \frac{4}{3} \cdot \frac{d}{dx}[x^{3/2}] - 3 \cdot \frac{d}{dx}[x^{-1}] - \frac{3}{4} \cdot \frac{d}{dx}[x^{4/3}] + \frac{d}{dx}[C]
$$

Apply the power rule for derivatives $\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha-1}$:

$$
F'(x) = \frac{4}{3} \left(\frac{3}{2} x^{1/2}\right) - 3 \left(-1 x^{-2}\right) - \frac{3}{4} \left(\frac{4}{3} x^{1/3}\right) + 0
$$

Simplify the coefficients:

$$
F'(x) = 2x^{1/2} + 3x^{-2} - x^{1/3} = 2\sqrt{x} + \frac{3}{x^2} - x^{1/3} = f(x)
$$

The result matches the original integrand.

---

### Final Answer

1. **Power Representation of Integrand:**

   $$
   f(x) = 2x^{1/2} + 3x^{-2} - x^{1/3}
   $$

2. **Domain of Integrand:**

   $$
   D_f = (0, \infty)
   $$

3. **Indefinite Integral:**

   $$
   \int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx = \frac{4}{3} x^{3/2} - \frac{3}{x} - \frac{3}{4} x^{4/3} + C
   $$

4. **Verification:**

   $$
   \frac{d}{dx}\left[\frac{4}{3} x^{3/2} - \frac{3}{x} - \frac{3}{4} x^{4/3} + C\right] = 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}
   $$
