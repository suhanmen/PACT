def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # Convert decimal to binary using built-in function
    binary_str = 'db' + binary + 'db' # Add extra characters
    return binary_str
