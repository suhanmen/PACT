Here is the Python function that counts the number of prime numbers less than a given non-negative number:

```python
def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
```

You can test the function with the following code:

```python
print(count_Primes_nums(5))  # Output: 2
```

This function works by first defining a helper function `is_prime(num)` that checks if a number is prime. It then iterates over all numbers less than `n`, checks if each number is prime, and increments a counter if it is. The function finally returns the counter.
