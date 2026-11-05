### Essential Formulas

1. **Standard Elementary Derivatives and Antiderivatives:**
   * $\frac{d}{dx}[e^x] = e^x \implies \int e^x \, dx = e^x + C$
   * $\frac{d}{dx}[\sin x] = \cos x \implies \int \cos x \, dx = \sin x + C$
   * $\frac{d}{dx}[\cos x] = -\sin x \implies \int \sin x \, dx = -\cos x + C$

2. **Linearity of Integration:**
   For constants $c_1, c_2, c_3 \in \mathbb{R}$:

   $$
   \int (c_1 f_1(x) + c_2 f_2(x) + c_3 f_3(x)) \, dx = c_1 \int f_1(x) \, dx + c_2 \int f_2(x) \, dx + c_3 \int f_3(x) \, dx
   $$

---

### Problem Statement

Compute

$$
\int\left(2e^x+3\cos x-4\sin x\right)\,dx.
$$

Match each term with a known derivative and verify the entire result with one differentiation.

> **Why this problem:** it builds a catalogue of basic antiderivatives from known derivatives.

---

### Solution

**Step 1: Match each term with a known derivative**

Break the integrand into its three basic component functions:

1. **First term ($2e^x$):**
   We know that:

   $$
   \frac{d}{dx}[e^x] = e^x
   $$

   Therefore:

   $$
   \int 2e^x \, dx = 2 \int e^x \, dx = 2e^x
   $$

2. **Second term ($3\cos x$):**
   We know that:

   $$
   \frac{d}{dx}[\sin x] = \cos x
   $$

   Therefore:

   $$
   \int 3\cos x \, dx = 3 \int \cos x \, dx = 3\sin x
   $$

3. **Third term ($-4\sin x$):**
   We know that:

   $$
   \frac{d}{dx}[\cos x] = -\sin x \implies \frac{d}{dx}[-\cos x] = \sin x
   $$

   Therefore:

   $$
   \int (-4\sin x) \, dx = -4 \int \sin x \, dx = -4(-\cos x) = +4\cos x
   $$

---

**Step 2: Combine the antiderivatives**

Summing the results and appending the arbitrary real constant of integration $C$:

$$
F(x) = \int\left(2e^x + 3\cos x - 4\sin x\right)\,dx = 2e^x + 3\sin x + 4\cos x + C
$$

---

**Step 3: Verify the entire result with one differentiation**

Differentiate the resulting expression $F(x)$ with respect to $x$:

$$
F'(x) = \frac{d}{dx}\left[2e^x + 3\sin x + 4\cos x + C\right]
$$

Apply the linearity of the derivative:

$$
F'(x) = 2\frac{d}{dx}[e^x] + 3\frac{d}{dx}[\sin x] + 4\frac{d}{dx}[\cos x] + \frac{d}{dx}[C]
$$

Substitute the elementary derivatives:

$$
F'(x) = 2(e^x) + 3(\cos x) + 4(-\sin x) + 0
$$

$$
F'(x) = 2e^x + 3\cos x - 4\sin x
$$

The derivative matches the original integrand.

---

### Final Answer

1. **Catalogue of Matched Derivatives:**
   * $\frac{d}{dx}[2e^x] = 2e^x$
   * $\frac{d}{dx}[3\sin x] = 3\cos x$
   * $\frac{d}{dx}[4\cos x] = -4\sin x$

2. **Indefinite Integral:**

   $$
   \int\left(2e^x+3\cos x-4\sin x\right)\,dx = 2e^x + 3\sin x + 4\cos x + C
   $$

3. **Unified Verification:**

   $$
   \frac{d}{dx}\left[2e^x + 3\sin x + 4\cos x + C\right] = 2e^x + 3\cos x - 4\sin x
   $$
