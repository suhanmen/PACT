def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the '0b' prefix
    return f"db{binary}db"  # add the 'db' prefix and suffix to the binary string
