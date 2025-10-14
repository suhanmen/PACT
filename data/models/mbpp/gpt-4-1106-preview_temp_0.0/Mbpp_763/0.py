"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""


import sys

def find_min_diff(arr, n):
    # Sort the array
    arr = sorted(arr)
    
    # Initialize difference as infinite
    min_diff = sys.maxsize
    
    # Find the min diff by comparing adjacent pairs in sorted array
    for i in range(n - 1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    
    return min_diff
