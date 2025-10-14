def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    for i in range(1, a+1):
        if i**3 == a:
            return True
    return False
