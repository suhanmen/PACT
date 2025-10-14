def hex_key(num):
    # Define a list of prime hexadecimal digits
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Convert the input string to a list of characters
    hex_list = list(num)
    
    # Initialize a counter for the number of prime digits
    prime_count = 0
    
    # Loop through each hexadecimal digit in the list
    for digit in hex_list:
        # Check if the digit is a prime hexadecimal digit
        if digit in prime_hex_digits:
            # Increment the prime count if the digit is prime
            prime_count += 1
    
    # Return the final prime count
    return prime_count
