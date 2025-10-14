"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""


import bisect

def left_insertion(sorted_list, value):
    return bisect.bisect_left(sorted_list, value)

# Example usage:
# sorted_list = [1, 2, 4, 5]
# value = 6
# print(left_insertion(sorted_list, value))  # Output: 4
