"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""



def find_kth(arr1, arr2, k):
    # Merge the two arrays
    merged_array = sorted(arr1 + arr2)
    # Return the kth element
    return merged_array[k-1]

# Example usage
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
