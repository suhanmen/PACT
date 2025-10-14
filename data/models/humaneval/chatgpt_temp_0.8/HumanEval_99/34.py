def closest_integer(value):
    value = float(value) # Convert value to a float
    if value >= 0: # positive number
        closest_int = int(value + 0.5) # round up
    else: # negative number
        closest_int = int(value - 0.5) # round down
    return closest_int
