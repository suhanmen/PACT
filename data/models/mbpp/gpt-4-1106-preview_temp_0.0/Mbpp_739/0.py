"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""


import math

def find_Index(n):
    # Function to find the index of smallest triangular number
    # with n digits

    # A Triangular number or a triangle number counts objects arranged in an equilateral triangle. Triangular numbers are therefore
    # given by the formula: Tn = n * (n + 1) / 2

    # The idea is to use binary search on the result. First find the upper
    # limit of result, then apply binary search

    # Find the upper limit
    low = 1
    high = 10
    while len(str((high * (high + 1)) // 2)) < n:
        low = high
        high *= 10

    # Apply binary search
    while low < high:
        mid = (low + high) // 2
        num = (mid * (mid + 1)) // 2

        if len(str(num)) == n:
            high = mid
        elif len(str(num)) < n:
            low = mid + 1
        else:
            high = mid - 1

    # Since we are finding the smallest index, we need to move back to find
    # the first occurrence of the number with n digits
    while len(str(((high - 1) * high) // 2)) == n:
        high -= 1

    return high

# Example usage
# assert find_Index(2) == 4
