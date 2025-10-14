def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers and False otherwise.
    Knowing that a is less than 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # First, we check if the number is less than 2 or greater than 97, since those are not prime numbers
    if a < 2 or a > 97:
        return False

    # Next, we find the prime factors of the number
    factors = []
    for i in range(2, a+1):
        while a % i == 0:
            factors.append(i)
            a //= i
        if a == 1:
            break

    # If the number has exactly 3 prime factors, then it is the multiplication of 3 prime numbers
    if len(factors) == 3 and all(is_prime(f) for f in factors):
        return True
    else:
        return False
