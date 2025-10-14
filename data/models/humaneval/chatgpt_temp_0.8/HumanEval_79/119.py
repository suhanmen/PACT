def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary using the built-in bin() function
    binary_string = 'db' + binary + 'db'  # Add the extra characters to the beginning and end
    return binary_string
