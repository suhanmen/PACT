def hex_key(num):
    # Define a set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Initialize a count variable
    count = 0
    
    # Convert the input string to a set of characters
    hex_set = set(num)
    
    # Iterate over each hexadecimal digit in the input set
    for digit in hex_set:
        # Check if the digit is prime and update the count if it is
        if digit in prime_hex_digits:
            count += 1
    
    return count
