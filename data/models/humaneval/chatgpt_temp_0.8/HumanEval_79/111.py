def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary format
    return "db" + binary + "db"  # return string with leading and trailing characters
