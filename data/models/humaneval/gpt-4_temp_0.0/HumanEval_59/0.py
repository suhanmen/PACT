def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
            while n % i == 0:
                n //= i
        if n == 1:
            break
    return largest_factor