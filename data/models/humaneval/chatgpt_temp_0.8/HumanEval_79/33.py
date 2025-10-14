def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove the '0b' prefix
    return f"db{binary}db"   # return the binary string with the extra characters
