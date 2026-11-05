### Essential Formulas

1. **Pythagorean Trigonometric Identity:**
   For any angle $x$:

   $$
   \sin^2 x + \cos^2 x = 1 \implies 1 - \cos^2 x = \sin^2 x
   $$

2. **Half-Angle Identity:**
   The difference $1 - \cos x$ can be rewritten in terms of sine:

   $$
   1 - \cos x = 2 \sin^2\left(\frac{x}{2}\right)
   $$

3. **Fundamental Trigonometric Limit:**

   $$
   \lim_{u \to 0} \frac{\sin u}{u} = 1 \implies \lim_{u \to 0} \left(\frac{\sin u}{u}\right)^2 = 1^2 = 1
   $$

---

### Problem Statement

Compute

$$
\lim_{x\to0}\frac{1-\cos x}{x^2}.
$$

Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

> **Why this exercise:** requires combining two known tools in one argument.

---

### Solution

**Step 1: Identify the indeterminate form**

Direct evaluation at $x = 0$ gives:

$$
\frac{1 - \cos 0}{0^2} = \frac{1 - 1}{0} = \frac{0}{0}
$$

This is an indeterminate form of type $\frac{0}{0}$. The problem specifically requires justification without l'Hôpital's rule.

---

**Step 2: Method 1 — Conjugate multiplication**

Multiply both the numerator and the denominator by the conjugate $1 + \cos x$:

$$
\frac{1 - \cos x}{x^2} = \frac{(1 - \cos x)(1 + \cos x)}{x^2 (1 + \cos x)}
$$

Using the difference of squares and the Pythagorean identity $(1 - \cos x)(1 + \cos x) = 1 - \cos^2 x = \sin^2 x$:

$$
= \frac{\sin^2 x}{x^2 (1 + \cos x)}
$$

Separate this product into standard components:

$$
= \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}
$$

Evaluate the limit of each factor as $x \to 0$:

$$
\lim_{x \to 0} \left(\frac{\sin x}{x}\right)^2 = 1^2 = 1
$$

$$
\lim_{x \to 0} \frac{1}{1 + \cos x} = \frac{1}{1 + \cos 0} = \frac{1}{1 + 1} = \frac{1}{2}
$$

By the product limit rule:

$$
\lim_{x \to 0} \frac{1 - \cos x}{x^2} = 1 \cdot \frac{1}{2} = \frac{1}{2}
$$

---

**Step 3: Method 2 — Half-angle trigonometric identity**

Alternatively, apply the half-angle formula $1 - \cos x = 2 \sin^2\left(\frac{x}{2}\right)$:

$$
\frac{1 - \cos x}{x^2} = \frac{2 \sin^2\left(\frac{x}{2}\right)}{x^2}
$$

To match the argument of the sine function, write $x^2 = 4 \left(\frac{x}{2}\right)^2$:

$$
= \frac{2 \sin^2\left(\frac{x}{2}\right)}{4 \left(\frac{x}{2}\right)^2} = \frac{2}{4} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2 = \frac{1}{2} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2
$$

Let $u = \frac{x}{2}$. As $x \to 0$, $u \to 0$.
Since $\lim_{u \to 0} \frac{\sin u}{u} = 1$:

$$
\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2} \cdot 1^2 = \frac{1}{2}
$$

Both methods rigorously yield $\frac{1}{2}$ without invoking derivatives.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{x\to0}\frac{1-\cos x}{x^2} = \frac{1}{2}
   $$

2. **Justification:**
   * Multiplying by the conjugate $1 + \cos x$ converts the numerator to $\sin^2 x$.
   * Grouping as $\left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}$ reduces the problem directly to the fundamental limit $1^2 \cdot \frac{1}{2} = \frac{1}{2}$.
