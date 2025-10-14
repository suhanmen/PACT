def closest_integer(value):
    # convert the string value to a float
    num = float(value)
    
    # find the two integers that the number is between
    lower_int = int(num)
    upper_int = lower_int + 1
    
    # calculate the distances to each integer
    lower_dist = num - lower_int
    upper_dist = upper_int - num
    
    # check which integer is closer and return it
    if lower_dist < upper_dist:
        return lower_int
    else:
        return upper_int
