def iscube(a):
    if a < 0:
        a = -a # consider absolute value for negative a
    root = round(a**(1/3)) # find cube root and round to integer
    return root**3 == a # check if integer root cubed equals the input
