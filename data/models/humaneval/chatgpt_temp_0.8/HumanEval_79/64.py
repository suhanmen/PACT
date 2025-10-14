def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary, omitting the '0b' prefix
    binary_string = 'db' + binary + 'db'  # add 'db' before and after the binary number
    return binary_string
