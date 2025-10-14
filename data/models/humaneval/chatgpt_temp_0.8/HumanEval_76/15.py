def is_simple_power(x, n):
    if x == 1:  # Special case for x = 1
        return True
    if n == 1:  # Special case for n = 1
        return False
    i = 1
    while i <= x:
        if i == x:
            return True
        i *= n  # Multiply i by n until it becomes greater than x
    return False
