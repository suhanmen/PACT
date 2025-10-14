def closest_integer(value):
    # convert value to float
    num = float(value)
    
    # check if the number is already an integer
    if num.is_integer():
        return int(num)
    
    # find the two integers closest to the number
    int1 = int(num)
    int2 = int(num) + 1
    
    # find the distance to each integer
    dist1 = abs(num - int1)
    dist2 = abs(num - int2)
    
    # if equidistant, round away from zero
    if dist1 == dist2:
        if num > 0:
            return int2
        else:
            return int1
    
    # return the closest integer
    elif dist1 < dist2:
        return int1
    else:
        return int2
