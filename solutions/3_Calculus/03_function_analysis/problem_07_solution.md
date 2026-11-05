### Essential Formulas

1. **Trigonometric Derivative Rules:**

   $$
   \frac{d}{dx}[\sin x] = \cos x, \qquad \frac{d}{dx}[\cos x] = -\sin x
   $$

2. **Harmonic Addition Identity:**

   $$
   \sin x + \cos x = \sqrt{2} \left(\frac{1}{\sqrt{2}} \sin x + \frac{1}{\sqrt{2}} \cos x\right) = \sqrt{2} \sin\left(x + \frac{\pi}{4}\right)
   $$

3. **Global Extrema on a Closed Bounded Interval:**
   By the Extreme Value Theorem, a continuous function on $[a, b]$ attains its absolute maximum and minimum. Candidates for absolute extrema are:
   * Interior critical points where $f'(x) = 0$.
   * Endpoints of the interval ($x = a$ and $x = b$).

---

### Problem Statement

On $[0,2\pi]$, find the intervals of monotonicity and the extrema of

$$
f(x)=\sin x+\cos x.
$$

Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

> **Why this problem:** it practices the analysis of a periodic function on a bounded interval.

---

### Solution

**Step 1: Compute the derivative and identify critical points**

The function is $f(x) = \sin x + \cos x$ on the closed domain $[0, 2\pi]$.
Differentiate term by term:

$$
f'(x) = \cos x - \sin x
$$

Set $f'(x) = 0$ to locate stationary points in the open interval $(0, 2\pi)$:

$$
\cos x - \sin x = 0 \iff \cos x = \sin x
$$

Since $\cos x \neq 0$ at points where $\cos x = \sin x$, divide both sides by $\cos x$:

$$
\tan x = 1
$$

Within the interval $[0, 2\pi]$, the equation $\tan x = 1$ has two solutions:
* In the first quadrant:

  $$
  x_1 = \frac{\pi}{4}
  $$

* In the third quadrant:

  $$
  x_2 = \frac{5\pi}{4}
  $$

---

**Step 2: Determine the intervals of monotonicity**

The critical points partition $[0, 2\pi]$ into three subintervals:
1. **Interval $\left[0, \frac{\pi}{4}\right)$:**
   Test at $x = 0$:

   $$
   f'(0) = \cos(0) - \sin(0) = 1 - 0 = 1 > 0
   $$

   Thus $f'(x) > 0$: the function is strictly increasing on $\left[0, \frac{\pi}{4}\right]$.

2. **Interval $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$:**
   Test at $x = \pi$:

   $$
   f'(\pi) = \cos(\pi) - \sin(\pi) = -1 - 0 = -1 < 0
   $$

   Thus $f'(x) < 0$: the function is strictly decreasing on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.

3. **Interval $\left(\frac{5\pi}{4}, 2\pi\right]$:**
   Test at $x = 2\pi$:

   $$
   f'(2\pi) = \cos(2\pi) - \sin(2\pi) = 1 - 0 = 1 > 0
   $$

   Thus $f'(x) > 0$: the function is strictly increasing on $\left[\frac{5\pi}{4}, 2\pi\right]$.

---

**Step 3: Evaluate function values at critical points and endpoints**

1. **Left Endpoint ($x = 0$):**

   $$
   f(0) = \sin(0) + \cos(0) = 0 + 1 = 1
   $$

2. **First Critical Point $\left(x = \frac{\pi}{4}\right)$:**

   $$
   f\left(\frac{\pi}{4}\right) = \sin\left(\frac{\pi}{4}\right) + \cos\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} \approx 1.4142
   $$

3. **Second Critical Point $\left(x = \frac{5\pi}{4}\right)$:**

   $$
   f\left(\frac{5\pi}{4}\right) = \sin\left(\frac{5\pi}{4}\right) + \cos\left(\frac{5\pi}{4}\right) = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} \approx -1.4142
   $$

4. **Right Endpoint ($x = 2\pi$):**

   $$
   f(2\pi) = \sin(2\pi) + \cos(2\pi) = 0 + 1 = 1
   $$

---

**Step 4: Classification and comparison**

* **Global Maximum:**
  Comparing all candidate values ($\{1, \sqrt{2}, -\sqrt{2}\}$), the largest value is $\sqrt{2}$.
  The function attains its absolute (and local) maximum at $x = \frac{\pi}{4}$, with value $\sqrt{2}$.
* **Global Minimum:**
  The smallest value is $-\sqrt{2}$.
  The function attains its absolute (and local) minimum at $x = \frac{5\pi}{4}$, with value $-\sqrt{2}$.
* **Endpoint Status:**
  * At $x = 0$, $f(0) = 1$. Because $f$ increases immediately to the right, $x = 0$ is a relative endpoint minimum.
  * At $x = 2\pi$, $f(2\pi) = 1$. Because $f$ increases leading up to $2\pi$, $x = 2\pi$ is a relative endpoint maximum.
  * Both endpoint values ($1$) lie strictly between the global minimum ($-\sqrt{2}$) and the global maximum ($\sqrt{2}$).

---

### Final Answer

1. **Monotonicity:**
   * Strictly increasing on $\left[0, \frac{\pi}{4}\right]$ and on $\left[\frac{5\pi}{4}, 2\pi\right]$
   * Strictly decreasing on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$

2. **Extrema on $[0, 2\pi]$:**
   * **Global Maximum:** at $x = \frac{\pi}{4}$ with value $f\left(\frac{\pi}{4}\right) = \sqrt{2}$
   * **Global Minimum:** at $x = \frac{5\pi}{4}$ with value $f\left(\frac{5\pi}{4}\right) = -\sqrt{2}$

3. **Comparison with Endpoints:**
   * Endpoints: $f(0) = 1$ and $f(2\pi) = 1$
   * Both endpoint values satisfy $-\sqrt{2} < 1 < \sqrt{2}$, confirming that the absolute extrema occur strictly in the interior of the interval at the stationary points.
