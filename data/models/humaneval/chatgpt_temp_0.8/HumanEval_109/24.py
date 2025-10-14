def move_one_ball(arr):
    """
    Determines if it is possible to sort the given array in non-decreasing order 
    by performing right shift operation any number of times.

    Args:
    arr: list of N integers

    Returns:
    True if it is possible to sort the array in non-decreasing order else False

    """
    n = len(arr)
    if n == 0:
        return True
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            # If an element is greater than its next element,
            # we cannot obtain non-decreasing order by performing right shift
            return False
    return True
