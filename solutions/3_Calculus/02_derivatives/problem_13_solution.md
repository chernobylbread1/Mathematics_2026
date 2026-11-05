### Essential Formulas

1. **Multi-Layer Chain Rule:**
   For a composition of three functions $y = f(x) = g(h(k(x)))$:

   $$
   f'(x) = g'(h(k(x))) \cdot h'(k(x)) \cdot k'(x)
   $$

   In Leibniz notation:

   $$
   \frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
   $$

2. **Constituent Elementary Derivatives:**
   * $\frac{d}{dv}[e^v] = e^v$
   * $\frac{d}{du}[\sin u] = \cos u$
   * $\frac{d}{dx}[x^2] = 2x$

---

### Problem Statement

For

$$
f(x)=e^{\sin(x^2)}
$$

compute the derivative. First write the layers

$$
x\longrightarrow x^2\longrightarrow \sin(x^2)\longrightarrow e^{\sin(x^2)}
$$

and explain why differentiation moves through them in the reverse order.

> **Why this problem:** it develops the chain rule as a method for working with multiple layers.

---

### Solution

**Step 1: Write down the functional layers from inside to outside**

The forward evaluation process constructs the function step by step:

$$
x \longrightarrow u = x^2 \longrightarrow v = \sin u = \sin(x^2) \longrightarrow y = e^v = e^{\sin(x^2)}
$$

* Layer 1 (innermost input): $u = k(x) = x^2$
* Layer 2 (intermediate trigonometric): $v = h(u) = \sin u$
* Layer 3 (outermost exponential): $y = g(v) = e^v$

---

**Step 2: Differentiate each layer**

Compute the derivative of each successive layer with respect to its own independent input:
1. Outermost layer with respect to $v$:

   $$
   \frac{dy}{dv} = \frac{d}{dv}[e^v] = e^v = e^{\sin(x^2)}
   $$

2. Middle layer with respect to $u$:

   $$
   \frac{dv}{du} = \frac{d}{du}[\sin u] = \cos u = \cos(x^2)
   $$

3. Innermost layer with respect to $x$:

   $$
   \frac{du}{dx} = \frac{d}{dx}[x^2] = 2x
   $$

---

**Step 3: Assemble the derivative via the multi-layer chain rule**

Multiply the derivatives of all three layers in Leibniz order:

$$
\frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
$$

Substitute the evaluated expressions:

$$
f'(x) = e^{\sin(x^2)} \cdot \cos(x^2) \cdot (2x)
$$

Rearranging the factors into standard algebraic order:

$$
f'(x) = 2x \cos(x^2) e^{\sin(x^2)}
$$

---

**Step 4: Explain why differentiation proceeds in reverse order**

1. **Forward Construction vs. Backward Sensitivity:**
   * In function evaluation, operations proceed forward: $x \to u \to v \to y$. You cannot compute $e^{\sin(x^2)}$ without first computing $x^2$ and then $\sin(x^2)$.
   * In differentiation, we ask how the final output $y$ responds to an infinitesimal disturbance. The outermost envelope $y = e^v$ is the direct interface with the output. We first ask how $y$ changes with respect to its immediate argument $v$ ($\frac{dy}{dv} = e^v$).
2. **Unpacking the Wrappers:**
   * Next, we look inside the argument $v$ and ask how $v$ responds to changes in $u$ ($\frac{dv}{du} = \cos u$).
   * Finally, we penetrate to the innermost variable and ask how $u$ changes with respect to the root independent variable $x$ ($\frac{du}{dx} = 2x$).
3. **Chain of Scaling Ratios:**
   In the product of differential ratios:

   $$
   \frac{dy}{dx} = \left(\frac{dy}{dv}\right) \left(\frac{dv}{du}\right) \left(\frac{du}{dx}\right)
   $$

   each factor acts as a scaling multiplier that transfers sensitivity from the outermost shell back to the core variable.

---

### Final Answer

1. **Layers of Composition:**
   * Inner: $u = x^2$
   * Middle: $v = \sin(x^2)$
   * Outer: $y = e^{\sin(x^2)}$

2. **Derivative:**

   $$
   f'(x) = 2x \cos(x^2) e^{\sin(x^2)}
   $$

3. **Why Differentiation Reverses the Order:**
   While evaluation builds the number from inside out ($x \to x^2 \to \sin \to \exp$), differentiation analyzes output sensitivity from outside in. The chain rule multiplies the sensitivity of the outermost function by the derivative of the next interior layer until reaching the base variable $x$.
