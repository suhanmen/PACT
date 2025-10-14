def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the '0b' prefix
    binary_string = 'db' + binary + 'db'  # add extra characters at the beginning and end
    return binary_string
