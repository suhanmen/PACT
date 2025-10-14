def hex_key(num):
    # Create a list of prime hexadecimal digits
    primes = ["2", "3", "5", "7", "B", "D"]
    
    # Initialize the count to 0
    count = 0
    
    # Loop through each hexadecimal digit in the input string
    for digit in num:
        # If the digit is a prime, increment the count
        if digit in primes:
            count += 1
    
    # Return the count of prime hexadecimal digits
    return count
