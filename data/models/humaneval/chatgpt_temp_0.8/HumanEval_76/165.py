def is_simple_power(x, n):
    if x == 1:
        return True
    elif x < n:
        return False
    while x > 1:
        if x % n != 0:
            return False
        x /= n
    return True
