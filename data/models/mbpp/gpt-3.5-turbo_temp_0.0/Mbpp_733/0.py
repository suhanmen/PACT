Here is the completed code snippet:

```python
def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

This function uses a binary search algorithm to find the first occurrence of the target number in the sorted array. It initializes two pointers, `left` and `right`, to the start and end of the array respectively. It then enters a while loop that continues until `left` is greater than `right`. In each iteration, it calculates the middle index `mid` and compares the value at that index with the target number. If they are equal, it updates the `result` variable to the current index and moves the `right` pointer to the left of `mid` to continue searching for earlier occurrences. If the value at `mid` is less than the target, it updates the `left` pointer to the right of `mid` to search in the upper half of the array. If the value at `mid` is greater than the target, it updates the `right` pointer to the left of `mid` to search in the lower half of the array. Finally, it returns the `result` variable, which will be the index of the first occurrence of the target number in the array.