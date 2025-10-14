def is_prime(n):
    """ Helper function to check if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """ Function to check if a number is the multiplication of 3 prime numbers """
    prime_factors = []
    for i in range(2, 100):
        if is_prime(i) and a % i == 0:
            prime_factors.append(i)
    return len(prime_factors) == 3
