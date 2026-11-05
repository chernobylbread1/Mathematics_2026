### Essential Formulas

1. **Stationary Condition for Local Extrema:**
   For a differentiable function $f(x)$, a necessary condition for a local extremum at an interior point $x_0$ is:

   $$
   f'(x_0) = 0
   $$

2. **Second Derivative Test:**
   * If $f'(x_0) = 0$ and $f''(x_0) > 0$, then $f(x)$ has a strict local minimum at $x_0$.
   * If $f'(x_0) = 0$ and $f''(x_0) < 0$, then $f(x)$ has a strict local maximum at $x_0$.

3. **Vertex Form of a Quadratic Polynomial:**
   Every quadratic polynomial $f(x) = a x^2 + b x + c$ ($a \neq 0$) can be rewritten by completing the square as:

   $$
   f(x) = a(x - x_v)^2 + y_v
   $$

   where $(x_v, y_v)$ is the vertex coordinates:

   $$
   x_v = -\frac{b}{2a}, \qquad y_v = f(x_v)
   $$

---

### Problem Statement

For $f(x)=x^2-4x+1$, find the minimum using the derivative. Compare the result with the vertex form and explain why both approaches lead to the same point.

> **Why this problem:** it connects a new tool with the familiar geometry of a parabola.

---

### Solution

**Step 1: Find the minimum using the derivative**

1. Compute the first derivative using the power rule:

   $$
   f'(x) = \frac{d}{dx}[x^2 - 4x + 1] = 2x - 4
   $$

2. Set the first derivative to zero to find the critical point:

   $$
   2x - 4 = 0 \implies 2x = 4 \implies x = 2
   $$

3. Compute the second derivative to confirm the nature of the extremum:

   $$
   f''(x) = \frac{d}{dx}[2x - 4] = 2
   $$

   Since $f''(2) = 2 > 0$, the function is strictly convex (concave upward) everywhere, and $x = 2$ is a strict global minimum.

4. Evaluate the minimum function value:

   $$
   f(2) = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3
   $$

   The minimum point on the graph is $(2, -3)$.

---

**Step 2: Find the minimum using the vertex form (completing the square)**

Complete the square for the quadratic expression $x^2 - 4x + 1$:

$$
f(x) = (x^2 - 4x + 4) - 4 + 1
$$

Recognize the binomial square $(x - 2)^2$:

$$
f(x) = (x - 2)^2 - 3
$$

Since the square of any real number is non-negative:

$$
(x - 2)^2 \ge 0 \quad \forall x \in \mathbb{R}
$$

with equality if and only if $x = 2$.
Therefore, subtracting $3$:

$$
f(x) = (x - 2)^2 - 3 \ge -3
$$

The minimum value is $-3$, and it occurs at $x = 2$. The vertex of the parabola is:

$$
V = (2, -3)
$$

---

**Step 3: Comparison and explanation of why both approaches agree**

1. **Geometric Connection:**
   The graph of $y = x^2 - 4x + 1$ is an upward-opening parabola with an axis of symmetry at $x = 2$. As a smooth curve, its lowest point (the vertex) is the turning point where the slope changes from negative to positive. At this exact turning point, the tangent line must be horizontal:

   $$
   f'(x) = 0
   $$

2. **Algebraic vs. Analytical Foundations:**
   * **Algebraic Approach (Vertex Form):** Uses the algebraic property that the square of a real number is non-negative ($(x - x_v)^2 \ge 0$), identifying the minimum by setting the square term to its absolute lower bound zero.
   * **Calculus Approach (Derivative):** Uses the concept of rates of change, identifying the minimum as the point where the instantaneous rate of change vanishes ($f'(x) = 2x - 4 = 0 \iff x = 2$).
3. **Equivalence:**
   Differentiating the vertex form $f(x) = a(x - x_v)^2 + y_v$ gives:

   $$
   f'(x) = 2a(x - x_v)
   $$

   Setting $f'(x) = 0$ yields $x = x_v = -\frac{b}{2a}$. Thus, the stationary point of calculus is identical to the geometric vertex of elementary algebra.

---

### Final Answer

1. **Calculus Method:**
   * Derivative: $f'(x) = 2x - 4 = 0 \implies x = 2$
   * Second Derivative: $f''(2) = 2 > 0$ (strict global minimum)
   * Minimum Point: $(2, -3)$

2. **Vertex Form Method:**
   * Completed Square: $f(x) = (x - 2)^2 - 3$
   * Vertex: $V(2, -3)$

3. **Why Both Approaches Agree:**
   The vertex of an upward-opening parabola is its unique lowest geometric point. Because the parabola is smooth, this turning point corresponds precisely to the unique location where the tangent line is horizontal ($f'(x) = 0$).

