def iscube(a):
    if a < 0:
        a = -a
    root = round(a**(1/3))
    if root**3 == a:
        return True
    else:
        return False
