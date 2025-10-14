Here is the Python function that solves the problem:

```python
def is_majority(arr, n, x):
    """
    This function checks if the given element is the majority element in the given sorted array.
    The majority element is the element that occurs more than n/2 times.
    """
    i = n // 2
    if arr[i] == x:
        return True
    else:
        return False
```

This function works by checking the middle element of the array. If the middle element is the target element, it returns True. Otherwise, it returns False. This is because in a sorted array, the majority element must be at the middle of the array if it exists.

Please note that this function assumes that the input array is sorted. If the array is not sorted, the function may not work as expected.
