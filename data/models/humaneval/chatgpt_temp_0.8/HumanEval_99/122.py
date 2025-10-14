def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # Check if the number is already an integer
    if num.is_integer():
        return int(num)
    
    # Check which integer is closest to the number
    lower_int = int(num)
    upper_int = lower_int + 1
    lower_diff = num - lower_int
    upper_diff = upper_int - num
    
    # Round away from zero if equidistant from two integers
    if lower_diff == upper_diff:
        return upper_int if num > 0 else lower_int
    
    # Return the closest integer
    return lower_int if lower_diff < upper_diff else upper_int
