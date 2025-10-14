Here is the Python function implemented in a markdown style code block:

```python
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(int(digit) != 0 and num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result

print(divisible_by_digits(1,22))
```

This function works by iterating over each number in the given range. For each number, it checks if the number is divisible by every digit it contains. If it is, the number is added to the result list. The function finally returns the result list.

The `all()` function is used to check if all digits of the number are divisible by the number. The `int(digit) != 0` condition is used to avoid division by zero.

The `str(num)` function is used to convert the number to a string so that we can iterate over its digits. The `int(digit)` function is used to convert each digit back to an integer so that we can perform the division operation.

The `num % int(digit) == 0` condition checks if the number is divisible by the digit. If it is, the `all()` function will return `True` for that number. If it is not, the `all()` function will return `False` for that number.
