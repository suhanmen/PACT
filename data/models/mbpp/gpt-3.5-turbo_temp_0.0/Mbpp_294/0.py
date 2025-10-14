Here is the completed code snippet:

```python
def max_val(lst):
    max_value = None
    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            if max_value is None or item > max_value:
                max_value = item
    return max_value

assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
```

In this code, the `max_val` function takes a list as input and iterates over each item in the list. It checks if the item is an integer or a float using the `isinstance` function. If it is, it compares the item with the current maximum value (`max_value`) and updates `max_value` if necessary. Finally, it returns the maximum value found in the list.

The `assert` statement at the end of the code verifies that the function returns the expected result for the given example.