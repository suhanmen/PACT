"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""



def check_greater(array, number):
    return all(number > element for element in array)

# Example usage
# assert check_greater([1, 2, 3, 4, 5], 4) == False
