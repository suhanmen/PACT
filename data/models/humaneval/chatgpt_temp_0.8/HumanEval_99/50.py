def closest_integer(value):
    # Convert the string to a float
    num = float(value)
    # Check if the number is already an integer
    if num.is_integer():
        # If it is, return it as an integer
        return int(num)
    else:
        # If it's not an integer, find the two integers it's between
        lower_int = int(num)
        upper_int = lower_int + 1
        # Calculate the distances from the number to the two integers
        distance_lower = abs(num - lower_int)
        distance_upper = abs(num - upper_int)
        # If the distances are equal, round away from zero
        if distance_lower == distance_upper:
            return upper_int if num > 0 else lower_int
        else:
            # Otherwise, return the closest integer
            return lower_int if distance_lower < distance_upper else upper_int
