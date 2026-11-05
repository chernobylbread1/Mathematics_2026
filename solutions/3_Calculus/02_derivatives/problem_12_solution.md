### Essential Formulas

1. **Product Rule:**
   For a product of two differentiable functions $u(x)$ and $v(x)$:

   $$
   (u \cdot v)' = u' \cdot v + u \cdot v'
   $$

2. **Chain Rule (Generalized Power Rule):**
   For a composite power $[g(x)]^n$:

   $$
   \frac{d}{dx}\left[(g(x))^n\right] = n [g(x)]^{n-1} \cdot g'(x)
   $$

3. **Derivative of the Exponential Function:**

   $$
   \frac{d}{dx}[e^x] = e^x
   $$

---

### Problem Statement

For

$$
f(x)=(x^2+1)^3e^x
$$

compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

> **Why this problem:** it practices the order of decisions when combining familiar differentiation rules.

---

### Solution

**Step 1: Write down the differentiation plan**

* **Overall Expression Level (Global Structure):**
  The expression $f(x) = (x^2 + 1)^3 e^x$ is the product of two distinct functions:
  * First factor: $u(x) = (x^2 + 1)^3$
  * Second factor: $v(x) = e^x$
  Therefore, the **Product Rule** applies to the whole expression:

  $$
  f'(x) = u'(x) v(x) + u(x) v'(x)
  $$

* **Individual Factor Level (Local Sub-problem):**
  * The factor $v(x) = e^x$ differentiates directly: $v'(x) = e^x$.
  * The factor $u(x) = (x^2 + 1)^3$ is a composition of an outer cubic power $w^3$ with an inner polynomial $w = x^2 + 1$. Therefore, the **Chain Rule** applies to the first factor:

    $$
    u'(x) = 3(x^2 + 1)^2 \cdot \frac{d}{dx}[x^2 + 1]
    $$

---

**Step 2: Differentiate the factors**

1. Compute $u'(x)$ using the chain rule:

   $$
   u'(x) = 3(x^2 + 1)^2 \cdot (2x) = 6x (x^2 + 1)^2
   $$

2. Compute $v'(x)$:

   $$
   v'(x) = e^x
   $$

---

**Step 3: Combine according to the product rule**

Substitute $u, u', v, v'$ into the product rule:

$$
f'(x) = u'(x) v(x) + u(x) v'(x)
$$

$$
f'(x) = \left[6x (x^2 + 1)^2\right] e^x + \left[(x^2 + 1)^3\right] e^x
$$

---

**Step 4: Factor out common algebraic factors**

Both terms contain the common factors:
* $(x^2 + 1)^2$
* $e^x$

Factor them out:

$$
f'(x) = (x^2 + 1)^2 e^x \cdot \left[6x + (x^2 + 1)\right]
$$

Rearrange the remaining polynomial factor into standard quadratic descending order:

$$
6x + x^2 + 1 = x^2 + 6x + 1
$$

Thus, the fully factored derivative is:

$$
f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x
$$

---

### Final Answer

1. **Differentiation Plan:**
   * **Global Rule:** The Product Rule $(u v)' = u' v + u v'$ governs the primary product of $(x^2+1)^3$ and $e^x$.
   * **Component Rule:** The Chain Rule governs the composite factor $u(x) = (x^2+1)^3$, yielding $u'(x) = 6x(x^2+1)^2$.

2. **Fully Factored Derivative:**

   $$
   f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x
   $$

