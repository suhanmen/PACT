Here is the Python function implemented in a markdown style code block:

```python
def sum_range_list(lst, start, end):
    """
    Write a function to find the sum of numbers in a list within a range specified by two indices.
    """
    return sum(lst[start:end+1])

# Test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
```

This function takes a list and two indices as input. It uses Python's list slicing feature to get the sublist between the two indices (inclusive), and then uses the built-in `sum` function to calculate the sum of the numbers in this sublist.
