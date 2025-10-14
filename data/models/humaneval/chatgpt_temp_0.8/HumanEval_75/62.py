def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
