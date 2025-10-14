"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""



def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_str = ''
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2
    return binary_str

# Example usage:
# binary_representation = decimal_to_binary(8)
# print(binary_representation)  # Output should be '1000'
