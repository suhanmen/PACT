def is_simple_power(x, n):
    if n == 1:
        return False
    elif x == 1:
        return True
    else:
        i = 1
        while n ** i <= x:
            if n ** i == x:
                return True
            i += 1
        return False
