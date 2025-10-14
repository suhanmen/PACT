python
def closest_integer(value):
    # Convert the value to a float
    x = float(value)
    
    # If the value is already an integer, return it
    if x.is_integer():
        return int(x)
    
    # Otherwise, find the two integers it is between
    lower_int = int(x)
    upper_int = lower_int + 1
    
    # Check which integer it is closest to
    if abs(x - lower_int) <= abs(x - upper_int):
        return lower_int
    else:
        return upper_int
