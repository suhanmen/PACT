Here is the Python function to check if a string represents an integer or not:

```python
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

This function uses a try-except block to attempt to convert the string to an integer. If the conversion is successful, the function returns True. If a ValueError is raised during the conversion (which happens when the string cannot be converted to an integer), the function returns False.
