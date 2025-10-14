def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # Sort the array in reverse order
    arr.sort(reverse=True)

    # Return the first k elements in the sorted array
    return arr[:k]
