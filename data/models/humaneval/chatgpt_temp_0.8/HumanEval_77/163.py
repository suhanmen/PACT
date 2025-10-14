def iscube(a):
    if a < 0:
        a = -a
    if a == 0:
        return True
    else:
        cube_root = int(round(a ** (1./3)))
        return cube_root ** 3 == a
