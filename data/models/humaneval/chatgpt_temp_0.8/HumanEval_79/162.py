def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:] # convert decimal to binary string
    return f"db{binary_string}db"   # add extra characters to beginning and end of string
