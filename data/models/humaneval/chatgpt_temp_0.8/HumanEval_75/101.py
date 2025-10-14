def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100."""
    prime_count = 0
    i = 2
    while i <= a:
        if is_prime(i) and a % i == 0:
            prime_count += 1
            if prime_count == 3:
                return True
            a //= i
        else:
            i += 1
    return False
