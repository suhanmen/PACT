def closest_integer(value):
    # Convert the input string to a float
    x = float(value)

    # If the float is already an integer, return it
    if int(x) == x:
        return int(x)

    # Otherwise, find the two integers closest to it
    lower = int(x)
    if x < 0:
        upper = lower - 1
    else:
        upper = lower + 1

    # Calculate the distances between the float and the two integers
    lower_dist = abs(x - lower)
    upper_dist = abs(x - upper)

    # If the distances are equal, round away from zero
    if lower_dist == upper_dist:
        if x < 0:
            return lower
        else:
            return upper

    # Otherwise, return the closer integer
    if lower_dist < upper_dist:
        return lower
    else:
        return upper
