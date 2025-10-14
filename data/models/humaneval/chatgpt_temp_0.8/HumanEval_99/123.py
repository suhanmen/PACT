def closest_integer(value):
    num = float(value)
    if num >= 0:
        closest_int = int(num + 0.5)
    else:
        closest_int = int(num - 0.5)        
    return closest_int
