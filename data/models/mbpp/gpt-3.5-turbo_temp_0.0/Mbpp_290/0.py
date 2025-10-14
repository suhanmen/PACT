Here is the completed code snippet:

```python
def max_length(lst):
    max_len = 0
    max_list = []
    for sublist in lst:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return max_len, max_list

assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
```

The `max_length` function takes a list of lists as input and iterates over each sublist. It keeps track of the maximum length found so far and the corresponding sublist. If a sublist with a greater length is found, the maximum length and sublist are updated. Finally, the function returns a tuple containing the maximum length and the sublist with that length.

The `assert` statement checks if the function returns the expected result for the given example input.