def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # sort the array in descending order
    arr.sort(reverse=True)
    # return the first k elements of the sorted array
    return arr[:k]
