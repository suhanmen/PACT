def decimal_to_binary(decimal):
    binary_num = bin(decimal)[2:]
    return 'db' + binary_num + 'db'
