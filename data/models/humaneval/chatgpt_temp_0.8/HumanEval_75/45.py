def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    factors = []
    for i in range(2, a//2+1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
    if len(factors) < 3:
        return False
    product = 1
    for factor in factors:
        product *= factor
    return product == a
