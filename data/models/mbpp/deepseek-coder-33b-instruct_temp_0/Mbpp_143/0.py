Here is the Python function implemented in a markdown style code block:

```python
def find_lists(tup):
    """
    Write a function to find number of lists present in the given tuple.
    """
    count = 0
    for item in tup:
        if isinstance(item, list):
            count += 1
    return count

# Test the function
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
```

In this function, we iterate over each item in the tuple. If the item is a list, we increment the count. Finally, we return the count. The `isinstance` function is used to check if an item is a list.
