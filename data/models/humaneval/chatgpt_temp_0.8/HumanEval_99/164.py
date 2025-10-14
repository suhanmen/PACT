def closest_integer(value):
    number = float(value)
    if number >= 0:
        if number - int(number) >= 0.5:
            return int(number) + 1
        else:
            return int(number)
    else:
        if abs(number - int(number)) >= 0.5:
            return int(number) - 1
        else:
            return int(number)
