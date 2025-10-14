"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""



def Split(lst):
    return [x for x in lst if x % 2 != 0]

# Example usage:
# odd_numbers = Split([1,2,3,4,5,6])
# print(odd_numbers)  # Output: [1, 3, 5]
