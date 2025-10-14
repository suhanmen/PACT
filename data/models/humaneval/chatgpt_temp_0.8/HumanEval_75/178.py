def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    primes = []
    for i in range(2, a+1):
        if is_prime(i):
            primes.append(i)
    if len(primes) < 3:
        return False
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i]*primes[j]*primes[k] == a:
                    return True
    return False
