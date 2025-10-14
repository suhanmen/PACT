def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    count_primes = 0
    i = 2
    while count_primes < 3 and i < 100:
        if is_prime(i) and a % i == 0:
            count_primes += 1
            a //= i
        else:
            i += 1
    return count_primes == 3 and a == 1
