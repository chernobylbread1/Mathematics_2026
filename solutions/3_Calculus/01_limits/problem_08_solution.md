### Essential Formulas

1. **Difference of Squares Factorization:**
   For any real numbers $A, B$:

   $$
   (A - B)(A + B) = A^2 - B^2
   $$

   In particular, for $x \ge 0$:

   $$
   (\sqrt{x} - 2)(\sqrt{x} + 2) = (\sqrt{x})^2 - 2^2 = x - 4
   $$

2. **Rationalizing Factor:**
   To eliminate a square root difference $\sqrt{u} - v$ from a fraction, multiply numerator and denominator by its conjugate $\sqrt{u} + v$:

   $$
   \frac{\sqrt{u} - v}{w} = \frac{(\sqrt{u} - v)(\sqrt{u} + v)}{w(\sqrt{u} + v)} = \frac{u - v^2}{w(\sqrt{u} + v)}
   $$

3. **Limit of a Quotient with Removable Singularity:**
   If $f(x) = \frac{p(x)}{q(x)}$ has $p(c) = 0$ and $q(c) = 0$, but algebraic manipulation yields $f(x) = g(x)$ for all $x \neq c$ where $g$ is continuous at $c$, then:

   $$
   \lim_{x \to c} f(x) = g(c)
   $$

---

### Problem Statement

Compute

$$
\lim_{x\to4}\frac{\sqrt{x}-2}{x-4}
$$

by rationalizing the numerator. Compare the idea with Exercise 3 involving a sequence.

> **Why this exercise:** reinforces transferring the same algebraic technique between two types of limits.

---

### Solution

**Step 1: Test substitution and identify the indeterminate form**

Substituting $x = 4$ directly into the expression gives:

$$
\frac{\sqrt{4} - 2}{4 - 4} = \frac{2 - 2}{0} = \frac{0}{0}
$$

This is an indeterminate form of type $\frac{0}{0}$. The radical in the numerator prevents direct factoring of $(x - 4)$ through standard polynomial methods.

---

**Step 2: Rationalize the numerator**

Multiply both the numerator and the denominator by the conjugate of $\sqrt{x} - 2$, which is $\sqrt{x} + 2$:

$$
\frac{\sqrt{x} - 2}{x - 4} = \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)}
$$

Apply the difference of squares identity in the numerator:

$$
(\sqrt{x} - 2)(\sqrt{x} + 2) = (\sqrt{x})^2 - 2^2 = x - 4
$$

Substituting this into the fraction yields:

$$
\frac{x - 4}{(x - 4)(\sqrt{x} + 2)}
$$

---

**Step 3: Cancel the common factor and evaluate the limit**

For $x \neq 4$, the factor $(x - 4)$ is non-zero and can be cancelled:

$$
\frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2}
$$

Now compute the limit as $x \to 4$ by substituting into this continuous expression:

$$
\lim_{x \to 4} \frac{1}{\sqrt{x} + 2} = \frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}
$$

---

**Step 4: Comparison with Exercise 3**

1. **Underlying Identity:**
   Both exercises rely on the algebraic identity $(A - B)(A + B) = A^2 - B^2$ to eliminate radical expressions.
2. **Context and Purpose:**
   * In **Exercise 3** ($\lim_{n \to \infty} (\sqrt{n^2 + 5n} - n)$), conjugation transformed an indeterminate difference $\infty - \infty$ at infinity into an algebraic fraction, canceling the unbounded $n^2$ terms.
   * In **Exercise 8** ($\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$), conjugation resolves an indeterminate ratio $\frac{0}{0}$ at a finite point $x = 4$, creating the factor $(x - 4)$ in the numerator to cancel the singularity in the denominator.
3. **Core Lesson:**
   The conjugate technique is universal: it rationalizes expressions to eliminate conflicting or vanishing terms, regardless of whether the limit is taken at infinity or at a finite point.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{x\to4}\frac{\sqrt{x}-2}{x-4} = \frac{1}{4}
   $$

2. **Comparison with Exercise 3:**
   Both problems use multiplication by the conjugate $(\sqrt{A} + B)$ to invoke the difference of squares identity. While Exercise 3 resolved an $\infty - \infty$ form at infinity by turning subtraction into addition, Exercise 8 resolves a $\frac{0}{0}$ form at a finite point by creating and canceling the singular factor $(x - 4)$.
