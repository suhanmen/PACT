def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary, remove '0b' prefix
    return f"db{binary}db"    # concatenate 'db' with binary string and return it
