def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:  # if the list has only one element or lesser, it is monotonic
        return True
    
    is_increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))  # check if elements are increasing
    is_decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))  # check if elements are decreasing
    
    return is_increasing or is_decreasing  # return True if either of the above conditions is True, else False
