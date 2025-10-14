def closest_integer(value):
    # Convert the string representing the number to a float
    num = float(value)

    # Round the float to the nearest integer
    rounded_num = round(num)

    # Calculate the difference between the rounded number and the original number
    diff = abs(num - rounded_num)

    # If the difference is exactly 0.5, the number is equidistant from two integers
    if diff == 0.5:
        # Round away from zero
        if num > 0:
            return int(rounded_num + 0.5)
        else:
            return int(rounded_num - 0.5)

    # Otherwise, return the rounded number
    return int(rounded_num)
