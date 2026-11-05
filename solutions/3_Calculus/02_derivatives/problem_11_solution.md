### Essential Formulas

1. **Definition of the Derivative as a Limit:**
   For a function $f(x)$ defined in a neighborhood of $x$, the derivative is defined as:

   $$
   f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
   $$

   provided this limit exists.

2. **Binomial Expansion for Quadratic Terms:**

   $$
   (x + h)^2 = x^2 + 2xh + h^2
   $$

3. **Power Rule:**
   For $f(x) = x^n$ with $n = 2$:

   $$
   \frac{d}{dx}[x^2] = 2 x^{2-1} = 2x
   $$

---

### Problem Statement

Using only

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,
$$

find the derivative of $f(x)=x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

> **Why this problem:** it shows the origin of the power rule and the direct connection between the derivative and a limit.

---

### Solution

**Step 1: Form the difference quotient**

For the function $f(x) = x^2$, evaluate $f(x + h)$:

$$
f(x + h) = (x + h)^2 = x^2 + 2xh + h^2
$$

Formulate the numerator of the difference quotient:

$$
f(x + h) - f(x) = (x^2 + 2xh + h^2) - x^2 = 2xh + h^2
$$

Write the full difference quotient for $h \neq 0$:

$$
\frac{f(x + h) - f(x)}{h} = \frac{2xh + h^2}{h}
$$

---

**Step 2: Simplify algebraically by canceling $h$**

Direct substitution of $h = 0$ yields the indeterminate form $\frac{0}{0}$.
Factor $h$ out of the numerator:

$$
\frac{2xh + h^2}{h} = \frac{h(2x + h)}{h}
$$

Because the limit examines values where $h \to 0$ with $h \neq 0$, cancel the common factor $h$:

$$
= 2x + h \qquad (h \neq 0)
$$

This algebraic cancellation resolves the indeterminacy.

---

**Step 3: Evaluate the limit as $h \to 0$**

Apply the limit process to the simplified expression:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{h \to 0} (2x + h)
$$

Because the polynomial $2x + h$ is continuous with respect to $h$, evaluate the limit by setting $h = 0$:

$$
f'(x) = 2x + 0 = 2x
$$

---

**Step 4: Comparison with the power rule**

The general power rule states:

$$
\frac{d}{dx}[x^n] = n x^{n-1}
$$

For $n = 2$:

$$
\frac{d}{dx}[x^2] = 2 x^{2-1} = 2x
$$

The result obtained from first principles matches the power rule.

---

**Step 5: Identify precisely where the limit is used**

1. **Before the limit:**
   The steps expanding $(x+h)^2$ and canceling $h$ are purely static algebraic transformations valid for any non-zero increment $h \neq 0$. The expression $\frac{f(x+h)-f(x)}{h} = 2x + h$ represents the *average rate of change* (the secant line slope) over an interval of length $h$.
2. **At the limit:**
   The limit operation $\lim_{h \to 0}$ transforms the secant slope into the *instantaneous rate of change* (the tangent line slope). It allows us to let the increment $h$ vanish completely ($2x + h \to 2x$) without dividing by zero, rigorously establishing that $f'(x) = 2x$.

---

### Final Answer

1. **Limit Computation:**

   $$
   f'(x) = \lim_{h\to0} \frac{(x+h)^2 - x^2}{h} = \lim_{h\to0} \frac{h(2x + h)}{h} = \lim_{h\to0} (2x + h) = 2x
   $$

2. **Comparison:**
   The first-principles derivation yields $2x$, confirming the power rule $\frac{d}{dx}[x^2] = 2x^{2-1} = 2x$.

3. **Where the Limit is Used:**
   The limit is invoked in the final transition from the secant slope $2x + h$ to the instantaneous slope $2x$, eliminating the increment $h$ after the $0/0$ singularity has been canceled.
