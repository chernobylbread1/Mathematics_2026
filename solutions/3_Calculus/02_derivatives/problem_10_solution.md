### Essential Formulas

1. **Equation of the Tangent Line (Point-Slope Form):**
   The equation of the tangent line to the differentiable curve $y = f(x)$ at the point $(x_0, f(x_0))$ is:

   $$
   y - f(x_0) = f'(x_0)(x - x_0)
   $$

   or in slope-intercept form:

   $$
   y = m x + b, \qquad m = f'(x_0)
   $$

2. **Power Rule for Polynomials:**

   $$
   \frac{d}{dx}[x^2 - 3x + 1] = 2x - 3
   $$

---

### Problem Statement

For

$$
f(x)=x^2-3x+1
$$

find the equation of the tangent line at the point with $x=2$. Give the point of tangency, the value $f'(2)$, the equation of the line, and verify that the point lies on the obtained tangent line.

> **Why this problem:** it combines the derivative and the equation of a line into a complete geometric problem.

---

### Solution

**Step 1: Find the point of tangency**

The given $x$-coordinate is $x_0 = 2$.
Compute the corresponding $y$-coordinate by evaluating $f(2)$:

$$
f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1
$$

Thus, the point of tangency is:

$$
P_0 = (2, -1)
$$

---

**Step 2: Compute the derivative and evaluate the slope $f'(2)$**

Differentiate the quadratic polynomial:

$$
f'(x) = \frac{d}{dx}[x^2 - 3x + 1] = 2x - 3
$$

Evaluate the derivative at $x = 2$ to determine the slope $m$:

$$
m = f'(2) = 2(2) - 3 = 4 - 3 = 1
$$

The slope of the tangent line is $m = 1$.

---

**Step 3: Determine the equation of the tangent line**

Using the point-slope formula with $x_0 = 2$, $y_0 = -1$, and $m = 1$:

$$
y - y_0 = m(x - x_0)
$$

Substitute the values:

$$
y - (-1) = 1(x - 2)
$$

$$
y + 1 = x - 2
$$

Subtract $1$ from both sides to obtain the slope-intercept form:

$$
y = x - 3
$$

In general linear form:

$$
x - y - 3 = 0
$$

---

**Step 4: Verify that the point of tangency lies on the tangent line**

Substitute the coordinates of the point of tangency $(x_0, y_0) = (2, -1)$ into the tangent line equation $y = x - 3$:

* Left-hand side:

  $$
  y = -1
  $$

* Right-hand side:

  $$
  x - 3 = 2 - 3 = -1
  $$

Since both sides are equal ($-1 = -1$), the point of tangency $P_0(2, -1)$ lies on the tangent line.

---

### Final Answer

1. **Point of Tangency:**

   $$
   (x_0, y_0) = (2, -1)
   $$

2. **Derivative Value (Slope):**

   $$
   f'(2) = 1
   $$

3. **Equation of the Tangent Line:**

   $$
   y = x - 3 \qquad (x - y - 3 = 0)
   $$

4. **Verification:**
   Substituting $x = 2$ yields $y = 2 - 3 = -1$, confirming that $(2, -1)$ satisfies the equation of the tangent line.
