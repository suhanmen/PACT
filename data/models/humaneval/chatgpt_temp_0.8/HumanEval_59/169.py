def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    # Find the smallest prime factor of n
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            # If i is a factor of n, divide n by i and repeat until n is no longer divisible by i
            while n % i == 0:
                n //= i
            # Check if the new value of n is a prime number
            if is_prime(n):
                return n
            # Otherwise, continue with the next smallest factor of n
            break
    # If we didn't find a prime factor yet, n must be a prime number
    return n
