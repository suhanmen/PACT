"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""


import math

def is_majority(arr, n, elem):
    count = 0
    for i in range(n):
        if arr[i] == elem:
            count += 1
    return count > math.floor(n/2)
