"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""



def armstrong_number(number):
    sum_of_powers = sum(int(digit) ** len(str(number)) for digit in str(number))
    return sum_of_powers == number

# Example usage
# assert armstrong_number(153) == True
