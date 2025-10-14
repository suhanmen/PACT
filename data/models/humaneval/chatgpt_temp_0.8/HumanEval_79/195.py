def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary, remove '0b' prefix
    return "db" + binary + "db"  # add prefix and suffix characters
