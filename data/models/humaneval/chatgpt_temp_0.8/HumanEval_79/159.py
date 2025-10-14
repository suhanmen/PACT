def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary string and remove the "0b" prefix
    binary_formatted = "db" + binary + "db" # add the "db" prefix and suffix
    return binary_formatted
