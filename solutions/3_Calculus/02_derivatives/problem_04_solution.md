### Essential Formulas

1. **Quotient Rule for Differentiation:**
   If $u(x)$ and $v(x)$ are differentiable functions, their quotient $\frac{u(x)}{v(x)}$ is differentiable at all points where $v(x) \neq 0$, with derivative:

   $$
   \left(\frac{u}{v}\right)' = \frac{u' \cdot v - u \cdot v'}{v^2}
   $$

2. **Domain of a Rational Function:**
   For $f(x) = \frac{P(x)}{Q(x)}$:

   $$
   D_f = \{x \in \mathbb{R} : Q(x) \neq 0\}
   $$

3. **Domain of the Derivative of a Rational Function:**
   The derivative cannot exist at any point where the original function is undefined:

   $$
   D_{f'} \subseteq D_f
   $$

---

### Problem Statement

For

$$
f(x)=\frac{x^2+1}{x-1}
$$

determine the domain, compute the derivative, simplify the result, and explain why the restriction $x\neq1$ remains important.

> **Why this problem:** it practices the quotient rule together with domain control.

---

### Solution

**Step 1: Determine the domain of $f(x)$**

The denominator of the rational function cannot be zero:

$$
x - 1 \neq 0 \implies x \neq 1
$$

In interval notation, the domain is:

$$
D_f = (-\infty, 1) \cup (1, \infty) = \mathbb{R} \setminus \{1\}
$$

---

**Step 2: Identify numerator and denominator and their derivatives**

Let $f(x) = \frac{u(x)}{v(x)}$:
* Numerator: $u(x) = x^2 + 1 \implies u'(x) = 2x$
* Denominator: $v(x) = x - 1 \implies v'(x) = 1$

---

**Step 3: Apply the quotient rule**

Substitute $u, u', v, v'$ into the quotient rule formula:

$$
f'(x) = \frac{u'(x) v(x) - u(x) v'(x)}{[v(x)]^2}
$$

$$
f'(x) = \frac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2}
$$

---

**Step 4: Expand and simplify the numerator**

Expand the terms in the numerator:

$$
(2x)(x - 1) - (x^2 + 1) = 2x^2 - 2x - x^2 - 1 = x^2 - 2x - 1
$$

Thus, the simplified derivative is:

$$
f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2}
$$

Alternatively, by rewriting $x^2 - 2x - 1 = (x - 1)^2 - 2$:

$$
f'(x) = \frac{(x - 1)^2 - 2}{(x - 1)^2} = 1 - \frac{2}{(x - 1)^2}
$$

---

**Step 5: Why the restriction $x \neq 1$ remains important**

1. **Existence and Differentiability:**
   A derivative at a point measures the limit of the difference quotient. If a function is undefined at $x = 1$, it cannot be continuous there, and therefore cannot be differentiable at $x = 1$. The denominator $(x - 1)^2$ explicitly becomes zero at $x = 1$.
2. **Domain Partitioning:**
   The point $x = 1$ is a vertical asymptote of both $f(x)$ and $f'(x)$. It partitions the domain into two independent, disconnected components: $(-\infty, 1)$ and $(1, \infty)$.
3. **Monotonicity and Mean Value Theorem:**
   The Mean Value Theorem and conclusions about monotonicity from the sign of $f'(x)$ apply only to connected subintervals. Ignoring $x \neq 1$ can lead to false global claims that violate the discontinuous split across the asymptote.

---

### Final Answer

1. **Domain:**

   $$
   D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)
   $$

2. **Derivative:**

   $$
   f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2}
   $$

3. **Importance of $x \neq 1$:**
   The point $x = 1$ is an essential singularity (vertical asymptote) where neither $f$ nor $f'$ exists. The restriction $x \neq 1$ ensures that the domain is properly partitioned into two disjoint open intervals, preventing erroneous applications of calculus theorems across the singularity.

