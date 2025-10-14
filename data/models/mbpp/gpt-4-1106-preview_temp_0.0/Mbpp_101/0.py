"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""



def kth_element(arr, k):
    # Sort the array
    arr.sort()
    # Return the kth element based on 1-based indexing
    return arr[k-1]

# Example usage
# assert kth_element([12,3,5,7,19], 2) == 3
