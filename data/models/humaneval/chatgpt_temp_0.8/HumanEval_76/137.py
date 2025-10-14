def is_simple_power(x, n):
    if x == 1 or x == n:
        return True
    elif x < n:
        return False
    else:
        return is_simple_power(x/n, n)
