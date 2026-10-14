### Essential Formulas

**Trigonometric Angle-Sum Identities:**
To simplify the product of the rotation matrices, we need the fundamental angle-sum formulas for sine and cosine:

$$
\cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha \sin\beta
$$

$$
\sin(\alpha + \beta) = \sin\alpha \cos\beta + \cos\alpha \sin\beta
$$

**Rotation Matrix:**
A rotation matrix $R(\theta)$ rotates a vector in the Euclidean plane by an angle $\theta$ counterclockwise relative to the origin.

---

### Problem Statement

**Exercise 14. Rotation Matrices**

The matrix for a rotation through an angle $\theta$ is

$$
R(\theta)= \begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}.
$$

Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that

$$
R(\alpha)R(\beta)=R(\alpha+\beta).
$$

Explain the result geometrically.

> **Why this exercise:** shows the consistency between matrix algebra and the geometry of composing rotations.

---

### Solution

**Step 1: Compute the matrix product $R(\alpha)R(\beta)$**

Set up the multiplication of the two rotation matrices:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}
\begin{pmatrix}
\cos\beta & -\sin\beta \\
\sin\beta & \cos\beta
\end{pmatrix}
$$

Calculate each entry by multiplying the rows of $R(\alpha)$ by the columns of $R(\beta)$:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
(\cos\alpha \cos\beta - \sin\alpha \sin\beta) & (-\cos\alpha \sin\beta - \sin\alpha \cos\beta) \\
(\sin\alpha \cos\beta + \cos\alpha \sin\beta) & (-\sin\alpha \sin\beta + \cos\alpha \cos\beta)
\end{pmatrix}
$$

**Step 2: Apply the angle-sum formulas**

We can factor out the negative sign in the top-right entry to make the pattern clearer:

$$
-\cos\alpha \sin\beta - \sin\alpha \cos\beta = -(\sin\alpha \cos\beta + \cos\alpha \sin\beta)
$$

Now, substitute the angle-sum identities into the matrix:
*   **Top-left:** $\cos\alpha \cos\beta - \sin\alpha \sin\beta = \cos(\alpha + \beta)$
*   **Top-right:** $-(\sin\alpha \cos\beta + \cos\alpha \sin\beta) = -\sin(\alpha + \beta)$
*   **Bottom-left:** $\sin\alpha \cos\beta + \cos\alpha \sin\beta = \sin(\alpha + \beta)$
*   **Bottom-right:** $\cos\alpha \cos\beta - \sin\alpha \sin\beta = \cos(\alpha + \beta)$

Replacing the entries in the matrix gives:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos(\alpha + \beta) & -\sin(\alpha + \beta) \\
\sin(\alpha + \beta) & \cos(\alpha + \beta)
\end{pmatrix}
$$

**Step 3: Show the final equality**

By the definition of the rotation matrix $R(\theta)$, a rotation by the angle $(\alpha + \beta)$ is written as:

$$
R(\alpha+\beta) = \begin{pmatrix}
\cos(\alpha + \beta) & -\sin(\alpha + \beta) \\
\sin(\alpha + \beta) & \cos(\alpha + \beta)
\end{pmatrix}
$$

Therefore, we have successfully mathematically shown that:

$$
R(\alpha)R(\beta) = R(\alpha+\beta)
$$

**Step 4: Geometric Explanation**

Matrix multiplication represents the composition of linear transformations. 
Multiplying a vector by $R(\beta)$ rotates it counterclockwise by an angle $\beta$. Multiplying that new result by $R(\alpha)$ rotates it further counterclockwise by an angle $\alpha$. 
Geometrically, rotating an object by $\beta$ and then immediately rotating it by $\alpha$ from its new position is completely identical to performing a single, continuous rotation by the total combined angle of $\alpha + \beta$. The algebraic proof perfectly confirms this intuitive geometric reality.
