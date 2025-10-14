def is_simple_power(x, n):
    if x <= 0: # x must be positive
        return False
    if n <= 0: # n must be a positive integer
        return False
    if n == 1: # n^1 is always equal to n
        return x == 1
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
