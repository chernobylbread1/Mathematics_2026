### Essential Formulas

1. **Sign of a Quadratic Expression:**
   For a quadratic polynomial $q(x) = a x^2 + b x + c = a(x - r_1)(x - r_2)$ with $r_1 < r_2$:
   * If the leading coefficient is positive ($a > 0$), the parabola opens upward:

     $$
     q(x) < 0 \quad \forall x \in (r_1, r_2)
     $$

     $$
     q(x) > 0 \quad \forall x \in (-\infty, r_1) \cup (r_2, \infty)
     $$

   * If $a < 0$, the signs are inverted.

2. **First Derivative Test:**
   * Transition from $+ \to - \implies$ local maximum.
   * Transition from $- \to + \implies$ local minimum.

---

### Problem Statement

For the function

$$
f(x)=x^3-3x
$$

the derivative was correctly computed as

$$
f'(x)=3(x-1)(x+1).
$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty,-1)\cup(1,\infty)$, increasing on $(-1,1)$, has a local minimum at $x=-1$, and a local maximum at $x=1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

> **Why this problem:** it teaches how to diagnose an error in a completed argument and shows that a correct derivative formula is not enough if its sign is interpreted incorrectly.

---

### Solution

**Step 1: Diagnose the error in the student's reasoning**

1. **Why finding zeros alone is insufficient:**
   Setting $f'(x) = 0$ identifies only the boundary points $x = -1$ and $x = 1$ where the sign *could* change. Finding where an expression equals zero provides zero information about which intervals are positive and which are negative; that requires testing points or analyzing the leading coefficient.
2. **The Specific Error:**
   The student asserted that the quadratic is positive between the zeros and negative outside them.
   Expanding the derivative:

   $$
   f'(x) = 3(x^2 - 1) = 3x^2 - 3
   $$

   The leading coefficient is $a = 3 > 0$. The graph of $y = f'(x)$ is a parabola that opens upward. Therefore, the parabola sinks **below** the $x$-axis between its roots (where $x^2 < 1$), making $f'(x) < 0$ on $(-1, 1)$, and rises **above** the $x$-axis outside its roots (where $x^2 > 1$), making $f'(x) > 0$ on $(-\infty, -1) \cup (1, \infty)$.
   The student inverted the sign chart completely, which cascaded into inverted monotonicity intervals and backwards classifications of the local extrema.

---

**Step 2: Construct the correct sign chart for $f'(x)$**

The boundary roots are $x = -1$ and $x = 1$:
* **On $(-\infty, -1)$:** $(x - 1) < 0$ and $(x + 1) < 0 \implies f'(x) = 3(-)(-) > 0$ (positive).
* **At $x = -1$:** $f'(-1) = 0$.
* **On $(-1, 1)$:** $(x - 1) < 0$ and $(x + 1) > 0 \implies f'(x) = 3(-)(+) < 0$ (negative).
* **At $x = 1$:** $f'(1) = 0$.
* **On $(1, \infty)$:** $(x - 1) > 0$ and $(x + 1) > 0 \implies f'(x) = 3(+)(+) > 0$ (positive).

---

**Step 3: Correct intervals of monotonicity and character of extrema**

1. **Monotonicity:**
   * The function $f(x)$ is **strictly increasing** on $(-\infty, -1]$ and on $[1, \infty)$.
   * The function $f(x)$ is **strictly decreasing** on $[-1, 1]$.

2. **Classification of Extrema:**
   * **At $x = -1$:** The derivative changes sign from positive to negative ($+ \to -$).
     Therefore, $x = -1$ is a **local maximum**.
     Function value:

     $$
     f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2
     $$

     Local maximum point: $(-1, 2)$.

   * **At $x = 1$:** The derivative changes sign from negative to positive ($- \to +$).
     Therefore, $x = 1$ is a **local minimum**.
     Function value:

     $$
     f(1) = 1^3 - 3(1) = 1 - 3 = -2
     $$

     Local minimum point: $(1, -2)$.

---

**Step 4: Verify with test points in each interval**

Evaluate $f'(x) = 3(x - 1)(x + 1)$ at one simple test value in each interval:
1. **Interval $(-\infty, -1)$:** Choose test point $x = -2$:

   $$
   f'(-2) = 3(-2 - 1)(-2 + 1) = 3(-3)(-1) = 9 > 0
   $$

   The positive sign confirms that $f$ is strictly increasing on $(-\infty, -1]$.

2. **Interval $(-1, 1)$:** Choose test point $x = 0$:

   $$
   f'(0) = 3(0 - 1)(0 + 1) = 3(-1)(1) = -3 < 0
   $$

   The negative sign confirms that $f$ is strictly decreasing on $[-1, 1]$.

3. **Interval $(1, \infty)$:** Choose test point $x = 2$:

   $$
   f'(2) = 3(2 - 1)(2 + 1) = 3(1)(3) = 9 > 0
   $$

   The positive sign confirms that $f$ is strictly increasing on $[1, \infty)$.

---

### Final Answer

1. **Diagnosis of the Error:**
   Zeros of a derivative indicate only where the sign may change, not what the sign is. The student incorrectly inverted the sign of the upward-opening parabola $f'(x) = 3(x^2 - 1)$, assuming it was positive inside and negative outside, which reversed all subsequent conclusions.

2. **Correct Sign Chart:**
   * $(-\infty, -1) \implies f'(x) > 0$
   * $(-1, 1) \implies f'(x) < 0$
   * $(1, \infty) \implies f'(x) > 0$

3. **Monotonicity and Extrema:**
   * Strictly increasing on $(-\infty, -1]$ and on $[1, \infty)$
   * Strictly decreasing on $[-1, 1]$
   * Local Maximum at $(-1, 2)$
   * Local Minimum at $(1, -2)$

4. **Test Point Confirmations:**
   * $x = -2 \implies f'(-2) = 9 > 0$
   * $x = 0 \implies f'(0) = -3 < 0$
   * $x = 2 \implies f'(2) = 9 > 0$
