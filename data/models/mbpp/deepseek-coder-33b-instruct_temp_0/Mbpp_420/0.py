Here is the Python function to find the cube sum of first n even natural numbers:

```python
def cube_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i ** 3
    return sum
```

You can test the function with the following code:

```python
print(cube_Sum(2))  # Output: 72
```

This function works by iterating over the first `n` even natural numbers (starting from 2, incrementing by 2 each time) and adding the cube of each number to a running total. The total is then returned.
