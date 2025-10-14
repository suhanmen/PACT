def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary
    return f"db{binary}db" # format string with 'db' at beginning and end
