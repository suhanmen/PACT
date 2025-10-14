def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary (without the '0b' prefix)
    return 'db' + binary + 'db' # add the extra characters at the beginning and end
