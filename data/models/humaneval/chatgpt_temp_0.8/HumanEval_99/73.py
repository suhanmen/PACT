def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # If the number is already an integer, return it
    if num.is_integer():
        return int(num)
    
    # Find the closest integers and calculate the distance
    lower_int = int(num)
    upper_int = lower_int + 1
    dist_lower = num - lower_int
    dist_upper = upper_int - num
    
    # If the distance to the lower integer is smaller, return it
    if dist_lower < dist_upper:
        return lower_int
    # If the distance to the upper integer is smaller, return it
    elif dist_upper < dist_lower:
        return upper_int
    # If the distances are equal, round away from zero
    else:
        if num < 0:
            return lower_int
        else:
            return upper_int
