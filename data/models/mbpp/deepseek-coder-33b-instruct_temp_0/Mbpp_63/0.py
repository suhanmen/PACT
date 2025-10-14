Here is the Python function implemented in a markdown style code block:

```python
def max_difference(tuple_list):
    """
    Write a function to find the maximum difference between available pairs in the given tuple list.
    """
    max_diff = 0
    for tup in tuple_list:
        diff = abs(tup[0] - tup[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

# Test the function
print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))  # Output: 7
```

This function works by iterating over each tuple in the list, calculating the absolute difference between the two elements in the tuple, and updating the maximum difference found so far if the current difference is greater. The function finally returns the maximum difference found.
