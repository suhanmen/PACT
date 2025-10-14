def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    prime_factors = []
    for i in range(2, int(a / 2) + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)
    if len(prime_factors) != 3:
        return False
    else:
        return True
