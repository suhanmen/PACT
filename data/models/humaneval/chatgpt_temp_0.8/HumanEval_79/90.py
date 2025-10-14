def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary_formatted = 'db' + binary + 'db'
    return binary_formatted
