Here is the Python function to return the sum of all divisors of a number:

```python
def sum_div(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum
```

You can test the function with the following code:

```python
print(sum_div(8))  # Output: 15
```

This function works by iterating over all numbers from 1 to n (inclusive) and checking if n is divisible by the current number. If it is, the current number is added to the sum. The function finally returns the sum.
