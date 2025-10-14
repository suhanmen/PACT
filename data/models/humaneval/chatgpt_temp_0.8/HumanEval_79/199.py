def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary_string = 'db' + binary + 'db'
    return binary_string
