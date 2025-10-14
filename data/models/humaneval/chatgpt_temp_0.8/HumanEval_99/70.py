python
def closest_integer(value):
    num = float(value)
    if num >= 0:
        if num - int(num) >= 0.5:
            return int(num) + 1
        else:
            return int(num)
    else:
        if abs(num) - abs(int(num)) >= 0.5:
            return int(num) - 1
        else:
            return int(num)
