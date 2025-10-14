Here is the Python function that solves the problem:

```python
def validate(n):
    n_str = str(n)
    for i in range(10):
        if n_str.count(str(i)) > i:
            return False
    return True
```

This function works by converting the integer to a string, then iterating over the digits 0-9. For each digit, it checks if the count of that digit in the string is greater than the digit itself. If it is, the function immediately returns `False`. If no such digit is found after checking all digits, the function returns `True`.

You can test the function with the provided test case:

```python
print(validate(1234))  # Output: True
```
