def iscube(a):
    if a < 0:
        a = -a
    # The cube root of a positive integer is always less than or equal to its integer part.
    # So we can check if the cube of the integer part is equal to a.
    n = int(a ** (1/3))
    return n ** 3 == a
