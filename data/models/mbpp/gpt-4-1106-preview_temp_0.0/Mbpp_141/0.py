"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""


import functools

def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    curr_size = len(arr)
    while curr_size > 1:
        max_index = find_max(arr, curr_size)
        if max_index != curr_size - 1:
            flip(arr, max_index)
            flip(arr, curr_size - 1)
        curr_size -= 1
    return arr

# Example usage
# sorted_arr = pancake_sort([15, 79, 25, 38, 69])
# print(sorted_arr)
