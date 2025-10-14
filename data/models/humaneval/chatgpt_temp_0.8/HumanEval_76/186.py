def is_simple_power(x, n):
    if x == 1: # special case
        return True
    if n == 1 or x % n != 0: # n cannot be 1, and x must be divisible by n
        return False
    power = 0
    while n ** power < x:
        power += 1
    return n ** power == x
