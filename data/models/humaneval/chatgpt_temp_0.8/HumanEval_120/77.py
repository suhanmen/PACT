def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if k == 0:
        return []
    
    # we can use the built-in function sorted() to sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # we can then return the first k elements of the sorted array
    return sorted_arr[:k]
