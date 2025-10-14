def hex_key(num):
    # A list of prime digits in hexadecimal
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    # Convert the input hexadecimal number to a list of its digits
    digits = list(num)
    # Initialize a count of prime digits
    prime_count = 0
    # Iterate over each digit in the input number
    for digit in digits:
        # If the digit is a prime digit, increment the count
        if digit in prime_digits:
            prime_count += 1
    # Return the count of prime digits
    return prime_count
