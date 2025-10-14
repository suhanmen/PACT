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
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    return count == 3
