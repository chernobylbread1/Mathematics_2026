### Essential Formulas

**Composition of Transformations:**
Applying a transformation $T_1$ followed by a transformation $T_2$ to a vector $x$ is represented by the matrix multiplication $T_2 T_1 x$. The transformation closest to the vector is applied first. 
Matrix multiplication is generally **non-commutative**, meaning $AB \neq BA$. In geometric terms, the order in which transformations (like scaling and rotation) are applied usually changes the final position of the vector.

---

### Problem Statement

**Exercise 9. Composing Transformations**

Let

$$
S= \begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix},\qquad R= \begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}.
$$

The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For

$$
x= \begin{pmatrix}
1 \\
2
\end{pmatrix}
$$

compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

> **Why this exercise:** interprets matrix multiplication as composition of transformations.

---

### Solution

**Step 1: Compute $RSx$ (Scale first, then Rotate)**
First, apply the scaling matrix $S$ to vector $x$:

$$
Sx = \begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 \\
2
\end{pmatrix}
= \begin{pmatrix}
2\cdot1 + 0\cdot2 \\
0\cdot1 + 1\cdot2
\end{pmatrix}
= \begin{pmatrix}
2 \\
2
\end{pmatrix}
$$

Next, apply the rotation matrix $R$ to the resulting vector $Sx$:

$$
R(Sx) = \begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
2 \\
2
\end{pmatrix}
= \begin{pmatrix}
0\cdot2 + (-1)\cdot2 \\
1\cdot2 + 0\cdot2
\end{pmatrix}
= \begin{pmatrix}
-2 \\
2
\end{pmatrix}
$$

Thus, $RSx = \begin{pmatrix} -2 \\ 2 \end{pmatrix}$.

**Step 2: Compute $SRx$ (Rotate first, then Scale)**
First, apply the rotation matrix $R$ to vector $x$:

$$
Rx = \begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
1 \\
2
\end{pmatrix}
= \begin{pmatrix}
0\cdot1 + (-1)\cdot2 \\
1\cdot1 + 0\cdot2
\end{pmatrix}
= \begin{pmatrix}
-2 \\
1
\end{pmatrix}
$$

Next, apply the scaling matrix $S$ to the resulting vector $Rx$:

$$
S(Rx) = \begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
-2 \\
1
\end{pmatrix}
= \begin{pmatrix}
2\cdot(-2) + 0\cdot1 \\
0\cdot(-2) + 1\cdot1
\end{pmatrix}
= \begin{pmatrix}
-4 \\
1
\end{pmatrix}
$$

Thus, $SRx = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$.

**Step 3: Comparison and Geometric Explanation**

Comparing the results, we can clearly see that $RSx \neq SRx$:

$$
\begin{pmatrix}
-2 \\
2
\end{pmatrix}
\neq
\begin{pmatrix}
-4 \\
1
\end{pmatrix}
$$

*Geometric Explanation:*
The order matters because the scaling matrix $S$ is non-uniform (it stretches only the x-axis by a factor of 2 and leaves the y-axis unchanged). 
* When computing **$RSx$**, we first stretch the vector's x-component. The original vector $(1, 2)$ becomes $(2, 2)$. Rotating this new vector $90^\circ$ counterclockwise maps the positive x-component to the negative y-axis, resulting in $(-2, 2)$.
* When computing **$SRx$**, we rotate the original vector $(1, 2)$ first, which moves it to $(-2, 1)$. Now, the vector's primary magnitude is aligned with the negative x-axis. When we apply the non-uniform scaling $S$ (which doubles only the x-coordinate), it doubles this new horizontal length, resulting in a much wider vector stretch: $(-4, 1)$.

Because the rotation changes the orientation of the vector relative to the axes, applying a non-uniform, axis-specific stretch *after* the rotation affects completely different geometric proportions than applying it *before*.
