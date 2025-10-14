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
    direction = None
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if direction is None:
                direction = "increasing"
            elif direction == "decreasing":
                return False
        elif l[i] < l[i-1]:
            if direction is None:
                direction = "decreasing"
            elif direction == "increasing":
                return False
    return True
