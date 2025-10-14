def is_simple_power(x, n):
    if x == 1:  # special case: any number raised to 0 is 1
        return True
    if n == 1:  # special case: 1 raised to any power is 1
        return False
    i = 0
    while n**i <= x:
        if n**i == x:
            return True
        i += 1
    return False
