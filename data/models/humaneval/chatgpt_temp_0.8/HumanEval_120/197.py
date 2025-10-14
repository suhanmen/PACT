def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: List[int]
    :param k: int
    :return: List[int]
    """
    if not arr or k == 0:
        return []
    
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]
