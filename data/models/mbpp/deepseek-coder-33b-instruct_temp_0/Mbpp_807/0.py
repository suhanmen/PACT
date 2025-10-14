Here is the Python function to find the first odd number in a given list of numbers:

```python
def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None
```

This function iterates over each number in the list. If the number is odd (i.e., its remainder when divided by 2 is not zero), it returns that number. If no odd number is found after checking all numbers, it returns None.
