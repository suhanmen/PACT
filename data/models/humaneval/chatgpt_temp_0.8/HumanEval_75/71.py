def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False
    elif a == 2 or a == 3 or a == 5:
        return True
    elif a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return is_multiply_prime(a/2) or is_multiply_prime(a/3) or is_multiply_prime(a/5)
    else:
        return False
