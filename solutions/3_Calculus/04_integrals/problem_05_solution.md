### Essential Formulas

1. **Structural Principle of Substitution:**
   An integral conforms to the substitution method whenever it can be partitioned into:

   $$
   \int f(g(x)) \cdot g'(x) \, dx
   $$

   The specific identity of the outer function $f$ (whether a power, exponential, or trigonometric function) does not change the core substitution mechanism.

2. **Exponential Integral Rule:**

   $$
   \int e^u \, du = e^u + C
   $$

3. **Chain Rule for Exponential Composites:**

   $$
   \frac{d}{dx}[e^{g(x)}] = e^{g(x)} \cdot g'(x)
   $$

---

### Problem Statement

Compute

$$
\int xe^{x^2}\,dx.
$$

First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

> **Why this problem:** it shows that the substitution mechanism is recognized by structure, not by the type of function.

---

### Solution

**Step 1: Compare the structure with Problem 4**

Let us place the integrands of Problem 4 and Problem 5 side by side:
* **Problem 4:** $\int (x^2 + 1)^4 \cdot (2x \, dx)$
  * Inner function: $g(x) = x^2 + 1$ (quadratic)
  * Derivative: $g'(x) = 2x$ (linear)
  * Outer operation: fourth power $[\dots]^4$
* **Problem 5:** $\int e^{x^2} \cdot (x \, dx)$
  * Inner function: $g(x) = x^2$ (quadratic)
  * Derivative: $g'(x) = 2x \implies x = \frac{1}{2} g'(x)$ (linear)
  * Outer operation: natural exponential $\exp(\dots)$

**What is Common:**
In both problems, an inner quadratic polynomial $x^2$ is trapped inside an outer function, while the remaining multiplying factor outside is a linear term in $x$. Because the derivative of a degree-$2$ polynomial is of degree $1$, the external factor $x \, dx$ provides the differential needed to execute the substitution, differing only by a constant coefficient $\frac{1}{2}$. The structural pattern is identical: reversing the chain rule.

---

**Step 2: Execute the substitution**

Define the new variable:

$$
u = x^2
$$

Compute the differential:

$$
du = \frac{d}{dx}[x^2] \, dx = 2x \, dx \implies x \, dx = \frac{1}{2} \, du
$$

Substitute $u$ and $x \, dx$ into the integral:

$$
\int x e^{x^2} \, dx = \int e^u \left(\frac{1}{2} \, du\right) = \frac{1}{2} \int e^u \, du
$$

---

**Step 3: Evaluate the integral and back-substitute**

The antiderivative of $e^u$ is simply $e^u$:

$$
\frac{1}{2} \int e^u \, du = \frac{1}{2} e^u + C
$$

Replace $u$ with $x^2$:

$$
= \frac{1}{2} e^{x^2} + C
$$

---

**Step 4: Verify the result by differentiation**

Differentiate the resulting expression with respect to $x$:

$$
\frac{d}{dx}\left[\frac{1}{2} e^{x^2} + C\right] = \frac{1}{2} \frac{d}{dx}\left[e^{x^2}\right] + 0
$$

By the chain rule:

$$
= \frac{1}{2} \cdot e^{x^2} \cdot \frac{d}{dx}[x^2] = \frac{1}{2} \cdot e^{x^2} \cdot (2x) = x e^{x^2}
$$

The result matches the original integrand.

---

### Final Answer

1. **Structural Comparison with Problem 4:**
   Both integrals feature an inner quadratic expression ($x^2$ or $x^2+1$) paired with a linear external factor ($x$ or $2x$) that provides the exact differential $du \propto x \, dx$. The substitution succeeds because of this shared relationship between degrees, regardless of whether the outer wrapper is a power function or an exponential function.

2. **Indefinite Integral:**

   $$
   \int xe^{x^2}\,dx = \frac{1}{2} e^{x^2} + C
   $$

3. **Verification:**

   $$
   \frac{d}{dx}\left[\frac{1}{2} e^{x^2} + C\right] = \frac{1}{2} (2x) e^{x^2} = x e^{x^2}
   $$
