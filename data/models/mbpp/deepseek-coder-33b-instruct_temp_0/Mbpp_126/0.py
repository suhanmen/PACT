Here is the Python function to find the sum of common divisors of two given numbers:

```python
def sum_common_divisors(num1, num2):
    def find_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            divisors.extend([i, n // i])
        return list(set(divisors))

    divisors1 = find_divisors(num1)
    divisors2 = find_divisors(num2)
    common_divisors = [i for i in divisors1 if i in divisors2]
    return sum(common_divisors)

print(sum_common_divisors(10, 15))  # Output: 6
```

This function first finds all the divisors of the two given numbers. Then it finds the common divisors by checking if each divisor of the first number is in the list of divisors of the second number. Finally, it returns the sum of the common divisors.
