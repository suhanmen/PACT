Here's the completed code snippet:

```
def eulerian_num(n, m):
    # Base cases
    if m >= n or n == 0:
        return 0
    if m == 0:
        return 1

    # Recursive formula
    return (n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)

assert eulerian_num(3, 1) == 4
```

The function `eulerian_num` takes two parameters `n` and `m` representing the Eulerian number to be calculated. It uses a recursive approach to calculate the Eulerian number based on the given formula. The base cases handle the scenarios where `m` is greater than or equal to `n` or `n` is 0. The recursive formula calculates the Eulerian number using the previous Eulerian numbers.

The assertion `assert eulerian_num(3, 1) == 4` checks if the function returns the expected Eulerian number for the given inputs.