def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary using built-in function and slice off '0b' prefix
    return f"db{binary}db"    # return binary string with extra characters added
