def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    factors = []
    i = 2
    while a > 1 and i <= 7:
        if a % i == 0:
            factors.append(i)
            a //= i
        else:
            i += 1
    if len(factors) == 3:
        return True
    else:
        return False
