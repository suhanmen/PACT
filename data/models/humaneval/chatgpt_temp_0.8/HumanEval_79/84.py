def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert the decimal to binary and remove the '0b' prefix
    return 'db' + binary + 'db'
