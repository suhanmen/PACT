def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary string
    binary_str = 'db' + binary + 'db'  # Add 'db' characters to the beginning and end of the string
    return binary_str
