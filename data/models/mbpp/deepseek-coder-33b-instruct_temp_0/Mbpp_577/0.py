Here is the Python function to find the last digit in factorial of a given number:

```python
def last_Digit_Factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        while factorial % 10 == 0:  # remove trailing zeros
            factorial //= 10
        factorial %= 10  # keep only the last digit
    return factorial % 10

print(last_Digit_Factorial(4))  # Output: 4
```

This function calculates the factorial of a number by multiplying all the numbers from 1 to the given number. It then removes any trailing zeros from the factorial and keeps only the last digit. The last digit of the factorial is then returned.
