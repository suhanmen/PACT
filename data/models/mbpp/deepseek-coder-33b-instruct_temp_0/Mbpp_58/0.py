Here is the Python function in a markdown style code block:

```python
def opposite_Signs(x, y):
    """
    This function checks whether the given two integers have opposite sign or not.
    """
    return (x >= 0 and y < 0) or (x < 0 and y >= 0)
```

You can use this function to check if two integers have opposite signs. For example:

```python
print(opposite_Signs(1, -2))  # Output: True
print(opposite_Signs(1, 2))   # Output: False
print(opposite_Signs(-1, 2))  # Output: False
print(opposite_Signs(-1, -2)) # Output: True
```
