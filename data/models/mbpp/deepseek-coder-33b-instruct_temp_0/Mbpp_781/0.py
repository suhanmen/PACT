Here is the Python function to check whether the count of divisors is even:

```python
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count % 2 == 0

# Test the function
print(count_divisors(10))  # Output: False
```

This function works by iterating from 1 to the square root of the input number `n`. For each number `i` in this range, if `n` is divisible by `i`, it means `i` and `n/i` are divisors of `n`. If `n/i` is equal to `i`, it means `i` is a perfect square root of `n`, and we only count it once. Otherwise, we count both `i` and `n/i` as divisors. Finally, we check if the count of divisors is even by checking if the count modulo 2 is equal to 0.
