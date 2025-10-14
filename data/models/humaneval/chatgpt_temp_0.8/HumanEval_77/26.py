def iscube(a):
    if a < 0:
        a = -a  # we can ignore the negative sign, since (-x)^3 = -x^3 for any x
    root = round(a**(1/3))  # find the cube root and round to the nearest integer
    return root**3 == a  # check if the cube of the rounded root is equal to a
