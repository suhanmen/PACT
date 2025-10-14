def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # Round the float to the nearest integer
    rounded = round(num)
    
    # Calculate the absolute difference between the float and the rounded value
    difference = abs(num - rounded)
    
    # Check if the float is equidistant from two integers
    if difference == 0.5:
        # Round away from zero
        if num > 0:
            return int(rounded + 0.5)
        else:
            return int(rounded - 0.5)
    
    # Return the rounded integer
    return int(rounded)
