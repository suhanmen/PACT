Here is the completed code snippet:

```python
def first_Digit(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Get the first character of the string
    first_digit = number_str[0]
    
    # Convert the first character back to an integer
    first_digit = int(first_digit)
    
    return first_digit

# Test the function
assert first_Digit(123) == 1
```