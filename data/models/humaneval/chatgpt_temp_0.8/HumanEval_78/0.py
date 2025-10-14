def hex_key(num):
    # Define a list of prime digits in hexadecimal
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Initialize a counter variable to keep track of the number of prime digits
    count = 0
    
    # Loop through each character in the input string
    for digit in num:
        # If the character is a prime digit, increment the counter
        if digit in prime_digits:
            count += 1
    
    # Return the final count of prime digits
    return count
