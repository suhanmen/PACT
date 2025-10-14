"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""



def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Example usage:
# odd_numbers = filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
