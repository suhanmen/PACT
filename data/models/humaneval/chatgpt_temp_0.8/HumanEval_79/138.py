def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return 'db' + binary_str + 'db'
