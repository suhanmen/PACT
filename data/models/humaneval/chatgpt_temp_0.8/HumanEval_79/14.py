def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string
    binary_string = 'db' + binary + 'db'  # add extra characters to beginning and end
    return binary_string
