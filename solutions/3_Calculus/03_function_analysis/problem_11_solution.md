### Essential Formulas

1. **Derivative of a Parametric Cubic Polynomial:**
   For $f_a(x) = x^3 - 3ax$:

   $$
   f'_a(x) = 3x^2 - 3a = 3(x^2 - a)
   $$

2. **Classification of Critical Points via First and Second Derivatives:**
   * Critical points occur where $f'_a(x) = 0$.
   * $f''_a(x) = 6x$.
   * A critical point $x_0$ with $f''_a(x_0) > 0$ is a strict local minimum.
   * A critical point $x_0$ with $f''_a(x_0) < 0$ is a strict local maximum.
   * A critical point $x_0$ where $f'_a(x)$ does not change sign is a stationary inflection point (no extremum).

---

### Problem Statement

For

$$
f_a(x)=x^3-3ax
$$

depending on $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

> **Why this problem:** it teaches how to analyze an entire family of functions instead of a single example.

---

### Solution

**Step 1: Compute the derivative and set up the critical point equation**

Differentiate the polynomial with respect to $x$:

$$
f'_a(x) = 3x^2 - 3a = 3(x^2 - a)
$$

Set $f'_a(x) = 0$:

$$
3(x^2 - a) = 0 \iff x^2 = a
$$

The number of real solutions to $x^2 = a$ depends entirely on the sign of the real parameter $a$.

---

**Step 2: Case 1 — Parameter $a > 0$ (Two critical points)**

When $a > 0$, the equation $x^2 = a$ has two distinct real roots:

$$
x_1 = -\sqrt{a}, \qquad x_2 = \sqrt{a}
$$

Compute the second derivative $f''_a(x) = 6x$:
1. **At $x = -\sqrt{a}$:**

   $$
   f''_a(-\sqrt{a}) = -6\sqrt{a} < 0
   $$

   The derivative changes from positive to negative.
   Thus, $x = -\sqrt{a}$ is a **strict local maximum**.
   Function value:

   $$
   f_a(-\sqrt{a}) = (-\sqrt{a})^3 - 3a(-\sqrt{a}) = -a\sqrt{a} + 3a\sqrt{a} = 2a\sqrt{a}
   $$

2. **At $x = \sqrt{a}$:**

   $$
   f''_a(\sqrt{a}) = 6\sqrt{a} > 0
   $$

   The derivative changes from negative to positive.
   Thus, $x = \sqrt{a}$ is a **strict local minimum**.
   Function value:

   $$
   f_a(\sqrt{a}) = (\sqrt{a})^3 - 3a(\sqrt{a}) = a\sqrt{a} - 3a\sqrt{a} = -2a\sqrt{a}
   $$

* **Monotonicity:** Increasing on $(-\infty, -\sqrt{a}]$, decreasing on $[-\sqrt{a}, \sqrt{a}]$, and increasing on $[\sqrt{a}, \infty)$.

---

**Step 3: Case 2 — Parameter $a = 0$ (One critical point, no extremum)**

When $a = 0$, the function reduces to $f_0(x) = x^3$.
The derivative is:

$$
f'_0(x) = 3x^2
$$

Setting $f'_0(x) = 0$ gives a single real solution of multiplicity $2$:

$$
x = 0
$$

Analyze the sign of $f'_0(x)$:
* For $x \neq 0$, $3x^2 > 0$.
* The derivative is strictly positive for all $x \neq 0$ and vanishes only at the isolated point $x = 0$.

Because $f'_0(x)$ does not change sign across $x = 0$, the function is strictly increasing on the entire real line $\mathbb{R}$.
The origin $(0, 0)$ is a **stationary inflection point** (a horizontal terrace/saddle point), not an extremum.

---

**Step 4: Case 3 — Parameter $a < 0$ (No critical points)**

When $a < 0$, let $a = -k$ with $k > 0$. The equation becomes:

$$
x^2 = -k < 0
$$

This equation has no real solutions.
Furthermore:

$$
f'_a(x) = 3(x^2 - a) = 3(x^2 + k) \ge 3k > 0 \quad \forall x \in \mathbb{R}
$$

The derivative is strictly positive everywhere. The function has **zero critical points** and is strictly increasing on $(-\infty, \infty)$ with no horizontal tangents.

---

**Step 5: Why the geometric structure of the graph changes**

1. **Bifurcation of Critical Points:**
   As the parameter $a$ decreases from positive values toward zero, the distance between the two extrema $2\sqrt{a}$ shrinks.
2. **Coalescence at the Critical Threshold ($a = 0$):**
   At $a = 0$, the local maximum and local minimum collide at the origin, merging into a single stationary point of inflection with a horizontal tangent.
3. **Disappearance into the Complex Plane ($a < 0$):**
   For $a < 0$, the roots of the derivative become imaginary ($\pm i\sqrt{|a|}$), leaving the real graph strictly monotonic without any stationary points.

---

### Final Answer

1. **Case $a > 0$:**
   * **Number of Critical Points:** $2$
   * **Character:**
     * Strict local maximum at $(-\sqrt{a}, 2a\sqrt{a})$
     * Strict local minimum at $(\sqrt{a}, -2a\sqrt{a})$

2. **Case $a = 0$:**
   * **Number of Critical Points:** $1$
   * **Character:** Stationary inflection point at $(0, 0)$ (no local extremum; function is strictly increasing)

3. **Case $a < 0$:**
   * **Number of Critical Points:** $0$
   * **Character:** No critical points and no extrema (derivative is strictly positive everywhere; function is strictly increasing)

4. **Geometric Transition:**
   As $a$ decreases through $0$, the pair of local extrema merge at $(0, 0)$ at $a = 0$ and vanish for $a < 0$, straightening the cubic wave into a monotonic curve.
