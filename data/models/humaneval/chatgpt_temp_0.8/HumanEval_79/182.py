def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the '0b' prefix
    binary_with_db = 'db' + binary + 'db'  # add 'db' to the beginning and end of the binary string
    return binary_with_db
