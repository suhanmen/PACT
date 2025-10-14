Here is the Python function implemented in a markdown style code block:

```python
def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum
```

You can test the function with the following code:

```python
print(square_Sum(2))  # Output: 10
```

This function works by iterating over the first `n` odd natural numbers (which are `2*n` numbers apart by `2`) and adding the square of each number to the sum. The `range` function is used to generate the sequence of numbers, and the `**` operator is used to square each number.
