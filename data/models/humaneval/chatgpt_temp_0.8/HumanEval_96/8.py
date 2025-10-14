def count_up_to(n):
    primes = []
    for num in range(2, n):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
            if len(primes) == n:
                break
    return primes
