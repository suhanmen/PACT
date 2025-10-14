def is_simple_power(x, n):
    if x == 1: # 1 raised to any power is always 1
        return True
    for i in range(2, int(x/2) + 1):
        if n**i == x: # check if n raised to i equals x
            return True
    return False
