def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing."""
    increasing = False
    decreasing = False
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            increasing = True
        elif l[i] > l[i+1]:
            decreasing = True
        if increasing and decreasing:
            return False
    return True
