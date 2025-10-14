Here is the Python function implemented in a markdown style code block:

```python
def big_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return max(arr) + min(arr)

# Test the function
assert big_sum([1,2,3]) == 4
```

This function works by first checking if the array is empty. If it is, it returns 0. If it's not, it finds the maximum and minimum values in the array using the built-in `max` and `min` functions, and returns their sum.
