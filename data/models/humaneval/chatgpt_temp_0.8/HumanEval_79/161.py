def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary
    binary_string = 'db' + binary + 'db'  # Add extra characters
    return binary_string
