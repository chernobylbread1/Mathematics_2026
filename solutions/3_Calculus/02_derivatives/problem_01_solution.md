### Essential Formulas

1. **Power Rule for Differentiation:**
   For any constant real exponent $n \in \mathbb{R}$:

   $$
   \frac{d}{dx}[x^n] = n x^{n-1}
   $$

2. **Linearity of the Derivative:**
   For differentiable functions $u(x), v(x)$ and constants $a, b \in \mathbb{R}$:

   $$
   \frac{d}{dx}[a u(x) + b v(x)] = a u'(x) + b v'(x)
   $$

3. **Geometric Interpretation of the Derivative:**
   The value of the derivative $f'(x_0)$ equals the slope $m$ of the tangent line to the graph of $y = f(x)$ at the point $(x_0, f(x_0))$:

   $$
   m = f'(x_0)
   $$

   * If $f'(x_0) > 0$, the tangent line has positive slope (slopes upward from left to right), and the function is strictly increasing locally.
   * If $f'(x_0) < 0$, the tangent line has negative slope (slopes downward from left to right), and the function is strictly decreasing locally.
   * If $f'(x_0) = 0$, the tangent line is horizontal.

---

### Problem Statement

For

$$
f(x)=3x^5-2x^3+7x-4
$$

find $f'(x)$. Then compute $f'(0)$ and $f'(1)$, determine the signs of the obtained values, and explain what they say about the slope of the tangent line to the graph at these two points.

> **Why this problem:** it reinforces the power rule and connects the value of the derivative at a point with the geometric meaning of the tangent slope.

---

### Solution

**Step 1: Compute the derivative $f'(x)$**

Differentiate the polynomial term by term using the linearity property and the power rule:

$$
f(x) = 3x^5 - 2x^3 + 7x - 4
$$

Differentiating each monomial:
* $\frac{d}{dx}[3x^5] = 3 \cdot 5x^4 = 15x^4$
* $\frac{d}{dx}[-2x^3] = -2 \cdot 3x^2 = -6x^2$
* $\frac{d}{dx}[7x] = 7 \cdot 1 = 7$
* $\frac{d}{dx}[-4] = 0$

Combining the terms gives:

$$
f'(x) = 15x^4 - 6x^2 + 7
$$

---

**Step 2: Compute $f'(0)$ and interpret its geometric meaning**

Evaluate the derivative at $x = 0$:

$$
f'(0) = 15(0)^4 - 6(0)^2 + 7 = 0 - 0 + 7 = 7
$$

* **Sign:** $f'(0) = 7 > 0$.
* **Geometric Interpretation:** At the point $(0, f(0)) = (0, -4)$, the tangent line has a positive slope of $m = 7$. The graph is rising steeply from left to right at this intercept.

---

**Step 3: Compute $f'(1)$ and interpret its geometric meaning**

Evaluate the derivative at $x = 1$:

$$
f'(1) = 15(1)^4 - 6(1)^2 + 7 = 15 - 6 + 7 = 16
$$

* **Sign:** $f'(1) = 16 > 0$.
* **Geometric Interpretation:** At the point $(1, f(1)) = (1, 4)$, the tangent line has a positive slope of $m = 16$. The curve is rising even more steeply at $x = 1$ than at $x = 0$ (slope $16$ compared to $7$).

---

### Final Answer

1. **General Derivative:**

   $$
   f'(x) = 15x^4 - 6x^2 + 7
   $$

2. **Evaluations and Signs:**
   * $f'(0) = 7 > 0$ (positive)
   * $f'(1) = 16 > 0$ (positive)

3. **Geometric Interpretation:**
   At both $x = 0$ and $x = 1$, the tangent lines have positive slopes ($m = 7$ and $m = 16$, respectively), meaning the graph is strictly increasing in the neighborhood of both points, with greater steepness at $x = 1$.

