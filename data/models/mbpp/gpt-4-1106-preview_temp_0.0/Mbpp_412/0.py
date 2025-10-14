"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""



def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage
# assert remove_odd([1,2,3]) == [2]
