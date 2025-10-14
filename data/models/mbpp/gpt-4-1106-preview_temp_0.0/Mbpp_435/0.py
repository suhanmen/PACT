"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""



def last_Digit(number):
    return abs(number) % 10

# Example usage:
# result = last_Digit(123)
# print(result)  # Output: 3
