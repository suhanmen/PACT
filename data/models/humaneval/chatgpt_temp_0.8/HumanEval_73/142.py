def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # First, we check if the array is already palindromic
    if arr == arr[::-1]:
        return 0

    # Otherwise, we iterate through each element and try changing it
    n = len(arr)
    min_changes = n
    for i in range(n):
        # Try changing the current element to each other element
        for j in range(n):
            if i != j:
                new_arr = arr.copy()
                new_arr[i] = new_arr[j]
                # Check if the new array is palindromic and if it requires fewer changes
                if new_arr == new_arr[::-1]:
                    min_changes = min(min_changes, abs(j - i))
    return min_changes
