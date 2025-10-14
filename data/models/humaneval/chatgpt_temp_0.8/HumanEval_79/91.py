def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # convert decimal to binary and remove '0b' prefix
    
    # add '0' padding to the left if necessary
    num_zeros = 8 - (len(binary) % 8)
    if num_zeros != 8:
        binary = '0' * num_zeros + binary
    
    # add 'db' prefix and suffix
    binary = 'db' + binary + 'db'
    return binary
