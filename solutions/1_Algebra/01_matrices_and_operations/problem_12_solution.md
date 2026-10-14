### Essential Formulas

**Matrix Powers:**
For a square matrix $A$, successive powers are computed by repeated multiplication:
$A^2 = A \cdot A$
$A^3 = A^2 \cdot A$
$A^{n+1} = A^n \cdot A$

**Mathematical Induction (Pattern Generalization):**
To prove that a generalized formula holds true for all positive integers $n$:
1. **Conjecture:** Recognize a pattern from the first few cases ($n=1, 2, 3, \dots$).
2. **Assumption:** Assume the formula is correct for an arbitrary integer $n$.
3. **Inductive Step:** Multiply the assumed formula by the base matrix and show that the result perfectly matches the formula for $n+1$.

---

### Problem Statement

**Exercise 12. Formula for a Matrix Power**

Let

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}.
$$

Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

> **Why this exercise:** teaches how to recognize a pattern and formulate a generalization from several computations.

---

### Solution

**Step 1: Compute $A^2$, $A^3$, and $A^4$**

First, compute $A^2 = A \cdot A$:

$$
A^2 = \begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1 + 1\cdot0) & (1\cdot1 + 1\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1)
\end{pmatrix}
= \begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
$$

Next, compute $A^3 = A^2 \cdot A$:

$$
A^3 = \begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1 + 2\cdot0) & (1\cdot1 + 2\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1)
\end{pmatrix}
= \begin{pmatrix}
1 & 3 \\
0 & 1
\end{pmatrix}
$$

Then, compute $A^4 = A^3 \cdot A$:

$$
A^4 = \begin{pmatrix}
1 & 3 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1 + 3\cdot0) & (1\cdot1 + 3\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1)
\end{pmatrix}
= \begin{pmatrix}
1 & 4 \\
0 & 1
\end{pmatrix}
$$

**Step 2: Formulate a conjecture for $A^n$**

Observing the results from Step 1, the main diagonal elements always remain $1$, and the bottom-left element remains $0$. The top-right element perfectly matches the exponent of the matrix power ($2$ for $A^2$, $3$ for $A^3$, $4$ for $A^4$). 

Based on this pattern, we can formulate the following conjecture for any positive integer $n$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1
\end{pmatrix}
$$

**Step 3: Prove the conjecture for $n+1$ (Inductive Step)**

Assume that our formula is true for a specific $n$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1
\end{pmatrix}
$$

To find $A^{n+1}$, we multiply $A^n$ by the original matrix $A$:

$$
A^{n+1} = A^n \cdot A = \begin{pmatrix}
1 & n \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
$$

Now, perform the matrix multiplication:

$$
A^{n+1} = \begin{pmatrix}
(1\cdot1 + n\cdot0) & (1\cdot1 + n\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1)
\end{pmatrix}
$$

$$
A^{n+1} = \begin{pmatrix}
1 & 1 + n \\
0 & 1
\end{pmatrix}
$$

Rearranging $1 + n$ to $n + 1$, we get:

$$
A^{n+1} = \begin{pmatrix}
1 & n+1 \\
0 & 1
\end{pmatrix}
$$

*Explanation:* 
By multiplying the assumed matrix $A^n$ by $A$, the row-by-column multiplication rule specifically adds $1$ to the existing top-right value ($n$), resulting in $n+1$. The $1$s and $0$s act as anchors that preserve the rest of the matrix structure. Because assuming the formula works for $n$ mathematically guarantees it works for $n+1$, and we already know it works for $n=1, 2, 3, 4$, the generalized formula is proven to be correct for all positive integers.
