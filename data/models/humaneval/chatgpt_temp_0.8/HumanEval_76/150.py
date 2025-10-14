def is_simple_power(x, n):
    if x == 1: # special case: any number to the power of 0 is 1
        return True
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
