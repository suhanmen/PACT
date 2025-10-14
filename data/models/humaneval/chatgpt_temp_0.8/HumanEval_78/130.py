def hex_key(num):
    # List of prime hexadecimal digits
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Count of prime hexadecimal digits
    count = 0
    
    # Loop through each hexadecimal digit in the input string
    for digit in num:
        # Check if the digit is a prime hexadecimal digit
        if digit in prime_hex_digits:
            # If it is, increment the count
            count += 1
    
    # Return the count of prime hexadecimal digits
    return count
