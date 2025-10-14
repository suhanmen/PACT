Here is the Python function to find the minimum difference between any two elements in a given array:

```python
def find_min_diff(arr, n):
    # Sort array in ascending order
    arr = sorted(arr)
    
    # Initialize difference as infinite
    diff = float('inf')
    
    # Find the min diff by comparing adjacent
    # pairs in sorted array
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    # Return min diff
    return diff
```

You can test the function with the following code:

```python
print(find_min_diff([1,5,3,19,18,25],6)) # Output: 1
```

This function works by first sorting the array in ascending order. Then it iterates over the sorted array, comparing each pair of adjacent elements and keeping track of the smallest difference found. The function finally returns this smallest difference.
