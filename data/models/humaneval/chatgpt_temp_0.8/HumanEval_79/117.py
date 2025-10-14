def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary format
    binary_string = "db" + binary + "db"  # add extra characters
    return binary_string
