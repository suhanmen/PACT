def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True
    # check if the list is strictly increasing
    increasing = all(l[i] < l[i+1] for i in range(len(l)-1))
    if increasing:
        return True
    # check if the list is strictly decreasing
    decreasing = all(l[i] > l[i+1] for i in range(len(l)-1))
    if decreasing:
        return True
    # otherwise, the list is not monotonic
    return False
