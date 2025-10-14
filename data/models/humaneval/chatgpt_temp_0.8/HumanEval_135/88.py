python
def can_arrange(arr):
    """
    Create a function which returns the largest index of an element which is not greater than or equal to the element
    immediately preceding it. If no such element exists then return -1. The given array will not contain duplicate values.
    """
    n = len(arr)
    ans = -1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            ans = i-1
    return ans
