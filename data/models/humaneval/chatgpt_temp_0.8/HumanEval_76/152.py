def is_simple_power(x, n):
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        power = 1
        while power < x:
            power *= n
        return power == x
