def closest_integer(value):
    # Convert string value to float
    value = float(value)
    
    # Check if the value is already an integer
    if value.is_integer():
        return int(value)
    
    # Round the value to the nearest integer
    rounded = round(value)
    
    # Check if the rounded value is closer to the next integer or the previous integer
    if rounded > value:
        return int(rounded)
    else:
        return int(rounded + 1)
