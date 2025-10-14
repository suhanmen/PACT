def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary string and remove the '0b' prefix
    result = 'db' + binary + 'db' # add 'db' to the beginning and end of the binary string
    return result
