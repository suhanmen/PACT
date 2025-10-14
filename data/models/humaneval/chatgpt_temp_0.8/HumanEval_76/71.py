def is_simple_power(x, n):
    if x < 1 or n < 2:  # invalid input, return False
        return False
    elif x == 1:  # special case: any number to the power of 0 is 1
        return True
    else:
        power = 0
        while n ** power < x:
            power += 1
        return n ** power == x
