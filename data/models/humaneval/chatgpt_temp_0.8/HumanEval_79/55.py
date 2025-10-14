def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert to binary and remove the '0b' prefix
    binary_string = 'db' + binary + 'db'
    return binary_string
