def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string, remove "0b" prefix
    return "db" + binary + "db"  # add "db" prefix and suffix to the binary string
