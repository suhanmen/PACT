def iscube(a):
    # Absolute value of a
    a = abs(a)
    
    # Find the integer cube root of a
    cube_root = round(a**(1/3))
    
    # Check if cube_root**3 equals a
    return cube_root**3 == a
