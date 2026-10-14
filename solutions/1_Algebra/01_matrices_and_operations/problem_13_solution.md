### Essential Formulas

**Numerical Recurrence (The Fibonacci Sequence):**
A recurrence relation defines the next term in a sequence based on previous terms. The sequence $0, 1, 1, 2, 3, 5, 8, \dots$ is the Fibonacci sequence, where each number is the sum of the two preceding ones. 
If we denote the $n$-th term as $f_n$, the recurrence is defined as:

$$
f_{n+1} = f_n + f_{n-1}
$$

**Matrix Form of Recurrence:**
We can represent the state of the sequence at any step $n$ using a column vector containing two consecutive terms. Multiplying this state vector by a specific transformation matrix generates the next state of the sequence.

---

### Problem Statement

**Exercise 13. A Recurrence Written in Matrix Form**

Let

$$
F = \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}.
$$

Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence

$$
0, 1, 1, 2, 3, 5, 8, \dots
$$

and describe the relationship you observe. Then compute

$$
F \begin{pmatrix}
a \\
b
\end{pmatrix}
$$

and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

> **Why this exercise:** shows the connection between matrix powers and a simple numerical recurrence.

---

### Solution

**Step 1: Compute $F^2, F^3, F^4,$ and $F^5$**

To find $F^2$, multiply $F$ by itself:

$$
F^2 = \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1 + 1\cdot1) & (1\cdot1 + 1\cdot0) \\
(1\cdot1 + 0\cdot1) & (1\cdot1 + 0\cdot0)
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
$$

To find $F^3$, multiply $F^2$ by $F$:

$$
F^3 = \begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
(2\cdot1 + 1\cdot1) & (2\cdot1 + 1\cdot0) \\
(1\cdot1 + 1\cdot1) & (1\cdot1 + 1\cdot0)
\end{pmatrix}
= \begin{pmatrix}
3 & 2 \\
2 & 1
\end{pmatrix}
$$

To find $F^4$, multiply $F^3$ by $F$:

$$
F^4 = \begin{pmatrix}
3 & 2 \\
2 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
(3\cdot1 + 2\cdot1) & (3\cdot1 + 2\cdot0) \\
(2\cdot1 + 1\cdot1) & (2\cdot1 + 1\cdot0)
\end{pmatrix}
= \begin{pmatrix}
5 & 3 \\
3 & 2
\end{pmatrix}
$$

To find $F^5$, multiply $F^4$ by $F$:

$$
F^5 = \begin{pmatrix}
5 & 3 \\
3 & 2
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
(5\cdot1 + 3\cdot1) & (5\cdot1 + 3\cdot0) \\
(3\cdot1 + 2\cdot1) & (3\cdot1 + 2\cdot0)
\end{pmatrix}
= \begin{pmatrix}
8 & 5 \\
5 & 3
\end{pmatrix}
$$

**Step 2: Compare with the sequence and describe the relationship**

Let's align the entries of our matrices with the given Fibonacci sequence $(0, 1, 1, 2, 3, 5, 8, \dots)$.
Let $f_0 = 0, f_1 = 1, f_2 = 1, f_3 = 2, f_4 = 3, f_5 = 5, f_6 = 8$.

Looking at the matrices:
*   $F^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} f_2 & f_1 \\ f_1 & f_0 \end{pmatrix}$
*   $F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} f_3 & f_2 \\ f_2 & f_1 \end{pmatrix}$
*   $F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} f_4 & f_3 \\ f_3 & f_2 \end{pmatrix}$
*   $F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} f_5 & f_4 \\ f_4 & f_3 \end{pmatrix}$
*   $F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} f_6 & f_5 \\ f_5 & f_4 \end{pmatrix}$

*Relationship Observation:* The entries of the matrix $F^n$ consist entirely of consecutive terms from the Fibonacci sequence. The top-left entry is the $(n+1)$-th Fibonacci number, the top-right and bottom-left entries are identical and represent the $n$-th number, and the bottom-right is the $(n-1)$-th number.

**Step 3: Compute the matrix-vector multiplication**

Multiply matrix $F$ by a column vector containing arbitrary variables $a$ and $b$:

$$
F \begin{pmatrix}
a \\
b
\end{pmatrix}
= \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
a \\
b
\end{pmatrix}
= \begin{pmatrix}
1\cdot a + 1\cdot b \\
1\cdot a + 0\cdot b
\end{pmatrix}
= \begin{pmatrix}
a + b \\
a
\end{pmatrix}
$$

**Step 4: Explain the recurrence step**

If we assume the vector $\begin{pmatrix} a \\ b \end{pmatrix}$ represents the current state of a sequence (where $a$ is the current term and $b$ is the previous term), the multiplication by $F$ updates the vector for the next step. 

The top row of the resulting vector evaluates to $a + b$, successfully creating the next term by summing the two consecutive terms. The bottom row evaluates simply to $a$, which takes the "current" term from the old vector and shifts it down to become the "previous" term for the new vector. By repeatedly multiplying by $F$, the matrix systematically shifts the window of terms forward, effectively generating the Fibonacci sequence algebraically.
