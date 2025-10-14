def hex_key(num):
    # A set of all prime hexadecimal digits:
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Initialize the count of prime digits to 0:
    prime_count = 0
    
    # Convert the hexadecimal string to a list of characters:
    hex_list = list(num)
    
    # Iterate over each character in the list:
    for hex_digit in hex_list:
        # Check if the character is a prime hexadecimal digit:
        if hex_digit in prime_hex_digits:
            # Increment the count if it is:
            prime_count += 1
    
    # Return the final count of prime digits:
    return prime_count
