def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string, ignore first two characters '0b'
    return f"db{binary}db"    # add 'db' at the beginning and at the end of the string
