def is_simple_power(x, n):
    if x == 1:  # any number to the power of 0 is 1
        return True
    elif n == 1:  # any number to the power of 1 is equal to itself
        return x == 1
    else:
        i = 0
        while n ** i <= x:
            if n ** i == x:
                return True
            i += 1
        return False
