def is_simple_power(x, n):
    if x == 1:
        return True
    for i in range(2, int(x**(1/2))+1):
        p = i
        while p <= x:
            p *= i
            if p == x and i == n:
                return True
    return False
