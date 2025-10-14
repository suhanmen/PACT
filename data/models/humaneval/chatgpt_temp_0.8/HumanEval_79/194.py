def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and slice off the '0b' prefix
    binary_string = 'db' + binary + 'db'  # Add 'db' at the beginning and end of the binary string
    return binary_string
