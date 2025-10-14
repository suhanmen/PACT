def is_simple_power(x, n):
    if x < 1:
        return False
    if x == 1:
        return True
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            exp = 0
            while x % i == 0:
                x //= i
                exp += 1
            if x == 1 and exp % n == 0:
                return True
            else:
                return False
    if x != 1 and x**n == x:
        return True
    return False
