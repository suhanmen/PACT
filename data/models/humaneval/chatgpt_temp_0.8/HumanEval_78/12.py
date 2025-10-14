def hex_key(num):
    # Define a list of prime hexadecimal digits
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Initialize a count variable for prime digits
    prime_count = 0
    
    # Iterate through each digit in the input number
    for digit in num:
        # If the digit is a prime hexadecimal digit, increment the count
        if digit in prime_digits:
            prime_count += 1
    
    # Return the count of prime digits found in the input number
    return prime_count
