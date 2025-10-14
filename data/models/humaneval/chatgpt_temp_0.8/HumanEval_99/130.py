def closest_integer(value):
    # convert the value (string) to a float
    value = float(value)
    # round the value to the nearest integer
    rounded_value = round(value)
    # check if the rounded value is less than the original value
    if rounded_value < value:
        # if it is, return the rounded value plus 1
        return rounded_value + 1
    # check if the rounded value is greater than the original value
    elif rounded_value > value:
        # if it is, return the rounded value minus 1
        return rounded_value - 1
    # if the rounded value is equal to the original value, return it
    else:
        return rounded_value
