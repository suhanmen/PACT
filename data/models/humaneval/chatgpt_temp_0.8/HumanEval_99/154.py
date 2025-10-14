def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # If the number is already an integer, return it
    if num.is_integer():
        return int(num)
    
    # Find the two integers that the number is between
    lower_int = int(num)
    upper_int = lower_int + 1
    
    # Find the distances between the number and each integer
    lower_dist = num - lower_int
    upper_dist = upper_int - num
    
    # If the distances are equal, round away from zero
    if lower_dist == upper_dist:
        if num >= 0:
            return upper_int
        else:
            return lower_int
    
    # Otherwise, return the closest integer
    elif lower_dist < upper_dist:
        return lower_int
    else:
        return upper_int
