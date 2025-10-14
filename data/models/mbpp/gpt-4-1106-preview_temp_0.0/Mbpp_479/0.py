"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""



def first_Digit(number):
    while number >= 10:
        number //= 10
    return number

# Example usage
# assert first_Digit(123) == 1
