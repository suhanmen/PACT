"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""


import math

def get_median(arr1, arr2, n):
    i = j = 0
    m1 = m2 = -1

    for count in range(n + 1):
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break

        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1

    return (m1 + m2)/2

# Example usage
# median = get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5)
# print(median)  # Output: 16.0
