def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary
    binary_string = "db" + binary + "db"  # add 'db' characters at beginning and end
    return binary_string
