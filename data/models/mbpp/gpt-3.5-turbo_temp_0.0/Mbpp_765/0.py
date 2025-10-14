Here's the completed code snippet:

```python
def is_polite(n):
    count = 0
    num = 1

    while count < n:
        if is_polite_number(num):
            count += 1
        num += 1

    return num - 1


def is_polite_number(num):
    if num == 1:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


assert is_polite(7) == 11
```

The `is_polite` function takes an integer `n` as input and returns the nth polite number. It uses a while loop to iterate through numbers starting from 1 until it finds the nth polite number. The `is_polite_number` function is a helper function that checks if a number is polite. It returns True if the number is polite (i.e., it is not divisible by any number other than 1 and itself), and False otherwise. The assert statement at the end verifies that the function returns the correct result for the given example.