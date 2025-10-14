python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary string and remove "0b" prefix
    return f"db{binary}db"
