import math

def is_prime(n):
    if n < 2:  # 1 is not a prime number
        return False
    elif n == 2:  # 2 is the only even prime number
        return True
    elif n % 2 == 0:  # even numbers other than 2 are not prime
        return False
    else:
        # check odd numbers up to the square root of n
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True
