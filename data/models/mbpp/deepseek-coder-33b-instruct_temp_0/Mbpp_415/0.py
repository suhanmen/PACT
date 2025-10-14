Here is the Python function to find a pair with highest product from a given array of integers:

```python
def max_product(arr):
    if len(arr) < 2:
        return None
    if len(arr) == 2:
        return tuple(arr)
    arr.sort()
    return (arr[-1], arr[-2]) if arr[-1]*arr[-2] > arr[0]*arr[1] else (arr[0], arr[1])

print(max_product([1,2,3,4,7,0,8,4]))  # Output: (7, 8)
```

This function first checks if the array has less than 2 elements, in which case it returns None. If the array has exactly 2 elements, it returns the pair as a tuple. If the array has more than 2 elements, it sorts the array in ascending order and then checks if the product of the last two elements (which are the largest in a sorted array) is greater than the product of the first two elements (which are the smallest in a sorted array). If it is, it returns the last two elements as a tuple, otherwise it returns the first two elements as a tuple.
