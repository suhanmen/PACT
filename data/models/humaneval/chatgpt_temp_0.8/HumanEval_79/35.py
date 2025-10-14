def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove first two characters '0b'
    return f"db{binary}db"    # add 'db' at the beginning and at the end of the binary string
