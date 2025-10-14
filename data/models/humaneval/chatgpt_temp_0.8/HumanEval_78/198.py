def hex_key(num):
    # Define a set of prime digits in hexadecimal
    primes = set(["2", "3", "5", "7", "B", "D"])
    # Initialise a variable to store the count of prime digits
    prime_count = 0
    # Iterate through each character in the input string
    for char in num:
        # Check if the character is a prime digit
        if char in primes:
            # Increment the count of prime digits
            prime_count += 1
    # Return the final count of prime digits
    return prime_count
