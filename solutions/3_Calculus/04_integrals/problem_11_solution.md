### Essential Formulas

1. **Linear Argument Substitution:**
   For any integrable function $f$ and constant $k \neq 0$:

   $$
   \int f(k x) \, dx = \frac{1}{k} F(k x) + C
   $$

2. **Integration by Parts (Logarithmic Factor):**
   When an integrand contains a logarithm $\ln x$ paired with a power $x^n$:
   * Choose $u = \ln x \implies u' = \frac{1}{x}$
   * Choose $v' = x^n \implies v = \frac{x^{n+1}}{n+1}$

3. **Radical Composite Substitution:**
   When an integrand contains $x(x^2 + a)^n$:
   * Choose $u = x^2 + a \implies du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du$

---

### Problem Statement

For each integral, first write which method you choose and how you recognize it, and then compute:

1. $\int\sin(3x)\,dx$,
2. $\int x\ln x\,dx$,
3. $\int\frac{x}{\sqrt{x^2+1}}\,dx$.

> **Why this problem:** it tests the choice of method based on the structure of the problem.

---

### Solution

**Step 1: Evaluate $\int \sin(3x) \, dx$**

* **Method Chosen:** Linear substitution (or anti-chain rule scaling).
* **Recognition:** The integrand is the elementary sine function evaluated at a linear argument $u = 3x$. The derivative of $3x$ is the constant $3$.
* **Calculation:**
  Let $u = 3x \implies du = 3 \, dx \implies dx = \frac{1}{3} \, du$.
  Substitute into the integral:

  $$
  \int \sin(3x) \, dx = \int \sin u \left(\frac{1}{3} \, du\right) = \frac{1}{3} \int \sin u \, du
  $$

  The antiderivative of $\sin u$ is $-\cos u$:

  $$
  = \frac{1}{3} (-\cos u) + C = -\frac{1}{3} \cos(3x) + C
  $$

---

**Step 2: Evaluate $\int x \ln x \, dx$**

* **Method Chosen:** Integration by parts.
* **Recognition:** The integrand is a product of two dissimilar functions: an algebraic power $x$ and a transcendental function $\ln x$. Differentiating $\ln x$ yields $\frac{1}{x}$, which eliminates the transcendental nature and reduces the problem to an algebraic power.
* **Calculation:**
  Set the parts:
  * $u = \ln x \implies du = \frac{1}{x} \, dx$
  * $dv = x \, dx \implies v = \frac{x^2}{2}$

  Apply the integration-by-parts formula $\int u \, dv = u v - \int v \, du$:

  $$
  \int x \ln x \, dx = (\ln x)\left(\frac{x^2}{2}\right) - \int \left(\frac{x^2}{2}\right) \left(\frac{1}{x} \, dx\right)
  $$

  Simplify the remaining integral:

  $$
  = \frac{x^2}{2} \ln x - \frac{1}{2} \int x \, dx = \frac{x^2}{2} \ln x - \frac{1}{2} \left(\frac{x^2}{2}\right) + C
  $$

  $$
  = \frac{x^2}{2} \ln x - \frac{x^2}{4} + C = \frac{x^2}{4}(2\ln x - 1) + C
  $$

---

**Step 3: Evaluate $\int \frac{x}{\sqrt{x^2+1}} \, dx$**

* **Method Chosen:** Algebraic substitution.
* **Recognition:** The denominator contains the quadratic radicand $x^2 + 1$, while the numerator contains $x \, dx$. Because the derivative of $x^2 + 1$ is $2x$, the external factor $x \, dx$ provides the required differential up to a factor of $\frac{1}{2}$.
* **Calculation:**
  Let $u = x^2 + 1 \implies du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du$.
  Rewrite the radical as a fractional power:

  $$
  \int \frac{x}{\sqrt{x^2+1}} \, dx = \int \frac{1}{\sqrt{u}} \left(\frac{1}{2} \, du\right) = \frac{1}{2} \int u^{-1/2} \, du
  $$

  Apply the power rule $\int u^\alpha \, du = \frac{u^{\alpha+1}}{\alpha+1}$:

  $$
  = \frac{1}{2} \cdot \frac{u^{1/2}}{\frac{1}{2}} + C = u^{1/2} + C = \sqrt{u} + C
  $$

  Substitute back $u = x^2 + 1$:

  $$
  = \sqrt{x^2 + 1} + C
  $$

---

### Final Answer

1. **Integral 1:**
   * **Method:** Linear substitution ($u = 3x$).

     $$
     \int\sin(3x)\,dx = -\frac{1}{3}\cos(3x) + C
     $$

2. **Integral 2:**
   * **Method:** Integration by parts ($u = \ln x, dv = x \, dx$).

     $$
     \int x\ln x\,dx = \frac{x^2}{2}\ln x - \frac{x^2}{4} + C = \frac{x^2}{4}(2\ln x - 1) + C
     $$

3. **Integral 3:**
   * **Method:** Algebraic substitution ($u = x^2 + 1$).

     $$
     \int\frac{x}{\sqrt{x^2+1}}\,dx = \sqrt{x^2+1} + C
     $$
