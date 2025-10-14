def is_prime(n):
    """
    Helper function that checks whether a given number is prime or not.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """
    Function that checks whether a given number is the multiplication of 3 prime numbers or not.
    """
    prime_factors = [i for i in range(2, a) if is_prime(i) and a % i == 0]
    if len(prime_factors) == 3:
        return True
    else:
        return False
