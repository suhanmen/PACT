def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary with prefix '0b' removed
    return "db" + binary + "db"  # add prefix and suffix to the binary string
