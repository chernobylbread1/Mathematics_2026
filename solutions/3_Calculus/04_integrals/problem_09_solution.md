### Essential Formulas

1. **Fundamental Theorem of Calculus (Evaluation Part):**
   If $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$, then:

   $$
   \int_a^b f(x) \, dx = [F(x)]_a^b = F(b) - F(a)
   $$

2. **Net Signed Area vs. Geometric Area:**
   * **Definite Integral (Net Signed Area):** Regions where $f(x) \ge 0$ contribute positively, and regions where $f(x) \le 0$ contribute negatively:

     $$
     \int_a^b f(x) \, dx = A_{\mathrm{above}} - A_{\mathrm{below}}
     $$

   * **Total Geometric Area:** Enclosed area is strictly positive, integrating the absolute value:

     $$
     A_{\mathrm{geom}} = \int_a^b |f(x)| \, dx = A_{\mathrm{above}} + A_{\mathrm{below}}
     $$

---

### Problem Statement

Compute

$$
\int_{-1}^{2}x\,dx.
$$

Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

> **Why this problem:** it clarifies the difference between signed accumulation and area.

---

### Solution

**Step 1: Compute the definite integral using the Fundamental Theorem of Calculus**

The integrand is $f(x) = x$. An antiderivative is $F(x) = \frac{x^2}{2}$.
Evaluate the definite integral from $x = -1$ to $x = 2$:

$$
\int_{-1}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{-1}^{2}
$$

Substitute the upper and lower limits:

$$
= \frac{2^2}{2} - \frac{(-1)^2}{2} = \frac{4}{2} - \frac{1}{2} = \frac{3}{2} = 1.5
$$

---

**Step 2: Compute the area of the region below the $x$-axis**

The function crosses the $x$-axis at $x = 0$.
On the interval $[-1, 0]$, $x \le 0$, so the graph lies below the $x$-axis.
The height of this region is $0 - x = -x$.
Compute the geometric area $A_1$:

$$
A_1 = \int_{-1}^{0} (-x) \, dx = \left[ -\frac{x^2}{2} \right]_{-1}^{0} = 0 - \left(-\frac{(-1)^2}{2}\right) = \frac{1}{2} = 0.5
$$

*Geometric Check:* This region is a right triangle with base $b_1 = 1$ (from $-1$ to $0$) and height $h_1 = 1$ (from $y = 0$ to $y = -1$):

$$
A_1 = \frac{1}{2} \cdot 1 \cdot 1 = \frac{1}{2}
$$

---

**Step 3: Compute the area of the region above the $x$-axis**

On the interval $[0, 2]$, $x \ge 0$, so the graph lies above the $x$-axis.
The height of this region is $x - 0 = x$.
Compute the geometric area $A_2$:

$$
A_2 = \int_{0}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{0}^{2} = \frac{2^2}{2} - 0 = \frac{4}{2} = 2.0
$$

*Geometric Check:* This region is a right triangle with base $b_2 = 2$ (from $0$ to $2$) and height $h_2 = 2$ (from $y = 0$ to $y = 2$):

$$
A_2 = \frac{1}{2} \cdot 2 \cdot 2 = 2.0
$$

The total geometric area of both triangles is:

$$
A_{\mathrm{geom}} = A_1 + A_2 = \frac{1}{2} + 2 = \frac{5}{2} = 2.5
$$

---

**Step 4: Explain the difference between definite integral and geometric area**

1. **Signed Cancellation in the Integral:**
   The definite integral accounts for orientation and direction. It treats areas above the $x$-axis as positive accumulation and areas below the $x$-axis as negative accumulation:

   $$
   \int_{-1}^{2} x \, dx = \int_{-1}^{0} x \, dx + \int_{0}^{2} x \, dx = (-A_1) + A_2 = -0.5 + 2.0 = 1.5
   $$

   The negative contribution from the left triangle cancels out $0.5$ units of the positive contribution from the right triangle.
2. **Absolute Non-Negativity of Geometric Area:**
   Geometric area is a non-negative physical measure representing the actual amount of two-dimensional surface space enclosed by the curves:

   $$
   A_{\mathrm{geom}} = \int_{-1}^{2} |x| \, dx = A_1 + A_2 = 0.5 + 2.0 = 2.5
   $$

   It does not allow cancellation across the axis.

---

### Final Answer

1. **Definite Integral:**

   $$
   \int_{-1}^{2}x\,dx = \frac{3}{2} = 1.5
   $$

2. **Component Areas:**
   * Area below $x$-axis (on $[-1, 0]$): $A_1 = \frac{1}{2} = 0.5$
   * Area above $x$-axis (on $[0, 2]$): $A_2 = 2$
   * Total Geometric Area: $A_1 + A_2 = \frac{5}{2} = 2.5$

3. **Conceptual Distinction:**
   The definite integral computes **net signed area** ($A_2 - A_1 = 2 - 0.5 = 1.5$), where regions below the $x$-axis cancel regions above it. Geometric area computes **total physical area** ($A_1 + A_2 = 2.5$) without cancellation.
