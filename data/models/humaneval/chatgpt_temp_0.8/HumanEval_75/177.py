def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # First, we need to find the prime factors of the given number.
    # We can use trial division to do this.
    factors = []
    n = 2
    while n <= a:
        if a % n == 0:
            factors.append(n)
            a //= n
        else:
            n += 1
    
    # If we have exactly 3 prime factors, then the input is the multiplication of 3 prime numbers.
    return len(factors) == 3 and all(is_prime(f) for f in factors)
