def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary using built-in function bin() and remove the prefix '0b'
    result = f"db{binary}db" # add 'db' at the beginning and the end of the binary string
    return result
