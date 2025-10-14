Here is the Python function to remove odd characters in a string:

```python
def remove_odd(input_string):
    return input_string[1::2]

print(remove_odd("python"))  # Output: yhn
```

This function works by using Python's string slicing feature. The `[1::2]` slice means "start at index 1 and take every second character". This effectively removes the odd-indexed characters from the string.
