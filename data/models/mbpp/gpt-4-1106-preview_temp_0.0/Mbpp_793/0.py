"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""



def last(arr, x):
    try:
        return len(arr) - arr[::-1].index(x) - 1
    except ValueError:
        return -1

# Example usage:
# assert last([1,2,3], 1) == 0
