"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""


import collections

def validate(number):
    # Convert the number to a string to iterate over each digit
    number_str = str(number)
    # Create a counter for all digits in the number
    digit_count = collections.Counter(number_str)

    # Iterate over each digit and its frequency
    for digit, freq in digit_count.items():
        # Check if the frequency is greater than the digit itself
        if freq > int(digit):
            return False
    return True

# Example usage
# assert validate(1234) == True
