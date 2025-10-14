def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    factors = []
    for i in range(2, a+1):
        while a % i == 0:
            factors.append(i)
            a = a // i
    return len(factors) == 3 and all(is_prime(x) for x in factors)
