def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string, and remove the '0b' prefix
    return 'db' + binary + 'db'  # add extra characters to beginning and end of string
