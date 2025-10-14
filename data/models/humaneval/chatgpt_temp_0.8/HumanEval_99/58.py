def closest_integer(value):
    # converting the string value to a float
    value = float(value)

    # getting the floor and ceil values of the float
    floor_value = int(value // 1)
    ceil_value = int(value // 1 + 1)

    # calculating the distances of the float from the floor and ceil values
    distance_from_floor = abs(value - floor_value)
    distance_from_ceil = abs(value - ceil_value)

    # returning the closest integer, rounding away from zero
    if distance_from_floor < distance_from_ceil:
        return floor_value
    elif distance_from_ceil < distance_from_floor:
        return ceil_value
    else:
        # if equidistant from two integers, round away from zero
        if value >= 0:
            return ceil_value
        else:
            return floor_value
