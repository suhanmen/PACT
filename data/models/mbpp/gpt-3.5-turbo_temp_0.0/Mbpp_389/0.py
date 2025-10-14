Here's the completed code snippet:

```python
def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = [2, 1]
        for i in range(2, n+1):
            lucas.append(lucas[i-1] + lucas[i-2])
        return lucas[n]

assert find_lucas(9) == 76
```

In this code, we define a function `find_lucas` that takes an integer `n` as input and returns the n'th Lucas number. The Lucas numbers are a series of numbers in which each number is the sum of the two preceding numbers, similar to the Fibonacci sequence.

The function first checks if `n` is 0 or 1, in which case it directly returns the corresponding Lucas number (2 and 1, respectively). For any other value of `n`, the function initializes a list `lucas` with the first two Lucas numbers (2 and 1). Then, it uses a loop to calculate the remaining Lucas numbers up to the n'th number. Each new number is the sum of the two preceding numbers in the list. Finally, the function returns the n'th Lucas number.

The `assert` statement at the end of the code snippet verifies that `find_lucas(9)` returns the expected result of 76.