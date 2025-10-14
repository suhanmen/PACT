def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary using built-in function, remove the '0b' prefix
    binary_string = 'db' + binary + 'db'  # add 'db' prefix and suffix
    return binary_string
