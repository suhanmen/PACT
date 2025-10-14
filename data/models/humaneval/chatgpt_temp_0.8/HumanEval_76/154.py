def is_simple_power(x, n):
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        i = 1
        while i <= x:
            if i == x:
                return True
            i *= n
        return False
