# CANNOT PARSE
def is_simple_power(x, n):
    if n==1:
        return False
    elif n==x:
        return True
    else:
        i = 2
        while i <= x/i:
            p = i
            while p <= x:
                p *= i
                if p == x:
                    return True
            i += 1
        return False
