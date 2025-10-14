Here is the Python function to interchange the first and last elements in a list:

```python
def swap_List(list):
    list[0], list[-1] = list[-1], list[0]
    return list
```

You can test this function with the following code:

```python
print(swap_List([12, 35, 9, 56, 24]))  # Output: [24, 35, 9, 56, 12]
```

This function works by using Python's list indexing feature to swap the first and last elements of the list. The `list[0]` and `list[-1]` are the first and last elements of the list, respectively. The `list[0], list[-1] = list[-1], list[0]` line swaps these two elements.
