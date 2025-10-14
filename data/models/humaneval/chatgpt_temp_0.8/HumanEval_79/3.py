def decimal_to_binary(decimal):
    binary = format(decimal, 'b')
    return 'db' + binary + 'db'
