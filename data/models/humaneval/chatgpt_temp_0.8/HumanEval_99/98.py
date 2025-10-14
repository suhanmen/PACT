python
def closest_integer(value):
    # Convert the input string to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # Calculate the distance to the nearest integer
    dist_to_floor = num - int(num)
    dist_to_ceil = 1 - dist_to_floor

    # Round away from zero
    if dist_to_floor < dist_to_ceil:
        return int(num)
    else:
        return int(num) + 1 if num > 0 else int(num) - 1
