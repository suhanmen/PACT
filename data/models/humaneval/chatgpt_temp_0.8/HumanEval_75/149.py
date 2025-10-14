def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = []
    for i in range(2, a + 1):
        if len(primes) == 3:
            break
        if is_prime(i) and a % i == 0:
            primes.append(i)
    if len(primes) == 3:
        return True
    else:
        return False
