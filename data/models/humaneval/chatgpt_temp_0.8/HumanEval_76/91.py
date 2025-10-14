def is_simple_power(x, n):
    if x == 1:  # special case when x=1, n^0 = 1
        return True 
    elif n == 1: # special case when n=1, 1 to any power is 1
        return False 
    else:
        power = 0
        while n ** power <= x:
            if n ** power == x:
                return True
            power += 1
        return False
