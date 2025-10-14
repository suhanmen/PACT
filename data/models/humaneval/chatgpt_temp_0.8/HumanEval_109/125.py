def move_one_ball(arr):
    """
    Determines if it is possible to sort the array by performing right shift operations.
    
    Args:
    arr: A list of N integers.
    
    Returns:
    True if it is possible to sort the array, False otherwise.
    """
    if len(arr) == 0:
        return True

    for i in range(len(arr)):
        if sorted(arr) == arr:
            return True
        arr = [arr[-1]] + arr[:-1]

    return False
