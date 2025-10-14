Here is the Python function implemented in a markdown style code block:

```python
def check_element(lst, element):
    return all(item == element for item in lst)

# Test the function
print(check_element(["green", "orange", "black", "white"],'blue'))
```

In this function, we use the `all()` function in combination with a generator expression to check if all elements in the list are equal to the given element. The `all()` function returns `True` if all elements in the iterable (in this case, the generator expression) are `True`, and `False` otherwise.

The generator expression `(item == element for item in lst)` generates a sequence of `True` or `False` values, one for each item in the list. If all items are equal to the given element, the `all()` function will return `True`, otherwise it will return `False`.
