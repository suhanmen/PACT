def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary, remove prefix "0b"
    binary_with_db = "db" + binary + "db" # add "db" before and after binary number
    return binary_with_db
