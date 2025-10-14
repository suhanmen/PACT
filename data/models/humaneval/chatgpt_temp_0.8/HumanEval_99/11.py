def closest_integer(value):
    num = float(value) # convert the input value to float
    if num > 0:
        return int(num + 0.5) # if the number is positive, round it normally
    else:
        return int(num - 0.5) # if the number is negative, round it away from zero
