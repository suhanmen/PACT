python
def is_multiply_prime(a):
    # check if a is less than 2 or greater than 97
    if a < 2 or a > 97:
        return False
    
    # find the three prime factors of a
    factors = []
    for i in range(2, a):
        if a % i == 0:  # i is a factor of a
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.append(i)
                if len(factors) == 3:
                    break
    
    # check if there are exactly three prime factors of a
    return len(factors) == 3
