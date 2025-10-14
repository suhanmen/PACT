def hex_key(num):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # Define the list of prime digits in hexadecimal
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Count the number of prime digits in the input hexadecimal number
    count = 0
    for digit in num:
        if digit in prime_hex_digits and is_prime(int(digit, 16)):
            count += 1
    
    return count
