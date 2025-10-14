def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary, and remove the first two characters '0b'
    binary_str = 'db' + binary + 'db'  # Add the extra characters 'db' at the beginning and at the end
    return binary_str
