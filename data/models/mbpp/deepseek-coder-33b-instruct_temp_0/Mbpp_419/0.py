Here is the Python function that solves the problem:

```python
def round_and_sum(numbers):
    total = sum(round(num) for num in numbers)
    return total * len(numbers)
```

You can test the function with the given example:

```python
print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
```

This should print `243`, which is the expected result.
