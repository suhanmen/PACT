Here is the Python function to join a list of multiple integers into a single integer:

```python
def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

# Test the function
print(multiple_to_single([11, 33, 50]))  # Output: 113350
```

This function works by first converting each integer in the list to a string using the `map` function and `str`. Then it joins all the strings together into a single string using the `join` function. Finally, it converts the resulting string back into an integer using the `int` function.
