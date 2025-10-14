def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    result = "db" + binary + "db"
    return result
