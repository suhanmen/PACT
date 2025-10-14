def hex_key(num):
    # create a dictionary to store the decimal values of each hexadecimal digit
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    # create a list of prime hexadecimal digits
    prime_hex = ['2', '3', '5', '7', 'B', 'D']
    
    # initialize a variable to keep track of the count of prime digits
    prime_count = 0
    
    # iterate through each digit in the input string
    for digit in num:
        # convert the hexadecimal digit to decimal using the hex_dict
        decimal_val = hex_dict[digit]
        
        # check if the decimal value is prime and a prime hexadecimal digit
        if decimal_val > 1 and all(decimal_val % i != 0 for i in range(2, decimal_val)) and digit in prime_hex:
            prime_count += 1
    
    return prime_count
