def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    if x == 1:
        return True
    power = n
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
