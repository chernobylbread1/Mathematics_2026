### Essential Formulas

1. **One-Sided Limits:**
   * **Right-hand limit ($x \to c^+$):** $x$ approaches $c$ strictly through values greater than $c$ ($x > c$):

     $$
     \lim_{x \to c^+} f(x)
     $$

   * **Left-hand limit ($x \to c^-$):** $x$ approaches $c$ strictly through values less than $c$ ($x < c$):

     $$
     \lim_{x \to c^-} f(x)
     $$

2. **Existence of the Two-Sided Limit:**
   The two-sided limit $\lim_{x \to c} f(x)$ exists and equals $L$ if and only if both one-sided limits exist and are equal:

   $$
   \lim_{x \to c} f(x) = L \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L
   $$

3. **Vertical Asymptote:**
   The vertical line $x = c$ is called a vertical asymptote of the graph of $y = f(x)$ if at least one of the following conditions holds:

   $$
   \lim_{x \to c^-} f(x) = \pm\infty, \qquad \lim_{x \to c^+} f(x) = \pm\infty
   $$

---

### Problem Statement

Analyze the left-hand and right-hand limits of

$$
f(x)=\frac1{x-2}
$$

as $x\to2$. Does the two-sided limit exist? Interpret the result on a sketch of the graph and identify the vertical asymptote.

> **Why this exercise:** teaches how to distinguish one-sided limits and connect them with the geometry of an asymptote.

---

### Solution

**Step 1: Compute the right-hand limit as $x \to 2^+$**

As $x$ approaches $2$ from the right, $x > 2$.
Therefore, the quantity $x - 2$ is strictly positive:

$$
x - 2 > 0 \implies x - 2 \to 0^+
$$

The reciprocal of a positive quantity approaching zero grows without bound:

$$
\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty
$$

---

**Step 2: Compute the left-hand limit as $x \to 2^-$**

As $x$ approaches $2$ from the left, $x < 2$.
Therefore, the quantity $x - 2$ is strictly negative:

$$
x - 2 < 0 \implies x - 2 \to 0^-
$$

The reciprocal of a negative quantity whose magnitude approaches zero decreases without bound:

$$
\lim_{x \to 2^-} \frac{1}{x - 2} = -\infty
$$

---

**Step 3: Determine the existence of the two-sided limit**

Comparing the two one-sided limits:

$$
\lim_{x \to 2^-} f(x) = -\infty \neq +\infty = \lim_{x \to 2^+} f(x)
$$

Because the left-hand and right-hand limits are not equal (and neither is a finite real number), the two-sided limit $\lim_{x \to 2} \frac{1}{x - 2}$ does not exist.

---

**Step 4: Geometric interpretation and vertical asymptote**

1. **Vertical Asymptote:**
   Since both one-sided limits are infinite, the vertical line:

   $$
   x = 2
   $$

   is a vertical asymptote of $f(x)$.
2. **Behavior on the Graph:**
   * **Left branch ($x < 2$):** As the curve approaches the line $x = 2$ from the left, $y$ drops precipitously toward $-\infty$, lying in the lower half-plane.
   * **Right branch ($x > 2$):** As the curve approaches the line $x = 2$ from the right, $y$ ascends steeply toward $+\infty$, lying in the upper half-plane.
   * The graph is a standard rectangular hyperbola shifted $2$ units to the right along the $x$-axis.

---

### Final Answer

1. **One-Sided Limits:**

   $$
   \lim_{x\to2^+} \frac{1}{x-2} = +\infty
   $$

   $$
   \lim_{x\to2^-} \frac{1}{x-2} = -\infty
   $$

2. **Two-Sided Limit:**
   The two-sided limit $\lim_{x\to2}\frac{1}{x-2}$ does not exist because the left-hand and right-hand limits disagree.

3. **Geometric Interpretation:**
   The vertical line $x = 2$ is a vertical asymptote. The function diverges to $-\infty$ on the left and to $+\infty$ on the right, forming two disconnected branches of a hyperbola.
