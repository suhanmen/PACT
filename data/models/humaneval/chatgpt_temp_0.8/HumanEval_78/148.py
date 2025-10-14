def hex_key(num):
    # Set of prime hexadecimal digits
    primes = {'2', '3', '5', '7', 'B', 'D'}
    # Counter variable for prime digits
    count = 0
    # Loop through each digit in the input string
    for digit in num:
        # Check if the digit is a prime hexadecimal digit
        if digit in primes:
            # Increment the counter variable
            count += 1
    # Return the count of prime hexadecimal digits
    return count
