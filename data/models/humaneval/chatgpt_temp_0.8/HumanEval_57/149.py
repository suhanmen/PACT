def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing."""
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    return increasing or decreasing
