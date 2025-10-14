def is_simple_power(x, n):
    if x < 1:
        return False
    elif x == 1:
        return True
    else:
        power = 0
        while n**power < x:
            power += 1
        return n**power == x
