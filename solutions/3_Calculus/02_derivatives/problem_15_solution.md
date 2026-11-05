### Essential Formulas

1. **Definition of the Derivative via Difference Quotient:**
   The derivative at $x_0$ is the limit of the difference quotient (the secant line slope) as the step size $h$ approaches zero:

   $$
   f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
   $$

2. **Secant Slope vs. Tangent Slope:**
   * **Secant slope:** $\frac{f(x_0 + h) - f(x_0)}{h}$ represents the average rate of change over $[x_0, x_0 + h]$.
   * **Tangent slope:** $f'(x_0)$ represents the instantaneous rate of change at $x_0$.

3. **Error of the Finite Difference Approximation:**
   By Taylor's theorem, for smooth functions:

   $$
   \frac{f(x_0 + h) - f(x_0)}{h} = f'(x_0) + \frac{1}{2} f''(x_0) h + \mathcal{O}(h^2)
   $$

---

### Problem Statement

Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate

$$
\frac{f(x_0+h)-f(x_0)}h
$$

for $h=1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

> **Why this problem:** it connects the definition of the derivative with concrete calculations and teaches the distinction between observation and proof.

---

### Solution

**Step 1: Choose the function and evaluate the exact derivative**

We choose the polynomial from Problem 10:

$$
f(x) = x^2 - 3x + 1, \qquad x_0 = 2
$$

1. Compute the exact function value at $x_0 = 2$:

   $$
   f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1
   $$

2. Compute the exact derivative using differentiation rules:

   $$
   f'(x) = 2x - 3
   $$

3. Evaluate at $x_0 = 2$:

   $$
   f'(2) = 2(2) - 3 = 1
   $$

The exact instantaneous slope is $f'(2) = 1$.

---

**Step 2: Express the difference quotient algebraically**

Evaluate $f(2 + h)$:

$$
f(2 + h) = (2 + h)^2 - 3(2 + h) + 1 = (4 + 4h + h^2) - (6 + 3h) + 1 = h^2 + h - 1
$$

Form the difference quotient for $h \neq 0$:

$$
\frac{f(2 + h) - f(2)}{h} = \frac{(h^2 + h - 1) - (-1)}{h} = \frac{h^2 + h}{h} = \frac{h(h + 1)}{h} = 1 + h
$$

---

**Step 3: Calculate the difference quotient for the specified values of $h$**

Substitute each value of $h$ into the simplified quotient $1 + h$:

1. **For $h = 1$:**

   $$
   \frac{f(2 + 1) - f(2)}{1} = 1 + 1 = 2.0
   $$

   (Secant line connecting $(2, -1)$ and $(3, 1)$ has slope $2.0$).

2. **For $h = 0.1$:**

   $$
   \frac{f(2 + 0.1) - f(2)}{0.1} = 1 + 0.1 = 1.1
   $$

   (Secant line connecting $(2, -1)$ and $(2.1, -0.89)$ has slope $1.1$).

3. **For $h = 0.01$:**

   $$
   \frac{f(2 + 0.01) - f(2)}{0.01} = 1 + 0.01 = 1.01
   $$

   (Secant line connecting $(2, -1)$ and $(2.01, -0.9899)$ has slope $1.01$).

---

**Step 4: Comparison with the exact derivative**

* For $h = 1.0$: value is $2.0$ (error $= 1.0$)
* For $h = 0.1$: value is $1.1$ (error $= 0.1$)
* For $h = 0.01$: value is $1.01$ (error $= 0.01$)
* Exact derivative: $f'(2) = 1.0$

As $h$ decreases by successive factors of $10$, the difference quotient systematically approaches the exact value $1.0$, with the error shrinking in exact proportion to $h$.

---

**Step 5: Consistency with definition and why computations do not replace proof**

1. **Consistency with the Definition:**
   The definition $f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h)-f(x_0)}{h}$ states that the secant slopes must converge to the tangent slope as the interval collapses. The observed numerical values $2.0 \to 1.1 \to 1.01$ provide direct empirical evidence of this convergence.
2. **Why Finite Computations do not Replace a Limit Argument:**
   * **Incompleteness:** A finite table tests only three specific positive values ($h = 1, 0.1, 0.01$). It provides no information about negative increments ($h \to 0^-$) or about the continuum of values in between.
   * **Pathological Counterexamples:** Functions such as $g(x) = x^2 \sin(1/x)$ or piecewise functions with rapid microscopic oscillations can appear stable at coarse increments while oscillating wildly at smaller scales.
   * **The Standard of Proof:** A deductive mathematical proof must establish that for *every* $\varepsilon > 0$, there exists a $\delta > 0$ such that all $0 < |h| < \delta$ satisfy the error bound. Only algebraic cancellation of the $0/0$ form proves convergence universally.

---

### Final Answer

1. **Exact Derivative:**

   $$
   f'(2) = 1
   $$

2. **Calculated Difference Quotients:**
   * $h = 1 \implies 2.0$
   * $h = 0.1 \implies 1.1$
   * $h = 0.01 \implies 1.01$

3. **Methodological Conclusion:**
   The numerical progression $2.0 \to 1.1 \to 1.01$ reflects the secant lines converging geometrically to the tangent slope of $1$. However, empirical sampling can never replace an analytical limit proof, which proves that the difference quotient approaches $1$ across the entire continuum as $h \to 0$.

