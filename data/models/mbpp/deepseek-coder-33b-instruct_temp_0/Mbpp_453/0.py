Here is the Python function to find the sum of even factors of a number:

```python
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum
```

You can test the function with the following code:

```python
print(sumofFactors(18))  # Output: 26
```

This function works by iterating over all numbers from 1 to n (inclusive) and checking if they are factors of n (i.e., if n is divisible by the current number). If the current number is both a factor of n and an even number, it is added to the sum.
