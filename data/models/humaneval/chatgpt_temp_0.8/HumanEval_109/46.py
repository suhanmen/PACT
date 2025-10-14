python
def move_one_ball(arr):
    """
    Determines if it is possible to get an array sorted in non-decreasing order
    by performing right shift operation any number of times.

    Args:
    arr: list of N integers

    Returns:
    True if it is possible to obtain the sorted array by performing the above operation
    False otherwise
    """
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if arr == sorted(arr):
            return True
        arr = [arr[-1]] + arr[:-1] # right shift operation
    return False
