def is_simple_power(x, n):
    if x == 1:
        return True
    elif x < n:
        return False
    else:
        power = n
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
