def iscube(a):
    if a == 0:
        return True
    else:
        return (abs(a)) ** (1/3) == int((abs(a)) ** (1/3))
