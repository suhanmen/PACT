Here's the completed code snippet:

```python
def count_Primes_nums(num):
    count = 0
    for i in range(2, num):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

assert count_Primes_nums(5) == 2
```

This function counts the number of prime numbers less than the given non-negative number by iterating through all numbers from 2 to the given number. For each number, it checks if it is divisible by any number from 2 to the square root of the number. If it is divisible by any number, it is not a prime number and the loop breaks. If it is not divisible by any number, it is a prime number and the count is incremented. Finally, the function returns the count of prime numbers.