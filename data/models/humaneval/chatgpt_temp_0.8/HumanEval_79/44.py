def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert to binary and remove '0b' prefix
    return f"db{binary}db"
