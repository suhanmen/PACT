def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary
    binary_str = 'db' + binary + 'db'  # add extra characters
    return binary_str
