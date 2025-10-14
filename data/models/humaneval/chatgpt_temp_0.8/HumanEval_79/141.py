def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary using the built-in bin function and remove the '0b' prefix
    binary_str = "db" + binary + "db" # add the extra characters 'db' at the beginning and at the end
    return binary_str
