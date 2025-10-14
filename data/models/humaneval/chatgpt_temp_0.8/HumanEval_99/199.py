def closest_integer(value):
    # convert the input string to a float number
    number = float(value)

    # get the integer part of the number
    integer = int(number)

    # calculate the distance from the number to the two neighboring integers
    distance_below = number - integer
    distance_above = 1 - distance_below

    # check which integer is closest
    if distance_below < distance_above:
        return integer
    elif distance_below > distance_above:
        return integer + 1
    else:
        # if equidistant, round away from zero
        if integer >= 0:
            return integer + 1
        else:
            return integer - 1
