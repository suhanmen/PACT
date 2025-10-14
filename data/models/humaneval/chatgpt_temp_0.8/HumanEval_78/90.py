def hex_key(num):
    # List of prime numbers in decimal format
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    count = 0
    # Loop through each character in the hexadecimal number
    for c in num:
        # Convert the character to decimal format
        dec = int(c, 16)
        
        # If the decimal number is prime, increment the count
        if dec in primes:
            count += 1
    
    return count
