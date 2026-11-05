### Essential Formulas

1. **Difference of Squares Identity:**
   For any algebraic expressions $A$ and $B$:

   $$
   (A - B)(A + B) = A^2 - B^2
   $$

   When $A = \sqrt{X}$ and $B = \sqrt{Y}$ (or $B = Y$):

   $$
   A - B = \frac{A^2 - B^2}{A + B}
   $$

2. **Rationalization of Indeterminate Differences ($\infty - \infty$):**
   An expression of the form $\sqrt{P(n)} - Q(n)$ yielding the indeterminate form $\infty - \infty$ is transformed into a quotient by multiplying and dividing by its conjugate $\sqrt{P(n)} + Q(n)$:

   $$
   \sqrt{P(n)} - Q(n) = \frac{(\sqrt{P(n)} - Q(n))(\sqrt{P(n)} + Q(n))}{\sqrt{P(n)} + Q(n)} = \frac{P(n) - (Q(n))^2}{\sqrt{P(n)} + Q(n)}
   $$

3. **Factoring Powers from Radicals:**
   For $n > 0$:

   $$
   \sqrt{n^2 + c n} = \sqrt{n^2 \left(1 + \frac{c}{n}\right)} = n \sqrt{1 + \frac{c}{n}}
   $$

---

### Problem Statement

Compute

$$
\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right).
$$

Use the conjugate expression and explain why this transformation removes the difficulty.

> **Why this exercise:** introduces conjugation as a deliberate technique for removing an indeterminate form.

---

### Solution

**Step 1: Identify the indeterminate form**

As $n \to \infty$:

$$
n^2 + 5n \to \infty \implies \sqrt{n^2 + 5n} \to \infty
$$

Thus the sequence:

$$
a_n = \sqrt{n^2 + 5n} - n
$$

exhibits the indeterminate form $\infty - \infty$. We cannot subtract infinities directly because their difference depends on the subleading growth rates.

---

**Step 2: Multiply and divide by the conjugate**

The algebraic conjugate of $\sqrt{n^2 + 5n} - n$ is $\sqrt{n^2 + 5n} + n$.
Multiplying and dividing by this non-zero conjugate expression:

$$
a_n = \frac{\left(\sqrt{n^2 + 5n} - n\right)\left(\sqrt{n^2 + 5n} + n\right)}{\sqrt{n^2 + 5n} + n}
$$

Apply the difference of squares identity $(A - B)(A + B) = A^2 - B^2$:

$$
a_n = \frac{\left(\sqrt{n^2 + 5n}\right)^2 - n^2}{\sqrt{n^2 + 5n} + n} = \frac{(n^2 + 5n) - n^2}{\sqrt{n^2 + 5n} + n} = \frac{5n}{\sqrt{n^2 + 5n} + n}
$$

---

**Step 3: Factor out the dominant term $n$**

In the denominator, factor $n^2$ from inside the square root. For $n > 0$, $\sqrt{n^2} = n$:

$$
\sqrt{n^2 + 5n} = \sqrt{n^2 \left(1 + \frac{5}{n}\right)} = n \sqrt{1 + \frac{5}{n}}
$$

Substitute this back into the denominator:

$$
a_n = \frac{5n}{n \sqrt{1 + \frac{5}{n}} + n} = \frac{5n}{n \left(\sqrt{1 + \frac{5}{n}} + 1\right)}
$$

Cancel the common factor $n \neq 0$:

$$
a_n = \frac{5}{\sqrt{1 + \frac{5}{n}} + 1}
$$

---

**Step 4: Evaluate the limit**

As $n \to \infty$, $\frac{5}{n} \to 0$. By continuity of the square root function:

$$
\lim_{n \to \infty} \sqrt{1 + \frac{5}{n}} = \sqrt{1 + 0} = 1
$$

Applying the quotient and sum limit laws:

$$
\lim_{n \to \infty} a_n = \frac{5}{1 + 1} = \frac{5}{2}
$$

---

**Step 5: Why conjugation removes the difficulty**

1. **Cancellation of the leading singular terms:**
   Both $\sqrt{n^2 + 5n}$ and $n$ grow at the linear rate $n$. In the difference $\sqrt{n^2 + 5n} - n$, subtracting two large nearly equal quantities results in catastrophic cancellation where the leading $n$ cancels out, leaving only the subleading contribution.
2. **Conversion of difference to quotient:**
   Conjugation turns the difference into a fraction whose numerator is the exact difference of squares $(n^2 + 5n) - n^2 = 5n$, where the cancellation has been carried out explicitly. The denominator becomes a sum $\sqrt{n^2 + 5n} + n$ where both terms are positive and reinforce each other rather than canceling.
3. **Removal of the indeterminacy:**
   Factoring $n$ from both numerator and denominator yields a determinate limit with a non-zero denominator $1 + 1 = 2$.

---

### Final Answer

1. **Value of the Limit:**

   $$
   \lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right) = \frac{5}{2}
   $$

2. **Why Conjugation Works:**
   Multiplying by the conjugate converts the indeterminate difference $\infty - \infty$ into an algebraic fraction through the identity $(A - B)(A + B) = A^2 - B^2$. This analytically eliminates the conflicting leading $n^2$ terms in the numerator, yielding $5n$, while replacing the subtraction in the denominator with an addition $\sqrt{n^2+5n} + n \sim 2n$, resulting in the determinate ratio $5/2$.
