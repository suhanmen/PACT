def any_int(x, y, z):
    # Check if all numbers are integers
    if not all(isinstance(num, int) for num in (x, y, z)):
        return False
    # Check if one of the numbers is equal to the sum of the other two
    if x == y + z or y == x + z or z == x + y:
        return True
    else:
        return False
