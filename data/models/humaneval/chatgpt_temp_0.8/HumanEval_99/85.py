def closest_integer(value):
    # convert the input string into a float
    num = float(value)

    # check if the number is already an integer
    if num.is_integer():
        return int(num)

    # check if the number is positive or negative
    if num > 0:
        # if the number is positive, round it up or down based on the decimal value
        if num - int(num) >= 0.5:
            return int(num) + 1
        else:
            return int(num)
    else:
        # if the number is negative, round it up or down based on the decimal value
        if abs(num - int(num)) >= 0.5:
            return int(num) - 1
        else:
            return int(num)
