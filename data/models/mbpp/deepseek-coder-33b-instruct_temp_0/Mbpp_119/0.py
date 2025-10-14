Here is the Python function to find the element that appears only once in a sorted array:

```python
def search(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] == arr[mid ^ 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]
```

This function uses binary search to find the element that appears only once in a sorted array. The binary search is performed on the indices of the array. The mid index is calculated as the average of the low and high indices. If the element at the mid index is equal to the element at the mid index XOR 1, then the single element is on the right side of the mid index, so the low index is updated to mid + 1. Otherwise, the single element is on the left side of the mid index, so the high index is updated to mid. The process continues until the low index is equal to the high index, at which point the single element is found.
