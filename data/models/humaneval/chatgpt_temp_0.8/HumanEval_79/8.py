def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # Convert decimal number to binary
    return "db" + binary + "db" # Add 'db' characters at the beginning and end of binary string
