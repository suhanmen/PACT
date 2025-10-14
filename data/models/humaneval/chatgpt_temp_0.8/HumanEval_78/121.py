def hex_key(num):
    # Create a set of all prime hexadecimal digits
    prime_hex = {'2', '3', '5', '7', 'B', 'D'}
    # Initialize a count for the prime hexadecimal digits
    count = 0
    # Loop through each character in the input string
    for char in num:
        # If the character is a prime hexadecimal digit, increment the count
        if char in prime_hex:
            count += 1
    # Return the count of prime hexadecimal digits
    return count
