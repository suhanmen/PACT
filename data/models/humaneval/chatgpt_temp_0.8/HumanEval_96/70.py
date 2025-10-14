def count_up_to(n):
    """
    Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    if n < 2:
        return []

    primes = [2]
    num = 3

    while len(primes) < n and num < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    return primes[:n]
