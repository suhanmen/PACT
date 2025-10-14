Here is the completed code snippet:

```python
def number_ctr(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

assert number_ctr('program2bedone') == 1
```

The `number_ctr` function takes a string as input and initializes a count variable to 0. It then iterates through each character in the string and checks if the character is a digit using the `isdigit()` method. If the character is a digit, the count variable is incremented by 1. Finally, the function returns the count of digits in the string.

The assert statement at the end of the code snippet verifies that the function returns the expected result for the given example.