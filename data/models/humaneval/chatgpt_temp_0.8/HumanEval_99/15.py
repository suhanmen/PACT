def closest_integer(value):
    # Convert the string value to a float
    x = float(value)
    
    # Check if the number is already an integer
    if x == int(x):
        return int(x)
    
    # Check if the absolute value of the decimal part is < 0.5
    if abs(x - int(x)) < 0.5:
        return int(x)
    
    # If not, round it away from zero
    elif x > 0:
        return int(x) + 1
    else:
        return int(x) - 1
