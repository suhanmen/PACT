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
    if arr == arr[::-1]:  # check if array is already palindromic
        return 0

    # initialize pointers to start and end of array
    left, right = 0, len(arr) - 1
    count = 0

    while left < right:
        if arr[left] != arr[right]:
            count += 1
            # change the smaller element to match the larger one
            if arr[left] < arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
        left += 1
        right -= 1

    return count
