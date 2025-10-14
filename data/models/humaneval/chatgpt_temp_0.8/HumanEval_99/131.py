def closest_integer(value):
    number = float(value)
    if number >= 0:
        integer = int(number + 0.5)
        if (number - integer) == 0.5:
            integer += 1
    else:
        integer = int(number - 0.5)
        if (integer - number) == 0.5:
            integer -= 1
    return integer
