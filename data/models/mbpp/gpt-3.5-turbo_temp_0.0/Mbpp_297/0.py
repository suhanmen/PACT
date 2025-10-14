Here is the completed code snippet:

```python
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```

The `flatten_list` function takes a nested list as input and returns a flattened version of the list. It uses recursion to handle nested lists within the input list. The function checks each item in the input list, and if the item is a list, it recursively calls `flatten_list` on that item and extends the flattened result to the `flattened_list`. If the item is not a list, it is directly appended to the `flattened_list`. Finally, the function returns the `flattened_list`.

The `assert` statement at the end of the code snippet verifies that the `flatten_list` function produces the expected output for the given example input.