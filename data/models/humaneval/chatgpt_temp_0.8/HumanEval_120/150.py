def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    sorted_arr = sorted(arr) # sort the array in ascending order
    return sorted_arr[-k:] # return the last k elements (i.e., the maximum k numbers) in the sorted array
