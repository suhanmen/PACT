def hex_key(num):
    # List of hexadecimal digits that are primes
    primes = ['2', '3', '5', '7', 'B', 'D']
    # Initialize count to 0
    count = 0
    # Iterate through each hexadecimal digit in the input string
    for digit in num:
        # If the digit is a prime, increment count
        if digit in primes:
            count += 1
    # Return the count of prime digits
    return count
