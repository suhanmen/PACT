Here is the Python function to get the first element of each sublist:

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]
```

You can test this function with the provided test case:

```python
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
```

This function uses a list comprehension to iterate over each sublist in the input list, and extract the first element of each sublist. The result is a new list containing the first elements of each sublist.
