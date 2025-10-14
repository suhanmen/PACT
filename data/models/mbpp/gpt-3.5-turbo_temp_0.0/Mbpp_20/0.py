Here's the completed code snippet:

```python
def is_woodall(number):
    """
    Check if the given number is woodall or not.
    A woodall number is a number that can be expressed as n * 2^n - 1, where n is a positive integer.
    """
    n = 1
    while True:
        woodall = n * 2**n - 1
        if woodall == number:
            return True
        elif woodall > number:
            return False
        n += 1

# Test the function
assert is_woodall(383) == True
```

In this code, the `is_woodall` function takes a number as input and checks if it is a woodall number. It uses a while loop to generate woodall numbers starting from n = 1. If the generated woodall number is equal to the input number, it returns True. If the generated woodall number exceeds the input number, it means the input number is not a woodall number, so it returns False.