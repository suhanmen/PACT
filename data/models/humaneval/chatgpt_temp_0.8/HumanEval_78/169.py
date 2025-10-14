def hex_key(num):
    # Create a set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    # Initialize the count of prime hexadecimal digits to 0
    prime_hex_count = 0
    # Iterate through each hexadecimal digit in the input string
    for digit in num:
        # If the digit is a prime hexadecimal digit, increment the count
        if digit in prime_hex_digits:
            prime_hex_count += 1
    # Return the count of prime hexadecimal digits
    return prime_hex_count
