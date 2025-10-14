Here is the completed code snippet:

```python
def sum_digits(n):
    """
    Function to get the sum of the digits of a non-negative integer.
    """
    # Convert the integer to a string
    num_str = str(n)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each character in the string
    for digit in num_str:
        # Convert the character back to an integer and add it to the sum
        digit_sum += int(digit)
    
    # Return the sum of digits
    return digit_sum

# Test the function
assert sum_digits(345) == 12
```

The `sum_digits` function takes a non-negative integer as input and converts it to a string. It then iterates through each character in the string, converts it back to an integer, and adds it to the `digit_sum` variable. Finally, it returns the sum of digits. The code includes an assertion to test the function with the example given in the prompt.