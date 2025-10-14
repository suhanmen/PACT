python
def is_multiply_prime(a):
    if a < 6:  # Multiplication of 3 primes is not possible if a < 6
        return False
    
    # Check if a is divisible by 2, 3, or 5
    if a % 2 == 0:
        return is_multiply_prime(a // 2)
    elif a % 3 == 0:
        return is_multiply_prime(a // 3)
    elif a % 5 == 0:
        return is_multiply_prime(a // 5)
    
    # Check if a is a product of 3 primes
    primes = [2, 3, 5]
    for p in primes:
        while a % p == 0:
            a //= p
    return a == 1
