def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the prefix '0b'
    return 'db' + binary + 'db'
