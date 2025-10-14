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

    # initialize counters for the number of elements to change
    left = 0
    right = len(arr)-1
    count = 0

    # compare elements from either end of the array
    while left < right:
        if arr[left] != arr[right]:
            count += 1
        left += 1
        right -= 1

    return count
