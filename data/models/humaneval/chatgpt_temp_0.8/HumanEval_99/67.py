def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # Check if the number is already an integer
    if num.is_integer():
        return int(num)
    
    # If the number is positive, round up to the nearest integer
    if num > 0:
        return int(num + 0.5)
    
    # If the number is negative, round down to the nearest integer
    if num < 0:
        return int(num - 0.5)
