def hex_key(num):
    # Define a helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Define a list of the prime hexadecimal digits
    primes = ['2', '3', '5', '7', 'B', 'D']
    
    # Count the number of hexadecimal digits that are primes
    count = 0
    for digit in num:
        if digit in primes:
            if is_prime(int(digit, 16)):
                count += 1
    
    return count
