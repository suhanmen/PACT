def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary string, removing the '0b' prefix
    output = 'db' + binary + 'db'  # Add the extra characters to the output string
    return output
