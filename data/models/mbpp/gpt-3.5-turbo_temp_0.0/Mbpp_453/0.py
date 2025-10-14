Here's the completed code snippet:

```python
def sumofFactors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0 and i % 2 == 0:
            factors.append(i)
    return sum(factors)

assert sumofFactors(18) == 26
```

In this code, we define a function `sumofFactors` that takes a number `num` as input. We initialize an empty list `factors` to store the even factors of `num`. 

We then iterate through the numbers from 1 to `num` using a for loop. For each number `i`, we check if it is a factor of `num` (i.e., `num % i == 0`) and if it is even (i.e., `i % 2 == 0`). If both conditions are true, we append `i` to the `factors` list.

Finally, we return the sum of the `factors` list using the `sum()` function.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example.