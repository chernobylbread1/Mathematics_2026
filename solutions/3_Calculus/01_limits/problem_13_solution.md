### Essential Formulas

1. **Fundamental Trigonometric Limit:**
   For any argument approaching zero:

   $$
   \lim_{u \to 0} \frac{\sin u}{u} = 1
   $$

2. **Scaling Argument Principle:**
   If $u = k x$ where $k \neq 0$ is a constant, then $x \to 0 \implies u \to 0$, and:

   $$
   \lim_{x \to 0} \frac{\sin(k x)}{k x} = 1
   $$

3. **Limit Product and Quotient Rules:**
   If $\lim_{x \to 0} f(x) = A$ and $\lim_{x \to 0} g(x) = B$ ($B \neq 0$):

   $$
   \lim_{x \to 0} [c \cdot f(x)] = c \cdot A
   $$

   $$
   \lim_{x \to 0} \frac{f(x)}{g(x)} = \frac{A}{B}
   $$

---

### Problem Statement

Using

$$
\lim_{x\to0}\frac{\sin x}{x}=1,
$$

compute

$$
\lim_{x\to0}\frac{\sin5x}{x},\qquad \lim_{x\to0}\frac{\sin2x}{\sin3x}.
$$

In each case, show how you reduce the expression to the fundamental limit.

> **Why this exercise:** teaches how to reduce new limits to one known pattern.

---

### Solution

**Step 1: Compute $\lim_{x \to 0} \frac{\sin 5x}{x}$**

Direct substitution yields the indeterminate form $\frac{\sin 0}{0} = \frac{0}{0}$.
To reduce to the fundamental limit $\lim_{u \to 0} \frac{\sin u}{u} = 1$, the denominator must match the argument inside the sine function, which is $5x$.

Multiply and divide the expression by $5$:

$$
\frac{\sin 5x}{x} = 5 \cdot \frac{\sin 5x}{5x}
$$

Let $u = 5x$. As $x \to 0$, $u \to 0$.
Now apply the constant multiple law and the fundamental limit:

$$
\lim_{x \to 0} \frac{\sin 5x}{x} = 5 \cdot \lim_{u \to 0} \frac{\sin u}{u} = 5 \cdot 1 = 5
$$

---

**Step 2: Compute $\lim_{x \to 0} \frac{\sin 2x}{\sin 3x}$**

Direct substitution again yields the indeterminate form $\frac{0}{0}$.
To reduce both trigonometric expressions to fundamental limits simultaneously, divide both the numerator and the denominator by $x$ (for $x \neq 0$):

$$
\frac{\sin 2x}{\sin 3x} = \frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}}
$$

Normalize each fraction so that its denominator matches the sine argument:

$$
\frac{\sin 2x}{x} = 2 \cdot \frac{\sin 2x}{2x}
$$

$$
\frac{\sin 3x}{x} = 3 \cdot \frac{\sin 3x}{3x}
$$

Substitute these into the quotient:

$$
\frac{\sin 2x}{\sin 3x} = \frac{2 \cdot \frac{\sin 2x}{2x}}{3 \cdot \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{\frac{\sin 2x}{2x}}{\frac{\sin 3x}{3x}}
$$

---

**Step 3: Evaluate the quotient limit**

As $x \to 0$, we have $2x \to 0$ and $3x \to 0$.
By the fundamental trigonometric limit:

$$
\lim_{x \to 0} \frac{\sin 2x}{2x} = 1, \qquad \lim_{x \to 0} \frac{\sin 3x}{3x} = 1
$$

Applying the quotient law:

$$
\lim_{x \to 0} \frac{\sin 2x}{\sin 3x} = \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}
$$

---

### Final Answer

1. **First Limit:**

   $$
   \lim_{x\to0}\frac{\sin5x}{x} = 5
   $$

   *Reduction:* Rewrite as $5 \cdot \frac{\sin 5x}{5x}$, whose limit is $5 \cdot 1 = 5$.

2. **Second Limit:**

   $$
   \lim_{x\to0}\frac{\sin2x}{\sin3x} = \frac{2}{3}
   $$

   *Reduction:* Divide numerator and denominator by $x$ and scale by coefficients to get $\frac{2}{3} \cdot \frac{\frac{\sin 2x}{2x}}{\frac{\sin 3x}{3x}}$, evaluating to $\frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}$.
