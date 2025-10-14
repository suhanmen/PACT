def is_simple_power(x, n):
    if x == 1:  # special case, 1 is a power of any number
        return True
    elif x < n:  # x is not a power of n if it's less than n
        return False
    else:
        power = 1
        while power < x:
            power *= n
        return power == x
