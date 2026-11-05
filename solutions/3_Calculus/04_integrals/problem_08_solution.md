### Essential Formulas

1. **Integration by Parts:**

   $$
   \int u \, dv = u v - \int v \, du
   $$

   or in functional form:

   $$
   \int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx
   $$

2. **Heuristic for Factor Choice (LIATE / Simplification Priority):**
   * Choose $u(x)$ to be a factor that becomes simpler upon differentiation ($\frac{d}{dx}[x^n] = n x^{n-1}$).
   * Choose $v'(x)$ to be a factor that can be integrated easily without increasing complexity ($\int \cos x \, dx = \sin x$).

---

### Problem Statement

Compute

$$
\int x\cos x\,dx.
$$

Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

> **Why this problem:** it teaches that integration by parts requires a deliberate choice of factors.

---

### Solution

**Step 1: Justify the choice of factors**

Integration by parts trades the original integral $\int u v' \, dx$ for the new integral $\int u' v \, dx$. The choice of which factor to assign to $u$ and which to $v'$ governs whether the calculation succeeds:

1. **Strategy 1 (Convenient Choice): $u(x) = x$ and $v'(x) = \cos x$**
   * Differentiating $u$: $u'(x) = \frac{d}{dx}[x] = 1$. The degree of the algebraic polynomial drops from $1$ to $0$, completely eliminating the variable $x$.
   * Integrating $v'$: $v(x) = \int \cos x \, dx = \sin x$. The trigonometric function oscillates between sine and cosine without gaining algebraic powers.
   * New integral: $\int u' v \, dx = \int 1 \cdot \sin x \, dx = -\cos x$, which is immediately solvable.

2. **Strategy 2 (Inconvenient Choice): $u(x) = \cos x$ and $v'(x) = x$**
   * Differentiating $u$: $u'(x) = -\sin x$.
   * Integrating $v'$: $v(x) = \int x \, dx = \frac{x^2}{2}$.
   * New integral: $\int u' v \, dx = \int \left(-\frac{x^2}{2}\sin x\right) dx$.
   * Here, the power of $x$ has increased from $1$ to $2$. The new integral is strictly more complex than the original, moving in the wrong direction.

Therefore, assigning $u = x$ and $v' = \cos x$ is the only productive choice.

---

**Step 2: Carry out the calculation**

Assign the parts:
* $u = x \implies du = dx$
* $dv = \cos x \, dx \implies v = \sin x$

Apply the integration-by-parts formula:

$$
\int x \cos x \, dx = x \sin x - \int \sin x \, dx
$$

Evaluate the remaining elementary integral $\int \sin x \, dx = -\cos x$:

$$
\int x \cos x \, dx = x \sin x - (-\cos x) + C
$$

Simplify the signs:

$$
= x \sin x + \cos x + C
$$

---

**Step 3: Verify the result by differentiation**

Differentiate $x \sin x + \cos x + C$:

$$
\frac{d}{dx}\left[x \sin x + \cos x + C\right] = \frac{d}{dx}[x \sin x] + \frac{d}{dx}[\cos x] + \frac{d}{dx}[C]
$$

Apply the product rule to $x \sin x$:

$$
= \left((1)\sin x + x \cos x\right) + (-\sin x) + 0
$$

Combine like terms:

$$
= \sin x + x \cos x - \sin x = x \cos x
$$

The result matches the integrand.

---

### Final Answer

1. **Justification of Factor Choice:**
   Differentiating $u = x$ yields $u' = 1$, reducing polynomial degree and eliminating the algebraic factor, while integrating $v' = \cos x$ yields $\sin x$. The reverse choice would increase the power to $x^2/2$, making the new integral more difficult.

2. **Indefinite Integral:**

   $$
   \int x\cos x\,dx = x \sin x + \cos x + C
   $$

3. **Verification:**

   $$
   \frac{d}{dx}\left[x \sin x + \cos x + C\right] = \sin x + x \cos x - \sin x = x \cos x
   $$

