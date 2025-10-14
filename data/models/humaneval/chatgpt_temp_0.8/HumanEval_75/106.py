# Define a helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    # Initialize a list to hold the prime factors of the given number
    prime_factors = []
    
    # Find the prime factors of the given number
    for i in range(2, a+1):
        if is_prime(i) and a % i == 0:
            prime_factors.append(i)
    
    # If there are exactly 3 prime factors, return True
    if len(prime_factors) == 3:
        return True
    
    # Otherwise, return False
    return False
