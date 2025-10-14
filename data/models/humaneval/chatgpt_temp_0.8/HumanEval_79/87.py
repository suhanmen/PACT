def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary
    binary_string = "db" + binary + "db" # add extra characters to the binary string
    return binary_string
