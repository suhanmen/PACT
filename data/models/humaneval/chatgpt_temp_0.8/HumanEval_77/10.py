def iscube(a):
    cube_root = round(a**(1/3))
    if cube_root**3 == a:
        return True
    else:
        return False
