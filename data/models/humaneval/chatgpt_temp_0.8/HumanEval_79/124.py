def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # convert decimal to binary string and remove the "0b" prefix
    return "db" + binary + "db" # add the extra characters 'db' at the beginning and at the end of the string
