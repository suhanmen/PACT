"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""


import math

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        index = 0
        while index + gap < len(arr):
            if arr[index] > arr[index + gap]:
                arr[index], arr[index + gap] = arr[index + gap], arr[index]
                sorted = False
            index += 1

    return arr
