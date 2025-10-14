Here is the Python function to count the number of lists in a given number of lists:

```python
def count_list(lst):
    """
    This function counts the number of lists in a given number of lists.
    """
    count = 0
    for i in lst:
        if isinstance(i, list):
            count += 1
    return count

# Test the function
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
```

In this function, we iterate over each element in the given list. If the element is a list itself, we increment the count. Finally, we return the count.
