def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) < 2:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    return increasing or decreasing
