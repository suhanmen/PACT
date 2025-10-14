def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    while x % n == 0:
        x = x // n
    return x == 1
