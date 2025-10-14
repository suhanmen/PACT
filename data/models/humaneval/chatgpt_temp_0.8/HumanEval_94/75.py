def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in lst if is_prime(n)]
    if not primes:
        return 0
    largest_prime = max(primes)
    return sum(int(d) for d in str(largest_prime))
