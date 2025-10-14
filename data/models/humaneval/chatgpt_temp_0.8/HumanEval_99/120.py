def closest_integer(value):
    num = float(value)
    if num >= 0:
        int_num = int(num + 0.5)
    else:
        int_num = int(num - 0.5)
    return int_num
