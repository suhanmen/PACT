def decimal_to_binary(decimal):
    # Convert the decimal number to binary using bin() function
    binary = bin(decimal)[2:]
    
    # Add extra characters to the string
    binary_with_db = "db" + binary + "db"
    
    return binary_with_db
