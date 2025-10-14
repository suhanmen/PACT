def iscube(a):
    if a < 0:
        a = -a
    x = int(round(a**(1/3))) # get the cube root and round to the nearest integer
    return x**3 == a # check if x cubed equals a
