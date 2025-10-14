def decimal_to_binary(decimal):
    binary = str(bin(decimal))[2:]
    return "db" + binary + "db"
