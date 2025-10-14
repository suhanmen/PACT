def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']  # List of prime hexadecimal digits
    count = 0  # Initialize count of prime digits to 0
    
    # Loop through each hexadecimal digit in the input string
    for digit in num:
        # If the digit is a prime hexadecimal digit, increment the count
        if digit in primes:
            count += 1
    
    # Return the count of prime digits
    return count
