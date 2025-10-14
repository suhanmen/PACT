def is_simple_power(x, n):
    if x == 1:  # special case
        return True
    power = n
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
