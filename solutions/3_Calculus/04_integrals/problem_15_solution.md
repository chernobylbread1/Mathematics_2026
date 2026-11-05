### Essential Formulas

1. **Initial Value Problem (IVP):**
   Given a differential equation $F'(x) = f(x)$ and an initial condition $F(x_0) = y_0$:
   * Step 1: Find the general family of antiderivatives:

     $$
     F(x) = \int f(x) \, dx = G(x) + C
     $$

   * Step 2: Determine the unique constant $C$ by substituting the point $(x_0, y_0)$:

     $$
     G(x_0) + C = y_0 \implies C = y_0 - G(x_0)
     $$

2. **Exponential Composite Substitution:**

   $$
   \int e^{g(x)} g'(x) \, dx = e^{g(x)} + C
   $$

3. **Zero Exponent Identity:**

   $$
   e^0 = 1
   $$

---

### Problem Statement

The function $F$ satisfies

$$
F'(x)=2xe^{x^2}
$$

and

$$
F(0)=3.
$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0)=3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x=0$.

> **Why this problem:** it combines recognition of substitution, the meaning of the constant of integration, and an initial condition in one problem, using only mechanisms introduced earlier.

---

### Solution

**Step 1: Recognize the method needed to find the function $F$**

We are tasked with computing the indefinite integral:

$$
F(x) = \int 2x e^{x^2} \, dx
$$

* The integrand contains the composite exponential term $e^{x^2}$, whose inner exponent is $g(x) = x^2$.
* The derivative of this exponent is $g'(x) = 2x$, which appears directly as a multiplying factor.

Because the integrand is in the form $e^{g(x)} g'(x)$, the appropriate method is **integration by substitution** (reversing the exponential chain rule).

---

**Step 2: Determine the entire family of antiderivatives**

Define the substitution variable:

$$
u = x^2
$$

Compute the differential:

$$
du = \frac{d}{dx}[x^2] \, dx = 2x \, dx
$$

Substitute $u$ and $du$ into the indefinite integral:

$$
F(x) = \int e^u \, du
$$

Evaluate the basic exponential integral:

$$
F(x) = e^u + C
$$

Substitute back $u = x^2$ to obtain the complete family of antiderivatives:

$$
F(x) = e^{x^2} + C, \qquad C \in \mathbb{R}
$$

---

**Step 3: Determine the constant $C$ using the initial condition $F(0) = 3$**

Substitute $x = 0$ into the general family $F(x) = e^{x^2} + C$:

$$
F(0) = e^{0^2} + C = e^0 + C
$$

Since $e^0 = 1$:

$$
F(0) = 1 + C
$$

Equate this to the specified initial condition $F(0) = 3$:

$$
1 + C = 3 \implies C = 3 - 1 = 2
$$

Substitute $C = 2$ back into the formula to isolate the unique function:

$$
F(x) = e^{x^2} + 2
$$

---

**Step 4: Verify the final result**

1. **Verify by differentiation:**
   Differentiate $F(x) = e^{x^2} + 2$ with respect to $x$:

   $$
   F'(x) = \frac{d}{dx}\left[e^{x^2} + 2\right] = \frac{d}{dx}\left[e^{x^2}\right] + \frac{d}{dx}[2]
   $$

   Apply the chain rule to $e^{x^2}$:

   $$
   F'(x) = e^{x^2} \cdot \frac{d}{dx}[x^2] + 0 = e^{x^2} \cdot (2x) = 2x e^{x^2}
   $$

   This matches the given differential equation $F'(x) = 2x e^{x^2}$.

2. **Verify by substituting $x = 0$:**

   $$
   F(0) = e^{0^2} + 2 = e^0 + 2 = 1 + 2 = 3
   $$

   This satisfies the given initial condition $F(0) = 3$.

Both conditions are satisfied.

---

### Final Answer

1. **Method Recognition:**
   Integration by substitution ($u = x^2$), recognized because the external factor $2x$ is the exact derivative of the exponent $x^2$.

2. **General Family of Functions:**

   $$
   F(x) = e^{x^2} + C, \qquad C \in \mathbb{R}
   $$

3. **Constant and Particular Solution:**

   $$
   C = 2 \implies F(x) = e^{x^2} + 2
   $$

4. **Verification:**
   * $F'(x) = \frac{d}{dx}[e^{x^2} + 2] = 2x e^{x^2}$
   * $F(0) = e^0 + 2 = 1 + 2 = 3$
