def closest_integer(value):
    num = float(value)  # Convert the input value to a floating point number
    if num >= 0:
        return int(num + 0.5)  # Round up if the decimal part is >= 0.5
    else:
        return int(num - 0.5)  # Round down if the decimal part is < 0.5
