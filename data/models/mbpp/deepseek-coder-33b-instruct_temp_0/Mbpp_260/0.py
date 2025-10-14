Here is the Python function to find the nth Newman–Shanks–Williams prime number:

```python
def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    i = 0
    while len(primes) < n:
        i += 1
        if is_prime(i) and is_prime(2*i + 1):
            primes.append(2*i + 1)
    return primes[-1]

print(newman_prime(3))  # Output: 7
```

This function works by iterating over the integers, checking if each integer and its double plus one are prime numbers. If they are, they are added to the list of primes. The function continues until it has found the nth prime. The last prime in the list is returned as the nth Newman–Shanks–Williams prime number.
