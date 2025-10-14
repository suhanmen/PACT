def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False
    elif a == 2 or a == 3 or a == 5:
        return True
    elif a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False
    else:
        count = 0
        factor = 2
        while count < 2 and factor * factor <= a:
            if a % factor == 0:
                a //= factor
                count += 1
            else:
                factor += 1
        if count == 2 and a != factor:
            return True
        else:
            return False
