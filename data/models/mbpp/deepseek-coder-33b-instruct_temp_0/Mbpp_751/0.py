Here is the Python function to check if the given array represents a min heap or not:

```python
def check_min_heap(arr):
    n = len(arr)

    # Iterate through every node
    for i in range(int(n/2)):
        # If left child is greater than parent
        if arr[2*i + 1] < arr[i]:
            return False
        # If right child exists and is greater than parent
        if 2*i+2 < n:
            if arr[2*i + 2] < arr[i]:
                return False
    return True
```

This function works by iterating through each node in the array and checking if the left child and right child (if they exist) are less than the parent. If any of these conditions are not met, the function returns False, indicating that the array does not represent a min heap. If the function completes its iteration without finding any such conditions, it returns True, indicating that the array does represent a min heap.
