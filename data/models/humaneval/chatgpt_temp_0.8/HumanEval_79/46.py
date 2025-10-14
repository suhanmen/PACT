def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]   # convert decimal to binary using built-in bin() function, and remove the '0b' prefix
    return 'db' + binary + 'db'   # add 'db' at the beginning and at the end of the binary string
