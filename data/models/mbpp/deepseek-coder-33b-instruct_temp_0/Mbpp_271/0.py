Here is the Python function that solves the problem:

```python
def even_Power_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i ** 5
    return sum
```

This function works by iterating over the first `n` even numbers (starting from 2, incrementing by 2 each time) and adding the fifth power of each number to a running total. The function then returns this total.

You can test the function with the provided test case:

```python
print(even_Power_Sum(2))  # Output: 1056
```

This should print `1056`, which is the sum of the first two even numbers (2 and 4) raised to the fifth power.
