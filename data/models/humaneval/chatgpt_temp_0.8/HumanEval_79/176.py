def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary format
    return 'db' + binary + 'db'  # add extra characters 'db' at the beginning and end
