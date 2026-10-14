# Exercise 3. When Can Matrices Be Multiplied?

## Dimension Compatibility Condition

If matrix $X$ has size $m \times n$ and matrix $Y$ has size $p \times q$, the product $XY$ is defined if and only if $n=p$.

In other words, the number of columns of the first matrix must equal the number of rows of the second matrix. If the product is defined, its size is $m \times q$.

Given

$$
A_{2\times3},\qquad B_{3\times4},\qquad
C_{4\times2},\qquad D_{2\times2},
$$

we examine each product separately.

## 1. Product $AB$

The sizes are $A:2\times3$ and $B:3\times4$.

The inner dimensions are both $3$, so the product is defined.

$$
(2\times\boxed{3})(\boxed{3}\times4)
$$

The result has the outer dimensions $2\times4$.

**Conclusion:** $AB$ is defined and has size $2\times4$.

## 2. Product $BA$

The sizes are $B:3\times4$ and $A:2\times3$.

The inner dimensions are $4$ and $2$, which are not equal. Therefore, the product is not defined.

**Conclusion:** $BA$ is undefined because $4\ne2$.

## 3. Product $BC$

The sizes are $B:3\times4$ and $C:4\times2$.

The inner dimensions are both $4$, so the product is defined.

$$
(3\times\boxed{4})(\boxed{4}\times2)
$$

The result has size $3\times2$.

**Conclusion:** $BC$ is defined and has size $3\times2$.

## 4. Product $CB$

The sizes are $C:4\times2$ and $B:3\times4$.

The inner dimensions are $2$ and $3$, which are not equal. Therefore, the product is not defined.

**Conclusion:** $CB$ is undefined because $2\ne3$.

## 5. Product $AC$

The sizes are $A:2\times3$ and $C:4\times2$.

The inner dimensions are $3$ and $4$, which are not equal. Therefore, the product is not defined.

**Conclusion:** $AC$ is undefined because $3\ne4$.

## 6. Product $CA$

The sizes are $C:4\times2$ and $A:2\times3$.

The inner dimensions are both $2$, so the product is defined.

$$
(4\times\boxed{2})(\boxed{2}\times3)
$$

The result has size $4\times3$.

**Conclusion:** $CA$ is defined and has size $4\times3$.

## 7. Product $AD$

The sizes are $A:2\times3$ and $D:2\times2$.

The inner dimensions are $3$ and $2$, which are not equal. Therefore, the product is not defined.

**Conclusion:** $AD$ is undefined because $3\ne2$.

## 8. Product $DA$

The sizes are $D:2\times2$ and $A:2\times3$.

The inner dimensions are both $2$, so the product is defined.

$$
(2\times\boxed{2})(\boxed{2}\times3)
$$

The result has size $2\times3$.

**Conclusion:** $DA$ is defined and has size $2\times3$.

## Summary Table

| Product | Inner dimensions | Defined? | Result size |
|---|---|---|---|
| $AB$ | $3=3$ | Yes | $2\times4$ |
| $BA$ | $4\ne2$ | No | Not defined |
| $BC$ | $4=4$ | Yes | $3\times2$ |
| $CB$ | $2\ne3$ | No | Not defined |
| $AC$ | $3\ne4$ | No | Not defined |
| $CA$ | $2=2$ | Yes | $4\times3$ |
| $AD$ | $3\ne2$ | No | Not defined |
| $DA$ | $2=2$ | Yes | $2\times3$ |

## Verification

For every defined product, the number of columns of the first matrix equals the number of rows of the second matrix. The result size is obtained from the number of rows of the first matrix and the number of columns of the second matrix.

All eight products satisfy these rules, so the decisions and result sizes are consistent with the dimension compatibility condition.
