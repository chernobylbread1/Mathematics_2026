### Essential Formulas

1. **Definition of Continuity at a Point:**
   A function $f(x)$ is continuous at $x = c$ if and only if:
   * The function value $f(c)$ is defined.
   * The limit $\lim_{x \to c} f(x)$ exists.
   * The limit equals the function value:

   $$
   \lim_{x \to c} f(x) = f(c)
   $$

2. **Continuity via One-Sided Limits:**
   Equivalently, $f(x)$ is continuous at $x = c$ if and only if the left-hand limit, the right-hand limit, and the function value all exist and coincide:

   $$
   \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c)
   $$

---

### Problem Statement

Find $a$ so that

$$
f(x)=
\begin{cases}
ax+1,&x<2, \\
x^2-1,&x\ge2
\end{cases}
$$

is continuous at $x=2$. Explicitly compare the left-hand limit, right-hand limit, and function value.

> **Why this exercise:** organizes the definition of continuity as agreement among three quantities.

---

### Solution

**Step 1: Compute the function value $f(2)$**

According to the piecewise definition, for $x \ge 2$, $f(x) = x^2 - 1$.
Evaluate at $x = 2$:

$$
f(2) = 2^2 - 1 = 4 - 1 = 3
$$

The function is defined at $x = 2$ and takes the value $3$.

---

**Step 2: Compute the right-hand limit as $x \to 2^+$**

For $x > 2$, $f(x) = x^2 - 1$. Since polynomials are continuous everywhere:

$$
\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (x^2 - 1) = 2^2 - 1 = 3
$$

The right-hand limit agrees with the function value:

$$
\lim_{x \to 2^+} f(x) = f(2) = 3
$$

---

**Step 3: Compute the left-hand limit as $x \to 2^-$**

For $x < 2$, $f(x) = ax + 1$. By continuity of linear polynomials:

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (ax + 1) = a(2) + 1 = 2a + 1
$$

---

**Step 4: Equate the three quantities to find $a$**

For $f(x)$ to be continuous at $x = 2$, the three quantities must all be equal:

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2)
$$

Substitute the computed expressions:

$$
2a + 1 = 3
$$

Solve the linear equation for $a$:

$$
2a = 3 - 1
$$

$$
2a = 2 \implies a = 1
$$

---

**Step 5: Verification of continuity for $a = 1$**

When $a = 1$, the function becomes:

$$
f(x)=
\begin{cases}
x+1,&x<2, \\
x^2-1,&x\ge2
\end{cases}
$$

Checking the three quantities:
* $\lim_{x \to 2^-} f(x) = 2(1) + 1 = 3$
* $\lim_{x \to 2^+} f(x) = 2^2 - 1 = 3$
* $f(2) = 2^2 - 1 = 3$

All three values equal $3$. Hence, $f(x)$ is continuous at $x = 2$.

---

### Final Answer

1. **Required Value of $a$:**

   $$
   a = 1
   $$

2. **Explicit Comparison of Quantities at $x = 2$:**
   * **Left-hand limit:** $\lim_{x \to 2^-} f(x) = 2a + 1 = 3$
   * **Right-hand limit:** $\lim_{x \to 2^+} f(x) = 3$
   * **Function value:** $f(2) = 3$

3. **Conclusion:**
   For $a = 1$, $\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2) = 3$, satisfying the definition of continuity.

