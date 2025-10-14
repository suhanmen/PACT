def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary (returns a string)
    return f"db{binary}db"    # add the extra characters and return the final string
