def closest_integer(value):
    # Convert the value to a float
    num = float(value)

    # Check if the fractional part is 0.5 and the integer part
    # is odd. If so, round up, otherwise round to the nearest integer.
    if num % 1 == 0.5:
        if int(num) % 2 == 1:
            return int(num) + 1
        else:
            return round(num)
    else:
        return round(num)
