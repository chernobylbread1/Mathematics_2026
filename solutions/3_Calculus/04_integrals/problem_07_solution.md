### Essential Formulas

1. **Product Rule for Differentiation:**
   For differentiable functions $u(x)$ and $v(x)$:

   $$
   \frac{d}{dx}[u(x) v(x)] = u'(x) v(x) + u(x) v'(x)
   $$

2. **Integration by Parts Formula:**
   Integrating the product rule and rearranging yields:

   $$
   \int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx
   $$

   or in differential notation:

   $$
   \int u \, dv = u v - \int v \, du
   $$

---

### Problem Statement

Compute

$$
\int xe^x\,dx.
$$

First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

> **Why this problem:** it connects a new technique with the familiar product rule.

---

### Solution

**Step 1: Derive the integration by parts formula from the product rule**

Start with the product rule of differential calculus:

$$
\frac{d}{dx}[u(x) v(x)] = u'(x) v(x) + u(x) v'(x)
$$

Take the indefinite integral of both sides with respect to $x$:

$$
\int \frac{d}{dx}[u(x) v(x)] \, dx = \int u'(x) v(x) \, dx + \int u(x) v'(x) \, dx
$$

Because integration is the inverse of differentiation:

$$
u(x) v(x) = \int u'(x) v(x) \, dx + \int u(x) v'(x) \, dx
$$

Isolate the term $\int u(x) v'(x) \, dx$:

$$
\int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx
$$

**Meaning of the Formula:**
Integration by parts allows us to trade the integral of $u \cdot v'$ for the integral of $u' \cdot v$. If $u(x)$ simplifies upon differentiation (such as a polynomial whose degree drops) and $v'(x)$ integrates without becoming more complex, the new integral $\int u' v \, dx$ becomes significantly easier to compute.

---

**Step 2: Assign the parts for $\int x e^x \, dx$**

Let the integrand be split into:
* $u(x) = x \implies u'(x) = 1$
* $v'(x) = e^x \implies v(x) = \int e^x \, dx = e^x$

Differentiating $u = x$ eliminates the variable $x$, reducing it to the constant $1$.

---

**Step 3: Apply the formula and evaluate**

Substitute $u, u', v, v'$ into the integration-by-parts formula:

$$
\int x e^x \, dx = x e^x - \int (1) e^x \, dx
$$

The remaining integral is elementary:

$$
\int e^x \, dx = e^x
$$

Therefore:

$$
\int x e^x \, dx = x e^x - e^x + C
$$

Factoring out the common exponential factor $e^x$:

$$
= (x - 1)e^x + C
$$

---

**Step 4: Verify the result by differentiation**

Differentiate $(x - 1)e^x + C$ using the product rule:

$$
\frac{d}{dx}\left[(x - 1)e^x + C\right] = \frac{d}{dx}[(x - 1)] \cdot e^x + (x - 1) \cdot \frac{d}{dx}[e^x] + 0
$$

Substitute the individual derivatives:

$$
= (1) e^x + (x - 1) e^x = e^x + x e^x - e^x = x e^x
$$

The derivative matches the original integrand.

---

### Final Answer

1. **Origin of Integration by Parts:**
   Derived directly by integrating the product rule $(u v)' = u' v + u v'$, yielding $\int u v' \, dx = u v - \int u' v \, dx$. It transfers the derivative from one factor to the other to simplify the integrand.

2. **Indefinite Integral:**

   $$
   \int xe^x\,dx = (x - 1)e^x + C
   $$

3. **Verification:**

   $$
   \frac{d}{dx}\left[(x - 1)e^x + C\right] = 1 \cdot e^x + (x - 1)e^x = x e^x
   $$

