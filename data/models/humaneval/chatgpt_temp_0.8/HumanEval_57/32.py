def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the list is monotonically increasing
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return True
    # Check if the list is monotonically decreasing
    elif all(l[i] >= l[i+1] for i in range(len(l)-1)):
        return True
    # If neither increasing nor decreasing, return False
    else:
        return False
