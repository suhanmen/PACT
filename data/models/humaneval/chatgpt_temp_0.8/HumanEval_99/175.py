def closest_integer(value):
    # Convert the string value to a float
    num = float(value)
    
    # Get the absolute difference between the number and its floor and ceil
    diff_floor = abs(num - int(num))
    diff_ceil = abs(num - int(num) - 1)
    
    # If the number is equidistant from two integers, round it away from zero
    if diff_floor == diff_ceil:
        return int(num + abs(num) / num)
    # Otherwise, return the closest integer
    else:
        return int(round(num))
