def hex_key(num):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Define a list of prime hexadecimal digits
    prime_hex = ['2', '3', '5', '7', 'B', 'D']

    # Convert hexadecimal number to a list of its digits
    hex_digits = list(num)

    # Count the number of prime hexadecimal digits
    count = 0
    for digit in hex_digits:
        if digit in prime_hex:
            if is_prime(int(digit, 16)):
                count += 1

    return count
