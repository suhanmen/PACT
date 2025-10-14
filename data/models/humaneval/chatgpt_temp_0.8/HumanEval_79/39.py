def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary
    return "db" + binary + "db"  # add extra characters to the beginning and end of the string
