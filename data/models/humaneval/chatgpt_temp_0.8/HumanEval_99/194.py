def closest_integer(value):
    # Convert the input value to a float number
    number = float(value)

    # Calculate the floor and ceiling of the number
    floor = int(number)
    ceiling = int(number) + 1

    # Calculate the distances from the floor and ceiling
    distance_from_floor = abs(number - floor)
    distance_from_ceiling = abs(number - ceiling)

    # If the distance from the floor is smaller or equal to the distance from the ceiling, 
    # return the floor. Otherwise, return the ceiling.
    if distance_from_floor <= distance_from_ceiling:
        return floor
    else:
        return ceiling
