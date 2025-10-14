def is_simple_power(x, n):
    if x == n:
        return True
    if n == 1:
        return False
    power = 1
    while power < x:
        power *= n
    return power == x
