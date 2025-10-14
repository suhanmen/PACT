python
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    midpoint = n // 2
    if n % 2 == 1:
        # odd number of elements
        return sorted_list[midpoint]
    else:
        # even number of elements
        return (sorted_list[midpoint - 1] + sorted_list[midpoint]) / 2
