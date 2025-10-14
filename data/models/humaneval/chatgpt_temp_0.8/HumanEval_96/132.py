def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i <= int(num**0.5) + 1:
        if num % i == 0:
            return False
        i += 2
    return True

def count_up_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
