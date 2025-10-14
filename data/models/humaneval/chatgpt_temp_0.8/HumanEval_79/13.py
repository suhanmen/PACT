def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the first two characters '0b'
    binary_str = 'db' + binary + 'db'  # add 'db' at the beginning and at the end of the binary string
    return binary_str
