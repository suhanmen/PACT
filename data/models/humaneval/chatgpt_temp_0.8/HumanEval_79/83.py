def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary string, remove the '0b' prefix
    return 'db' + binary + 'db' # add 'db' prefix and suffix to binary string
