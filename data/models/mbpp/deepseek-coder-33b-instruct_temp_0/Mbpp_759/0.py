Here is the Python function implemented in a markdown style code block:

```python
def is_decimal(s):
    try:
        float(s)
        if s.count('.') == 1 and len(s.split('.')[-1]) == 2:
            return True
        else:
            return False
    except ValueError:
        return False
```

This function first tries to convert the input string to a float. If this fails, it means the string is not a valid decimal number and the function returns False. If the conversion is successful, it checks if the string contains exactly one decimal point and exactly two digits after the decimal point. If these conditions are met, the function returns True, otherwise it returns False.
