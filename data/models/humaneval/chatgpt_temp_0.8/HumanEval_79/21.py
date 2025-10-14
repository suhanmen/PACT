def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string
    return 'db' + binary + 'db'  # add extra characters at the beginning and end
