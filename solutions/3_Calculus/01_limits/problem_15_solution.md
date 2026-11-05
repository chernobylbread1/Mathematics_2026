### Essential Formulas

1. **Formal Definition of a Sequence Limit ($\varepsilon$-$N$ Criterion):**
   $\lim_{n \to \infty} a_n = L$ if and only if:

   $$
   \forall \varepsilon > 0, \ \exists N \in \mathbb{N}: \ \forall n > N \implies |a_n - L| < \varepsilon
   $$

2. **Formal Definition of a Function Limit ($\varepsilon$-$\delta$ Criterion):**
   $\lim_{x \to c} f(x) = L$ if and only if:

   $$
   \forall \varepsilon > 0, \ \exists \delta > 0: \ 0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon
   $$

3. **Role of Empirical Observation:**
   Tables of values and graphical plots provide heuristic guidance, formulate conjectures, and build visual intuition, but deductive proof requires an argument universally valid across all $\varepsilon > 0$.

---

### Problem Statement

Choose one sequence and one function from this set. For the sequence, compute several values for increasingly large $n$. For the function, prepare a table of values with arguments approaching the limit point from the left and right. Sketch the behavior of both objects.

Compare the observation with the analytical result and explain why a finite number of calculations or a sketch does not constitute a proof that the limit exists.

> **Why this exercise:** teaches how to distinguish intuition and observation from mathematical argument.

---

### Solution

**Step 1: Choose a sequence and compute numerical terms**

We choose the rational sequence from Exercise 1:

$$
a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}
$$

Evaluating for increasingly large $n$:
* For $n = 2$:

  $$
  a_2 = \frac{4(4) - 6 + 1}{2(4) + 10 - 7} = \frac{11}{11} = 1.00000
  $$

* For $n = 5$:

  $$
  a_5 = \frac{4(25) - 15 + 1}{2(25) + 25 - 7} = \frac{86}{68} \approx 1.26471
  $$

* For $n = 10$:

  $$
  a_{10} = \frac{4(100) - 30 + 1}{2(100) + 50 - 7} = \frac{371}{243} \approx 1.52675
  $$

* For $n = 100$:

  $$
  a_{100} = \frac{4(10000) - 300 + 1}{2(10000) + 500 - 7} = \frac{39701}{20493} \approx 1.93730
  $$

* For $n = 1000$:

  $$
  a_{1000} = \frac{4(10^6) - 3000 + 1}{2(10^6) + 5000 - 7} = \frac{3997001}{2004993} \approx 1.99352
  $$

* For $n = 10000$:

  $$
  a_{10000} \approx 1.99935
  $$

The terms monotonically ascend toward $2$, matching the analytical limit $L = 2$.

---

**Step 2: Choose a function and prepare a two-sided table of values**

We choose the fundamental trigonometric function from Exercise 13:

$$
f(x) = \frac{\sin x}{x} \qquad (c = 0)
$$

We compute values approaching $c = 0$ symmetrically from the left ($x \to 0^-$) and right ($x \to 0^+$):

* **Left-hand approach ($x < 0$):**
  * $x = -0.5 \implies f(-0.5) = \frac{\sin(-0.5)}{-0.5} \approx 0.958851$
  * $x = -0.1 \implies f(-0.1) = \frac{\sin(-0.1)}{-0.1} \approx 0.998334$
  * $x = -0.01 \implies f(-0.01) = \frac{\sin(-0.01)}{-0.01} \approx 0.999983$
  * $x = -0.001 \implies f(-0.001) = \frac{\sin(-0.001)}{-0.001} \approx 0.9999998$

* **Right-hand approach ($x > 0$):**
  * $x = +0.5 \implies f(0.5) = \frac{\sin(0.5)}{0.5} \approx 0.958851$
  * $x = +0.1 \implies f(0.1) = \frac{\sin(0.1)}{0.1} \approx 0.998334$
  * $x = +0.01 \implies f(0.01) = \frac{\sin(0.01)}{0.01} \approx 0.999983$
  * $x = +0.001 \implies f(0.001) = \frac{\sin(0.001)}{0.001} \approx 0.9999998$

Both sides demonstrate clear convergence toward $1$, matching the analytical limit $L = 1$.

---

**Step 3: Characterize the sketches of both objects**

1. **Sequence $a_n$:**
   Plotting discrete pairs $(n, a_n)$ in the Cartesian plane shows points starting at $(2, 1.00)$ and curving upwards asymptotically toward the horizontal line $y = 2$. No values reach or exceed $2$ for large $n$.
2. **Function $f(x)$:**
   The curve $y = \frac{\sin x}{x}$ is symmetric across the $y$-axis (even function), peaking smoothly at $(0, 1)$ with a removable discontinuity (a hole) at $(0, 1)$ because $f(0)$ is undefined, with damped waves undulating outward for larger $|x|$.

---

**Step 4: Why empirical calculations or sketches do not constitute a proof**

1. **Finite Sampling cannot establish Universal Truth:**
   Calculating values for five or even five million points checks an insignificant subset of the domain. An analytical proof requires truth for *every* $\varepsilon > 0$ across all infinite $n > N$ or all $0 < |x - c| < \delta$.
2. **Hidden High-Frequency Oscillations:**
   Consider a function such as $g(x) = \sin\left(\frac{\pi}{x}\right)$. If sampled at $x = \frac{1}{k}$ for integer $k$, every computed value is $\sin(k\pi) = 0$. A table of values would suggest $\lim_{x \to 0} g(x) = 0$, whereas the true limit does not exist because $g(x)$ oscillates infinitely between $-1$ and $+1$ near $0$.
3. **Slow Divergence and Deceptive Plateaus:**
   The partial sums of the harmonic series $H_n = \sum_{k=1}^n \frac{1}{k}$ change imperceptibly when sampled at scattered intervals, giving the visual illusion of a horizontal asymptote, yet $H_n \to \infty$.
4. **Resolution Limits of Plots:**
   A graphical sketch is constrained by physical pixel resolution and drawing thickness. Discontinuities, jumps, or singularities narrower than the line thickness are completely invisible on any sketch.

---

### Final Answer

1. **Calculated Data:**
   * Sequence $a_n = \frac{4n^2-3n+1}{2n^2+5n-7}$: values increase monotonically from $1.000$ to $1.99935$, approaching $2$.
   * Function $f(x) = \frac{\sin x}{x}$: symmetric two-sided values approach $0.9999998$, approaching $1$.

2. **Epistemological Reason:**
   A table of values or a graph shows only finitely many points and is subject to graphical and numerical resolution limits. It cannot detect high-frequency oscillations (such as $\sin(1/x)$), logarithmic divergence, or behavior past large thresholds. Deductive proof via $\varepsilon$-$\delta$ / $\varepsilon$-$N$ arguments or analytical limit laws is the only rigorous foundation in mathematics.
