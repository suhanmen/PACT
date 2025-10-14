# CANNOT PARSE CODE SNIPPET
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing."""
    if len(l) < 2:
        return True  # A list with one element is always monotonic.
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return increasing or decreasing
