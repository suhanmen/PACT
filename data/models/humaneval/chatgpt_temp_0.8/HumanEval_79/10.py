def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert the decimal to binary, ignoring the '0b' prefix
    binary_string = 'db' + binary + 'db'  # add the extra characters to the beginning and end
    return binary_string
