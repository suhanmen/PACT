def is_simple_power(x, n):
    if n == 1:
        return False
    elif x == 1:
        return True
    else:
        p = 1
        while p < x:
            p *= n
        return p == x
