def count_up_to(n):
    primes = []
    if n > 1:
        for num in range(2, n):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
