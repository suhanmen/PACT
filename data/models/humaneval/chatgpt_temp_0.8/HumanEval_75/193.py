def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = []
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    count = 0
    for p in primes:
        if a % p == 0:
            count += 1
    return count == 3
