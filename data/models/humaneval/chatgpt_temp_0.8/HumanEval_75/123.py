def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_count = 0
    for i in range(2, a):
        if a % i == 0:
            factor = a // i
            if is_prime(i) and is_prime(factor):
                prime_count += 1
    return prime_count == 3
