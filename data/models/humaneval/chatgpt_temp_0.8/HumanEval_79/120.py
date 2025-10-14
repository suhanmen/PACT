def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary using built-in function
    return f"db{binary}db"    # add 'db' to beginning and end of binary string
