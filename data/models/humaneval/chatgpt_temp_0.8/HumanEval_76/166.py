# CANNOT PARSE
def is_simple_power(x, n):
    if x == 1:
        return True
    elif n == 1:
        return False
    elif x % n != 0:
        return False
    else:
        while x % n == 0:
            x = x / n
        if x == 1:
            return True
        else:
            return False
