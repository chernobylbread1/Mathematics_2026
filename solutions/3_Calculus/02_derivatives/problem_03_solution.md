### Essential Formulas

1. **Product Rule for Differentiation:**
   If $u(x)$ and $v(x)$ are differentiable functions, their product $f(x) = u(x) v(x)$ is differentiable, and its derivative is given by:

   $$
   (u \cdot v)' = u' \cdot v + u \cdot v'
   $$

2. **Derivative of the Natural Exponential Function:**

   $$
   \frac{d}{dx}[e^x] = e^x
   $$

3. **Origin of the Product Rule (Difference Quotient):**
   Expanding the difference quotient of a product:

   $$
   \frac{u(x+h)v(x+h) - u(x)v(x)}{h} = \frac{u(x+h) - u(x)}{h} v(x+h) + u(x) \frac{v(x+h) - v(x)}{h}
   $$

   As $h \to 0$, both terms contribute to the derivative, producing $u' v + u v'$.

---

### Problem Statement

For

$$
f(x)=(x^2+1)e^x
$$

compute the derivative. Then compare the correct result with the incorrect idea

$$
f'(x)\stackrel{?}{=}(2x)e^x
$$

and explain which term is missing.

> **Why this problem:** it teaches the product rule by analyzing a common mistake.

---

### Solution

**Step 1: Identify factors and their individual derivatives**

Let the function be $f(x) = u(x) v(x)$, where:
* $u(x) = x^2 + 1 \implies u'(x) = 2x$
* $v(x) = e^x \implies v'(x) = e^x$

---

**Step 2: Apply the product rule correctly**

According to the product rule:

$$
f'(x) = u'(x) v(x) + u(x) v'(x)
$$

Substitute the individual components:

$$
f'(x) = (2x) e^x + (x^2 + 1) e^x
$$

Factor out the common factor $e^x$:

$$
f'(x) = (2x + x^2 + 1) e^x = (x^2 + 2x + 1) e^x
$$

Notice that $x^2 + 2x + 1$ is a perfect square $(x + 1)^2$:

$$
f'(x) = (x + 1)^2 e^x
$$

---

**Step 3: Analyze the common misconception**

The incorrect proposal suggests:

$$
f'(x) \stackrel{?}{=} (2x) e^x
$$

Comparing the two expressions:
* Correct derivative: $f'(x) = u'(x) v(x) + u(x) v'(x) = 2x e^x + (x^2 + 1) e^x$
* Proposed formula: $u'(x) v(x) = 2x e^x$

The term that is missing is:

$$
u(x) v'(x) = (x^2 + 1) e^x
$$

---

**Step 4: Explanation of why the missing term is essential**

1. **Simultaneous Change:**
   When the independent variable $x$ changes, *both* factors $u(x) = x^2+1$ and $v(x) = e^x$ change simultaneously.
2. **Two Contributions to the Rate of Change:**
   * The first contribution, $u'(x) v(x) = (2x)e^x$, measures the change in the product caused solely by the variation in $x^2+1$ while $e^x$ is held momentary constant.
   * The second contribution, $u(x) v'(x) = (x^2+1)e^x$, measures the change in the product caused solely by the variation in $e^x$ while $x^2+1$ is held momentary constant.
3. **Conclusion:**
   Omitting $u(x) v'(x)$ falsely assumes that the exponential factor $e^x$ behaves as an inert constant, ignoring that $\frac{d}{dx}[e^x] = e^x \neq 0$.

---

### Final Answer

1. **Correct Derivative:**

   $$
   f'(x) = (x^2 + 2x + 1) e^x = (x + 1)^2 e^x
   $$

2. **Missing Term:**
   The term $(x^2 + 1) e^x$ (which corresponds to $u \cdot v'$) is missing from the erroneous expression $(2x) e^x$.

3. **Conceptual Reason:**
   The product rule demands summing the rates of change contributed by both factors: $(u v)' = u' v + u v'$. The erroneous calculation differentiated only the polynomial factor while treating the non-constant exponential factor $e^x$ as a static multiplier.

