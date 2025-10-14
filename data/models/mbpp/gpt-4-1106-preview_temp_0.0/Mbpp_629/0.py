"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""



def Split(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage:
# even_numbers = Split([1,2,3,4,5])
# print(even_numbers)  # Output: [2, 4]
