def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary_with_db = f"db{binary}db"
    return binary_with_db
