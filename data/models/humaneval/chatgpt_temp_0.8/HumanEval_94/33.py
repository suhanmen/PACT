def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [x for x in lst if is_prime(x)]
    largest_prime = max(primes)
    digit_sum = sum(int(d) for d in str(largest_prime))
    return digit_sum
