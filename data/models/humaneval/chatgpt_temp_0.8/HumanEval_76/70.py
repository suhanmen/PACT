def is_simple_power(x, n):
    if x == 1:  # 1 is a special case where any number raised to 0 is 1
        return True if n == 1 else False
    elif n == 1:  # Any number raised to 1 is itself, so x cannot be a power of 1
        return False
    
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    
    return False
