def is_simple_power(x, n):
    if n == 1:
        return False
    elif x == 1:
        return True
    else:
        power = 0
        while n**power <= x:
            if n**power == x:
                return True
            power += 1
        return False
