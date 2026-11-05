### Essential Formulas

1. **Continuity at a Point:**
   A function $f(x)$ is continuous at $x = c$ if and only if:

   $$
   \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c)
   $$

2. **One-Sided Derivatives from First Principles:**
   * **Right-hand derivative:**

     $$
     f'_+(c) = \lim_{h \to 0^+} \frac{f(c + h) - f(c)}{h}
     $$

   * **Left-hand derivative:**

     $$
     f'_-(c) = \lim_{h \to 0^-} \frac{f(c + h) - f(c)}{h}
     $$

3. **Differentiability at a Point:**
   A function $f(x)$ is differentiable at $x = c$ if and only if both one-sided derivatives exist, are finite, and are equal:

   $$
   \exists f'(c) \iff f'_-(c) = f'_+(c)
   $$

   Differentiability strictly implies continuity, but the converse is false.

---

### Problem Statement

Investigate the behavior at $x=0$ of

$$
f(x)=
\begin{cases}
x^2,&x\ge0, \\
ax,&x<0.
\end{cases}
$$

For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

> **Why this problem:** it requires an organized argument and a clear distinction between two concepts.

---

### Solution

**Step 1: Investigate continuity at $x = 0$**

Evaluate the three relevant quantities at $x = 0$:
1. **Function value:**
   According to the branch $x \ge 0$:

   $$
   f(0) = 0^2 = 0
   $$

2. **Right-hand limit ($x \to 0^+$):**
   Using $f(x) = x^2$ for $x > 0$:

   $$
   \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} x^2 = 0
   $$

3. **Left-hand limit ($x \to 0^-$):**
   Using $f(x) = ax$ for $x < 0$:

   $$
   \lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (ax) = a(0) = 0
   $$

Because $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0) = 0$ for every real number $a$, the function $f(x)$ is continuous at $x = 0$ for all $a \in \mathbb{R}$.

---

**Step 2: Compute the one-sided derivatives at $x = 0$**

1. **Right-hand derivative $f'_+(0)$:**
   For $h > 0$, $f(h) = h^2$ and $f(0) = 0$:

   $$
   f'_+(0) = \lim_{h \to 0^+} \frac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^+} \frac{h^2 - 0}{h} = \lim_{h \to 0^+} h = 0
   $$

   Thus, $f'_+(0) = 0$ for any value of $a$.

2. **Left-hand derivative $f'_-(0)$:**
   For $h < 0$, $f(h) = ah$ and $f(0) = 0$:

   $$
   f'_-(0) = \lim_{h \to 0^-} \frac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^-} \frac{ah - 0}{h} = \lim_{h \to 0^-} a = a
   $$

   Thus, $f'_-(0) = a$.

---

**Step 3: Condition for one-sided derivatives to agree and differentiability**

Both one-sided derivatives exist for every $a \in \mathbb{R}$.
For them to agree:

$$
f'_-(0) = f'_+(0) \iff a = 0
$$

Therefore:
* If $a = 0$: $f'_-(0) = f'_+(0) = 0$. The two-sided derivative exists, and $f'(0) = 0$.
* If $a \neq 0$: $f'_-(0) = a \neq 0 = f'_+(0)$. The two-sided derivative does not exist.

Conclusion: $f(x)$ is differentiable at $x = 0$ if and only if $a = 0$.

---

**Step 4: Explain why continuity alone is not sufficient**

1. **Topological vs. Smoothness Conditions:**
   * **Continuity** is a positional property: it guarantees that the two branches meet at the same point $(0, 0)$ without a tear or jump. For any value of $a$, both branches end at $(0, 0)$.
   * **Differentiability** is a directional / geometric property: it requires not only that the curves connect, but that they do so with matching directional tangents, forming a smooth curve without an abrupt kink.
2. **The Geometric Corner:**
   When $a \neq 0$, the graph approaches the origin from the left as a straight line with constant slope $a$, while from the right it approaches the origin as a parabola with slope approaching $0$. At the junction $(0, 0)$, the graph forms a sharp corner (a point of non-differentiability). This demonstrates that continuity is a strictly weaker condition than differentiability.

---

### Final Answer

1. **Continuity:**
   The function is continuous at $x = 0$ for **all** $a \in \mathbb{R}$, because $\lim_{x\to0^-} f(x) = \lim_{x\to0^+} f(x) = f(0) = 0$.

2. **One-Sided Derivatives:**
   * $f'_+(0) = 0$
   * $f'_-(0) = a$
   They exist for all $a \in \mathbb{R}$, and they agree if and only if $a = 0$.

3. **Differentiability:**
   The function is differentiable at $x = 0$ if and only if:

   $$
   a = 0
   $$

4. **Why Continuity is Insufficient:**
   Continuity ensures the branches meet at $(0, 0)$, but differentiability requires the curves to merge smoothly with equal slopes. For $a \neq 0$, the abrupt change in slope from $a$ to $0$ creates a sharp corner where no unique tangent line exists.
