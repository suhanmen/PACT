def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) < 2:   # if list has less than two elements, return True
        return True
    elif l[0] <= l[-1]:   # check if the list is monotonically increasing
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                return False
    else:   # check if the list is monotonically decreasing
        for i in range(1, len(l)):
            if l[i] > l[i-1]:
                return False
    return True
