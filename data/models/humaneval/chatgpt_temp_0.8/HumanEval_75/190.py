from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 2:
        return False
    count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            count += 1
    return count == 3
