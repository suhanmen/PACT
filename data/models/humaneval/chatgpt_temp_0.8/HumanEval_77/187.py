def iscube(a):
    if a == 0:
        return True  # 0 is the cube of 0
    elif a < 0:
        a = -a  # treat negative numbers as positive for cube root calculation
    cube_root = round(a ** (1/3))  # find the cube root and round to nearest integer
    return cube_root ** 3 == a  # check if cube root cubed is equal to a
