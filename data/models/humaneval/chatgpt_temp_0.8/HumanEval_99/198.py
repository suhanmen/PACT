def closest_integer(value):
    # Convert the value to a float
    value = float(value)
    
    # Check if the value is already an integer
    if value.is_integer():
        return int(value)
    
    # Calculate the closest integer
    closest_int = round(value)
    
    # Check if the closest integer is equidistant from two integers
    if closest_int - 0.5 == value or closest_int + 0.5 == value:
        # Round away from zero
        if value < 0:
            return int(closest_int - 1)
        else:
            return int(closest_int + 1)
    
    return int(closest_int)
