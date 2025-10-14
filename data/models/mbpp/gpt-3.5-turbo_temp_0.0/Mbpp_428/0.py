Here is the completed code snippet:

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```

The `shell_sort` function implements the shell sort algorithm. It starts with a large gap between elements and gradually reduces the gap until it becomes 1. In each iteration, the function performs an insertion sort on subarrays separated by the gap. This process continues until the entire array is sorted. The function returns the sorted array.