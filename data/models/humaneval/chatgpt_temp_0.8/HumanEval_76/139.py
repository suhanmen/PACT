def is_simple_power(x, n):
    if x == 1:   # special case where x is 1
        return True
    elif n == 1: # special case where n is 1
        return False
    else:
        i = 0
        power = n**i
        while power <= x:
            if power == x:
                return True
            i += 1
            power = n**i
        return False
