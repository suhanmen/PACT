def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]   # Convert decimal to binary and remove the "0b" prefix
    binary_string = "db" + binary + "db"   # Add the extra characters to the beginning and end
    return binary_string
