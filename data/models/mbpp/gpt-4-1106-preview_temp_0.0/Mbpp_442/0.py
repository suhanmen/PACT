"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""


import typing

def positive_count(numbers: typing.List[int]) -> float:
    positive_nums = [num for num in numbers if num > 0]
    if not numbers:
        return 0
    ratio = len(positive_nums) / len(numbers)
    return round(ratio, 2)

# Example usage:
# assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
