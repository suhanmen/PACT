def closest_integer(value):
    # convert the input string to a float
    num = float(value)

    # if the number is already an integer, return it
    if num.is_integer():
        return int(num)

    # find the two integers that the number is between
    lower_int = int(num)
    upper_int = lower_int + 1

    # find the distance between the number and each integer
    lower_dist = num - lower_int
    upper_dist = upper_int - num

    # if the distances are equal, round away from zero
    if lower_dist == upper_dist:
        return int(num + abs(num) / num)

    # return the integer that the number is closest to
    return lower_int if lower_dist < upper_dist else upper_int
