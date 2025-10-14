def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # converts decimal to binary string
    binary_with_format = "db" + binary + "db"  # adds format characters
    return binary_with_format
