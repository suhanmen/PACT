def closest_integer(value):
    if "." not in value: # check if the value is already an integer
        return int(value)
    else:
        # convert the value to a float and get the integer parts of the value and its absolute value
        x = float(value)
        y = abs(x)
        integer_part = int(x)
        integer_part_abs = int(y)
        # find the closest integer by comparing the distance between x and integer_part with the distance between x and integer_part+1
        if y - integer_part_abs < integer_part + 1 - y:
            return integer_part
        else:
            return integer_part + 1 if x > 0 else integer_part - 1
