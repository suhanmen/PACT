def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    num_primes = 0
    for i in range(2, a):
        if a % i == 0:
            # check if i is a prime number
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                num_primes += 1
    return num_primes == 3
