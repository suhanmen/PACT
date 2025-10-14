Here is the Python function that solves the problem:

```python
def square_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**2
    return sum
```

This function works by iterating over the first `n` even numbers, squaring each one, and adding it to the sum. The `range` function is used to generate the sequence of even numbers, starting from `2` and incrementing by `2` each time. The `**` operator is used to square each number.

You can test the function with the provided test case:

```python
assert square_Sum(2) == 20
```

This should return `None`, indicating that the test case passed.
