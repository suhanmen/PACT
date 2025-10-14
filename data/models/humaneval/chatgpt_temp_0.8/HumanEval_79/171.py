def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary using built-in bin() function, and remove '0b' prefix
    return 'db' + binary + 'db'  # concatenate 'db' to the beginning and end of binary string, and return it
