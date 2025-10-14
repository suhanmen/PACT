def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
    
def prime_fib(n: int):
    a, b = 1, 1
    count = 0
    while count < n:
        c = a + b
        a, b = b, c
        if is_prime(c):
            count += 1
    return c
