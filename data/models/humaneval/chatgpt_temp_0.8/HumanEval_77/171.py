def iscube(a):
    cube_root = abs(a) ** (1/3)
    return int(cube_root) ** 3 == abs(a)
