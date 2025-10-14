def closest_integer(value):
    # Convert value to float
    value = float(value)
    
    # Check if value is already an integer
    if value.is_integer():
        return int(value)
    
    # Calculate distance to nearest integer
    dist_to_lower = value - int(value)
    dist_to_upper = 1 - dist_to_lower
    
    # Round away from zero
    if dist_to_lower > dist_to_upper:
        return int(value + 1)
    else:
        return int(value - 1)
