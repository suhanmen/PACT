Here is the Python function to find the kth element in the given array using 1-based indexing:

```python
def kth_element(arr, k):
    if k < 1 or k > len(arr):
        return None
    return arr[k-1]
```

You can test this function with the following code:

```python
print(kth_element([12,3,5,7,19], 2))  # Output: 3
```

This function first checks if the provided index `k` is within the valid range (1 to the length of the array). If it's not, it returns `None`. Otherwise, it returns the element at the `k-1` index (since Python uses 0-based indexing).
