def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary and remove the '0b' prefix
    binary_str = 'db' + binary + 'db' # format the output string with 'db' at both ends
    return binary_str
