### Essential Formulas

1. **Bounding Property of Definite Integrals (Comparison Theorem):**
   If a continuous function $f(x)$ satisfies $m \le f(x) \le M$ for all $x \in [a, b]$, then:

   $$
   m(b - a) \le \int_a^b f(x) \, dx \le M(b - a)
   $$

2. **Fundamental Theorem of Calculus:**
   For a continuous function $f(x)$ with antiderivative $F(x)$:

   $$
   \int_a^b f(x) \, dx = F(b) - F(a)
   $$

3. **Power Rule for Definite Integrals:**

   $$
   \int_a^b x^n \, dx = \left[ \frac{x^{n+1}}{n+1} \right]_a^b
   $$

---

### Problem Statement

Before carrying out the exact calculation, estimate the possible range of values of the integral

$$
\int_0^2(x^2+1)\,dx,
$$

using

$$
1\le x^2+1\le5
$$

on $[0,2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

> **Why this problem:** it teaches how to predict the possible range of a result and check the calculation.

---

### Solution

**Step 1: Estimate the possible range of the integral**

The integration interval is $[a, b] = [0, 2]$, so the interval length is:

$$
b - a = 2 - 0 = 2
$$

We are given that on $[0, 2]$, the integrand satisfies:

$$
1 \le x^2 + 1 \le 5
$$

* The absolute minimum value on $[0, 2]$ is $m = 1$ (attained at $x = 0$).
* The absolute maximum value on $[0, 2]$ is $M = 5$ (attained at $x = 2$).

Apply the bounding property of integrals:

$$
m(b - a) \le \int_0^2 (x^2 + 1) \, dx \le M(b - a)
$$

Substitute $m = 1$, $M = 5$, and $b - a = 2$:

$$
1 \cdot (2 - 0) \le \int_0^2 (x^2 + 1) \, dx \le 5 \cdot (2 - 0)
$$

$$
2 \le \int_0^2 (x^2 + 1) \, dx \le 10
$$

The integral must strictly lie within the interval $[2, 10]$.

---

**Step 2: Compute the integral exactly**

Find the general antiderivative of $f(x) = x^2 + 1$:

$$
F(x) = \frac{x^3}{3} + x
$$

Apply the Fundamental Theorem of Calculus from $x = 0$ to $x = 2$:

$$
\int_0^2 (x^2 + 1) \, dx = \left[ \frac{x^3}{3} + x \right]_0^2
$$

Evaluate at the upper limit $x = 2$:

$$
F(2) = \frac{2^3}{3} + 2 = \frac{8}{3} + 2 = \frac{8 + 6}{3} = \frac{14}{3}
$$

Evaluate at the lower limit $x = 0$:

$$
F(0) = \frac{0^3}{3} + 0 = 0
$$

Subtract the lower limit evaluation:

$$
\int_0^2 (x^2 + 1) \, dx = \frac{14}{3} - 0 = \frac{14}{3} = 4\frac{2}{3} \approx 4.6667
$$

---

**Step 3: Compare the exact result with the estimate**

We compare the exact result with our predicted bounds:

$$
2 \le \frac{14}{3} \approx 4.6667 \le 10
$$

The exact value $\frac{14}{3} \approx 4.67$ falls comfortably within the range $[2, 10]$, situated close to the middle of the bounding box.

---

**Step 4: Explain what computational errors this check can detect**

An a priori geometric estimate establishes an envelope that catches several major classes of errors:
1. **Sign and Inversion Errors:**
   If a student accidentally subtracted terms (obtaining a negative number or a value $< 2$), the lower bound $2$ immediately reveals the mistake. Since $x^2 + 1 \ge 1 > 0$, the integral cannot be negative or smaller than $2$.
2. **Gross Miscalculations and Wrong Rules:**
   If a student accidentally differentiated instead of integrating (evaluating $[2x]_0^2 = 4 - 0 = 4$ without the polynomial power), or incorrectly computed the power as $x^4/4$ (yielding $2^4/4 + 2 = 6$), checking against tighter sub-bounds exposes structural formula errors.
3. **Boundary Slip Errors:**
   If the student forgot to substitute the upper limit $2$ properly, or divided by the wrong constant (e.g. $[x^3 + x]_0^2 = 8 + 2 = 10$), the proximity to the extreme upper bound alerts the student that the calculation corresponds to assuming the function stays at its maximum $5$ everywhere.

---

### Final Answer

1. **A Priori Estimate:**

   $$
   2 \le \int_0^2(x^2+1)\,dx \le 10
   $$

2. **Exact Calculation:**

   $$
   \int_0^2(x^2+1)\,dx = \frac{14}{3} = 4\frac{2}{3} \approx 4.6667
   $$

3. **Comparison:**
   $2 \le 4.6667 \le 10$, confirming that the exact value lies comfortably within the predicted range.

4. **Errors Detected by the Check:**
   The check detects sign errors (negative results), wrong operations (such as differentiation instead of integration), incorrect exponent rules, or misapplied limits of integration.

