"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""


import math

def power_base_sum(base, power):
    # Calculate base to the power
    result = base ** power
    
    # Convert the result to a string to iterate over each digit
    result_str = str(result)
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in result_str)
    
    return digit_sum

# Example usage
# assert power_base_sum(2, 100) == 115
