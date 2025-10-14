Here is the Python function implemented in a markdown style code block:

```python
def find_substring(list_of_strings, substring):
    """
    This function checks if a substring is present in a given list of string values.
    """
    for string in list_of_strings:
        if substring in string:
            return True
    return False
```

You can test the function with the following code:

```python
print(find_substring(["red", "black", "white", "green", "orange"],"ack"))
```

This should return `True` as "ack" is a substring of "black".
