def is_simple_power(x, n):
    if x == 1:  # special case where n can be any value
        return True
    elif n == 1:  # special case where x can only be 1
        return x == 1
    else:
        i = 0
        while n ** i <= x:  # check all powers of n up to x
            if n ** i == x:
                return True
            i += 1
        return False
