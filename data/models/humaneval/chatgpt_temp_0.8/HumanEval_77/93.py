def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = abs(a)
    x = int(round(a ** (1/3)))
    return x ** 3 == a
