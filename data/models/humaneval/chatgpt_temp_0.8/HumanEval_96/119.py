def count_up_to(n):
    """
    Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    if n < 2:  # if n is less than 2, no prime numbers exist
        return []
    primes = [2]  # 2 is the first prime number
    num = 3  # start checking for primes from 3
    while len(primes) < n and num < n:
        is_prime = True
        for p in primes:
            if p * p > num:  # no need to check further if p^2 is greater than num
                break
            if num % p == 0:  # num is divisible by p, not a prime
                is_prime = False
                break
        if is_prime:
            primes.append(num) # add num to primes
        num += 2  # check only odd numbers since even numbers are not prime except for 2
    return primes
