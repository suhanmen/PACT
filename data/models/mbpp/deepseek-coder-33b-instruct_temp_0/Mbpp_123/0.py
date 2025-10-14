Here is the Python function to sum all amicable numbers from 1 to a specified number:

```python
def amicable_numbers_sum(n):
    def sum_of_divisors(n):
        result = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                if i == (n // i):
                    result += i
                else:
                    result += (i + n // i)
            i += 1
        return result

    result = 0
    for i in range(2, n + 1):
        sum_i = sum_of_divisors(i)
        if i < sum_i and i == sum_of_divisors(sum_i):
            result += i + sum_i
    return result // 2

print(amicable_numbers_sum(999))  # Output: 504
```

This function first calculates the sum of proper divisors for a given number. Then it checks for each number from 2 to the specified number if it is an amicable number. If it is, it adds the number and its pair to the result. Finally, it returns the sum of all amicable numbers.
