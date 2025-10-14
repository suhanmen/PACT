def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary string, remove '0b' prefix
    return "db" + binary + "db"  # Add 'db' prefix and suffix to binary string
