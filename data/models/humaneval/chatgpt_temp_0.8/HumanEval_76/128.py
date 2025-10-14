def is_simple_power(x, n):
    if n == 1:
        return x == 1
    elif x == 1:
        return True
    else:
        power = n
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
