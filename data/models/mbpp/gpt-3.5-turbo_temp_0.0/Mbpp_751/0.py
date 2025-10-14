Here is the completed code snippet:

```python
def check_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        if arr[i] > arr[2*i + 1] or (2*i + 2 < n and arr[i] > arr[2*i + 2]):
            return False
    return True

assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
```

The function `check_min_heap` takes an array `arr` as input and checks if it represents a min heap or not. It iterates through the array starting from the last non-leaf node (n//2 - 1) to the root (0). For each node, it compares the value with its left child (2*i + 1) and right child (2*i + 2) if it exists. If the value is greater than any of its children, it returns False indicating that the array does not represent a min heap. If the loop completes without returning False, it means the array represents a min heap and it returns True.