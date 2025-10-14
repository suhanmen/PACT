def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]   # Convert decimal to binary and remove the '0b' prefix
    return "db" + binary + "db"   # Add 'db' prefix and suffix to the binary string
