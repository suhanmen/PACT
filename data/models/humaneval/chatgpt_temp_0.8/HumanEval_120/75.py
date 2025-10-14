def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if k == 0:
        return []
    elif k >= len(arr):
        return sorted(arr, reverse=True)
    else:
        return sorted(arr, reverse=True)[:k]
