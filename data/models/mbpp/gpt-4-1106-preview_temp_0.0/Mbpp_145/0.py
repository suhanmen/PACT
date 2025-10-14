"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""



def max_Abs_Diff(arr):
    return max(arr) - min(arr)

# Example usage
# assert max_Abs_Diff((2,1,5,3)) == 4
