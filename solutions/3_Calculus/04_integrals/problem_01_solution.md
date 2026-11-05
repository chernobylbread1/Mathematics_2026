### Essential Formulas

1. **Definition of Antiderivative (Indefinite Integral):**
   A function $F(x)$ is called an antiderivative of $f(x)$ on an open interval $I$ if for all $x \in I$:

   $$
   F'(x) = f(x)
   $$

2. **Power Rule for Integration:**
   For any constant real exponent $n \neq -1$:

   $$
   \int x^n \, dx = \frac{x^{n+1}}{n+1} + C
   $$

3. **Linearity of the Indefinite Integral:**
   For continuous functions $f(x), g(x)$ and constants $a, b \in \mathbb{R}$:

   $$
   \int (a f(x) + b g(x)) \, dx = a \int f(x) \, dx + b \int g(x) \, dx
   $$

4. **Constant of Integration Theorem:**
   If $F(x)$ is an antiderivative of $f(x)$ on an interval $I$, then the general family of antiderivatives is:

   $$
   \int f(x) \, dx = F(x) + C, \qquad C \in \mathbb{R}
   $$

---

### Problem Statement

For

$$
f(x)=3x^2-4x+5
$$

find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

> **Why this problem:** it introduces integration as the inverse operation to differentiation.

---

### Solution

**Step 1: Find one specific antiderivative $F_0(x)$**

Integrate the polynomial $f(x) = 3x^2 - 4x + 5$ term by term using the linearity property and the power rule:
* $\int 3x^2 \, dx = 3 \cdot \frac{x^3}{3} = x^3$
* $\int (-4x) \, dx = -4 \cdot \frac{x^2}{2} = -2x^2$
* $\int 5 \, dx = 5x$

Choosing the particular integration constant $C = 0$ yields one specific antiderivative:

$$
F_0(x) = x^3 - 2x^2 + 5x
$$

---

**Step 2: Write the entire family of antiderivatives**

The indefinite integral encompasses all possible antiderivatives differing by an arbitrary real constant $C$:

$$
F(x) = \int (3x^2 - 4x + 5) \, dx = x^3 - 2x^2 + 5x + C, \qquad C \in \mathbb{R}
$$

---

**Step 3: Verify the result by differentiation**

Differentiate the general family $F(x)$ with respect to $x$:

$$
F'(x) = \frac{d}{dx}\left[x^3 - 2x^2 + 5x + C\right]
$$

Apply the derivative linearity and power rule:

$$
F'(x) = \frac{d}{dx}[x^3] - 2\frac{d}{dx}[x^2] + 5\frac{d}{dx}[x] + \frac{d}{dx}[C]
$$

$$
F'(x) = 3x^2 - 2(2x) + 5(1) + 0 = 3x^2 - 4x + 5 = f(x)
$$

Because $F'(x) = f(x)$, the antiderivative is mathematically verified.

---

**Step 4: Explain the meaning of the constant $C$**

1. **Vanishing of Constant Rates:**
   Differentiation measures rates of change. Because any constant value $C$ has zero rate of change ($\frac{d}{dx}[C] = 0$), adding an arbitrary constant does not alter the derivative.
2. **Mean Value Theorem Consequence:**
   By the Mean Value Theorem, if two differentiable functions $F_1(x)$ and $F_2(x)$ have identical derivatives on an interval ($F_1'(x) = F_2'(x)$), their difference has zero derivative:

   $$
   (F_1 - F_2)'(x) = 0 \implies F_1(x) - F_2(x) = C
   $$

   Therefore, any two antiderivatives on a connected interval must differ strictly by a constant.
3. **Geometric Interpretation:**
   The parameter $C$ generates an entire family of parallel curves that are vertical translations of one another. The slope of the tangent line at any vertical slice $x = x_0$ is identical for every curve in the family, equal to $f(x_0)$.

---

### Final Answer

1. **One Antiderivative:**

   $$
   F_0(x) = x^3 - 2x^2 + 5x
   $$

2. **Entire Family of Antiderivatives:**

   $$
   F(x) = x^3 - 2x^2 + 5x + C, \qquad C \in \mathbb{R}
   $$

3. **Verification:**

   $$
   \frac{d}{dx}\left[x^3 - 2x^2 + 5x + C\right] = 3x^2 - 4x + 5 = f(x)
   $$

4. **Meaning of $C$:**
   The constant $C$ accounts for the fact that differentiating any constant yields $0$. It represents the family of all vertical translations of the curve that share the exact same slope field $f(x)$.
