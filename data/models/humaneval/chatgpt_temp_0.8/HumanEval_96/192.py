def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

def count_up_to(n):
    primes = []
    for i in range(2, n):
        if len(primes) == n:
            break
        if is_prime(i):
            primes.append(i)
    return primes
