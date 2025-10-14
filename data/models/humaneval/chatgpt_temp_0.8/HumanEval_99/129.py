def closest_integer(value):
    # convert the input value to a float
    value = float(value)
    
    # calculate the floor and ceiling of the float value
    floor_value = int(value)
    ceiling_value = int(value) + 1
    
    # calculate the distance from the input value to the floor and ceiling
    distance_to_floor = abs(value - floor_value)
    distance_to_ceiling = abs(value - ceiling_value)
    
    # if the distance to the floor is greater than or equal to the distance to the ceiling,
    # return the ceiling value. Otherwise, return the floor value.
    if distance_to_floor >= distance_to_ceiling:
        return ceiling_value
    else:
        return floor_value
