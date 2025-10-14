def decimal_to_binary(decimal):
    # Using format() method to convert decimal to binary and adding leading zeros to get a 8-bit binary number
    binary_str = format(decimal, '08b')
    
    # Adding extra characters to the binary string
    binary_str = "db" + binary_str + "db"
    
    return binary_str
