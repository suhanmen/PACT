def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary using built-in method
    binary_str = f"db{binary}db"  # add "db" to the beginning and end of binary string
    return binary_str
