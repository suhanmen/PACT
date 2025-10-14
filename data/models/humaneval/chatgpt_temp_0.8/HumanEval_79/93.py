def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary using built-in bin() function
    return "db" + binary + "db"  # Add "db" characters to the beginning and end of the binary string
