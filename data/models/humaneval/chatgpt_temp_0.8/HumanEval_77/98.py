def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    x = round(a**(1/3))
    if x**3 == a:
        return True
    else:
        return False
