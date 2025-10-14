def decimal_to_binary(decimal):
    # convert decimal to binary using built-in bin() function
    binary = bin(decimal)[2:]

    # add 'db' to beginning and end of binary string
    binary_with_db = 'db' + binary + 'db'

    return binary_with_db
