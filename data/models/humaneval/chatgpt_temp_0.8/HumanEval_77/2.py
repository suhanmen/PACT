python
def iscube(a):
    return (a >= 0 and int(a ** (1/3)) ** 3 == a) or (a < 0 and int(abs(a) ** (1/3)) ** 3 == abs(a))
