def is_prime(n):
    """Helper function to check if a number is prime"""
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    primes = []
    for i in range(2, a+1):
        if is_prime(i) and a % i == 0:
            primes.append(i)
    if len(primes) == 3:
        return True
    else:
        return False
