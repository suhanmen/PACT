def closest_integer(value):
    # Convert the string to a float
    num = float(value)
    
    # Check if the number is already an integer
    if num.is_integer():
        return int(num)
    
    # Calculate the distance to the nearest integers
    dist_to_floor = abs(num - int(num))
    dist_to_ceil = abs(num - (int(num) + 1))
    
    # If the number is equidistant from two integers, round it away from zero
    if dist_to_floor == dist_to_ceil:
        if num > 0:
            return int(num + 1)
        else:
            return int(num - 1)
    # Otherwise, return the closest integer
    elif dist_to_floor < dist_to_ceil:
        return int(num)
    else:
        return int(num + 1)
