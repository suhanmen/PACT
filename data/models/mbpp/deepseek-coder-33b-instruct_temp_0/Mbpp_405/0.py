Here is the Python function implemented in a markdown style code block:

```python
def check_tuplex(tuplex, element):
    """
    Write a function to check whether an element exists within a tuple.
    """
    return element in tuplex

# Test the function
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r'))
```

This function `check_tuplex` takes a tuple and an element as input. It uses the `in` operator to check if the element exists in the tuple. If the element is found, it returns `True`, otherwise it returns `False`.

The test case `check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')` should return `True`.
