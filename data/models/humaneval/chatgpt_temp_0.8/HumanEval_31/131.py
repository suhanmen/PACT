def is_prime(n):
    # Check if n is less than or equal to 1, in which case it is not prime.
    if n <= 1:
        return False
    
    # Check if n is divisible by any number between 2 and its square root,
    # in which case it is not prime.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If n is not divisible by any number between 2 and its square root, it is prime.
    return True
