### Essential Formulas

1. **Definition of a Limit at a Point:**
   Let $f(x)$ be defined on an open interval containing $c$, except possibly at $c$ itself. We write $\lim_{x \to c} f(x) = L$ if for every $\varepsilon > 0$, there exists $\delta > 0$ such that:

   $$
   0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon
   $$

   The condition $0 < |x - c|$ explicitly excludes the point $x = c$ from consideration.

2. **Factor Theorem:**
   If a polynomial $P(x)$ satisfies $P(c) = 0$, then $(x - c)$ is an algebraic factor of $P(x)$, so:

   $$
   P(x) = (x - c) Q(x)
   $$

3. **Equality of Functions on a Punctured Neighborhood:**
   If $f(x) = g(x)$ for all $x \neq c$ in an open interval containing $c$, then:

   $$
   \lim_{x \to c} f(x) = \lim_{x \to c} g(x)
   $$

---

### Problem Statement

Compute

$$
\lim_{x\to3}\frac{x^2-4x+3}{x-3}.
$$

Explain why the value of the function at $x=3$ is not needed to compute the limit.

> **Why this exercise:** separates the concept of a limit from the value of a function at a point.

---

### Solution

**Step 1: Check substitution and identify the indeterminate form**

Direct substitution of $x = 3$ gives:

$$
\frac{3^2 - 4(3) + 3}{3 - 3} = \frac{9 - 12 + 3}{0} = \frac{0}{0}
$$

This is an indeterminate form of type $\frac{0}{0}$. The function $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ is undefined at $x = 3$.

---

**Step 2: Factor the numerator**

Find the roots of the quadratic numerator $x^2 - 4x + 3$:

$$
x^2 - 4x + 3 = (x - 3)(x - 1)
$$

Substitute the factorization into the fraction:

$$
f(x) = \frac{(x - 3)(x - 1)}{x - 3}
$$

---

**Step 3: Simplify for $x \neq 3$ and evaluate the limit**

When evaluating $\lim_{x \to 3} f(x)$, we consider only values of $x$ approaching $3$, meaning $x \neq 3$.
Since $x - 3 \neq 0$, we can cancel $(x - 3)$:

$$
f(x) = x - 1 \qquad (x \neq 3)
$$

Now evaluate the limit by direct substitution into the simplified continuous function:

$$
\lim_{x \to 3} \frac{x^2 - 4x + 3}{x - 3} = \lim_{x \to 3} (x - 1) = 3 - 1 = 2
$$

---

**Step 4: Why the function value at $x = 3$ is not needed**

1. **Punctured Neighborhood Concept:**
   The definition of the limit $\lim_{x \to c} f(x)$ describes the behavior of $f(x)$ as $x$ gets arbitrarily close to $c$, without ever setting $x = c$. It inspects the punctured neighborhood:

   $$
   0 < |x - 3| < \delta
   $$

2. **Independence from $f(c)$:**
   Whether $f(3)$ is undefined, equal to $2$, or arbitrarily redefined as $f(3) = 100$, the limit remains strictly $2$. The limit reflects local proximity and trend, not instantaneous point evaluation.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{x\to3}\frac{x^2-4x+3}{x-3} = 2
   $$

2. **Conceptual Explanation:**
   The limit evaluates the value that $f(x)$ approaches as $x$ gets arbitrarily close to $3$ in a punctured neighborhood ($x \neq 3$). Therefore, whether $f(3)$ exists or what value it assumes has no bearing on the limit.
