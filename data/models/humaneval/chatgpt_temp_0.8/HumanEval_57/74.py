# CANNOT PARSE CODE SNIPPET
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        elif l[i] > l[i-1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True
