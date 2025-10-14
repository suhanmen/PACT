def closest_integer(value):
    # Convert the string value to a float
    float_value = float(value)
    
    # Round the float to the nearest integer
    rounded_value = round(float_value)
    
    # Calculate the difference between the rounded value and the float value
    difference = abs(rounded_value - float_value)
    
    # Check if the difference is exactly 0.5
    if difference == 0.5:
        # If the float value is positive, round away from zero
        if float_value > 0:
            rounded_value = int(float_value) + 1
        # If the float value is negative, round away from zero
        elif float_value < 0:
            rounded_value = int(float_value) - 1
    
    # Convert the rounded value to an integer and return it
    return int(rounded_value)
