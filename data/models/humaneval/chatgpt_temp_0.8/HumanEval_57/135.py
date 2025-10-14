# CANNOT PARSE CODE SNIPPET
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    else:
        return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))
