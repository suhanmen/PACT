def closest_integer(value):
    # convert value to float
    value = float(value)
    
    # get the floor and ceiling of the value
    floor = int(value - 0.5)  # round down
    ceil = int(value + 0.5)   # round up
    
    # check which integer is closest
    if abs(value - floor) < abs(value - ceil):
        return floor
    elif abs(value - floor) > abs(value - ceil):
        return ceil
    else:
        # if equidistant, round away from zero
        if value > 0:
            return ceil
        else:
            return floor
