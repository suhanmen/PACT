Here is the completed code snippet:

```python
def find_solution(a, b, n):
    for x in range(n+1):
        for y in range(n+1):
            if a*x + b*y == n:
                return (x, y)
    return None

assert find_solution(2, 3, 7) == (2, 1)
```

This code defines a function `find_solution` that takes three parameters: `a`, `b`, and `n`. It uses nested loops to iterate through all possible values of `x` and `y` within the range of `n+1`. For each combination of `x` and `y`, it checks if `ax + by` equals `n`. If a solution is found, it returns a tuple `(x, y)`. If no solution is found, it returns `None`.

The `assert` statement at the end of the code snippet verifies that the function returns the expected result for the given example.