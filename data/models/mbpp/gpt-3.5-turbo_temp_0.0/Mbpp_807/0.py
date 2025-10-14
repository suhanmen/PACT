Here is the completed code snippet:

```python
def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None

# Test the function
assert first_odd([1,3,5]) == 1
```

The `first_odd` function takes a list of numbers as input and iterates through each number. It checks if the number is odd by using the modulo operator `%` to check if the number divided by 2 has a remainder. If the number is odd, it is returned. If no odd number is found, the function returns `None`.