def is_prime(n):
    if n < 2:
        return False
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
