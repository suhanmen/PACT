def is_multiply_prime(a):
    if a < 2:
        return False
    if a == 2 or a == 3 or a == 5:
        return True
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False
    # check if a is the product of 3 primes
    count = 0
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            count += 1
            if count > 2:
                return False
            while a % i == 0:
                a //= i
    if a > 1:
        count += 1
        if count > 2:
            return False
    return count == 2
