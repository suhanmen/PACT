Here is the completed code snippet:

```python
def last(arr, target):
    left = 0
    right = len(arr) - 1
    last_position = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last_position = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_position

assert last([1,2,3], 1) == 0
```

The `last` function takes in a sorted array `arr` and a target element `target`. It uses a binary search algorithm to find the last position of the target element in the array. The function initializes `left` and `right` pointers to the start and end of the array respectively. It also initializes `last_position` to -1, which will be updated with the last position of the target element if found.

The function then enters a while loop that continues until `left` is greater than `right`. In each iteration, it calculates the middle index `mid` and checks if the element at that index is equal to the target. If it is, it updates `last_position` to `mid` and moves the `left` pointer to `mid + 1` to search for the last occurrence of the target element. If the element at `mid` is less than the target, it updates `left` to `mid + 1` to search in the right half of the array. If the element at `mid` is greater than the target, it updates `right` to `mid - 1` to search in the left half of the array.

Once the while loop ends, the function returns `last_position`, which will be the last position of the target element in the array. The assert statement at the end verifies that the function returns the expected result for the given example.