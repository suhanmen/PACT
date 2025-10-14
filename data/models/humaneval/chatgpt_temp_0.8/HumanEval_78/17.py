def hex_key(num):
    # Define a list of hexadecimal digits to check for primes
    primes = ['2', '3', '5', '7', 'B', 'D']
    
    # Initialize a counter for the prime digits
    count = 0
    
    # Loop through each character in the hexadecimal number
    for digit in num:
        # Check if the digit is in the list of primes
        if digit in primes:
            # If yes, increment the counter
            count += 1
    
    # Return the final count of prime digits
    return count
