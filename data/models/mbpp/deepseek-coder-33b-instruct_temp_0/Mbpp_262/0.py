Here is the Python function that solves the problem:

```python
def split_two_parts(lst, L):
    return (lst[:L], lst[L:])
```

This function uses Python's list slicing feature to split the list into two parts. The first part is from the start of the list to the Lth element (exclusive), and the second part is from the Lth element to the end of the list. The resulting two parts are then returned as a tuple.
