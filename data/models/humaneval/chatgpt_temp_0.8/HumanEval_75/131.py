def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = []
    for num in range(2, 101):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    count = 0
    for prime in primes:
        while a % prime == 0:
            a = a / prime
            count += 1
        if count >= 3:
            return True
    return False
