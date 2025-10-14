Here's the completed code snippet:

```python
def search(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        if (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid % 2 != 0 and arr[mid] == arr[mid-1]):
            left = mid + 1
        else:
            right = mid - 1
```

This function uses binary search to find the element that appears only once in the sorted array. It checks the first and last elements separately, and then iteratively checks the middle element and its adjacent elements to determine the unique element.