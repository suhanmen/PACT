def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary using built-in function
    return "db" + binary + "db"
