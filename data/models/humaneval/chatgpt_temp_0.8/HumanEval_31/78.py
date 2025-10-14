def is_prime(n):
    if n < 2:
        return False
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True
