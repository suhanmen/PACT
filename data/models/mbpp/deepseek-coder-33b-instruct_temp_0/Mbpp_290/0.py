Here is the Python function implemented in a markdown style code block:

```python
def max_length(list_of_lists):
    """
    Write a function to find the list of maximum length in a list of lists.
    """
    max_len = -1
    max_list = []
    for lst in list_of_lists:
        if len(lst) > max_len:
            max_len = len(lst)
            max_list = lst
    return max_len, max_list
```

You can test the function with the provided assertion:

```python
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
```

This function works by iterating over each list in the input list of lists. If the length of the current list is greater than the current maximum length, it updates the maximum length and the list associated with that length. At the end of the function, it returns a tuple containing the maximum length and the list with that length.
