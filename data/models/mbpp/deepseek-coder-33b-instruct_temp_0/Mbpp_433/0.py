Here is the Python function implemented in a markdown style code block:

```python
def check_greater(arr, num):
    """
    This function checks whether the entered number is greater than the elements of the given array.
    """
    for i in arr:
        if i > num:
            return False
    return True
```

You can test the function with the following code:

```python
print(check_greater([1, 2, 3, 4, 5], 4))  # Output: False
```

This function works by iterating over each element in the array. If it finds an element that is greater than the input number, it immediately returns `False`. If it doesn't find any such element, it returns `True`.
