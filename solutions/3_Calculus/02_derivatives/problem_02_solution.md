### Essential Formulas

1. **Exponent Rules for Radicals and Reciprocals:**
   * $\sqrt[n]{x} = x^{1/n} \implies \sqrt{x} = x^{1/2}$
   * $\frac{1}{x^n} = x^{-n} \implies \frac{1}{x^2} = x^{-2}$

2. **General Power Rule for Differentiation:**
   For any real exponent $\alpha \in \mathbb{R}$:

   $$
   \frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}
   $$

3. **Domain of a Function vs. Domain of its Derivative:**
   A function can only be differentiable at interior points of its domain where the derivative limit exists:

   $$
   D_{f'} \subseteq D_f
   $$

---

### Problem Statement

For

$$
f(x)=2\sqrt{x}-\frac{3}{x^2}+x^{3/2}
$$

1. rewrite the function using powers,
2. determine the domain,
3. compute the derivative,
4. compare the domain of the function with the domain of its derivative.

> **Why this problem:** it teaches how to rewrite different forms so that the power rule can be applied and how to keep track of the domain.

---

### Solution

**Step 1: Rewrite the function using power notation**

Convert the radical and reciprocal terms into fractional and negative exponents:
* $2\sqrt{x} = 2 x^{1/2}$
* $-\frac{3}{x^2} = -3 x^{-2}$
* $x^{3/2}$ is already in power form.

Thus:

$$
f(x) = 2 x^{1/2} - 3 x^{-2} + x^{3/2}
$$

---

**Step 2: Determine the domain of $f(x)$**

Analyze the restrictions on each term of $f(x)$:
1. $\sqrt{x} = x^{1/2}$ requires $x \ge 0$ for real values.
2. $\frac{3}{x^2} = 3 x^{-2}$ requires a non-zero denominator: $x^2 \neq 0 \implies x \neq 0$.
3. $x^{3/2} = (\sqrt{x})^3$ requires $x \ge 0$.

Intersecting these conditions ($x \ge 0$ and $x \neq 0$):

$$
D_f = (0, \infty)
$$

---

**Step 3: Compute the derivative $f'(x)$**

Apply the general power rule $\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}$ term by term:
* $\frac{d}{dx}[2 x^{1/2}] = 2 \cdot \frac{1}{2} x^{(1/2 - 1)} = x^{-1/2}$
* $\frac{d}{dx}[-3 x^{-2}] = -3 \cdot (-2) x^{(-2 - 1)} = 6 x^{-3}$
* $\frac{d}{dx}[x^{3/2}] = \frac{3}{2} x^{(3/2 - 1)} = \frac{3}{2} x^{1/2}$

Combining the terms:

$$
f'(x) = x^{-1/2} + 6 x^{-3} + \frac{3}{2} x^{1/2}
$$

Converting back to radical and fractional form:

$$
f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}
$$

---

**Step 4: Determine the domain of $f'(x)$ and compare with $D_f$**

Examining the terms of $f'(x)$:
1. $\frac{1}{\sqrt{x}}$ requires $x > 0$ (radicand non-negative and non-zero denominator).
2. $\frac{6}{x^3}$ requires $x \neq 0$.
3. $\frac{3}{2}\sqrt{x}$ requires $x \ge 0$.

The simultaneous satisfaction of these conditions requires $x > 0$:

$$
D_{f'} = (0, \infty)
$$

**Comparison:**
Both domains are identical:

$$
D_f = D_{f'} = (0, \infty)
$$

The function is differentiable at every single point in its domain.

---

### Final Answer

1. **Power Representation:**

   $$
   f(x) = 2 x^{1/2} - 3 x^{-2} + x^{3/2}
   $$

2. **Domain of $f$:**

   $$
   D_f = (0, \infty)
   $$

3. **Derivative:**

   $$
   f'(x) = x^{-1/2} + 6 x^{-3} + \frac{3}{2} x^{1/2} = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}
   $$

4. **Domain Comparison:**
   $D_{f'} = (0, \infty)$, which coincides exactly with $D_f$.
