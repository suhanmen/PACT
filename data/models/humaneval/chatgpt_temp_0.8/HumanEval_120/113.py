def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    arr = sorted(arr, reverse=True) # Sort the array in descending order
    return arr[:k] # Return the first k elements of the sorted array
