"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""



def big_diff(numbers):
    return max(numbers) - min(numbers)


# Example usage
# assert big_diff([1,2,3,4]) == 3
