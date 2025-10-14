def closest_integer(value):
    if "." not in value:
        return int(value)
    else:
        num = float(value)
        if num > 0:
            if num - int(num) >= 0.5:
                return int(num) + 1
            else:
                return int(num)
        else:
            if num - int(num) <= -0.5:
                return int(num) - 1
            else:
                return int(num)
