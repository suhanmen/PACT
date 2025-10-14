def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # First, we need to find all prime numbers less than or equal to 100
    primes = []
    for num in range(2, 101):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

    # Next, we need to check if a is the product of three prime numbers
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
        if count == 3:
            return True

    # If we didn't find three prime factors, return False
    return False
