python
def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    # find the cube root of a using integer division
    root = int(a ** (1/3))
    # check if the cube of the root is equal to a
    return root ** 3 == a
